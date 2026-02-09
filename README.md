# Image to SVG Converter

A Python script that converts raster images (PNG, JPG, etc.) to vector SVG format while preserving color and detail.

## Features

- ✨ High-quality vectorization using vtracer (Rust-based)
- 🎨 Full color preservation
- 🔧 Adjustable quality settings
- 📐 Maintains original image dimensions
- 🚀 Fast processing with spline curve fitting

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install vtracer Pillow
```

**Note**: vtracer requires Rust to be installed. If you don't have Rust:

**macOS/Linux:**
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**
Download and install from [rustup.rs](https://rustup.rs/)

After installing Rust, install vtracer:
```bash
pip install vtracer
```

## Usage

### Basic Usage

Convert an image with default settings (recommended for most cases):

```bash
python img_svg.py input.png
```

This creates `input.svg` in the same directory.

### Specify Output File

```bash
python img_svg.py input.png -o output.svg
```

### Advanced Usage

#### Maximum Quality (More Colors, Fine Details)

```bash
python img_svg.py idea.png -c 6 -m spline -f 2
```

- `-c 6`: Maximum color precision (0-6)
- `-m spline`: Smooth curves
- `-f 2`: Minimal speckle filtering (preserves detail)

#### Clean/Smooth Result (Fewer Colors, Less Noise)

```bash
python img_svg.py photo.jpg -c 4 -m spline -f 8
```

- `-c 4`: Moderate color precision
- `-f 8`: Heavy speckle filtering (removes noise)

#### Sharp Edges (Logos, Icons)

```bash
python img_svg.py logo.png -c 5 -m polygon -f 6
```

- `-m polygon`: Sharp corners instead of curves

## Command Line Options

| Option | Short | Description | Values | Default |
|--------|-------|-------------|--------|---------|
| `--output` | `-o` | Output SVG file path | file path | `input.svg` |
| `--color-precision` | `-c` | Color detail level | 0-6 | 6 |
| `--mode` | `-m` | Curve fitting mode | `polygon`, `spline`, `none` | `spline` |
| `--filter-speckle` | `-f` | Noise reduction | 0-10 | 4 |

### Parameter Guide

#### Color Precision (`-c`)
- **0-2**: Very few colors, posterized effect
- **3-4**: Good for simple graphics
- **5**: Balanced (good for most photos)
- **6**: Maximum colors (best quality, larger file)

#### Mode (`-m`)
- **spline**: Smooth curves (best for photos, organic shapes)
- **polygon**: Sharp corners (best for logos, diagrams)
- **none**: No curve fitting

#### Filter Speckle (`-f`)
- **0-2**: Preserve tiny details (may include noise)
- **3-5**: Balanced
- **6-10**: Heavy smoothing (cleaner but less detail)

## Examples

### Converting Different Image Types

```bash
# PNG with transparency
python img_svg.py logo.png -c 6 -m polygon

# JPEG photograph
python img_svg.py photo.jpg -c 6 -m spline -f 5

# Simple icon
python img_svg.py icon.png -c 4 -m polygon -f 8
```

### Batch Processing

Convert multiple images:

```bash
for img in *.png; do
    python img_svg.py "$img" -c 6 -m spline
done
```

## Output

The script generates an SVG file with:
- Vector paths for each color layer
- Preserved dimensions from original image
- Optimized curves (spline mode) or polygons (polygon mode)
- Full color information

## Troubleshooting

### "vtracer is not installed"

```bash
pip install vtracer
```

If this fails, ensure Rust is installed first.

### SVG looks blocky or pixelated

- Increase color precision: `-c 6`
- Use spline mode: `-m spline`
- Reduce filtering: `-f 2`

### SVG has too much noise/detail

- Increase filtering: `-f 8`
- Reduce color precision: `-c 4`

### File size is too large

- Reduce color precision: `-c 3` or `-c 4`
- Use polygon mode: `-m polygon`
- Increase filtering: `-f 6`

## How It Works

1. **Image Loading**: Opens the raster image and reads dimensions
2. **Vectorization**: Uses vtracer (Rust-based) to trace edges and create vector paths
3. **Color Separation**: Identifies and separates distinct color regions
4. **Path Optimization**: Fits curves (spline) or polygons to traced edges
5. **SVG Generation**: Combines all paths into a layered SVG file

## Performance

- **Small images** (< 500px): < 1 second
- **Medium images** (500-1000px): 1-5 seconds
- **Large images** (> 1000px): 5-30 seconds

Processing time depends on:
- Image resolution
- Number of colors
- Detail level (filter_speckle setting)

## Recommended Settings by Image Type

| Image Type | Color Precision | Mode | Filter Speckle |
|------------|----------------|------|----------------|
| Logo/Icon | 4-5 | polygon | 6-8 |
| Photograph | 6 | spline | 4-5 |
| Illustration | 5-6 | spline | 3-4 |
| Line Art | 3-4 | polygon | 8-10 |
| Screenshot | 5 | spline | 5-6 |

## Project Structure

```
image_svg/
├── img_svg.py          # Main conversion script
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

## Dependencies

- **vtracer**: High-quality image vectorization library
- **Pillow (PIL)**: Python imaging library for loading images

## License

This project uses vtracer, which is licensed under MIT License.

## Contributing

Suggestions and improvements welcome! This is a utility script for converting raster images to SVG format.

## Tips for Best Results

1. **Start with high-quality input**: Higher resolution inputs produce better SVGs
2. **Clean your image first**: Remove backgrounds or noise in an image editor if needed
3. **Experiment with settings**: Different images work best with different parameters
4. **Check file size**: Very detailed SVGs can be large - adjust settings if needed
5. **Preview the output**: Open the SVG in a browser or vector editor to verify quality

## Common Use Cases

- Converting logos to scalable vector format
- Creating SVG assets from raster designs
- Preparing images for laser cutting/engraving
- Generating resolution-independent graphics
- Converting scanned artwork to vectors

## Alternative Tools

If vtracer doesn't work for your use case:
- **Inkscape**: Free desktop app with "Trace Bitmap" feature
- **Adobe Illustrator**: Professional image trace
- **Vector Magic**: Online conversion service

This script provides a free, scriptable alternative with good quality results!