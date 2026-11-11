import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DIAGRAMS_DIR = os.path.join(BASE_DIR, "public", "diagrams")
SOURCE_DIR = os.path.join(DIAGRAMS_DIR, "source_plates")
TERMS_DIR = os.path.join(BASE_DIR, "curriculum_docs_auto", "LifeSciences_Gr12")

# ---------------------------------------------------------
# Helper: Create Exam Stipple / Line-Art Plate
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# 1. Female Reproductive System
# ---------------------------------------------------------
def prepare_female_plates():
    print("\n--- Preparing Female Reproductive Plates ---")
    # A. Textbook Master from DBE Textbook Figure 4
    # Textbook_LifeSciences_Gr12_Human_Reproduction.pdf-0006-10.png
    src_tb = os.path.join(TERMS_DIR, "Term 2", "images", "Textbook_LifeSciences_Gr12_Human_Reproduction.pdf-0006-10.png")
    img_tb = Image.open(src_tb).convert("RGB")
    w, h = img_tb.size

    # The organ itself is in the middle: x ~ 280 to 730, y ~ 150 to 880
    # Let's wipe all text and leader lines outside the organ
    draw = ImageDraw.Draw(img_tb)
    # Background color of the pelvic silhouette
    bg_color = (255, 255, 255)

    # Wipe text on left: "fallopian tube", "ovary"
    draw.rectangle([0, 0, 300, h], fill=bg_color)
    # Wipe text on right: "uterus", "endometrium", "cervix", "vagina", "vulva"
    draw.rectangle([720, 0, w, h], fill=bg_color)
    # Wipe horizontal leader lines connecting to the sides
    # Left lines: from x=300 to x=325
    draw.rectangle([200, 240, 345, 275], fill=bg_color) # fallopian line
    draw.rectangle([200, 350, 345, 385], fill=bg_color) # ovary line
    # Right lines: connecting to right labels
    draw.rectangle([600, 305, 800, 335], fill=bg_color) # uterus line
    draw.rectangle([520, 425, 800, 455], fill=bg_color) # endometrium line
    draw.rectangle([530, 580, 800, 610], fill=bg_color) # cervix line
    draw.rectangle([530, 700, 800, 730], fill=bg_color) # vagina line
    draw.rectangle([500, 880, 800, 920], fill=bg_color) # vulva line

    # Crop to organ
    bbox = img_tb.getbbox()
    cropped = img_tb.crop(bbox)

    # Place centered on pure white 600x480 canvas
    canvas = Image.new("RGB", (600, 480), (255, 255, 255))
    cw, ch = cropped.size
    scale = min(520 / cw, 420 / ch)
    nw, nh = int(cw * scale), int(ch * scale)
    resized = cropped.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas.paste(resized, ((600 - nw) // 2, (480 - nh) // 2))

    dst_tb = os.path.join(DIAGRAMS_DIR, "female_reproductive_textbook.jpg")
    canvas.save(dst_tb, "JPEG", quality=95)
    print(f"Saved {dst_tb} ({os.path.getsize(dst_tb)} bytes)")

    # B. Exam Stipple Plate from NSC Exam Diagram
    # Textbook_LifeSciences_Gr12_Human_Reproduction.pdf-0007-04.png
    src_exam = os.path.join(TERMS_DIR, "Term 2", "images", "Textbook_LifeSciences_Gr12_Human_Reproduction.pdf-0007-04.png")
    img_exam = Image.open(src_exam).convert("RGB")
    ew, eh = img_exam.size
    # Right half is female system (x from ~390 to ew)
    crop_female_exam = img_exam.crop((390, 0, ew, eh))
    # Wipe letters E, F, G, H and leader lines
    draw_e = ImageDraw.Draw(crop_female_exam)
    draw_e.rectangle([0, 0, 150, 100], fill=(255, 255, 255)) # F
    draw_e.rectangle([0, 200, 180, eh], fill=(255, 255, 255)) # E
    draw_e.rectangle([400, 200, crop_female_exam.width, eh], fill=(255, 255, 255)) # G
    draw_e.rectangle([250, 350, crop_female_exam.width, eh], fill=(255, 255, 255)) # H

    # Invert/threshold cleanly to pure black and white line art
    exam_bbox = crop_female_exam.getbbox()
    exam_cropped = crop_female_exam.crop(exam_bbox)
    ecw, ech = exam_cropped.size
    scale_e = min(520 / ecw, 420 / ech)
    enw, enh = int(ecw * scale_e), int(ech * scale_e)
    exam_resized = exam_cropped.resize((enw, enh), Image.Resampling.LANCZOS)

    canvas_e = Image.new("RGB", (600, 480), (255, 255, 255))
    canvas_e.paste(exam_resized, ((600 - enw) // 2, (480 - enh) // 2))
    dst_exam = os.path.join(DIAGRAMS_DIR, "female_reproductive_exam_stipple.jpg")
    canvas_e.save(dst_exam, "JPEG", quality=95)
    print(f"Saved {dst_exam} ({os.path.getsize(dst_exam)} bytes)")


# ---------------------------------------------------------
# 2. Male Reproductive System
# ---------------------------------------------------------
def prepare_male_plates():
    print("\n--- Preparing Male Reproductive Plates ---")
    # A. Textbook Master: Clean OpenStax / SEER anatomical master plate
    src_male = os.path.join(SOURCE_DIR, "openstax_male_28_01_01.jpg")
    img_m = Image.open(src_male).convert("RGB")
    # Panel (c) is located from y=480 to 876
    crop_m = img_m.crop((40, 470, 800, 876))
    mw, mh = crop_m.size

    # Wipe external labels on left, right, top, bottom
    draw_m = ImageDraw.Draw(crop_m)
    # Top label: "Prostate gland"
    draw_m.rectangle([300, 0, 500, 50], fill=(255, 255, 255))
    draw_m.line([395, 0, 395, 120], fill=(255, 255, 255), width=3)

    # Left labels: "Ductus (vas) deferens", "Suspensory ligament", "Urinary bladder", "Pubic symphysis", "Corpus cavernosum", "Corpus spongiosum", "External urethral opening"
    draw_m.rectangle([0, 0, 180, mh], fill=(255, 255, 255))
    # Wipe horizontal leader lines extending from left
    draw_m.rectangle([100, 0, 240, 150], fill=(255, 255, 255))
    draw_m.rectangle([0, 250, 150, mh], fill=(255, 255, 255))

    # Right labels: "Ampulla", "Seminal vesicle", "Ejaculatory duct", "Prostatic urethra", "Deep muscles", "Bulbourethral gland", "Muscles of perineum", "Membranous urethra", "Spongy urethra", "Testis", "Epididymis", "Scrotum"
    draw_m.rectangle([550, 0, mw, mh], fill=(255, 255, 255))
    # Wipe right horizontal leader lines extending past x=480
    draw_m.rectangle([450, 50, mw, 120], fill=(255, 255, 255))
    draw_m.rectangle([420, 150, mw, 220], fill=(255, 255, 255))
    draw_m.rectangle([350, 230, mw, 360], fill=(255, 255, 255))

    # Crop organ
    m_bbox = crop_m.getbbox()
    m_cropped = crop_m.crop(m_bbox)
    mcw, mch = m_cropped.size
    scale_m = min(500 / mcw, 420 / mch)
    mnw, mnh = int(mcw * scale_m), int(mch * scale_m)
    m_resized = m_cropped.resize((mnw, mnh), Image.Resampling.LANCZOS)

    canvas_m = Image.new("RGB", (600, 480), (255, 255, 255))
    canvas_m.paste(m_resized, ((600 - mnw) // 2, (480 - mnh) // 2))
    dst_tb_m = os.path.join(DIAGRAMS_DIR, "male_reproductive_textbook.jpg")
    canvas_m.save(dst_tb_m, "JPEG", quality=95)
    print(f"Saved {dst_tb_m} ({os.path.getsize(dst_tb_m)} bytes)")

    # B. Exam Stipple: Authentic South African Matric Examination Line-Art
    # Textbook_LifeSciences_Gr12_Human_Reproduction.pdf-0007-04.png (Left half)
    src_exam = os.path.join(TERMS_DIR, "Term 2", "images", "Textbook_LifeSciences_Gr12_Human_Reproduction.pdf-0007-04.png")
    img_exam = Image.open(src_exam).convert("RGB")
    ew, eh = img_exam.size
    crop_male_exam = img_exam.crop((0, 0, 390, eh))
    # Wipe letters A, B, C, D and leader lines
    draw_me = ImageDraw.Draw(crop_male_exam)
    draw_me.rectangle([0, 250, 80, eh], fill=(255, 255, 255)) # A
    draw_me.rectangle([0, 120, 100, 220], fill=(255, 255, 255)) # B
    draw_me.rectangle([260, 150, 390, 260], fill=(255, 255, 255)) # C
    draw_me.rectangle([220, 350, 390, 440], fill=(255, 255, 255)) # D

    m_exam_bbox = crop_male_exam.getbbox()
    m_exam_cropped = crop_male_exam.crop(m_exam_bbox)
    m_ecw, m_ech = m_exam_cropped.size
    scale_me = min(480 / m_ecw, 420 / m_ech)
    menw, menh = int(m_ecw * scale_me), int(m_ech * scale_me)
    m_exam_resized = m_exam_cropped.resize((menw, menh), Image.Resampling.LANCZOS)

    canvas_me = Image.new("RGB", (600, 480), (255, 255, 255))
    canvas_me.paste(m_exam_resized, ((600 - menw) // 2, (480 - menh) // 2))
    dst_exam_m = os.path.join(DIAGRAMS_DIR, "male_reproductive_exam_stipple.jpg")
    canvas_me.save(dst_exam_m, "JPEG", quality=95)
    print(f"Saved {dst_exam_m} ({os.path.getsize(dst_exam_m)} bytes)")


# ---------------------------------------------------------
# 3. Meiosis Crossing Over
# ---------------------------------------------------------
def prepare_meiosis_plates():
    print("\n--- Preparing Meiosis Crossing Over Plates ---")
    tb_path = os.path.join(DIAGRAMS_DIR, "meiosis_crossing_over_textbook.jpg")
    stipple_path = os.path.join(DIAGRAMS_DIR, "meiosis_crossing_over_exam_stipple.jpg")
    assert os.path.exists(tb_path), "meiosis_crossing_over_textbook.jpg must exist"
    create_exam_stipple(tb_path, stipple_path)


if __name__ == "__main__":
    prepare_female_plates()
    prepare_male_plates()
    prepare_meiosis_plates()
    print("\n[SUCCESS] All Milestone 4 plates generated successfully!")
