from PIL import Image
import os

src_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "openstax_female_28_02_06.jpg")
img = Image.open(src_path)
print("Female image size:", img.size)

# The central organ is between the two histology insets
# Histology left ends at x ~ 350, right starts at x ~ 700
crop_f = img.crop((350, 100, 720, 500))
crop_f.save(os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "female_central.jpg"))
print("Saved female_central.jpg")
