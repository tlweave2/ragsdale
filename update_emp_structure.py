#!/usr/bin/env python3
"""
Update maintenance pages to reflect Energy Management Plans (EMP) two-tier structure
with Gold Plan (twice-yearly) and Black Plan (once-yearly)
"""

import re

def update_maintenance_html():
    """Update maintenance.html with EMP Gold/Black structure"""
    
    with open('/workspaces/ragsdale/maintenance.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update hero banner title
    content = content.replace(
        '<h1>Ragsdales Priority<br />\nMaintenance Membership</h1>',
        '<h1>Ragsdale\'s Energy<br />\nManagement Plans (EMP)</h1>'
    )
    
    # 2. Update subtitle
    content = content.replace(
        'Ragsdales Priority Members Keep Money In Their Pocket',
        'Stay Ahead of Breakdowns with Hassle-Free Comfort'
    )
    
    # 3. Update card title for plan tiers
    content = content.replace(
        'Here are a few reasons why a you&#39;ll feel like a VIP as a Ragsdales Priority Member:',
        'Two Flexible Membership Levels for Reliable Comfort:'
    )
    
    # 4. Replace the four tick-list items with two plan descriptions
    # Find and replace the tick list section
    old_tick_pattern = r'(<div class="tick-list__item-text">\s*<h3 class="tick-list__item-title">\s*Priority Service:.*?</h3>\s*</div>\s*</li>\s*<li class="d-flex tick-list__item">.*?Special Giveaways:.*?</h3>\s*</div>\s*</li>)'
    
    new_tick_items = '''<div class="tick-list__item-text">
                        <h3 class="tick-list__item-title">
                          <strong>Gold Plan</strong> – Twice-yearly comprehensive service (spring AC tune-up + fall heating check). Ideal for maximum efficiency and protection.
                        </h3>
                      </div>
                    </li>
                    <li class="d-flex tick-list__item">
                      <div class="tick-list__item-icon">
                        <div class="d-flex justify-content-center align-middle align-items-center wg-round-icon wg-round-icon--small">
                          <span class="wg-round-icon__icon wg-icon-checkmark"></span>
                        </div>
                      </div>
                      <div class="tick-list__item-text">
                        <h3 class="tick-list__item-title">
                          <strong>Black Plan</strong> – Once-yearly service. Perfect for dependable basic coverage.
                        </h3>
                      </div>
                    </li>'''
    
    content = re.sub(old_tick_pattern, new_tick_items, content, flags=re.DOTALL)
    
    # 5. Update main description text
    content = content.replace(
        'When you have a Ragsdales Priority Membership, you can trust our expert team',
        'When you have a Ragsdale\'s Energy Management Plan, you can trust our expert team'
    )
    content = content.replace(
        '<strong>Ask Our Team Member About A Ragsdales Priority Membership</strong>',
        '<strong>Ask Our Team About Ragsdale\'s Energy Management Plans</strong>'
    )
    
    # 6. Update benefits section title
    content = content.replace(
        'What You Get As A Ragsdales Priority Member',
        'Key Benefits Include:'
    )
    
    # 7. Reorganize benefits list to highlight key benefits
    old_benefits = '<ul><li>Members-Only Hotline</li><li>Two HVAC Maintenance Visits Per Year</li><li>FREE Drain Cabling Services - must have cleanout up to 75 feet ($328&#43; Value)</li><li>15% Off Any Repairs Needed (All Services)</li><li>5% Off Equipment, HVAC Systems, Water Heaters, Generators, etc.</li><li>$30 Off Trip/Diagnostic Fee</li><li>Fast, Priority Service</li><li>5-Year Parts &amp; Labor Warranty On Repairs</li><li>Schedule Reminders</li><li>Members-Only Newsletter</li><li>Members-Only Special Offers</li><li>HVAC Safety Inspections At Every Visit</li><li></li></ul>'
    
    new_benefits = '''<ul><li><strong>Priority scheduling</strong> – Get faster service when demand is high</li><li><strong>Discounted repairs</strong> – 15% off qualifying work</li><li><strong>$30 off diagnostic service calls</strong></li><li><strong>24-hour emergency service access</strong></li><li><strong>Exclusive newsletter</strong> with tips and special offers</li><li><strong>Extended warranties on repairs for members</strong> – 5-year parts &amp; labor coverage</li><li><strong>Members-Only Hotline</strong></li><li><strong>FREE Drain Cabling Services</strong> - must have cleanout up to 75 feet ($328+ Value)</li><li><strong>5% Off Equipment</strong> - HVAC Systems, Water Heaters, Generators, etc.</li><li><strong>HVAC Safety Inspections</strong> At Every Visit</li></ul>'''
    
    content = content.replace(old_benefits, new_benefits)
    
    # 8. Update FAQ section title
    content = content.replace(
        'Frequently Asked Questions for Ragsdales Priority Maintenance',
        'Frequently Asked Questions for Ragsdale\'s Energy Management Plans'
    )
    
    # 9. Update meta description
    content = content.replace(
        'When you have a Ragsdales Priority Membership, you can trust our expert team is doing everything possible',
        'Choose the Gold Plan (twice-yearly) or Black Plan (once-yearly). Ragsdale\'s Energy Management Plans ensure reliable comfort'
    )
    
    # 10. Update page title
    content = content.replace(
        '<title>Maintenance Plans for Central Valley, CA - Ragsdales\'s Heat &amp; Air LLC</title>',
        '<title>Energy Management Plans - Central Valley, CA - Ragsdales\'s Heat &amp; Air LLC</title>'
    )
    
    # 11. Update FAQ question about Priority Membership
    content = content.replace(
        'Q: What is the pricing for a Ragsdales Priority Membership',
        'Q: What is the pricing for Ragsdale\'s Energy Management Plans'
    )
    content = content.replace(
        'Q: Are service calls free as a Ragsdales Priority Member?',
        'Q: Are service calls free as an EMP member?'
    )
    content = content.replace(
        'A: Ragsdales Priority Members receive a 15% discount',
        'A: EMP members receive a 15% discount'
    )
    content = content.replace(
        'Q: Will Ragsdales contact me when it&#39;s time for my visits?',
        'Q: Will Ragsdale\'s contact me when it&#39;s time for my visits?'
    )
    content = content.replace(
        'we send our Ragsdales Priority Members email',
        'we send our EMP members email'
    )
    content = content.replace(
        'Q: Does Ragsdales offer payment plans?',
        'Q: Does Ragsdale\'s offer payment plans?'
    )
    content = content.replace(
        'A: Yes! Ragsdales Priority Members can make convenient',
        'A: Yes! EMP members can make convenient'
    )
    
    with open('/workspaces/ragsdale/maintenance.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Updated maintenance.html with EMP Gold/Black structure")

def update_maintenance_renewal():
    """Update maintenance-renewal.html with EMP terminology"""
    
    with open('/workspaces/ragsdale/maintenance-renewal.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update all Priority Membership references
    content = content.replace('Ragsdales Priority Membership', 'Ragsdale\'s Energy Management Plan')
    content = content.replace('Ragsdale Priority Membership', 'Ragsdale\'s Energy Management Plan')
    content = content.replace('Ragsdales Priority Member', 'EMP member')
    content = content.replace('Priority Member', 'EMP member')
    
    # Update title
    content = content.replace(
        'Keep Receiving Ragsdales Priority Membership Benefits!',
        'Keep Receiving Your Energy Management Plan Benefits!'
    )
    
    # Update VIP reasons
    content = content.replace(
        'why a you&#39;ll feel like a VIP as a Ragsdales Priority Member',
        'why you\'ll feel like a VIP with your Energy Management Plan'
    )
    
    with open('/workspaces/ragsdale/maintenance-renewal.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Updated maintenance-renewal.html with EMP terminology")

if __name__ == '__main__':
    print("Updating maintenance pages with Energy Management Plans structure...")
    update_maintenance_html()
    update_maintenance_renewal()
    print("\n✅ All updates complete!")
    print("\nChanges made:")
    print("  • Renamed 'Priority Membership' to 'Energy Management Plans (EMP)'")
    print("  • Added Gold Plan (twice-yearly) and Black Plan (once-yearly) descriptions")
    print("  • Reorganized benefits to highlight key features")
    print("  • Updated all FAQ references to EMP")
    print("  • Updated meta descriptions and page titles")
