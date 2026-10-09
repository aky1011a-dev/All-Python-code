
from PIL import Image
import pillow_heif


# Register HEIF opener with Pillow
pillow_heif.register_heif_opener()
# Open HEIC file
img = Image.open(r'C:\Users\gunse\OneDrive\Desktop\Code\Python\IMG_0499.HEIC')
# Save as JPG
img.save(r'C:\Users\gunse\OneDrive\Desktop\Code\Python\IMG_0499.jpg', format='JPEG')

print("test")