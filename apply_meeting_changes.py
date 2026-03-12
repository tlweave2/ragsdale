#!/usr/bin/env python3
"""
Ragsdale Website – Meeting Changes Script
Based on Haylee / Jane meeting, March 12, 2026

Run from the repo root:
    python apply_meeting_changes.py

Creates .bak backups before writing each file.
"""

import os, shutil, re

REPO = os.path.dirname(os.path.abspath(__file__))
changes_log = []

def load(filename):
    path = os.path.join(REPO, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def save(filename, content, original):
    path = os.path.join(REPO, filename)
    bak  = path + '.meeting_bak'
    if not os.path.exists(bak):
        with open(bak, 'w', encoding='utf-8') as f:
            f.write(original)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def replace_once(content, old, new, label):
    if old not in content:
        changes_log.append(f"  ⚠ NOT FOUND – skipped: {label}")
        return content
    result = content.replace(old, new, 1)
    changes_log.append(f"  ✓ {label}")
    return result

def replace_regex(content, pattern, replacement, label, flags=re.DOTALL):
    result, n = re.subn(pattern, replacement, content, count=1, flags=flags)
    if n:
        changes_log.append(f"  ✓ {label}")
    else:
        changes_log.append(f"  ⚠ NOT FOUND – skipped: {label}")
    return result


# ─────────────────────────────────────────────────────────────
# INDEX.HTML
# ─────────────────────────────────────────────────────────────
changes_log.append("\n── index.html ──")
orig = load('index.html')
c = orig

# 1. Replace "From The Name You Know You Can Trust" heading
c = replace_once(c,
    'From The Name You Know You Can Trust',
    "We've Set the Gold Standard in Service, Sales &amp; Quick Turnaround",
    "Replace tagline: 'Name You Know You Can Trust' → gold standard slogan"
)

# 2. Fix double-s typo: "Energy Management Planss"
c = replace_once(c,
    'Energy Management Planss',
    'Energy Management Plans',
    "Fix typo: 'Energy Management Planss' → 'Energy Management Plans'"
)

# 3. Fix "Certified HVAC Technicians, and," → remove trailing ", and,"
c = replace_once(c,
    'Certified HVAC Technicians, and,',
    'Certified HVAC Technicians',
    "Fix punctuation: remove ', and,' after 'Certified HVAC Technicians'"
)

# 4. Remove "THE PREMIERE CHOICE" h2 heading only (keep the reviews widget below it)
c = replace_once(c,
    '<h2 class="cmp-title__text">THE PREMIERE CHOICE</h2>',
    '',
    "Remove 'THE PREMIERE CHOICE' heading"
)

# 5. Remove the black-box "Serving the Central Valley, California" section
#    This is the container with background-image: commercial.jpg
#    We match from that container open tag to its closing wrapper.
#    Strategy: remove the entire outer div that has the commercial.jpg background.
c = replace_regex(c,
    r'<div class="container-fluid wrapper [^"]*" id="container-426d0151c1"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>',
    '',
    "Remove 'Serving the Central Valley' black-box section (commercial.jpg background)"
)

# 6. Remove "Our Central Valley, CA HVAC Services" heading + its intro paragraph block
c = replace_regex(c,
    r'<div class="title title--text-center title--color-dark">\s*<div class="cmp-title "[^>]*>\s*<h2 class="cmp-title__text">Our Central Valley, CA HVAC Services</h2>\s*</div>\s*</div>',
    '',
    "Remove 'Our Central Valley, CA HVAC Services' section heading"
)

# 7. Suppress the popup/modal Julian image (comment it out so it's recoverable)
c = replace_once(c,
    '<div class="rai-dialog-container"></div>',
    '<!-- popup disabled per 2026-03-12 meeting -->\n<div class="rai-dialog-container" style="display:none;"></div>',
    "Disable Julian popup on page load"
)

save('index.html', c, orig)
print("index.html — done")


# ─────────────────────────────────────────────────────────────
# SERVICE-AREA.HTML  – keep the map, remove the county/city walls of text
# ─────────────────────────────────────────────────────────────
changes_log.append("\n── service-area.html ──")
orig = load('service-area.html')
c = orig

# Remove the dark-gradient "Offering Heating & Cooling Services Near You" section
# that contains all the county/city lists
c = replace_regex(c,
    r'<div class="container-fluid wrapper container--dark-gradient "[^>]*id="container-e5c8f55f01"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>',
    '',
    "Remove county/city list section from service area page"
)

# Also remove the blue/purple "Offering Services Near You" duplicate section
c = replace_regex(c,
    r'<div class="container-fluid wrapper container--light-gradient "[^>]*id="container-ce5da7c8b3"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>',
    '',
    "Remove duplicate 'Offering Services Near You' section"
)

save('service-area.html', c, orig)
print("service-area.html — done")


# ─────────────────────────────────────────────────────────────
# ALL PAGES – strip the "Air Quality" nav link from dropdown menus
# (Haylee: "we don't need air quality…right now")
# ─────────────────────────────────────────────────────────────
AIR_QUALITY_NAV = '''\
 <li class="main-header__nav-item-dropdown-link-item"> <a class="main-header__nav-item-dropdown-link" href="air-quality.html" target="_self"> <span class="main-header__nav-item-dropdown-link-text">Air Quality</span> </a> </li>'''

html_files = [f for f in os.listdir(REPO) if f.endswith('.html') and not f.endswith('.bak')]

changes_log.append("\n── Remove 'Air Quality' nav link from all pages ──")
for fname in sorted(html_files):
    orig_content = load(fname)
    if AIR_QUALITY_NAV in orig_content:
        new_content = orig_content.replace(AIR_QUALITY_NAV, '', 1)
        save(fname, new_content, orig_content)
        changes_log.append(f"  ✓ {fname}")


# ─────────────────────────────────────────────────────────────
# REPORT
# ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("CHANGE REPORT")
print("="*60)
for line in changes_log:
    print(line)

print("\n" + "="*60)
print("ITEMS REQUIRING HAYLEE'S INPUT BEFORE COMPLETION:")
print("="*60)
pending = [
    "1. Replacement slogan – currently set to 'We've Set the Gold Standard in Service, Sales & Quick Turnaround'.",
    "   Confirm with Haylee or swap once she emails the final wording.",
    "",
    "2. Goodman equipment images – need Haylee to identify which images are Goodman",
    "   and provide Carrier replacement photos. Goodman images flagged in image-gallery.html.",
    "",
    "3. Popup / promo slot – Julian's popup is disabled. Once Haylee sends promo graphic",
    "   and copy, re-enable with the new content.",
    "",
    "4. Top announcement bar – add a slim pre-season promo bar above the header once",
    "   Haylee confirms what special to run.",
    "",
    "5. HouseCall Pro reviews – needs Haylee to provide login so reviews can be linked.",
    "",
    "6. Careers tab – add once Haylee sends job descriptions / Indeed/LinkedIn links.",
    "",
    "7. New field photos – replace stock imagery once today's photo shoot is delivered.",
    "",
    "8. Buttons: round corners on header CTAs, convert nav dropdowns to flat buttons.",
    "   (CSS/design change – coordinate with Tim on implementation.)",
    "",
    "9. Font change from Arial/default to Poppins or similar.",
    "   (CSS change – coordinate with Tim.)",
    "",
    "10. Header color – change white header background to red as discussed.",
    "    (CSS change – coordinate with Tim.)",
]
for line in pending:
    print(line)

print("\n✅ Script complete. Check .meeting_bak files to restore any file if needed.")
