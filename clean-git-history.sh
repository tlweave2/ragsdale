#!/bin/bash

echo "========================================="
echo "Git History Cleanup Script"
echo "========================================="
echo ""
echo "This script will remove the HouseCall Pro API key from Git history."
echo "WARNING: This rewrites Git history and requires force-push."
echo ""
echo "What this does:"
echo "1. Creates a backup branch"
echo "2. Removes sensitive data from all commits"
echo "3. Force pushes the cleaned history"
echo ""
read -p "Do you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 1
fi

echo ""
echo "Step 1: Creating backup branch..."
git branch backup-before-history-clean

echo ""
echo "Step 2: Removing API keys from history..."
echo "This may take a few minutes..."

# Use sed to replace the API key in all files in history
git filter-branch --force --tree-filter '
  if [ -f housecallpro-booking.js ]; then
    sed -i "s/9a480eda745743d28a7f3cf00ac5a58f/REDACTED_API_KEY/g" housecallpro-booking.js 2>/dev/null || true
  fi
  if [ -f housecallpro-booking-simple.js ]; then
    sed -i "s/9a480eda745743d28a7f3cf00ac5a58f/REDACTED_API_KEY/g" housecallpro-booking-simple.js 2>/dev/null || true
  fi
  if [ -f housecallpro-config.js ]; then
    sed -i "s/9a480eda745743d28a7f3cf00ac5a58f/REDACTED_API_KEY/g" housecallpro-config.js 2>/dev/null || true
  fi
' --tag-name-filter cat -- --all

echo ""
echo "Step 3: Cleaning up refs..."
rm -rf .git/refs/original/
git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo ""
echo "Step 4: Force pushing to GitHub..."
git push origin --force --all

echo ""
echo "========================================="
echo "✅ Git history cleaned successfully!"
echo "========================================="
echo ""
echo "What happened:"
echo "- Old API key (9a480eda745743d28a7f3cf00ac5a58f) replaced with 'REDACTED_API_KEY' in all commits"
echo "- A backup branch 'backup-before-history-clean' was created (just in case)"
echo "- Changes have been force-pushed to GitHub"
echo ""
echo "FINAL STEP: You still need to get a NEW API key from HouseCall Pro"
echo "and update your local housecallpro-config.js file"
echo ""
