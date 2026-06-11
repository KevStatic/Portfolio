"""Static-site build step.

Renders templates/index.html -> output/index.html, enriching the hand-picked
projects in data.py with live GitHub metadata (language, stars, topics) and
appending any other non-fork repos. If GitHub is unreachable, it falls back to
the curated list in data.py so the build never breaks.

Usage:  python build.py
"""

import os
import sys
import shutil
import datetime

import requests

# Windows consoles default to cp1252; force UTF-8 so status emojis don't crash.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
from jinja2 import Environment, FileSystemLoader

import data

API = f"https://api.github.com/users/{data.GITHUB_USERNAME}/repos"

# Language -> dot colour, mirroring GitHub's palette.
LANG_COLORS = {
    "Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "Java": "#b07219", "C": "#555555", "C++": "#f34b7d", "C#": "#178600",
    "HTML": "#e34c26", "CSS": "#563d7c", "Jupyter Notebook": "#DA5B0B",
    "Shell": "#89e051", "Go": "#00ADD8", "Rust": "#dea584",
}


def _title(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").title()


def fetch_repos() -> dict:
    """Return {repo_name: metadata} for non-fork repos, or {} on failure."""
    try:
        resp = requests.get(
            API, params={"per_page": 100, "sort": "updated"},
            headers={"Accept": "application/vnd.github+json"}, timeout=15,
        )
        resp.raise_for_status()
        repos = resp.json()
        if not isinstance(repos, list):
            return {}
    except Exception as exc:  # network error / rate limit -> fall back gracefully
        print(f"WARNING: GitHub fetch failed ({exc}); using curated projects only.")
        return {}

    out = {}
    for r in repos:
        if r.get("fork"):
            continue
        out[r["name"]] = {
            "name": r["name"],
            "language": r.get("language"),
            "stars": r.get("stargazers_count", 0),
            "forks": r.get("forks_count", 0),
            "topics": r.get("topics", []) or [],
            "desc": r.get("description"),
            "link": r["html_url"],
            "homepage": r.get("homepage"),
            "updated": r.get("updated_at", ""),
        }
    return out


def build_projects(repos: dict) -> list:
    """Merge curated featured projects with the rest of the live repos."""
    projects = []
    used = set()

    # 1. Curated projects first, enriched with live data where available.
    for p in data.featured_projects:
        repo = repos.get(p.get("repo", ""), {})
        used.add(p.get("repo", ""))
        lang = repo.get("language") or (p["tags"][-1] if p.get("tags") else None)
        projects.append({
            "title": p["title"],
            "desc": p["desc"],
            "link": repo.get("link") or p["link"],
            "homepage": repo.get("homepage"),
            "language": lang,
            "lang_color": LANG_COLORS.get(lang, "#8b949e"),
            "stars": repo.get("stars", 0),
            "tags": p.get("tags", []),
            "featured": p.get("featured", False),
        })

    # 2. Remaining live repos (skip the personal/profile repo and dupes).
    extras = [
        r for name, r in repos.items()
        if name not in used and name.lower() != data.GITHUB_USERNAME.lower()
    ]
    extras.sort(key=lambda r: (r["stars"], r["updated"]), reverse=True)
    for r in extras:
        lang = r.get("language")
        projects.append({
            "title": _title(r["name"]),
            "desc": r.get("desc") or "No description provided.",
            "link": r["link"],
            "homepage": r.get("homepage"),
            "language": lang,
            "lang_color": LANG_COLORS.get(lang, "#8b949e"),
            "stars": r.get("stars", 0),
            "tags": r.get("topics", [])[:3],
            "featured": False,
        })

    return projects


def sync_resume():
    """If a resume.pdf sits in the project root, copy it into output/.

    Lets you drop/replace resume.pdf in the project folder and have it picked
    up on the next build. (output/resume.pdf is otherwise left untouched.)"""
    if os.path.exists("resume.pdf"):
        shutil.copyfile("resume.pdf", os.path.join("output", "resume.pdf"))
        print("Copied resume.pdf -> output/resume.pdf")


def main():
    os.makedirs("output", exist_ok=True)
    sync_resume()
    repos = fetch_repos()
    projects = build_projects(repos)

    env = Environment(
        loader=FileSystemLoader("templates"),
        trim_blocks=True, lstrip_blocks=True,
    )
    template = env.get_template("index.html")

    html = template.render(
        name=data.name,
        handle=data.handle,
        role=data.role,
        taglines=data.taglines,
        about=data.about,
        email=data.email,
        location=data.location,
        resume_path=data.resume_path,
        socials=data.socials,
        stats=data.stats,
        experience=data.experience,
        skill_groups=data.skill_groups,
        projects=projects,
        accolades=data.accolades,
        year=datetime.date.today().year,
    )

    with open("output/index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Built output/index.html - {len(projects)} projects "
          f"({'live GitHub data' if repos else 'curated fallback'}).")


if __name__ == "__main__":
    main()
