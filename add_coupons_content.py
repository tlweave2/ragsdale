#!/usr/bin/env python3
"""Add duct cleaning promotion and United Refrigeration partnership to coupons page"""

# Read the file
with open('/workspaces/ragsdale/coupons-and-savings.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add duct cleaning promotion card after air quality card
duct_cleaning_card = ''' <div class="card-container__card-holder"> <div class="coupons"> <div class="coupon-card "> <div class="coupon-card__main-container "> <div class="coupon-card__title-container"> <div class="coupon-card__img-container"> <img loading="lazy" src="images/thislogo.png" alt="Professional Duct Cleaning Special" class="coupon-card__logo"/> </div> <a> <h2 class="coupon-card__title">PROFESSIONAL DUCT CLEANING SPECIAL!</h2> </a> </div> <p class="coupon-card__description">IMPROVE YOUR INDOOR AIR QUALITY</p> </div> <div class="coupon-card__footer"> <div class="coupon-card__footer-content coupon-card__footer--has-text"> <p class="coupon-card__footer-heading">EXPIRES March 31, 2026</p> <p class="coupon-card__footer-description"><em>Restrictions apply. Coupon must be presented at time of service. Not to be combined with other offers. </em></p> </div> </div> </div> </div> </div>'''

# Find the air quality card and insert after it
air_quality_marker = '10% OFF INDOOR AIR QUALITY PRODUCTS!'
if air_quality_marker in content:
    # Find the end of the air quality card
    idx = content.find(air_quality_marker)
    # Find the closing divs after the card
    search_start = idx + len(air_quality_marker)
    # Look for the pattern that closes the air quality card before the next section
    closing_pattern = '</div> </div> </div> </div> </div> </div>'
    closing_idx = content.find(closing_pattern, search_start)
    
    if closing_idx > -1:
        # Insert the duct cleaning card before the closing divs
        insert_pos = closing_idx
        content = content[:insert_pos] + duct_cleaning_card + content[insert_pos:]
        print(f"✓ Added duct cleaning promotion card at position {insert_pos}")
    else:
       print("✗ Could not find closing pattern for air quality card")
else:
    print("✗ Could not find air quality card")

# 2. Add United Refrig partnership section after copyright
copyright_marker = 'License: #1037539</p> </div>'
united_refrig_section = ''' <div class="footer__partners-section text-center" style="margin-top: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.05); border-radius: 8px;"> <h4 style="color: #fff; font-size: 1.1rem; margin-bottom: 1rem; font-weight: 600;">Proud Elite Dealer Partner</h4> <div class="partner-logos d-flex justify-content-center align-items-center flex-wrap gap-3"> <div class="partner-logo-item" style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 6px; min-width: 150px;"> <img src="images/united-refrigeration-logo-placeholder.png" alt="United Refrigeration Elite Dealer" style="max-height: 60px; width: auto;" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';" /> <div style="display: none; color: #333; font-weight: 600; font-size: 0.9rem;">United Refrigeration<br/><span style="font-size: 0.8rem;">Elite Dealer</span></div> </div> </div>  </div>'''

if copyright_marker in content:
    idx = content.find(copyright_marker)
    insert_pos = idx + len(copyright_marker)
    content = content[:insert_pos] + united_refrig_section + content[insert_pos:]
    print(f"✓ Added United Refrigeration partnership section at position {insert_pos}")
else:
    print("✗ Could not find copyright marker")

# Write the updated content
with open('/workspaces/ragsdale/coupons-and-savings.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✓ Successfully updated coupons-and-savings.html")
