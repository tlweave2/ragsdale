# Photo Renaming Reference Guide

Quick reference showing how the uploaded photos were renamed for the website.

## Photo Mapping

| Original Filename | New Filename | Usage |
|------------------|--------------|-------|
| ragsdalejan26-00827.jpg | technician-at-unit.jpg | Technician working on HVAC unit |
| ragsdalejan26-00832.jpg | tech-greeting-customer.jpg | AC maintenance hero, customer greeting scenes |
| ragsdalejan26-00834.jpg | customer-consultation.jpg | Homepage 99% stat, consultation scenes |
| ragsdalejan26-00844.jpg | tech-with-customer.jpg | Generic service cards, default images |
| ragsdalejan26-00849.jpg | team-photo.jpg | Team photo carousel, tenure stats |
| ragsdalejan26-00856.jpg | office-building.jpg | Office/warehouse photo in about carousel |
| ragsdalejan26-00867.jpg | tech-team-meeting.jpg | Training stats, team meetings |
| ragsdalejan26-00870.jpg | tech-with-homeowner.jpg | Heating maintenance hero |
| ragsdalejan26-00877.jpg | tech-walking-vans.jpg | About page carousel, walking past fleet |
| ragsdalejan26-00911.jpg | tech-outdoor-unit.jpg | Outdoor unit inspection carousel |
| ragsdalejan26-00913.jpg | customer-service-rep.jpg | Customer service representative carousel |
| ragsdalejan26-00926.jpg | tech-explaining-options.jpg | Outdoor consultation carousel |
| ragsdalejan26-00971.jpg | tech-kitchen-consultation.jpg | Kitchen counter consultation scenes |
| ragsdalejan26-00973.jpg | tech-inspecting-furnace.jpg | Furnace inspection carousel |
| ragsdalejan26-00986.jpg | tech-at-back-of-truck.jpg | About/coupons hero, truck scenes |
| ragsdalejan26-01001.jpg | art-ragsdale-president.jpg | Maintenance page hero, president photo |
| ragsdalejan26-01008.jpg | tech-working-furnace.jpg | Heating repair hero, furnace work |
| ragsdalejan26-01013.jpg | customer-service-headset.jpg | Contact page hero, CSR with headset |
| ragsdalejan26-01019.jpg | van-driveway.jpg | Expert zoning hero, van arriving |
| ragsdalejan26-01027.jpg | tech-and-customer-photo.jpg | Customer interaction photos |
| ragsdalejan26-01050.jpg | hero-placeholder.jpg | Generic hero backup image |

## Already Named Files (Kept As-Is)

| Filename | Usage |
|----------|-------|
| hero-technician.jpg | Alternative hero image |
| hero-technician3.jpg | Alternative hero image |
| hero-truck.jpg | Background images, service cards |
| icon-cooling-red.png | Air conditioning navigation icon |
| icon-heating-red.png | Heating navigation icon |
| logo1.png | President's Award placeholder |
| logo2.png | My Home Improvement Award placeholder |
| logo3.png | Angie's List Award placeholder |
| logo4.png | Paulding County Schools Award placeholder |
| logo5.png | Main company logo (most used) |
| logo7.png | Best Electrician Award placeholder |

## Total Images in Use

- **24 renamed photos** from uploaded set
- **11 existing images** (logos, icons, heroes)
- **35 total images** actively used across the website
- **334 placeholder replacements** made across 27 HTML files

## How to Find Image Usage

To see where a specific image is used:
```bash
grep -r "imagename.jpg" *.html
```

Example:
```bash
grep -r "tech-greeting-customer.jpg" *.html
```

## Original Files Location

All original uploaded files are preserved in `/workspaces/ragsdale/images/` with their original names (ragsdalejan26-XXXXX.jpg). The renamed versions are copies.
