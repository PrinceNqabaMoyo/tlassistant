import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageOps
import os

PUBLIC_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams")

def create_exam_stipple(src_path, dst_path):
    print(f"Processing {src_path} -> {dst_path}...")
    # Load image
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    
    # Target size: 600x480 or keep original aspect ratio centered
    # Let's convert to grayscale
    gray = ImageOps.grayscale(img)
    
    # Increase contrast
    autocontrast = ImageOps.autocontrast(gray, cutoff=2)
    
    # In OpenCV for precise edge extraction + stipple
    np_gray = np.array(autocontrast)
    
    # 1. Bilateral filter to smooth noise while keeping crisp anatomical edges
    blurred = cv2.bilateralFilter(np_gray, 9, 75, 75)
    
    # 2. Adaptive threshold for fine pencil / pen ink line art
    adaptive_edges = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3
    )
    
    # 3. Canny edges for strong contours
    canny = cv2.Canny(blurred, 40, 120)
    canny_inv = cv2.bitwise_not(canny)
    
    # Combine lines
    lines = cv2.bitwise_and(adaptive_edges, canny_inv)
    
    # 4. Create authentic stippling from tonal values: Floyd-Steinberg dithering
    # Subtle gamma curve so background stays clean white
    gamma = 1.3
    table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    toned = cv2.LUT(blurred, table)
    
    toned_pil = Image.fromarray(toned)
    # 1-bit Floyd-Steinberg dither (dot stipple)
    dithered = toned_pil.convert('1')
    np_dither = np.array(dithered).astype(np.uint8) * 255
    
    # 5. Composite: Lines + Stipple
    # Stipple darkens areas that have tonal shading; lines define structure.
    # Where background was pure white or near white (>240), keep pure white (255)
    clean_white_mask = np_gray > 245
    
    final = cv2.bitwise_and(lines, np_dither)
    final[clean_white_mask] = 255
    
    # Morphological clean up tiny solitary speckles in pure white zones
    kernel = np.ones((1, 1), np.uint8)
    final = cv2.morphologyEx(final, cv2.MORPH_CLOSE, kernel)
    
    out_pil = Image.fromarray(final).convert("RGB")
    out_pil.save(dst_path, quality=95)
    print(f"Saved {dst_path} ({os.path.getsize(dst_path)} bytes)")

def main():
    targets = [
        ("alveolus_textbook.jpg", "alveolus_exam_stipple.jpg"),
        ("digestive_textbook.jpg", "digestive_exam_stipple.jpg"),
        ("villus_textbook.jpg", "villus_exam_stipple.jpg"),
        ("nephron_textbook.jpg", "nephron_exam_stipple.jpg"),
        ("human_eye_textbook.jpg", "human_eye_exam_stipple.jpg"),
        ("human_ear_textbook.jpg", "human_ear_exam_stipple.jpg"),
        ("endocrine_system_textbook.jpg", "endocrine_system_exam_stipple.jpg"),
    ]
    for src, dst in targets:
        s = os.path.join(PUBLIC_DIR, src)
        d = os.path.join(PUBLIC_DIR, dst)
        if os.path.exists(s):
            create_exam_stipple(s, d)
        else:
            print(f"Warning: {s} does not exist!")

if __name__ == "__main__":
    main()
