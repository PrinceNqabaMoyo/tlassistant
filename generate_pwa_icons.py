import math
from PIL import Image, ImageDraw

def create_graduation_cap_icon(size, is_maskable=False):
    # Supersample at 4x for anti-aliasing
    scale = 4
    canvas_size = size * scale
    
    # Brand blue background: #13519C -> (19, 81, 156)
    bg_color = (19, 81, 156, 255)
    img = Image.new("RGBA", (canvas_size, canvas_size), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Maskable icons need more padding (safe area is inner 80%, so 40% radius circle)
    # Standard icon safe area ~ 70% width, maskable ~ 55% width
    target_width = canvas_size * (0.55 if is_maskable else 0.68)
    
    cx = canvas_size / 2
    cy = canvas_size / 2 - (canvas_size * 0.02) # slightly raised center
    
    w = target_width
    h = w * 0.44 # mortarboard aspect
    
    # 1. Skullcap / Head band (curved arch under the diamond)
    # Lucide-style lower curve
    cap_w = w * 0.58
    cap_top = cy + h * 0.1
    cap_bot = cy + h * 0.85
    cap_left = cx - cap_w / 2
    cap_right = cx + cap_w / 2
    
    # Draw lower skullcap arc
    points_cap = []
    # Left edge going down
    points_cap.append((cap_left, cap_top))
    # Bottom curved arch
    steps = 30
    for i in range(steps + 1):
        t = i / steps
        px = cap_left + t * cap_w
        # Parabolic/elliptical sag
        py = cap_bot + math.sin(t * math.pi) * (h * 0.25)
        points_cap.append((px, py))
    points_cap.append((cap_right, cap_top))
    
    # Fill skullcap (lower arch in slightly deeper brand orange)
    draw.polygon(points_cap, fill=(230, 122, 0, 255))
    
    # 2. Mortarboard Diamond (Top rhomboid)
    top_pt = (cx, cy - h * 0.72)
    right_pt = (cx + w * 0.50, cy)
    bottom_pt = (cx, cy + h * 0.72)
    left_pt = (cx - w * 0.50, cy)
    
    # Shadow under mortarboard for crisp 3D separation from brand blue background
    shadow_offset = canvas_size * 0.018
    draw.polygon([
        (top_pt[0], top_pt[1] + shadow_offset),
        (right_pt[0], right_pt[1] + shadow_offset),
        (bottom_pt[0], bottom_pt[1] + shadow_offset),
        (left_pt[0], left_pt[1] + shadow_offset)
    ], fill=(10, 48, 96, 220)) # rich deep navy shadow
    
    # Main Brand Orange (#FF9100) mortarboard diamond
    draw.polygon([top_pt, right_pt, bottom_pt, left_pt], fill=(255, 145, 0, 255))

    # Subtle top highlight facet on mortarboard diamond
    draw.polygon([top_pt, right_pt, (cx, cy), left_pt], fill=(255, 165, 30, 255))
    
    # 3. Mortarboard Center Button
    btn_r = w * 0.042
    draw.ellipse([cx - btn_r, cy - btn_r, cx + btn_r, cy + btn_r], fill=(255, 185, 75, 255), outline=(204, 112, 0, 255), width=max(2, int(w * 0.008)))
    
    # 4. Tassel (Ribbon & Fringe in brand orange / amber gold)
    line_w = max(4, int(w * 0.026))
    
    tassel_k1 = (cx + w * 0.22, cy + h * 0.1)
    tassel_k2 = (cx + w * 0.44, cy + h * 0.35)
    tassel_drop = (cx + w * 0.46, cy + h * 0.88)
    
    draw.line([ (cx, cy), tassel_k1, tassel_k2, tassel_drop ], fill=(255, 175, 50, 255), width=line_w)
    
    # Tassel fringe/tail
    fringe_w = w * 0.052
    fringe_h = h * 0.44
    draw.rounded_rectangle([
        tassel_drop[0] - fringe_w / 2,
        tassel_drop[1],
        tassel_drop[0] + fringe_w / 2,
        tassel_drop[1] + fringe_h
    ], radius=int(fringe_w * 0.3), fill=(255, 145, 0, 255), outline=(230, 122, 0, 255), width=max(1, int(w * 0.006)))

    # Downscale with high-quality Lanczos filter
    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    return final_img

# Generate all required PWA icons
icons = {
    "public/pwa-192x192.png": (192, False),
    "public/pwa-512x512.png": (512, False),
    "public/pwa-maskable-512x512.png": (512, True),
    "public/apple-touch-icon.png": (180, False),
}

for path, (size, maskable) in icons.items():
    icon_img = create_graduation_cap_icon(size, is_maskable=maskable)
    icon_img.save(path, "PNG")
    print(f"Generated {path} ({size}x{size}, maskable={maskable})")

print("All PWA icons generated successfully!")
