from PIL import Image
import os

src_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "openstax_male_28_01_01.jpg")
img = Image.open(src_path)
print("Image dimensions:", img.size)

# Panel (c) is in the lower portion: y from ~480 to 950, x from 50 to 800
crop_c = img.crop((40, 480, 800, 970))
crop_c.save(os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "male_panel_c.jpg"))
print("Saved male_panel_c.jpg")
