import cv2
import numpy as np
from PIL import Image
import os

img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "female_reproductive_textbook.jpg")
img = Image.open(img_path).convert("RGB")
np_img = np.array(img)

# Female colors:
# Ovaries are purple: high R, low G, high B (R ~ 120-160, G < 60, B > 120)
# Uterus wall is red: high R, low G, low B (R > 200, G < 70, B < 80)
# Endometrium is peach: high R, mid G, mid B (R > 220, G ~ 140-190, B ~ 100-140)
# Vagina is orange: high R, mid G, low B (R > 210, G ~ 100-140, B < 60)
# Vestibular bulbs are dark blue: low R, mid G, high B (R < 60, G ~ 90-130, B > 140)

colors = {
    "purple_ovary": (np_img[:, :, 0] > 100) & (np_img[:, :, 0] < 160) & (np_img[:, :, 1] < 70) & (np_img[:, :, 2] > 100),
    "red_uterus_wall": (np_img[:, :, 0] > 190) & (np_img[:, :, 1] < 70) & (np_img[:, :, 2] < 80),
    "peach_endometrium": (np_img[:, :, 0] > 220) & (np_img[:, :, 1] > 130) & (np_img[:, :, 1] < 190) & (np_img[:, :, 2] > 90) & (np_img[:, :, 2] < 150),
    "orange_vagina": (np_img[:, :, 0] > 210) & (np_img[:, :, 1] > 90) & (np_img[:, :, 1] < 140) & (np_img[:, :, 2] < 60),
    "blue_vestibular": (np_img[:, :, 0] < 80) & (np_img[:, :, 1] > 80) & (np_img[:, :, 1] < 140) & (np_img[:, :, 2] > 140),
}

print(f"Female Textbook image dimensions: {img.size}")
for name, mask in colors.items():
    ys, xs = np.where(mask)
    if len(xs) > 0:
        # If there are left and right (e.g. ovaries)
        if name == "purple_ovary":
            left_mask = mask & (np.arange(img.size[0])[None, :] < img.size[0] // 2)
            right_mask = mask & (np.arange(img.size[0])[None, :] >= img.size[0] // 2)
            for side, s_mask in [("left_ovary", left_mask), ("right_ovary", right_mask)]:
                s_ys, s_xs = np.where(s_mask)
                if len(s_xs) > 0:
                    cx, cy = int(np.mean(s_xs)), int(np.mean(s_ys))
                    svg_x = 40 + (cx / img.size[0]) * 520
                    svg_y = 0 + (cy / img.size[1]) * 480
                    print(f"{side:18}: img=({cx}, {cy}) -> SVG=({int(svg_x)}, {int(svg_y)})")
        else:
            cx, cy = int(np.mean(xs)), int(np.mean(ys))
            svg_x = 40 + (cx / img.size[0]) * 520
            svg_y = 0 + (cy / img.size[1]) * 480
            print(f"{name:18}: img=({cx}, {cy}) -> SVG=({int(svg_x)}, {int(svg_y)}) [count={len(xs)}]")
    else:
        print(f"{name:18}: NOT FOUND")
