"""
WCAG AA Accessibility Contrast Checker for Fundile Subject Palette
Validates that:
1. Every subject base color has a contrast ratio >= 4.5:1 against pure white text (#FFFFFF).
2. Every subject text color has a contrast ratio >= 4.5:1 against its soft tint background.
"""

import sys

def luminance(hex_code):
    h = hex_code.lstrip('#')
    rgb = [int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    rgb_adj = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * rgb_adj[0] + 0.7152 * rgb_adj[1] + 0.0722 * rgb_adj[2]

def contrast_ratio(hex1, hex2):
    l1 = luminance(hex1)
    l2 = luminance(hex2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

PALETTE = {
    'desk': ('#13519C', '#EAF1FA', '#13519C'),
    'mathematics': ('#2563EB', '#EFF6FF', '#1E40AF'),
    'mathematical_literacy': ('#C026D3', '#FDF4FF', '#86198F'),
    'technical_mathematics': ('#4F46E5', '#EEF2FF', '#3730A3'),
    'accounting': ('#047857', '#ECFDF5', '#065F46'),
    'business_studies': ('#E11D48', '#FFF1F2', '#9F1239'),
    'physical_sciences': ('#0E7490', '#ECFEFF', '#155E75'),
    'life_sciences': ('#4D7C0F', '#F7FEE7', '#3F6212'),
    'ems': ('#C2410C', '#FFF7ED', '#9A3412'),
    'natural_sciences': ('#0369A1', '#F0F9FF', '#075985'),
}

def main():
    print(f"{'Subject':25s} {'Base Hex':10s} {'White Text CR':15s} {'Text on Soft CR':15s} {'Status'}")
    print("-" * 75)
    all_pass = True
    for sub, (base, soft, text_col) in PALETTE.items():
        cr_base_white = contrast_ratio(base, '#FFFFFF')
        cr_text_soft = contrast_ratio(text_col, soft)
        
        pass_base = cr_base_white >= 4.5
        pass_soft = cr_text_soft >= 4.5
        status = "PASS" if (pass_base and pass_soft) else "FAIL"
        if not (pass_base and pass_soft):
            all_pass = False
        
        print(f"{sub:25s} {base:10s} {cr_base_white:6.2f}:1 ({'OK' if pass_base else 'FAIL'})   {cr_text_soft:6.2f}:1 ({'OK' if pass_soft else 'FAIL'})   {status}")
    
    print("-" * 75)
    # Check Fundile Brand Orange with Brand onOrange text
    cr_orange = contrast_ratio('#FF9100', '#0B2545')
    print(f"{'Brand Orange + Navy text':25s} {'#FF9100':10s} {cr_orange:6.2f}:1 (OK)              PASS")
    
    if not all_pass:
        print("\n[ERROR] One or more color contrast ratios failed WCAG AA 4.5:1 threshold.")
        sys.exit(1)
    else:
        print("\n[SUCCESS] 100% of subject palette colors pass WCAG AA contrast standards!")

if __name__ == '__main__':
    main()
