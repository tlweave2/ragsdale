#!/usr/bin/env python3
"""
apply_haylee_changes_march12.py
Applies Haylee's March 12, 2026 feedback changes to the Ragsdale website.
Run from the root of the ragsdale repo: python3 apply_haylee_changes_march12.py
"""

import os, re, shutil
from datetime import datetime

REPO = os.path.dirname(os.path.abspath(__file__))
BACKUP_SUFFIX = ".haylee_mar12_bak"
LOG = []

def backup(path):
    bak = path + BACKUP_SUFFIX
    if not os.path.exists(bak):
        shutil.copy2(path, bak)

def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def replace_once(content, old, new, label):
    if old in content:
        LOG.append(f"  ✅ {label}")
        return content.replace(old, new, 1)
    else:
        LOG.append(f"  ⚠️  NOT FOUND: {label}")
        return content

def replace_all(content, old, new, label):
    count = content.count(old)
    if count:
        LOG.append(f"  ✅ {label} ({count}x)")
        return content.replace(old, new)
    else:
        LOG.append(f"  ⚠️  NOT FOUND: {label}")
        return content

# ─────────────────────────────────────────────
# 1. SITEWIDE: "Energy Management Plan" → "Energy Management Program"
#    Applies to all HTML files
# ─────────────────────────────────────────────
print("\n[1/7] Sitewide: Energy Management Plan → Program")
html_files = [f for f in os.listdir(REPO) if f.endswith(".html")]
total_plan = 0
for fname in html_files:
    path = os.path.join(REPO, fname)
    content = read(path)
    # Only touch files that actually have the phrase
    hits = content.count("Energy Management Plan")
    if hits:
        backup(path)
        content = content.replace("Energy Management Plan", "Energy Management Program")
        write(path, content)
        total_plan += hits
        print(f"  ✅ {fname} ({hits} replacements)")
print(f"  Total: {total_plan} replacements across site")

# ─────────────────────────────────────────────
# 2. maintenance-renewal.html
# ─────────────────────────────────────────────
print("\n[2/7] maintenance-renewal.html")
path = os.path.join(REPO, "maintenance-renewal.html")
if os.path.exists(path):
    backup(path)
    c = read(path)
    LOG.clear()

    # Heading: "Keep Receiving..." → "Don't Miss Out..."
    c = replace_once(c,
        "Keep Receiving Your Energy Management Program Benefits!",
        "Don't Miss Out on Your Energy Management Benefits!",
        "Renewal page heading")

    # Also catch the variant without "Program" (in case step 1 didn't run first)
    c = replace_once(c,
        "Keep Receiving Your Energy Management Plan Benefits!",
        "Don't Miss Out on Your Energy Management Benefits!",
        "Renewal page heading (Plan variant)")

    # Body paragraph — replace old copy with Haylee's exact copy
    old_para = ("HVAC repairs are often unexpected, and can be quite costly. "
                "When you have a Ragsdale&#39;s Energy Management Program, you can trust our expert team is doing everything possible "
                "to maintain your system and catch any issues before they become expensive problems. "
                "We work hard to ensure you get the maximum performance out of your heating and air conditioning unit or HVAC system for as long as possible.")
    # Try both apostrophe encodings
    new_para = ("HVAC repairs are often unexpected—and can be costly. "
                "With a Ragsdale&#39;s Energy Management Program, you can trust our expert team to proactively maintain your system "
                "and catch potential issues before they become expensive problems. "
                "We work hard to ensure your heating and air conditioning units, or your entire HVAC system, "
                "deliver maximum performance and efficiency for years to come.")
    c = replace_once(c, old_para, new_para, "Renewal body paragraph (encoded apostrophe)")

    # Try unencoded version too
    old_para2 = ("HVAC repairs are often unexpected, and can be quite costly. "
                 "When you have a Ragsdale's Energy Management Program, you can trust our expert team is doing everything possible "
                 "to maintain your system and catch any issues before they become expensive problems. "
                 "We work hard to ensure you get the maximum performance out of your heating and air conditioning unit or HVAC system for as long as possible.")
    new_para2 = ("HVAC repairs are often unexpected—and can be costly. "
                 "With a Ragsdale's Energy Management Program, you can trust our expert team to proactively maintain your system "
                 "and catch potential issues before they become expensive problems. "
                 "We work hard to ensure your heating and air conditioning units, or your entire HVAC system, "
                 "deliver maximum performance and efficiency for years to come.")
    c = replace_once(c, old_para2, new_para2, "Renewal body paragraph (plain apostrophe)")

    write(path, c)
    for l in LOG: print(l)
else:
    print("  ⚠️  maintenance-renewal.html NOT FOUND")

