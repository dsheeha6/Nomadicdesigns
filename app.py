from flask import Flask, render_template, jsonify
import json, os, requests

app = Flask(__name__)

# Optional CMS: Google Sheet (published CSV) URL via env
SHEET_CSV_URL = os.environ.get("SHEET_CSV_URL", "")

def fetch_sheet_rows():
    """Fetch published CSV (Google Sheets) if SHEET_CSV_URL set, else return None."""
    if not SHEET_CSV_URL:
        return None
    try:
        r = requests.get(SHEET_CSV_URL, timeout=8)
        r.raise_for_status()
        lines = [l for l in r.text.splitlines() if l.strip()]
        headers = [h.strip() for h in lines[0].split(",")]
        rows = []
        for line in lines[1:]:
            cols = []
            current = ""
            in_quotes = False
            for ch in line:
                if ch == '"' and not in_quotes:
                    in_quotes = True
                elif ch == '"' and in_quotes:
                    in_quotes = False
                elif ch == ',' and not in_quotes:
                    cols.append(current)
                    current = ""
                    continue
                current += ch
            cols.append(current)
            row = { headers[i]: (cols[i].strip().strip('"') if i < len(cols) else "") for i in range(len(headers)) }
            rows.append(row)
        return rows
    except Exception:
        return None

def load_local_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hire-me")
def hire_me():
    """
    Render Hire Me page with content from Google Sheet if available,
    else fall back to /cms/hire-me.local.json.
    """
    rows = fetch_sheet_rows()
    data = None

    if rows:
        # Expect a flat schema: page, section, key, value, imageUrl, link, category, sort
        def section(page, sec):
            items = [r for r in rows if r.get("page")==page and r.get("section")==sec]
            def sort_key(r): 
                s = r.get("sort","0")
                try: return int(s)
                except: return 0
            return sorted(items, key=sort_key)

        intro = {
            "headline": next((r.get("value") for r in rows if r.get("page")=="hire" and r.get("section")=="intro" and r.get("key")=="headline"), "Designer, Builder, Operator"),
            "subhead":  next((r.get("value") for r in rows if r.get("page")=="hire" and r.get("section")=="intro" and r.get("key")=="subhead"), "I ship clean, conversion-focused websites and lightweight automations."),
            "location": next((r.get("value") for r in rows if r.get("page")=="hire" and r.get("section")=="intro" and r.get("key")=="location"), "Atlanta, GA — open to remote"),
        }
        work = section("hire","work")
        projects = section("hire","projects")
        skills = [r.get("value") for r in section("hire","skills")]
        exp = section("hire","experience")
        learning = [r.get("value") for r in section("hire","learning")]
        cta = {
            "resumeUrl": next((r.get("link") for r in rows if r.get("page")=="hire" and r.get("section")=="cta" and r.get("key")=="resumeUrl"), "/static/assets/dannysheehanresume.pdf"),
            "email":     next((r.get("value") for r in rows if r.get("page")=="hire" and r.get("section")=="cta" and r.get("key")=="email"), "daniel.sheehan03@gmail.com"),
            "cal":       next((r.get("link") for r in rows if r.get("page")=="hire" and r.get("section")=="cta" and r.get("key")=="cal"), "https://calendly.com/daniel-sheehan03/intro"),
        }

        data = {"intro": intro, "work": work, "projects": projects, "skills": skills, "experience": exp, "learning": learning, "cta": cta}
    else:
        data = load_local_json("cms/hire-me.local.json")

    return render_template("hire_me.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

