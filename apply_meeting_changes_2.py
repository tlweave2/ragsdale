#!/usr/bin/env python3
"""
Ragsdale Website – Meeting Changes Script #2
Handles the three remaining items from the March 12 2026 meeting:

  A) Remove black subheader overlay boxes (section under hero on inner pages)
  B) Service area page – strip remaining city-list text, leave map div clean
  C) All pages – replace the full dropdown nav with four flat buttons
     (Air Conditioning | Heating | Maintenance | Why Us?)

Run from the repo root:
    python apply_meeting_changes_2.py
"""

import os, re

REPO = os.path.dirname(os.path.abspath(__file__))
log = []

def load(filename):
    path = os.path.join(REPO, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def save(filename, content, original):
    path = os.path.join(REPO, filename)
    bak = path + '.meeting2_bak'
    if not os.path.exists(bak):
        with open(bak, 'w', encoding='utf-8') as f:
            f.write(original)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def sub(content, pattern, replacement, label, flags=re.DOTALL):
    result, n = re.subn(pattern, replacement, content, count=1, flags=flags)
    if n:
        log.append(f'  ✓ {label}')
    else:
        log.append(f'  ⚠ NOT FOUND – skipped: {label}')
    return result

def replace(content, old, new, label):
    if old in content:
        log.append(f'  ✓ {label}')
        return content.replace(old, new, 1)
    log.append(f'  ⚠ NOT FOUND – skipped: {label}')
    return content


# ─────────────────────────────────────────────────────────────────────────────
# A) BLACK OVERLAY BOXES
#
# In the original site these are the dark `container--dark-gradient` or
# `container--black` banner blocks that appear as a subheader strip beneath
# the hero on many pages, e.g. the "Serving the Central Valley, California"
# block with a background image (commercial.jpg / trucks photo).
#
# On index.html that specific block was already removed in script 1.
# The remaining pattern is the eyebrow-header dark bar that sits above the
# main header – Haylee called it the "black box" above the truck photos and
# the section heading strips.  We hide the eyebrow entirely via CSS injected
# into every page's <head>, which is the safest non-destructive approach
# (keeps the HTML intact, easy to re-enable later for the promo bar).
# ─────────────────────────────────────────────────────────────────────────────

EYEBROW_HIDE_CSS = '<style>/* meeting 2026-03-12: hide eyebrow bar */ .header__eyebrow-container { display: none !important; }</style>'

html_files = sorted([
    f for f in os.listdir(REPO)
    if f.endswith('.html') and not f.endswith('.bak')
])

log.append('\n── A) Hide eyebrow/subheader black bar on all pages (CSS inject) ──')
for fname in html_files:
    orig = load(fname)
    if EYEBROW_HIDE_CSS in orig:
        log.append(f'  – {fname} already patched, skipping')
        continue
    if '</head>' not in orig:
        log.append(f'  ⚠ no </head> in {fname}, skipping')
        continue
    new = orig.replace('</head>', f'{EYEBROW_HIDE_CSS}\n</head>', 1)
    save(fname, new, orig)
    log.append(f'  ✓ {fname}')


# ─────────────────────────────────────────────────────────────────────────────
# B) SERVICE-AREA.HTML – strip remaining "Offering Services Near You" body text
#    that was inside the purple/light-gradient container not caught in script 1,
#    and clean up the lingering "Offering Heating & Cooling Services Near You"
#    dark section if it survived.  Leave the map div untouched.
# ─────────────────────────────────────────────────────────────────────────────

log.append('\n── B) service-area.html cleanup ──')
orig = load('service-area.html')
c = orig

# Remove any remaining dark-gradient county/city blob (belt-and-suspenders)
c = sub(c,
    r'<div[^>]*container--dark-gradient[^>]*>.*?(?=<div class="container responsivegrid)',
    '',
    'Remove dark-gradient county/city section (belt-and-suspenders)'
)

# Remove the "Offering Services Near You" purple section if still present
c = sub(c,
    r'<h2 class="cmp-title__text">Offering Services Near You</h2>.*?(?=</div>\s*</div>\s*</div>\s*</div>\s*<div class="container)',
    '',
    'Remove "Offering Services Near You" heading + body'
)

# Remove the 770-area-code phone number that's still in the service-card
c = replace(c,
    'Give us a call at 770-441-4141 to confirm we don&#39;t service your area.',
    'Give us a call at (209) 633-6332 to confirm we don\'t service your area.',
    'Fix wrong phone number in service area card (770 → 209)'
)

save('service-area.html', c, orig)


# ─────────────────────────────────────────────────────────────────────────────
# C) REPLACE DROPDOWN NAV WITH FOUR FLAT BUTTONS ON ALL PAGES
#
# The existing nav contains three top-level dropdown items:
#   Air Conditioning (with sub-menu)
#   Heating (with sub-menu)
#   Why Us?
#   Maintenance (with sub-menu)
#   Search
#
# Haylee asked to collapse these to four flat clickable buttons:
#   Air Conditioning | Heating | Maintenance | Why Us?
# (no dropdowns for now – keeping it simple until content is ready)
#
# Strategy: replace the entire <ul class="main-header__nav-wrapper"> ... </ul>
# block (which contains all the dropdown li items) with a lean flat-button ul.
# We preserve the Search li since it controls the search input toggle.
#
# The new markup uses the same BEM classes so existing CSS styles it correctly.
# ─────────────────────────────────────────────────────────────────────────────

FLAT_NAV = '''\
<ul class="main-header__nav-wrapper main-header__nav" role="menubar">
 <li class="main-header__nav-item" role="menuitem">
  <a class="main-header__nav-item-link main-header__nav-item-link--has-no-sub-menu" href="air-conditioning.html" aria-label="Air Conditioning">Air Conditioning</a>
 </li>
 <li class="main-header__nav-item" role="menuitem">
  <a class="main-header__nav-item-link main-header__nav-item-link--has-no-sub-menu" href="heating.html" aria-label="Heating">Heating</a>
 </li>
 <li class="main-header__nav-item" role="menuitem">
  <a class="main-header__nav-item-link main-header__nav-item-link--has-no-sub-menu" href="maintenance.html" aria-label="Maintenance">Maintenance</a>
 </li>
 <li class="main-header__nav-item" role="menuitem">
  <a class="main-header__nav-item-link main-header__nav-item-link--has-no-sub-menu" href="about.html" aria-label="Why Us?">Why Us?</a>
 </li>
 <li class="main-header__nav-item main-header__nav-item--search" role="menuitem">
  <a class="main-header__nav-item-link main-header__nav-item-link--has-no-sub-menu" aria-expanded="false" aria-haspopup="false" href="#" aria-label="header nav search">Search <button class="main-header__nav-search-icon wg-icon wg-icon-search"></button></a>
 </li>
</ul>'''

# Pattern matches the opening of the nav ul through End: Main Elements comment
NAV_PATTERN = (
    r'<ul class="main-header__nav-wrapper[^"]*"[^>]*role="menubar">.*?'
    r'<!-- End: Main Elements -->'
)
NAV_REPLACEMENT = FLAT_NAV + '\n<!-- End: Main Elements -->'

log.append('\n── C) Replace dropdown nav with flat buttons on all pages ──')
for fname in html_files:
    orig = load(fname)
    if 'main-header__nav-wrapper' not in orig:
        continue
    new, n = re.subn(NAV_PATTERN, NAV_REPLACEMENT, orig, count=1, flags=re.DOTALL)
    if n:
        save(fname, new, orig)
        log.append(f'  ✓ {fname}')
    else:
        log.append(f'  ⚠ pattern not matched in {fname}')


# ─────────────────────────────────────────────────────────────────────────────
# REPORT
# ─────────────────────────────────────────────────────────────────────────────
print('\n' + '='*60)
print('CHANGE REPORT – Script 2')
print('='*60)
for line in log:
    print(line)

print('\n' + '='*60)
print('NOTES FOR TIM / HAYLEE')
print('='*60)
print('''
A) Eyebrow bar hidden via CSS (display:none). When Haylee confirms the
   promo/announcement bar copy, remove that CSS rule and populate the
   .header__notification-bar element with the promo text instead.

B) Service area – the map div (id="service-area-map") is untouched.
   The city/county list text blocks have been removed.
   The old 770 phone number in the service card was corrected to (209) 633-6332.

C) Nav dropdowns replaced with four flat buttons sitewide:
     Air Conditioning → air-conditioning.html
     Heating          → heating.html
     Maintenance      → maintenance.html
     Why Us?          → about.html
   Search toggle preserved. Mobile hamburger menu is unaffected.
   If Haylee wants to add more pages to the nav later (Careers, etc.)
   just add more <li> items to the FLAT_NAV block in this script and re-run,
   or edit index.html and copy the pattern to other pages.

.meeting2_bak files saved next to each changed file for rollback.
''')
print('✅ Script 2 complete.')
