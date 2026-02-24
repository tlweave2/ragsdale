#!/usr/bin/env python3
"""
Add full navigation (header and footer) to all guide pages in guides/ folder.
"""

import re
from pathlib import Path

# CSS styles for the page
STYLES = """<style>
* { box-sizing: border-box; }
body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    color: #333;
}
.site-header {
    background: #fff;
    border-bottom: 3px solid #dc2626;
    padding: 15px 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
.header-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}
.site-logo img {
    height: 60px;
    width: auto;
}
.site-nav {
    display: flex;
    gap: 25px;
    align-items: center;
    flex-wrap: wrap;
}
.site-nav a {
    text-decoration: none;
    color: #1f2937;
    font-weight: 600;
    font-size: 15px;
    transition: color 0.3s;
}
.site-nav a:hover {
    color: #dc2626;
}
.header-cta {
    display: flex;
    gap: 12px;
    align-items: center;
}
.btn-phone {
    background: #dc2626;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
    font-size: 16px;
    transition: background 0.3s;
    white-space: nowrap;
}
.btn-phone:hover {
    background: #b91c1c;
}
.btn-schedule {
    background: #1e40af;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    font-weight: bold;
    font-size: 16px;
    border: none;
    cursor: pointer;
    transition: background 0.3s;
    white-space: nowrap;
}
.btn-schedule:hover {
    background: #1e3a8a;
}
.content-wrapper {
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
}
.content-wrapper h1 {
    color: #1e40af;
    font-size: 2.5em;
    margin-bottom: 20px;
}
.content-wrapper h2 {
    color: #1f2937;
    font-size: 1.8em;
    margin-top: 30px;
    margin-bottom: 15px;
}
.content-wrapper h3 {
    color: #374151;
    font-size: 1.3em;
    margin-top: 25px;
}
.content-wrapper ul, .content-wrapper ol {
    margin: 15px 0;
    padding-left: 30px;
}
.content-wrapper li {
    margin: 10px 0;
}
.content-wrapper a {
    color: #1e40af;
    text-decoration: underline;
}
.content-wrapper a:hover {
    color: #dc2626;
}
.content-wrapper hr {
    margin: 40px 0;
    border: none;
    border-top: 2px solid #e5e7eb;
}
.site-footer {
    background: #1f2937;
    color: #fff;
    padding: 40px 20px 20px;
    margin-top: 60px;
}
.footer-container {
    max-width: 1200px;
    margin: 0 auto;
}
.footer-logo {
    text-align: center;
    margin-bottom: 30px;
}
.footer-logo img {
    height: 50px;
    width: auto;
}
.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 30px;
    margin-bottom: 30px;
}
.footer-section h3 {
  color: #dc2626;
    margin-bottom: 15px;
    font-size: 16px;
}
.footer-section ul {
    list-style: none;
    padding: 0;
    margin: 0;
}
.footer-section ul li {
    margin-bottom: 8px;
}
.footer-section a {
    color: #d1d5db;
    text-decoration: none;
    font-size: 14px;
    transition: color 0.3s;
}
.footer-section a:hover {
    color: #fff;
}
.footer-bottom {
    border-top: 1px solid #374151;
    padding-top: 20px;
    text-align: center;
    color: #9ca3af;
    font-size: 14px;
}
@media (max-width: 768px) {
    .header-container {
        flex-direction: column;
        gap: 15px;
    }
    .site-nav {
        order: 3;
        width: 100%;
        justify-content: center;
        gap: 15px;
    }
    .header-cta {
        flex-direction: column;
        gap: 10px;
        width: 100%;
    }
    .btn-phone, .btn-schedule {
        width: 100%;
        text-align: center;
    }
    .content-wrapper h1 {
        font-size: 2em;
    }
    .content-wrapper h2 {
        font-size: 1.5em;
    }
}
</style>"""

# Header HTML (with ../ paths for guides subdirectory)
HEADER = """<header class="site-header">
    <div class="header-container">
        <div class="site-logo">
            <a href="../index.html">
                <img src="../images/thislogo.png" alt="Ragsdales's Heat & Air LLC"/>
            </a>
        </div>
        <nav class="site-nav">
            <a href="../air-conditioning.html">Air Conditioning</a>
            <a href="../heating.html">Heating</a>
            <a href="../about.html">About</a>
            <a href="../maintenance.html">Maintenance</a>
            <a href="../contact-us.html">Contact</a>
        </nav>
        <div class="header-cta">
            <a href="tel:2096336332" class="btn-phone">(209) 633-6332</a>
            <button class="btn-schedule" onclick="window.HouseCallProScheduler && window.HouseCallProScheduler.open()">Schedule Now</button>
        </div>
    </div>
</header>"""

