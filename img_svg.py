#!/usr/bin/env python3
"""
Image to SVG Converter using vtracer
Much better quality than potrace-based solutions
"""

import sys
from pathlib import Path

try:
    import vtracer
except ImportError:
    print("Error: vtracer is not installed")
    print("\nInstall with: pip install vtracer")
    sys.exit(1)

from PIL import Image

def image_to_svg(input_path, output_path, color_precision=6, mode='polygon', filter_speckle=4):
    """
    Convert image to SVG using vtracer
    
    Args:
        input_path: Path to input image
        output_path: Path to output SVG file
        color_precision: Color precision (0-6, higher = more colors)
        mode: 'polygon', 'spline', or 'none'
        filter_speckle: Filter speckle size (0-10, higher = less noise)
    """
    print(f"Converting {input_path} to SVG...")
    print(f"Color precision: {color_precision}")
    print(f"Mode: {mode}")
    
    # Get image info
    img = Image.open(input_path)
    width, height = img.size
    print(f"Image size: {width}x{height}")
    
    # Convert image to SVG - vtracer writes directly to file
    vtracer.convert_image_to_svg_py(
        str(input_path),
        str(output_path),
        colormode='color',  # Use full color mode
        hierarchical='stacked',  # Stack colors
        mode=mode,
        filter_speckle=filter_speckle,
        color_precision=color_precision,
        layer_difference=16,
        corner_threshold=60,
        length_threshold=4.0,
        max_iterations=10,
        splice_threshold=45,
        path_precision=8
    )
    
    print(f"\n✓ SVG saved to {output_path}")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Convert raster images to SVG with color preservation'
    )
    parser.add_argument('input', help='Input image file (PNG, JPG, etc.)')
    parser.add_argument('-o', '--output', help='Output SVG file (default: input name + .svg)')
    parser.add_argument('-c', '--color-precision', type=int, default=6, choices=range(0, 7),
                       help='Color precision 0-6, higher = more colors (default: 6)')
    parser.add_argument('-m', '--mode', choices=['polygon', 'spline', 'none'], default='spline',
                       help='Curve fitting mode (default: spline)')
    parser.add_argument('-f', '--filter-speckle', type=int, default=4, choices=range(0, 11),
                       help='Filter speckle 0-10, higher = smoother (default: 4)')
    
    args = parser.parse_args()
    
    # Determine output path
    output = args.output
    if not output:
        output = str(Path(args.input).with_suffix('.svg'))
    
    image_to_svg(args.input, output, args.color_precision, args.mode, args.filter_speckle)