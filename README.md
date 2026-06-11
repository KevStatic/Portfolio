# Portfolio — kevalyashah.netlify.app

A fast, single-page portfolio. Content lives in plain Python, the page is built
with Jinja2 + Tailwind, and projects are pulled live from GitHub at build time.

## Stack
- **`data.py`** — all site content (bio, experience, skills, featured projects, socials).
- **`build.py`** — fetches GitHub repos, merges them with the curated list, renders the template.
- **`templates/index.html`** — the design + all client-side behaviour.
- **`output/`** — the generated, deploy-ready site (`index.html` + `resume.pdf`). This is what Netlify serves.

## Features
- Light / dark theme toggle (remembers your choice)
- Command palette — press **K** (or ⌘/Ctrl-K) to jump anywhere
- Typing hero, animated stat counters, scroll-spy nav, scroll progress, cursor glow
- Live GitHub project cards (language, stars, topics) with instant search/filter
- Working contact form via **Netlify Forms** (submissions appear in your Netlify dashboard)
- SEO + Open Graph meta, responsive, reduced-motion friendly

## Build locally
```bash
pip install -r requirements.txt
python build.py                 # regenerates output/index.html from live GitHub data
python -m http.server 8123 --directory output   # preview at http://localhost:8123
```

If GitHub is unreachable, the build falls back to the curated projects in `data.py`, so it never fails.

## Deploy (Netlify)
The `output/` folder is pre-built and committed, so Netlify just serves it
(`publish = "output"` in `netlify.toml`) — no build step can break a deploy.
To refresh project data, run `python build.py` and redeploy.

To let Netlify rebuild automatically on every deploy instead, uncomment the
`command` line in `netlify.toml`.

## Update content
Edit `data.py` → run `python build.py` → redeploy. That's it.
