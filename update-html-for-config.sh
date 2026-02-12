#!/bin/bash

# Update HTML files to load config before booking script

echo "Updating HTML files to load HouseCall Pro config..."

# For root directory HTML files
for html_file in *.html; do
    if [ -f "$html_file" ]; then
        if grep -q "housecallpro-booking-simple.js" "$html_file"; then
            # Replace the single script tag with both config and booking script
            sed -i 's|<script src="housecallpro-booking-simple.js"></script>|<!-- HouseCall Pro Booking Integration -->\n<script src="housecallpro-config.js"></script>\n<script src="housecallpro-booking-simple.js"></script>|' "$html_file"
            echo "✓ Updated $html_file"
        fi
    fi
done

# For guides subdirectory
if [ -d "guides" ]; then
    for html_file in guides/*.html; do
        if [ -f "$html_file" ]; then
            if grep -q "housecallpro-booking-simple.js" "$html_file"; then
                # Replace with relative paths for subdirectory
                sed -i 's|<script src="../housecallpro-booking-simple.js"></script>|<!-- HouseCall Pro Booking Integration -->\n<script src="../housecallpro-config.js"></script>\n<script src="../housecallpro-booking-simple.js"></script>|' "$html_file"
                echo "✓ Updated $html_file"
            fi
        fi
    done
fi

echo ""
echo "✅ All HTML files updated!"
echo ""
echo "⚠️  IMPORTANT SECURITY STEPS:"
echo "1. Go to your HouseCall Pro account and REGENERATE your API key"
echo "2. Update housecallpro-config.js with the NEW API key"
echo "3. The old key (9a480eda745743d28a7f3cf00ac5a58f) is now public and should be revoked"
