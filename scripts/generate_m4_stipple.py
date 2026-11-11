import os
import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageOps

DIAGRAMS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams")

def create_exam_stipple(src_path, dst_path):
    print(f"Generating Exam Stipple: {src_path} -> {dst_path}")
    img = Image.open(src_path).convert("RGB")
    gray = ImageOps.grayscale(img)
    autocontrast = ImageOps.autocontrast(gray, cutoff=2)
    np_gray = np.array(autocontrast)

    # 1. Bilateral filter for smooth noise reduction with sharp edges
    blurred = cv2.bilateralFilter(np_gray, 9, 75, 75)

    # 2. Adaptive threshold for crisp pen-and-ink line art
    adaptive_edges = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3
    )

    # 3. Canny edges for strong structural boundaries
    canny = cv2.Canny(blurred, 40, 120)
    canny_inv = cv2.bitwise_not(canny)
    lines = cv2.bitwise_and(adaptive_edges, canny_inv)

    # 4. Floyd-Steinberg dithering for stipple shading
    gamma = 1.3
    table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    toned = cv2.LUT(blurred, table)
    toned_pil = Image.fromarray(toned)
    dithered = toned_pil.convert('1')
    np_dither = np.array(dithered).astype(np.uint8) * 255

    # 5. Composite: Lines + Stipple
    clean_white_mask = np_gray > 245
    final = cv2.bitwise_and(lines, np_dither)
    final[clean_white_mask] = 255

    # Clean tiny speckles
    kernel = np.ones((1, 1), np.uint8)
    final = cv2.morphologyEx(final, cv2.MORPH_CLOSE, kernel)

    res_img = Image.fromarray(final)
    res_img.save(dst_path, "JPEG", quality=95)
    print(f"Saved {dst_path} ({os.path.getsize(dst_path)} bytes)")

pairs = [
    ("female_reproductive_textbook.jpg", "female_reproductive_exam_stipple.jpg"),
    ("male_reproductive_textbook.jpg", "male_reproductive_exam_stipple.jpg"),
    ("meiosis_crossing_over_textbook.jpg", "meiosis_crossing_over_exam_stipple.jpg"),
]

for src_name, dst_name in pairs:
    src_p = os.path.join(DIAGRAMS_DIR, src_name)
    dst_p = os.path.join(DIAGRAMS_DIR, dst_name)
    create_exam_stipple(src_p, dst_p)

print("\n[SUCCESS] All 3 NSC exam stipple plates generated!")
