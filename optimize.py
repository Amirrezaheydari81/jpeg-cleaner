from pathlib import Path
from PIL import Image
import shutil
import secrets

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

QUALITY = 60


def clear_output():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def optimize_image(input_file, output_file):
    with Image.open(input_file) as img:

        # حذف متادیتا + آماده‌سازی برای JPG
        img = img.convert("RGBA")

        # ساخت بک‌گراند سفید برای PNG های شفاف
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])  # alpha channel

        # حذف کامل دیتا با ساخت تصویر جدید
        clean = Image.new("RGB", background.size)
        clean.paste(background)

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

        if file.suffix.lower() not in (".jpg", ".jpeg", ".png"):
            continue

        relative = file.relative_to(INPUT_DIR)
        random_name = f"{secrets.token_hex(6)}.jpg"
        output_file = OUTPUT_DIR / random_name
        output_file.parent.mkdir(parents=True, exist_ok=True)

        optimize_image(file, output_file)

        print(f"✔ {relative}")
        count += 1

    print(f"\nDone! {count} image(s) processed.")


if __name__ == "__main__":
    main()