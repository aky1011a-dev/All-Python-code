from PIL import Image
import pillow_heif
import os
import shutil

pillow_heif.register_heif_opener()

# Default location = folder where this script lives
try:
    DEFAULT_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    DEFAULT_BASE_DIR = os.getcwd()

print("Press ENTER to use the default location:")
print(DEFAULT_BASE_DIR)
print()

user_input = input("Or enter a custom folder path: ").strip()

# Decide base directory
BASE_DIR = user_input if user_input else DEFAULT_BASE_DIR
CONVERT_DIR = os.path.join(BASE_DIR, "CONVERT")
CONVERTED_DIR = os.path.join(BASE_DIR, "CONVERTED")

# Create folders
os.makedirs(CONVERT_DIR, exist_ok=True)
os.makedirs(CONVERTED_DIR, exist_ok=True)
delete_originals = input("Delete original files after conversion? (y/n) -> ").lower() == "y"

for filename in os.listdir(CONVERT_DIR):
    input_path = os.path.join(CONVERT_DIR,filename)
    if not os.path.isfile(input_path):
        continue
    name, ext = os.path.splitext(filename)
    ext = ext.lower()
    # Convert HEIC / HEIF
    if ext in [".heic",".heif"]:
        output_path = os.path.join(CONVERTED_DIR,name +".jpg")
        try:
            img = Image.open(input_path)
            img.save(output_path,format="JPEG")
            print(f"Converted: {filename}")
            if delete_originals:
                os.remove(input_path)
        except Exception as e:
            print(f"Failed: {filename} ({e})")
    # Move JPG / JPEG
    elif ext in [".jpg",".jpeg"]:
        shutil.move(input_path,os.path.join(CONVERTED_DIR,filename))
        print(f"Moved: {filename}")
    else:
        print(f"Skipped: {filename}")

print("All done ✅")
