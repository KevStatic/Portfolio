# ---------------------------------------------------------------------------
# Portfolio content. Everything the site shows lives here so you can update
# copy without touching the template or build logic.
# ---------------------------------------------------------------------------

GITHUB_USERNAME = "KevStatic"

name = "Kevalya Shah"
handle = "Kev"
role = "Software Engineer · AI & ML"

# Rotating phrases used by the hero typing animation.
taglines = [
    "Building scalable web systems.",
    "Applying ML to real-world problems.",
    "Shipping AI-driven solutions.",
    "Turning ideas into products.",
]

about = (
    "I'm a software engineer who enjoys living at the intersection of full-stack "
    "engineering and machine learning. I've fine-tuned speech and translation models, "
    "built data pipelines that move fast, and shipped end-to-end web platforms. "
    "I care about clean systems, measurable impact, and learning something new on every project."
)

# Optional. Leave email as None to hide the copy-email button and rely on the
# contact form + social links instead.
email = None
location = "India"
# relative so it works locally (file://) and on Netlify
resume_path = "resume.pdf"

socials = {
    "github": "https://github.com/KevStatic",
    "linkedin": "https://www.linkedin.com/in/kevalyashah/",
    "buymeacoffee": "https://buymeacoffee.com/kevstatic",
}

# Lightweight, animated stats shown in the hero. (count, label)
stats = [
    ("3+", "Internships & roles"),
    ("10+", "Shipped projects"),
    ("6", "Languages used"),
]

experience = [
    {
        "role": "Application Developer",
        "company": "Larsen & Toubro",
        "duration": "Jan 2026 — Present",
        "desc": "Full-stack development driving feature improvements across the platform.",
        "tags": ["Full-Stack", "Web", "Enterprise"],
    },
    {
        "role": "AI Intern",
        "company": "Intelehealth",
        "duration": "May 2025 — Jul 2025",
        "desc": "Researched and fine-tuned speech-to-text and translation models, improving "
                "transcription accuracy and handling large-scale audio datasets.",
        "tags": ["NLP", "Speech", "PyTorch"],
    },
    {
        "role": "Software Developer Intern",
        "company": "Kellogg Brown & Root",
        "duration": "May 2024 — Jul 2024",
        "desc": "Built Python data pipelines that cut processing time and improved ML model "
                "accuracy on new datasets.",
        "tags": ["Python", "Data Pipelines", "ML"],
    },
]

# Skills grouped by category for a cleaner, scannable layout.
skill_groups = {
    "Languages": ["Python", "C", "C++", "Java", "TypeScript", "JavaScript", "C#"],
    "Web & Frameworks": ["React", "Next.js", "Node.js", "MERN Stack", "Tailwind", ".NET"],
    "Data & ML": ["TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "Pandas"],
    "Databases": ["MongoDB", "SQL", "PL/SQL"],
    "Foundations": ["Data Structures & Algorithms", "System Software", "OOP"],
}

# Hand-picked projects shown first and used as a fallback if the GitHub API is
# unreachable at build time. `repo` (optional) lets the build enrich the card
# with live language/stars. Set `featured` to pin a project to the top.
featured_projects = [
    {
        "title": "Vehicle Damage Severity Classifier",
        "desc": "Explainable deep-learning model that classifies vehicle damage severity, "
                "with Grad-CAM heatmaps so predictions can be visually justified.",
        "repo": "Multi-Class-Vehicle-Damage-Severity-Classification-with-Grad-CAM-Explainability",
        "link": "https://github.com/KevStatic/Multi-Class-Vehicle-Damage-Severity-Classification-with-Grad-CAM-Explainability",
        "tags": ["Deep Learning", "Grad-CAM", "Python"],
        "featured": True,
    },
    {
        "title": "AI Pit-Stop Strategy Optimizer",
        "desc": "Final-year project that models race conditions to recommend optimal pit-stop "
                "strategy using data-driven decision making.",
        "repo": "AI-Driven-Pit-Stop-Strategy-Optimizer",
        "link": "https://github.com/KevStatic/AI-Driven-Pit-Stop-Strategy-Optimizer",
        "tags": ["AI", "Optimization", "Python"],
        "featured": True,
    },
    {
        "title": "ETMS — Employee Transfer Management",
        "desc": "End-to-end workflow platform handling the full employee-transfer lifecycle, "
                "from request to approval.",
        "repo": "ETMS_Solution",
        "link": "https://github.com/KevStatic/ETMS_Solution",
        "tags": ["Full-Stack", "Workflow", "Web"],
        "featured": True,
    },
    {
        "title": "Trade Matching Engine",
        "desc": "A matching engine for trading orders, built to explore low-latency order-book "
                "design and matching logic in Java.",
        "repo": "Trade-Matching-Engine",
        "link": "https://github.com/KevStatic/Trade-Matching-Engine",
        "tags": ["Java", "Systems", "Finance"],
    },
    {
        "title": "Voice Bot (OpenAI)",
        "desc": "A voice assistant integration demonstrating real-time speech interaction with "
                "large language models.",
        "repo": "Voice-Bot-Development",
        "link": "https://github.com/KevStatic/Voice-Bot-Development",
        "tags": ["Voice", "LLM", "JavaScript"],
    },
    {
        "title": "Handwriting Classifier",
        "desc": "A deep-learning model trained to recognise my own handwriting — a hands-on "
                "dive into CNNs and dataset building.",
        "repo": "Personal-Handwriting-classification-model",
        "link": "https://github.com/KevStatic/Personal-Handwriting-classification-model",
        "tags": ["CNN", "Deep Learning", "Jupyter"],
    },
]

accolades = [
    "Showcased inter-school winning robotics project at EXPO 2020 Dubai",
    "Runner-up at Mindbend, NIT Surat",
    "Active competitive programmer on LeetCode",
]