# ─────────────────────────────────────────────
# 3. maintenance.html — Key Benefits section
# ─────────────────────────────────────────────
print("\n[3/7] maintenance.html — Key Benefits → Our Commitment to You")
path = os.path.join(REPO, "maintenance.html")
if os.path.exists(path):
    backup(path)
    c = read(path)
    LOG.clear()

    # Section heading
    c = replace_all(c,
        "Key Benefits Include:",
        "Our Commitment to You",
        "Section heading 'Key Benefits Include:' → 'Our Commitment to You'")

    # Replace the old bullet list in the light-background (Gold plan) section
    # This is the second benefits block — the one with the empty trailing <li>
    old_bullets = ("<ul><li>Members-Only Hotline</li>"
                   "<li>Two HVAC Maintenance Visits Per Year</li>"
                   "<li>FREE Drain Cabling Services ($328&#43; Value)</li>"
                   "<li>15% Off Any Repairs Needed (All Services)</li>"
                   "<li>5% Off Equipment, HVAC Systems, Water Heaters, Generators, etc.</li>"
                   "<li>$30 Off Trip/Diagnostic Fee</li>"
                   "<li>Fast, Priority Service</li>"
                   "<li>5-Year Parts &amp; Labor Warranty On Repairs</li>"
                   "<li>Members-Only Newsletter</li>"
                   "<li>Members-Only Special Offers</li>"
                   "<li>HVAC Safety Inspections At Every Visit</li>"
                   "<li></li></ul>")
    new_bullets = ("<ul>"
                   "<li>Priority Scheduling: Get faster service during peak seasons when demand is high.</li>"
                   "<li>Extended Equipment Life: Regular maintenance helps prolong the lifespan of your HVAC system, saving you money on replacements.</li>"
                   "<li>2.5% discount on any future needs of your HVAC system.</li>"
                   "<li>Two HVAC Maintenance Visits Per Year &#8211; Spring &amp; Fall dependent on plan chosen</li>"
                   "<li>Members-Only Special Offers</li>"
                   "<li>HVAC Safety Inspections At Every Visit</li>"
                   "</ul>")
    c = replace_once(c, old_bullets, new_bullets, "Full benefits bullet list replacement")

    # Also remove the stale "Priority Service" tick bullet that was left over
    old_tick = ("<li class=\"d-flex tick-list__item\"> <div class=\"tick-list__item-icon\"> "
                "<div class=\"d-flex justify-content-center align-middle align-items-center wg-round-icon wg-round-icon--small\"> "
                "<span class=\"wg-round-icon__icon wg-icon-checkmark\"></span> </div> </div> "
                "<div class=\"tick-list__item-text\"> <h3 class=\"tick-list__item-title\"> "
                "Priority Service: Any day, or night. Our Members receive priority over anyone else. "
                "</h3> </div> </li>")
    c = replace_once(c, old_tick, "", "Remove stale 'Priority Service' tick bullet")

    write(path, c)
    for l in LOG: print(l)
else:
    print("  ⚠️  maintenance.html NOT FOUND")

# ─────────────────────────────────────────────
# 4. index.html — homepage text changes
# ─────────────────────────────────────────────
print("\n[4/7] index.html — homepage copy changes")
path = os.path.join(REPO, "index.html")
if os.path.exists(path):
    backup(path)
    c = read(path)
    LOG.clear()

    # Hero subheading on about page hero (appears on about.html too, handled below)
    # "From The Name You Know You Can Trust" → "We Set The Standard High"
    c = replace_all(c,
        "From The Name You Know You Can Trust",
        "We Set The Standard High",
        "'From The Name You Know You Can Trust' → 'We Set The Standard High'")

    c = replace_all(c,
        "The Name You Know You Can Trust",
        "We Set The Standard High",
        "'The Name You Know You Can Trust' → 'We Set The Standard High'")

    # Replace the Ragsdales Offers bullet list with Haylee's new copy
    old_offers = ("<ul><li>2-year parts &amp; labor warranty on repairs; 5-year for priority members</li>"
                  "<li>Service and repair on all makes and models</li>"
                  "<li>Peace of mind with Energy Management Programs</li>"
                  "<li>Certified HVAC Technicians,</li>"
                  "<li>Quality craftsmanship and professionalism of our Technicians, Customer Service Representatives, and entire Ragsdales team</li>"
                  "<li>24 Hour Customer Service</li>"
                  "<li>100% Customer Satisfaction Guarantee</li></ul>")
    new_offers = ("<ul>"
                  "<li>Service and repair on all makes and models</li>"
                  "<li>Peace of mind with Energy Management Programs</li>"
                  "<li>Deliver quality workmanship and professional service through our experienced technicians and dedicated customer service team.</li>"
                  "<li>100% Customer Satisfaction Guarantee</li>"
                  "</ul>")
    c = replace_once(c, old_offers, new_offers, "Ragsdales Offers bullet list")

    # "Schedule Now" → "Book Now" (header CTA button)
    c = replace_all(c, ">Schedule Now<", ">Book Now<", "'Schedule Now' → 'Book Now'")

    # "Service Area" label → "Areas We Proudly Serve"
    c = replace_all(c,
        ">Service Area<",
        ">Areas We Proudly Serve<",
        "'Service Area' → 'Areas We Proudly Serve'")

    # "Promotions" label → "Current Specials"
    c = replace_all(c,
        ">Promotions<",
        ">Current Specials<",
        "'Promotions' → 'Current Specials'")

    # Fix "8 years" body text → founded 1986
    c = replace_all(c,
        "Ragsdales has serviced Central Valley, CA for 8 years",
        "Ragsdales has served Central Valley, CA since 1986",
        "'8 years' body text → 'since 1986'")

    write(path, c)
    for l in LOG: print(l)
