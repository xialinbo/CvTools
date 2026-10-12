#!/usr/bin/env python3
"""Convert a BMP image so near-black pixels become pure black and near-white
pixels become pure white.
"""

import sys
from PIL import Image

BLACK_THRESHOLD = 30
WHITE_THRESHOLD = 225


def convert_to_monochrome(image: Image.Image) -> Image.Image:
    """Map near-black pixels to (0,0,0) and near-white pixels to (255,255,255)."""
    new_image = image.convert("RGB")
    pixels = new_image.load()

    for y in range(new_image.height):
        for x in range(new_image.width):
            r, g, b = pixels[x, y]
            brightness = (r + g + b) / 3.0

            if brightness <= BLACK_THRESHOLD:
                pixels[x, y] = (0, 0, 0)
            elif brightness >= WHITE_THRESHOLD:
                pixels[x, y] = (255, 255, 255)

    return new_image


def main() -> None:
    input_path = "..\\artifacts\\color.bmp"
    output_path = "..\\artifacts\\mono.bmp" 
    
    try:
        with Image.open(input_path) as image:
            mono_image = convert_to_monochrome(image)
            mono_image.save(output_path, format="BMP")
    except FileNotFoundError:
        print(f"Input file not found: {input_path}")
        raise SystemExit(1)
    except Exception as exc:
        print(f"Failed to process image: {exc}")
        raise SystemExit(1)

    print(f"Saved converted image to {output_path}")


if __name__ == "__main__":
    main()
