#!/usr/bin/env python3
"""
Script to replace all SVG placeholder images with actual images
"""

import os
import re
from pathlib import Path

# Define the placeholder SVG pattern
PLACEHOLDER_SVG = r'data:image/svg\+xml,%3Csvg xmlns="http://www\.w3\.org/2000/svg" width="400" height="300"%3E%3Crect fill="%23ddd" width="400" height="300"/%3E%3Ctext x="50%25" y="50%25" dominant-baseline="middle" text-anchor="middle" font-family="Arial" font-size="14" fill="%23666"%3EImage Placeholder%3C/text%3E%3C/svg%3E'

# Image mapping based on alt text keywords
IMAGE_MAPPINGS = {
    # Navigation icons
    r'alt="Air Conditioning Icon"': 'images/icon-cooling-red.png',
    r'alt="Heating Icon"': 'images/icon-heating-red.png',
    r'alt="Hands shaking icon"': 'images/icon-heating-red.png',  # Placeholder for now
    
    # Hero images
    r'alt="Ragsdaless Hero Placeholder"': 'images/hero-truck.jpg',
    r'alt="Ragsdaless van pulling up driveway"': 'images/van-driveway.jpg',
    r'alt="Ragsdaless employee in back of truck"': 'images/tech-at-back-of-truck.jpg',
    r'alt="Ragsdaless employee smiling by back of truck"': 'images/tech-at-back-of-truck.jpg',
    
    # Team & Management
    r'alt="Art Ragsdaless, President smiling for camera "': 'images/art-ragsdales-president.jpg',
    r'alt="Ragsdaless Team Photo 2024"': 'images/team-photo.jpg',
    r'alt="Ragsdaless Office"': 'images/office-building.jpg',
    
    # Customer interactions
    r'alt="Customer greeting Ragsdaless technician"': 'images/tech-greeting-customer.jpg',
    r'alt="Customer service representative with headset on"': 'images/customer-service-headset.jpg',
    r'alt="Ragsdaless Team Member Talking with Homeowner at Kitchen Counter"': 'images/tech-kitchen-consultation.jpg',
    r'alt="Smiling Customer Service Representative at Ragsdaless"': 'images/customer-service-rep.jpg',
    r'alt="Ragsdaless Technician Explaining Options Outdoors"': 'images/tech-explaining-options.jpg',
    r'alt="Professional HVAC Technician from Ragsdaless Inpsecting Outdoor Units"': 'images/tech-outdoor-unit.jpg',
    r'alt="HVAC tech walking past Ragsdaless vans"': 'images/tech-walking-vans.jpg',
    r'alt="Ragsdaless Heating Technician with an Central Valley, CA area homeowner"': 'images/tech-with-homeowner.jpg',
    
    # Logos & branding
    r'alt="Ragsdaless\'s Heat &amp; Air LLC"': 'images/logo5.png',
    r'alt="Ragsdaless Heating, Air"': 'images/logo5.png',
    
    # Awards (using logo as placeholder)
    r'alt="President\'s Award logo"': 'images/logo1.png',
    r'alt="My Home Improvement for Plumbing Award logo"': 'images/logo2.png',
    r'alt="Angie\'s List Award logo"': 'images/logo3.png',
    r'alt="Paulding County Schools Award logo"': 'images/logo4.png',
    r'alt="My Home Improvement Best Electrician"': 'images/logo7.png',
    r'alt="Owens Cornings AirCare Professional with the Pink Panther"': 'images/logo1.png',
    
    # Generic stats/infographics (using available team photos)
    r'alt="99% of customers would recommend Ragsdaless"': 'images/customer-consultation.jpg',
    r'alt="500 hours of training for technicians"': 'images/tech-team-meeting.jpg',
    r'alt="8 years average employee tenure"': 'images/team-photo.jpg',
    
    # Coupons (using logos as placeholders)
    r'alt="UP TO \$1700 OFF"': 'images/logo5.png',
    r'alt="\$79 FURNACE TUNE-UP"': 'images/logo5.png',
    r'alt="10% off indoor air quality products"': 'images/logo5.png',
    r'alt="Buy one get one free on a dimmer switch replacement or new install"': 'images/logo5.png',
    r'alt="\$100 off an EV charger install"': 'images/logo5.png',
    r'alt="Up to \$3000 off generator installs while supplies last"': 'images/logo5.png',
    r'alt="\$100 off a standard 6 year warranty water heater"': 'images/logo5.png',
    r'alt="HVAC Inspection"': 'images/logo5.png',
    r'alt="\$100 OFF ANY HEATING, PLUMBING, OR AC SERVICE REPAIR OR DIAGNOSTIC FEE"': 'images/logo5.png',
}

# Generic fallback for unmatched placeholders
GENERIC_FALLBACKS = {
    'hero': 'images/hero-technician.jpg',
    'card': 'images/tech-with-customer.jpg',
    'background': 'images/hero-truck.jpg',
    'generic': 'images/team-photo.jpg',
}

def replace_placeholders_in_file(filepath):
    """Replace placeholder images in a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replacements_made = 0
    
    # First pass: Replace based on alt text
    for alt_pattern, image_path in IMAGE_MAPPINGS.items():
        # Find instances with this alt text and placeholder
        pattern = f'src="{PLACEHOLDER_SVG}"([^>]*?){alt_pattern}'
        replacement = f'src="{image_path}"\\1{alt_pattern}'
        content, count = re.subn(pattern, replacement, content)
        replacements_made += count
    
    # Second pass: Replace remaining placeholders with generic images
    # For background images in style attributes
    style_placeholder_pattern = r"style=\"background-image: url\('data:image/svg\+xml[^']+'\);"
    style_replacement = f"style=\"background-image: url('images/hero-truck.jpg');"
    content, count = re.subn(style_placeholder_pattern, style_replacement, content)
    replacements_made += count
    
    # For remaining img src placeholders
    remaining_pattern = f'src="{PLACEHOLDER_SVG}"'
    remaining_replacement = 'src="images/tech-with-customer.jpg"'
    content, count = re.subn(remaining_pattern, remaining_replacement, content)
    replacements_made += count
    
    # Write back if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {filepath.name}: {replacements_made} replacements")
        return replacements_made
    else:
        print(f"  {filepath.name}: No changes needed")
        return 0

def main():
    """Process all HTML files in the workspace."""
    workspace_dir = Path('/workspaces/ragsdales')
    html_files = list(workspace_dir.glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    total_replacements = 0
    for html_file in sorted(html_files):
        replacements = replace_placeholders_in_file(html_file)
        total_replacements += replacements
    
    print(f"\n{'='*60}")
    print(f"Total replacements made: {total_replacements}")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
