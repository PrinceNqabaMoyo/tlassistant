import xml.etree.ElementTree as ET
import base64
import os
from PIL import Image
import io

svg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "female_organs_frontal_unlabeled.svg")
tree = ET.parse(svg_path)
root = tree.getroot()

image_elem = root.find('{http://www.w3.org/2000/svg}image')
href = image_elem.attrib.get('{http://www.w3.org/1999/xlink}href', '')
assert href.startswith("data:image/png;base64,")
b64_data = href[len("data:image/png;base64,"):]
png_bytes = base64.b64decode(b64_data)

img = Image.open(io.BytesIO(png_bytes))
print("Extracted image size:", img.size, "mode:", img.mode)

# Save to public/diagrams/female_reproductive_textbook.jpg centered on pure white #FFFFFF
# Let's crop to bbox with margin
bbox = img.getbbox()
print("BBox:", bbox)
cropped = img.crop(bbox)

# Create a clean 600x480 canvas on pure white
canvas = Image.new("RGB", (600, 480), (255, 255, 255))
w, h = cropped.size
scale = min(540 / w, 400 / h)
new_w, new_h = int(w * scale), int(h * scale)
resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
# Center
offset_x = (600 - new_w) // 2
offset_y = (480 - new_h) // 2
if resized.mode == 'RGBA':
    canvas.paste(resized, (offset_x, offset_y), resized)
else:
    canvas.paste(resized, (offset_x, offset_y))

target_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "female_reproductive_textbook.jpg")
canvas.save(target_path, "JPEG", quality=95)
print(f"Saved textbook plate to {target_path} ({os.path.getsize(target_path)} bytes)")
