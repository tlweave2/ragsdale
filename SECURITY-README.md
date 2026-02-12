# HouseCall Pro Integration - Security Guide

## ⚠️ URGENT: API Key Exposed

Your HouseCall Pro API key was previously committed to this repository and is now public. You need to take immediate action:

### Step 1: Regenerate Your API Key
1. Log into your HouseCall Pro account
2. Go to Settings → Integrations → API
3. **Revoke/Regenerate** your API key
4. Copy the new API key

### Step 2: Update Your Configuration
1. Open `housecallpro-config.js`
2. Replace the API key with your NEW key:
   ```javascript
   window.HOUSECALLPRO_CONFIG = {
     bookingUrl: 'https://book.housecallpro.com/book/Ragsdales-Heat--Air/YOUR_COMPANY_ID?v2=true&lead_source=website',
     apiKey: 'YOUR_NEW_API_KEY_HERE',
     merchantId: 'YOUR_MERCHANT_ID',
     companyId: 'YOUR_COMPANY_ID'
   };
   ```
3. Save the file

### Step 3: Verify .gitignore
The `.gitignore` file now includes `housecallpro-config.js` to prevent future commits of sensitive data.

### Step 4: Clean Git History (Optional but Recommended)
The old API key is still in your Git history. To completely remove it:

```bash
# Remove the file from all commits
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch housecallpro-booking.js housecallpro-booking-simple.js" \
  --prune-empty --tag-name-filter cat -- --all

# Force push to update remote
git push origin --force --all
```

**WARNING**: This rewrites history. Coordinate with any collaborators first.

## How It Works Now

### File Structure
- `housecallpro-config.js` - Contains your API key (gitignored, never committed)
- `housecallpro-config.template.js` - Template file for other developers (committed)
- `housecallpro-booking-simple.js` - Booking integration script (committed, no secrets)
- `.gitignore` - Prevents committing sensitive files

### For Other Developers
If someone else clones this repository:
1. Copy the template: `cp housecallpro-config.template.js housecallpro-config.js`
2. Update `housecallpro-config.js` with the actual API key
3. The file won't be tracked by Git

## Testing
After updating your API key:
1. Refresh any open webpage
2. Click a "Schedule Now" button
3. Verify the HouseCall Pro booking popup opens

## Best Practices Going Forward
- ✅ Never commit API keys, passwords, or secrets to Git
- ✅ Use environment variables or config files that are gitignored
- ✅ Use template files (`.template` or `.example`) to show structure
- ✅ Regularly rotate API keys
- ✅ Monitor your API key usage for suspicious activity

## Need Help?
Contact HouseCall Pro support if you need assistance regenerating your API key or have questions about security.
