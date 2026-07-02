# JPEG Cleaner

A lightweight Python tool to optimize JPEG images and remove all metadata (EXIF, IPTC, XMP) while preserving image quality.

## Features

- Remove all metadata
- Optimize JPEG compression
- Progressive JPEG output
- Batch process entire folders
- Preserve directory structure
- Automatically clean the output folder before each run

## Project Structure

```text
project/
│
├── input/
│   ├── image1.jpg
│   └── ...
│
├── output/
│
└── optimize.py
```

## Installation

```bash
pip install pillow
```

## Usage

1. Place your `.jpg` and `.jpeg` files inside the `input` folder.

2. Run:

```bash
python optimize.py
```

3. Optimized images will be generated in the `output` folder.

## Configuration

You can modify the compression quality in the script:

```python
QUALITY = 85
```

Higher values preserve more quality but produce larger files.

## Supported Formats

- JPG
- JPEG

## Requirements

- Python 3.9+
- Pillow

## License

MIT
