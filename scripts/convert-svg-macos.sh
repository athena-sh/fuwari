#!/bin/bash

# convert-svg-macos.sh - Convert FontAwesome SVGs to 50% size with currentColor
# macOS compatible version
# Usage: ./convert-svg-macos.sh input.svg [output.svg]

input_file="$1"
output_file="${2:-$1}"  # If no output specified, overwrite input

if [ -z "$input_file" ]; then
    echo "Usage: $0 input.svg [output.svg]"
    exit 1
fi

if [ ! -f "$input_file" ]; then
    echo "Error: File '$input_file' not found"
    exit 1
fi

# Extract current viewBox values (macOS compatible)
viewbox=$(sed -n 's/.*viewBox="\([^"]*\)".*/\1/p' "$input_file" | head -1)
if [ -z "$viewbox" ]; then
    echo "Error: No viewBox found in SVG"
    exit 1
fi

# Parse viewBox values
read -r x y width height <<< "$viewbox"

# For common FontAwesome sizes, use pre-calculated values
# This avoids needing bc for arithmetic
case "$width $height" in
    "640 640")
        new_viewbox="-320 -320 1280 1280"
        ;;
    "512 512")
        new_viewbox="-256 -256 1024 1024"
        ;;
    "448 512")
        new_viewbox="-224 -256 896 1024"
        ;;
    "384 512")
        new_viewbox="-192 -256 768 1024"
        ;;
    "576 512")
        new_viewbox="-288 -256 1152 1024"
        ;;
    *)
        echo "Warning: Non-standard viewBox size: $width x $height"
        echo "Using Python for calculation..."
        # Use Python for arithmetic if available (macOS has Python by default)
        if command -v python3 &> /dev/null; then
            new_viewbox=$(python3 -c "
x, y, w, h = $x, $y, $width, $height
px = w / 2
py = h / 2
print(f'{x - px:.0f} {y - py:.0f} {w * 2:.0f} {h * 2:.0f}')
")
        else
            echo "Error: Cannot calculate new viewBox for non-standard size"
            echo "Please install Python 3 or use a standard FontAwesome icon"
            exit 1
        fi
        ;;
esac

# Create the converted SVG
sed -E \
    -e "s/viewBox=\"[^\"]*\"/viewBox=\"$new_viewbox\"/g" \
    -e 's/<path d="/<path fill="currentColor" d="/g' \
    -e 's/<path fill="[^"]*" d="/<path fill="currentColor" d="/g' \
    -e 's/fill="#[0-9A-Fa-f]{3,6}"/fill="currentColor"/gi' \
    -e 's/stroke="#[0-9A-Fa-f]{3,6}"/stroke="currentColor"/gi' \
    "$input_file" > "$output_file.tmp"

mv "$output_file.tmp" "$output_file"

echo "✓ Converted: $output_file"
echo "  - Original viewBox: $viewbox"
echo "  - New viewBox: $new_viewbox (50% size)"
echo "  - Fill/Stroke: currentColor"
