#!/bin/bash

# Add HouseCall Pro integration to all HTML files

echo "Adding HouseCall Pro booking integration to all HTML pages..."

# Find all HTML files in the workspace (excluding guides subdirectory for now)
for html_file in *.html; do
    if [ -f "$html_file" ]; then
        # Check if the HouseCall Pro script is already added
        if grep -q "housecallpro-booking.js" "$html_file"; then
            echo "✓ $html_file already has HouseCall Pro integration"
        else
            # Find the line with appendSE(); and add the HouseCall Pro script after it
            if grep -q "}; appendSE();" "$html_file"; then
                # Create a backup
                cp "$html_file" "$html_file.bak"
                
                # Add the HouseCall Pro script
                sed -i 's@}; appendSE();@}; appendSE();\n</script>\n<!-- HouseCall Pro Booking Integration -->\n<script src="housecallpro-booking.js"></script>\n<script>@' "$html_file"
                
                echo "✓ Added HouseCall Pro to $html_file"
            else
                echo "⚠ Could not find insertion point in $html_file"
            fi
        fi
    fi
done

# Handle files in guides subdirectory
if [  -d "guides" ]; then
    for html_file in guides/*.html; do
        if [ -f "$html_file" ]; then
           # Check if the HouseCall Pro script is already added
            if grep -q "housecallpro-booking.js" "$html_file"; then
                echo "✓ $html_file already has HouseCall Pro integration"
            else
                # Find the line with appendSE(); and add the HouseCall Pro script after it
                if grep -q "}; appendSE();" "$html_file"; then
                    # Create a backup
                    cp "$html_file" "$html_file.bak"
                    
                    # Add the HouseCall Pro script (with correct path for subdirectory)
                    sed -i 's@}; appendSE();@}; appendSE();\n</script>\n<!-- HouseCall Pro Booking Integration -->\n<script src="../housecallpro-booking.js"></script>\n<script>@' "$html_file"
                    
                    echo "✓ Added HouseCall Pro to $html_file"
                else
                    echo "⚠ Could not find insertion point in $html_file"
                fi
            fi
        fi
    done
fi

# Handle privacy-policy subdirectory
if [ -d "privacy-policy" ]; then
    for html_file in privacy-policy/*.html; do
        if [ -f "$html_file" ]; then
            # Check if the HouseCall Pro script is already added
            if grep -q "housecallpro-booking.js" "$html_file"; then
                echo "✓ $html_file already has HouseCall Pro integration"
            else
                # Find the line with appendSE(); and add the HouseCall Pro script after it
                if grep -q "}; appendSE();" "$html_file"; then
                    # Create a backup
                    cp "$html_file" "$html_file.bak"
                    
                    # Add the HouseCall Pro script (with correct path for subdirectory)
                    sed -i 's@}; appendSE();@}; appendSE();\n</script>\n<!-- HouseCall Pro Booking Integration -->\n<script src="../housecallpro-booking.js"></script>\n<script>@' "$html_file"
                    
                    echo "✓ Added HouseCall Pro to $html_file"
                else
                    echo "⚠ Could not find insertion point in $html_file"
                fi
            fi
        fi
    done
fi

echo ""
echo "✅ HouseCall Pro integration complete!"
echo ""
echo "Next steps:"
echo "1. Test the 'Schedule Now' buttons on your pages"
echo "2. The booking modal should open with your HouseCall Pro form"
echo "3. If you want to remove ServiceTitan completely, you can delete the ServiceTitan script loading code"
