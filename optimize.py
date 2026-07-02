from pathlib import Path
from PIL import Image
import shutil

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

QUALITY = 85


def clear_output():
    """پاک کردن کامل پوشه خروجی"""
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def optimize_image(input_file, output_file):
    with Image.open(input_file) as img:

        # حذف کامل متادیتا
        clean = Image.new(img.mode, img.size)
        clean.putdata(list(img.getdata()))

        clean.save(
            output_file,
            format="JPEG",
            quality=QUALITY,
            optimize=True,
            progressive=True,
        )


def main():
    clear_output()

    count = 0

    for file in INPUT_DIR.rglob("*"):
        if file.suffix.lower() not in (".jpg", ".jpeg"):
            continue

        relative = file.relative_to(INPUT_DIR)
        output_file = OUTPUT_DIR / relative
        output_file.parent.mkdir(parents=True, exist_ok=True)

        optimize_image(file, output_file)

        print(f"✔ {relative}")
        count += 1

    print(f"\nDone! {count} image(s) processed.")


if __name__ == "__main__":
    main()