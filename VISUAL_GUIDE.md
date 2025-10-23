# Visual Guide: Before → After

## 🏠 Home Page Changes

### Before (index.html - line 185)
```html
<a href="#contact" class="inline-block px-6 sm:px-8 py-3 bg-forest text-white rounded-lg font-semibold shadow-lg hover:bg-accent transition">
  Start Journey
</a>
```

### After (templates/index.html)
```html
<div class="cta-row">
  <a href="/#contact" class="btn btn-primary" data-cta="start_journey">Start Journey</a>
  <a href="/hire-me" class="btn btn-outline" aria-label="Hire Danny" data-cta="hire_me">Hire Me</a>
</div>
```

**Result**: Two buttons side-by-side on desktop, stacked on mobile

---

## 📄 New /hire-me Page

### Layout Structure
```
┌─────────────────────────────────────┐
│  Navigation (with Hire Me link)    │
├─────────────────────────────────────┤
│  INTRO SECTION                      │
│  Designer, Builder, Operator        │
│  [headline, subhead, location]      │
├─────────────────────────────────────┤
│  SELECTED WORK                      │
│  ┌────────┐ ┌────────┐             │
│  │ Card 1 │ │ Card 2 │             │
│  └────────┘ └────────┘             │
├─────────────────────────────────────┤
│  PERSONAL PROJECTS                  │
│  ┌────────┐ ┌────────┐             │
│  │ Card 1 │ │ Card 2 │             │
│  └────────┘ └────────┘             │
├─────────────────────────────────────┤
│  SKILLS SNAPSHOT                    │
│  [HTML] [CSS] [JavaScript] [Python] │
├─────────────────────────────────────┤
│  EXPERIENCE                         │
│  ┌──────────────────────────────┐  │
│  │ Role + Dates                 │  │
│  │ • Bullet 1                   │  │
│  │ • Bullet 2                   │  │
│  └──────────────────────────────┘  │
├─────────────────────────────────────┤
│  CURRENTLY LEARNING                 │
│  [Accessibility] [Image opt] [Forms]│
├─────────────────────────────────────┤
│  CTA FOOTER                         │
│  [Resume] [Book Call] [Email]       │
└─────────────────────────────────────┘
```

---

## 🎨 Style Conversion: Tailwind → Vanilla CSS

### Navigation Example

**Before (Tailwind)**:
```html
<nav class="fixed w-full z-50 bg-background/80 backdrop-blur border-b border-darkgrey">
  <div class="max-w-7xl mx-auto flex items-center justify-between px-4 sm:px-6 py-4">
```

**After (Vanilla CSS)**:
```html
<nav class="site-nav">
  <div class="nav-container">
```

**CSS**:
```css
.site-nav {
  position: fixed;
  width: 100%;
  z-index: 50;
  background-color: rgba(18, 18, 18, 0.8);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid #23272A;
}

.nav-container {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
}
```

### Button Example

**Before (Tailwind)**:
```html
<a class="inline-block px-6 sm:px-8 py-3 bg-forest text-white rounded-lg font-semibold shadow-lg hover:bg-accent transition">
```

**After (Vanilla CSS)**:
```html
<a class="btn btn-primary">
```

**CSS**:
```css
.btn {
  display: inline-block;
  padding: 12px 24px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 700;
  font-size: 1rem;
  border: 2px solid transparent;
  transition: all 0.2s;
}

.btn-primary {
  background: #4CAF50;
  color: #fff;
  border-color: #4CAF50;
}

.btn-primary:hover {
  background: #81C784;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3);
}
```

---

## 📱 Responsive Breakpoints

```css
/* Mobile First (default) */
.portfolio-grid {
  grid-template-columns: 1fr;
}

/* Tablet (640px+) */
@media (min-width: 640px) {
  .portfolio-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Desktop (768px+) */
@media (min-width: 768px) {
  .portfolio-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .nav-links {
    display: flex;
  }
}
```

---

## 🔄 Flask Route Flow

```
User Request → Flask App → Template → Response
─────────────────────────────────────────────

GET /
  └→ @app.route("/")
     └→ render_template("index.html")
        └→ templates/index.html (extends base.html)
           └→ Hero with dual CTAs

GET /hire-me
  └→ @app.route("/hire-me")
     └→ fetch_sheet_rows() OR load_local_json()
        └→ Parse content into sections
           └→ render_template("hire_me.html", data=data)
              └→ templates/hire_me.html (extends base.html)
```

---

## 📊 CMS Data Flow

### Option 1: Google Sheets (Remote)
```
Google Sheet (Published CSV)
  ↓
SHEET_CSV_URL environment variable
  ↓
fetch_sheet_rows()
  ↓
Parse CSV → Python dict
  ↓
render_template(data=parsed_data)
```

### Option 2: Local JSON (Fallback)
```
cms/hire-me.local.json
  ↓
load_local_json()
  ↓
Python dict
  ↓
render_template(data=data)
```

---

## 🎯 Key Interactions

### Mobile Menu
```javascript
// site.js
menuBtn.onclick = function() {
  mobileMenu.classList.toggle('show');
};
```

```css
/* site.css */
.mobile-menu {
  display: none;
}

.mobile-menu.show {
  display: flex;
}
```

### Scroll Fade-In
```javascript
// site.js
function onScrollFadeIn() {
  document.querySelectorAll('.fade-in').forEach(el => {
    const rect = el.getBoundingClientRect();
    if (rect.top < window.innerHeight - 60) {
      el.classList.add('visible');
    }
  });
}
```

```css
/* site.css */
.fade-in {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.7s, transform 0.7s;
}

.fade-in.visible {
  opacity: 1;
  transform: none;
}
```

---

## 🎨 Color Themes

### Home Page (Dark)
```css
Background:  #121212  ███████
Secondary:   #181c1f  ███████
Cards:       #23272A  ███████
Green:       #4CAF50  ███████
Orange:      #e34c26  ███████
Text:        #F0F0F0  ███████
```

### Hire Me Page (Light)
```css
Background:  #F7F3EA  ███████
Cards:       #FFFFFF  ███████
Navy:        #1F2A44  ███████
Gray:        #6D8AA6  ███████
```

---

## 🚀 Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python3 app.py

# Visit in browser
http://localhost:5000
http://localhost:5000/hire-me

# Optional: Set Google Sheets CMS
export SHEET_CSV_URL="https://docs.google.com/spreadsheets/d/YOUR_ID/gviz/tq?tqx=out:csv"
```

---

## ✨ What You Can Customize

### Content
- `cms/hire-me.local.json` - Edit all hire page content
- `templates/index.html` - Modify home page sections
- `templates/hire_me.html` - Adjust hire page layout

### Styling
- `static/css/site.css` - All visual styling
- Colors defined at top of CSS file
- Responsive breakpoints clearly marked

### Functionality
- `static/js/site.js` - Add custom JavaScript
- `app.py` - Add new routes or modify data processing

---

**Pro Tip**: The hire page uses a light theme (#F7F3EA background) while the home page uses a dark theme (#121212). This visual distinction helps employers see this as a professional portfolio space.