# Footer HTML (with ../ paths for guides subdirectory)
FOOTER = """<footer class="site-footer">
    <div class="footer-container">
        <div class="footer-logo">
            <img src="../images/thislogo.png" alt="Ragsdales's Heat & Air LLC"/>
        </div>
        <div class="footer-content">
            <div class="footer-section">
                <h3>Services</h3>
                <ul>
                    <li><a href="../air-conditioning.html">Air Conditioning</a></li>
                    <li><a href="../heating.html">Heating</a></li>
                    <li><a href="../repairs.html">Repairs</a></li>
                    <li><a href="../maintenance.html">Maintenance</a></li>
                    <li><a href="../air-quality.html">Air Quality</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Company</h3>
                <ul>
                    <li><a href="../about.html">About Us</a></li>
                    <li><a href="../careers.html">Careers</a></li>
                    <li><a href="../service-area.html">Service Area</a></li>
                    <li><a href="../contact-us.html">Contact Us</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Help</h3>
                <ul>
                    <li><a href="../hvac-help-guides.html">Help Guides</a></li>
                    <li><a href="../financing.html">Financing</a></li>
                    <li><a href="../guarantees-warranties.html">Warranties</a></li>
                    <li><a href="../coupons-and-savings.html">Coupons</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Legal</h3>
                <ul>
                    <li><a href="../privacy-policy.html">Privacy Policy</a></li>
                    <li><a href="../terms-of-use.html">Terms of Use</a></li>
                    <li><a href="../sitemap.html">Sitemap</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© 2026 Ragsdales's Heat & Air LLC. All rights reserved. | License: #1037539</p>
            <p>Serving Manteca, Escalon, Farmington, Turlock, Hilmar, Ripon, Lathrop, Oakdale, Merced, Modesto & Central Valley, CA</p>
        </div>
    </div>
</footer>"""


def add_navigation_to_guide(filepath):
    """Add navigation to a guide page."""
    print(f"Processing {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation already exists
    if 'site-header' in content:
        print(f"  ✓ {filepath} already has navigation, skipping")
        return
    
    # Add styles before </head>
    if STYLES not in content:
        content = content.replace('</head>', f'{STYLES}\n</head>')
    
    # Add header after <body>
    if '<header class="site-header">' not in content:
        content = content.replace('<body>', f'<body>\n{HEADER}')
    
    # Wrap existing content div in content-wrapper
    # Find the opening <div class="content"> tag
    content_match = re.search(r'<div class="content">', content)
    if content_match:
        # Replace the opening div
        content = content.replace('<div class="content">', '<div class="content-wrapper">', 1)
    
    # Add footer before the HouseCall Pro scripts or before </body>
    if '<footer class="site-footer">' not in content:
        # Find the HouseCall Pro comment or scripts
        hcp_match = re.search(r'<!-- HouseCall Pro Booking Integration -->', content)
        if hcp_match:
            content = content.replace('<!-- HouseCall Pro Booking Integration -->', 
                                     f'{FOOTER}\n\n<!-- HouseCall Pro Booking Integration -->', 1)
        else:
            # If no HouseCall Pro, add before </body>
            content = content.replace('</body>', f'{FOOTER}\n\n<!-- HouseCall Pro Booking Integration -->\n<script src="../housecallpro-config.js"></script>\n<script src="../housecallpro-booking-simple.js"></script>\n</body>')
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"  ✓ Navigation added to {filepath}")


def main():
    """Process all guide pages."""
    guides_dir = Path('guides')
    
    if not guides_dir.exists():
        print("Error: guides/ directory not found")
        return
    
    guide_files = list(guides_dir.glob('*.html'))
    
    if not guide_files:
        print("No HTML files found in guides/ directory")
        return
    
    print(f"Found {len(guide_files)} guide pages to process\n")
    
    for guide_file in guide_files:
        add_navigation_to_guide(guide_file)
    
    print(f"\n✅ Successfully processed {len(guide_files)} guide pages!")
    print("\nGuide pages now have:")
    print("  ✓ Full header navigation with logo, menu, phone, and Schedule button")
    print("  ✓ Professional footer with service links")
    print("  ✓ Responsive design for mobile devices")
    print("  ✓ HouseCall Pro booking integration")


if __name__ == '__main__':
    main()
