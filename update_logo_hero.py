#!/usr/bin/env python3
"""
Replace logos with thislogo.png and hero images with cutwidth.png
"""

import re
from pathlib import Path

def replace_images_in_file(filepath):
    """Replace logo and hero images in HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    replacements = 0
    
    # Replace all logo*.png with thislogo.png
    for logo_num in ['1', '2', '3', '4', '5', '7']:
        old_logo = f'images/logo{logo_num}.png'
        new_logo = 'images/thislogo.png'
        count = content.count(old_logo)
        content = content.replace(old_logo, new_logo)
        replacements += count
    
    # Replace hero images with cutwidth.png
    hero_images = [
        'images/hero-truck.jpg',
        'images/hero-technician.jpg',
        'images/hero-technician3.jpg',
        'images/hero-placeholder.jpg'
    ]
    
    for hero in hero_images:
        count = content.count(hero)
        content = content.replace(hero, 'images/cutwidth.png')
        replacements += count
    
    # Write back if changes were made
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return replacements
    return 0

def main():
    workspace_dir = Path('/workspaces/ragsdale')
    html_files = list(workspace_dir.glob('*.html'))
    
    print(f"Processing {len(html_files)} HTML files...\n")
    
    total_replacements = 0
    for html_file in sorted(html_files):
        replacements = replace_images_in_file(html_file)
        if replacements > 0:
            print(f"✓ {html_file.name}: {replacements} replacements")
            total_replacements += replacements
    
    print(f"\n{'='*60}")
    print(f"Total replacements: {total_replacements}")
    print(f"  - All logo*.png → thislogo.png")
    print(f"  - All hero images → cutwidth.png")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