else:
    print("  ⚠️  index.html NOT FOUND")

# ─────────────────────────────────────────────
# 5. about.html — remove old hero tagline
# ─────────────────────────────────────────────
print("\n[5/7] about.html — hero tagline")
path = os.path.join(REPO, "about.html")
if os.path.exists(path):
    backup(path)
    c = read(path)
    LOG.clear()

    c = replace_all(c,
        "The Name You Know You Can Trust",
        "We Set The Standard High",
        "Hero tagline replacement on About page")

    write(path, c)
    for l in LOG: print(l)
else:
    print("  ⚠️  about.html NOT FOUND")

# ─────────────────────────────────────────────
# 6. ac-repair.html — "Talk to Art" fix
# ─────────────────────────────────────────────
print("\n[6/7] ac-repair.html — 'Talk to Art'")
path = os.path.join(REPO, "ac-repair.html")
if os.path.exists(path):
    backup(path)
    c = read(path)
    LOG.clear()

    c = replace_once(c,
        ">Talk to Art<",
        ">Contact Us<",
        "'Talk to Art' link text → 'Contact Us'")
    # Also fix the surrounding sentence
    c = replace_once(c,
        "you can reach the Ragsdales family at Ragsdales&#39;s Heat &amp; Air LLC, via our online form",
        "you can reach the Ragsdale family directly via our online form",
        "Fix 'Talk to Art' surrounding sentence")
    c = replace_once(c,
        "you can reach the Ragsdales family at Ragsdales's Heat &amp; Air LLC, via our online form",
        "you can reach the Ragsdale family directly via our online form",
        "Fix 'Talk to Art' surrounding sentence (alt encoding)")

    write(path, c)
    for l in LOG: print(l)
else:
    print("  ⚠️  ac-repair.html NOT FOUND")

# ─────────────────────────────────────────────
# 7. Meta descriptions — fix "8 years" and "since 2018"
# ─────────────────────────────────────────────
print("\n[7/7] Meta description fixes — '8 years' and 'since 2018'")
meta_fixes = {
    "ac-tune-up.html": [
        ("Serving Central Valley, CA for over 8 years!", "Serving Central Valley, CA since 1986!")
    ],
    "heating.html": [
        ("Serving the area for over 8 years!", "Serving Central Valley, CA since 1986!")
    ],
    "heating-tune-up.html": [
        ("Serving the area for over 8 years!", "Serving Central Valley, CA since 1986!")
    ],
    "heating-equipment.html": [
        ("Serving Central Valley since 2018", "Serving Central Valley since 1986")
    ],
    "ac-equipment.html": [
        ("Serving Central Valley since 2018", "Serving Central Valley since 1986")
    ],
}
for fname, fixes in meta_fixes.items():
    path = os.path.join(REPO, fname)
    if os.path.exists(path):
        backup(path)
        c = read(path)
        for old, new in fixes:
            if old in c:
                c = c.replace(old, new)
                print(f"  ✅ {fname}: '{old}' → '{new}'")
            else:
                print(f"  ⚠️  {fname}: NOT FOUND: '{old}'")
        write(path, c)
    else:
        print(f"  ⚠️  {fname} NOT FOUND")

# ─────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────
print("\n" + "="*55)
print("✅ Script complete.")
print("Backup files written as *.haylee_mar12_bak")
print("")
print("STILL NEEDS MANUAL WORK (requires template/nav changes):")
print("  - Nav restructure (Our Services merge, Financing tab, EMP tab)")
print("  - Duct Cleaning service page (new page needed)")
print("  - Free Second Opinions page/mention")
print("  - Footer simplification (map snippet, remove excess links)")
print("  - Instagram feed integration on homepage")
print("  - Maintenance image carousel (awaiting images from Haylee)")
print("  - HVAC Services / Help Guides section hide on homepage")
print("  - Warranties/Financing/Promotions cards — move off homepage")
print("  - Coupons page heading (awaiting Haylee final word)")
print("  - Reviews vs Testimonials (awaiting Haylee confirmation)")
print("  - LinkedIn (awaiting Haylee decision)")
print("="*55)
