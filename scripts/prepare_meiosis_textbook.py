from PIL import Image
import os

source_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "synapsis_crossing_over_nolabels.png")
img = Image.open(source_path)

# Check bounding box of non-white / non-transparent pixels
bbox = img.getbbox()
print("Image size:", img.size)
print("BBox:", bbox)

# Create an image on pure white background
white_bg = Image.new("RGB", img.size, (255, 255, 255))
if img.mode == 'RGBA':
    white_bg.paste(img, (0, 0), img)
else:
    white_bg.paste(img, (0, 0))

target_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "meiosis_crossing_over_textbook.jpg")
# Let's crop to bbox with margin and resize nicely to standard textbook aspect (e.g., width 800-1000)
cropped = white_bg.crop(bbox)
# Center on a 600x480 canvas or similar
canvas = Image.new("RGB", (700, 520), (255, 255, 255))
# Scale cropped to fit nicely
w, h = cropped.size
scale = min(620 / w, 440 / h)
new_w, new_h = int(w * scale), int(h * scale)
resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
canvas.paste(resized, ((700 - new_w) // 2, (520 - new_h) // 2))
canvas.save(target_path, "JPEG", quality=95)
print(f"Saved {target_path} ({os.path.getsize(target_path)} bytes)")
