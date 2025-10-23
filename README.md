# Nomadic Designs

A lightweight Flask-based portfolio and business website with CMS capabilities.

## Features

- **Home Page**: Hero section with dual CTAs ("Start Journey" and "Hire Me")
- **Hire Me Page**: Employer-facing portfolio with work samples, skills, experience, and contact options
- **Google Sheets CMS**: Optional content management via published CSV
- **No Framework Dependencies**: Pure CSS (no Tailwind/Bootstrap)
- **Accessible**: Semantic HTML, WCAG AA compliant, keyboard navigable
- **Responsive**: Mobile-first design

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   python app.py
   ```

3. **Visit**: http://localhost:5000

## Routes

- `/` - Home page
- `/hire-me` - Employer-facing portfolio page

## Google Sheets CMS (Optional)

To use Google Sheets as a CMS for the `/hire-me` page:

1. Create a Google Sheet with columns: `page`, `section`, `key`, `value`, `imageUrl`, `link`, `category`, `sort`
2. Publish it as CSV: File > Share > Publish to web > CSV
3. Set environment variable:
   ```bash
   export SHEET_CSV_URL="https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/gviz/tq?tqx=out:csv"
   ```

### Sheet Schema for Hire Page

- `page`: "hire"
- `section`: "intro", "work", "projects", "skills", "experience", "learning", "cta"
- `key`: varies by section (e.g., "headline", "subhead", "location" for intro)
- `value`: main content text
- `tags`: pipe-separated tags (e.g., "Web Design|QA|SEO")
- `bullets`: pipe-separated bullet points
- `link`: URL for links
- `sort`: numeric sort order

If no sheet URL is provided, the app falls back to `cms/hire-me.local.json`.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: Vanilla HTML/CSS/JS (no frameworks)
- **Templating**: Jinja2
- **Styling**: Custom CSS (no Tailwind/Bootstrap)
- **CMS**: Google Sheets (optional) or local JSON

## Directory Structure

```
nomadlabs/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── cms/
│   └── hire-me.local.json # Local content fallback
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   └── hire_me.html       # Hire me page
└── static/
    ├── css/
    │   └── site.css       # All styles
    ├── js/
    │   └── site.js        # JavaScript
    └── [images, videos, etc.]
```

## Deployment

For production:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server (Gunicorn, uWSGI)
3. Set environment variables as needed
4. Configure reverse proxy (nginx/Apache)

Example with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

