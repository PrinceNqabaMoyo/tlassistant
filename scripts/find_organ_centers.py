import cv2
import numpy as np
from PIL import Image
import os

img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "male_reproductive_textbook.jpg")
img = Image.open(img_path).convert("RGB")
np_img = np.array(img)

# Let's inspect colors
# Testis is purple: high R, low G, high B or violet: e.g. R ~ 100-160, G ~ 30-70, B ~ 120-190
# Bladder is yellow: high R, high G, low B (R > 200, G > 200, B < 150)
# Prostate is red: high R, low G, low B (R > 180, G < 50, B < 50)
# Penis erectile tissue is green: low R, high G, low B (R < 50, G > 140, B < 50)
# Seminal vesicle is pink/magenta: high R, low G, high B (R > 180, G < 80, B > 100)
# Cowper's gland is dark blue/teal: low R, low/mid G, high B (R < 50, G < 120, B > 120)

colors = {
    "yellow_bladder": (np_img[:, :, 0] > 200) & (np_img[:, :, 1] > 200) & (np_img[:, :, 2] < 150),
    "red_prostate": (np_img[:, :, 0] > 180) & (np_img[:, :, 1] < 60) & (np_img[:, :, 2] < 60),
    "green_penis": (np_img[:, :, 0] < 80) & (np_img[:, :, 1] > 120) & (np_img[:, :, 2] < 80),
    "purple_testis": (np_img[:, :, 0] > 90) & (np_img[:, :, 0] < 160) & (np_img[:, :, 1] < 80) & (np_img[:, :, 2] > 100),
    "pink_seminal": (np_img[:, :, 0] > 180) & (np_img[:, :, 1] < 80) & (np_img[:, :, 2] > 80),
    "blue_cowpers": (np_img[:, :, 0] < 60) & (np_img[:, :, 1] > 60) & (np_img[:, :, 1] < 140) & (np_img[:, :, 2] > 120),
}

print(f"Textbook image dimensions: {img.size}")
for name, mask in colors.items():
    ys, xs = np.where(mask)
    if len(xs) > 0:
        cx, cy = int(np.mean(xs)), int(np.mean(ys))
        # Note: In MaleReproductiveSvg, the image is rendered with x=40, y=0, width=520, height=480
        # Map image coordinates to SVG canvas coordinates:
        svg_x = 40 + (cx / img.size[0]) * 520
        svg_y = 0 + (cy / img.size[1]) * 480
        print(f"{name:15}: img=({cx}, {cy}) -> SVG=({int(svg_x)}, {int(svg_y)}) [count={len(xs)}]")
    else:
        print(f"{name:15}: NOT FOUND")
