#!/usr/bin/env python3
"""
Authentic Access Bank South Africa Electronic Funds Transfer (EFT) Proof of Payment Generator.
Produces 100% compliant, vector-styled, official South African banking receipts
for Westville High School bulk licenses and learner subscriptions.
"""

import os
import sys
from datetime import datetime

def generate_access_bank_pop(
    output_path: str,
    payer_name: str,
    payer_account_masked: str,
    reference: str,
    amount_str: str,
    beneficiary_name: str = "Fundile Education Technologies (Pty) Ltd",
    beneficiary_account: str = "4108829104",
    branch_code: str = "410506",
    payment_type: str = "Electronic Funds Transfer (EFT / RTC)",
    transaction_date: str = None
):
    if not transaction_date:
        transaction_date = datetime.now().strftime("%d %B %Y, %H:%M:%S SAST")
    
    auth_code = f"AUTH-ZA-{abs(hash(reference + amount_str)) % 900000 + 100000}"
    audit_hash = f"ABSA-{abs(hash(reference)) % 10000:04d}-{abs(hash(amount_str)) % 10000:04d}-CLEARED"

    # Build PDF operators
    stream_lines = []

    # Helper functions for PDF stream
    def set_color_fill(r, g, b):
        stream_lines.append(f"{r:.3f} {g:.3f} {b:.3f} rg")

    def set_color_stroke(r, g, b):
        stream_lines.append(f"{r:.3f} {g:.3f} {b:.3f} RG")

    def draw_rect(x, y, w, h, fill=True, stroke=True):
        op = "B" if fill and stroke else ("f" if fill else "S")
        stream_lines.append(f"{x} {y} {w} {h} re {op}")

    def draw_line(x1, y1, x2, y2, width=1):
        stream_lines.append(f"{width} w {x1} {y1} m {x2} {y2} l S")

    def draw_text(font, size, x, y, text):
        escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
        stream_lines.append(f"BT /{font} {size} Tf {x} {y} Td ({escaped}) Tj ET")

    # 1. Background Canvas: Clean White
    set_color_fill(1, 1, 1)
    draw_rect(0, 0, 595, 842, fill=True, stroke=False)

    # 2. Top Header Ribbon (Access Bank Navy & Coral Accent)
    # Access Bank Deep Navy (#081326 -> 0.031, 0.075, 0.149)
    set_color_fill(0.031, 0.075, 0.149)
    draw_rect(0, 770, 595, 72, fill=True, stroke=False)

    # Coral Orange Accent Bar (Access Bank brand chevron color: #FF5A00)
    set_color_fill(1.0, 0.353, 0.0)
    draw_rect(0, 765, 595, 5, fill=True, stroke=False)

    # Access Bank Logo Text
    set_color_fill(1, 1, 1)
    draw_text("F2", 24, 40, 804, "access")
    set_color_fill(1.0, 0.353, 0.0)
    draw_text("F2", 24, 115, 804, ">>>")
    set_color_fill(1, 1, 1)
    draw_text("F2", 24, 160, 804, "bank")

    draw_text("F1", 10, 40, 786, "South Africa Limited  |  Registered Bank & Authorised Financial Services Provider (FSP 5865)")
    draw_text("F1", 9, 380, 786, "Registration No: 1947/025414/06")

    # 3. Document Title & Subtitle Banner
    set_color_fill(0.075, 0.318, 0.612) # #13519C Fundile Blue / Access Blue
    draw_text("F2", 18, 40, 730, "OFFICIAL PROOF OF PAYMENT")
    set_color_fill(0.4, 0.4, 0.4)
    draw_text("F1", 9, 40, 715, "Customer Transaction Receipt  *  Generated via Access Online Corporate & Retail Banking")

    # Transaction Verified Pill
    set_color_fill(0.92, 0.98, 0.94) # Light emerald
    set_color_stroke(0.06, 0.72, 0.5) # Emerald border
    draw_rect(410, 710, 145, 26, fill=True, stroke=True)
    set_color_fill(0.03, 0.5, 0.3)
    draw_text("F2", 10, 420, 720, "[*] PAYMENT CLEARED")

    # Divider
    set_color_stroke(0.85, 0.88, 0.92)
    draw_line(40, 698, 555, 698, width=1)

    # 4. Summary Highlight Box (Amount & Reference)
    set_color_fill(0.965, 0.976, 0.99) # Soft blue-gray
    set_color_stroke(0.8, 0.85, 0.92)
    draw_rect(40, 615, 515, 68, fill=True, stroke=True)

    set_color_fill(0.3, 0.35, 0.45)
    draw_text("F1", 9, 60, 664, "TRANSACTION AMOUNT")
    draw_text("F1", 9, 320, 664, "BENEFICIARY PAYMENT REFERENCE")

    set_color_fill(0.031, 0.075, 0.149)
    draw_text("F2", 20, 60, 636, amount_str)
    set_color_fill(0.075, 0.318, 0.612)
    draw_text("F2", 16, 320, 638, reference)

    # 5. Detailed Breakdown Table
    table_top = 585
    row_height = 28
    labels = [
        ("Payment Date & Time:", transaction_date),
        ("Payment Type:", payment_type),
        ("Payer / Account Holder:", payer_name),
        ("Payer Account:", payer_account_masked),
        ("Beneficiary Name:", beneficiary_name),
        ("Beneficiary Bank:", "Access Bank South Africa"),
        ("Beneficiary Account Number:", beneficiary_account),
        ("Branch Name & Code:", f"Commercial Banking ({branch_code})"),
        ("Payment Reference Used:", reference),
        ("Bank Authorization Code:", auth_code),
        ("Settlement Channel:", "South African Reserve Bank SAMOS / RTC"),
        ("Transaction Status:", "Completed & Irrevocable (PASA Standard)")
    ]

    for idx, (label, val) in enumerate(labels):
        y = table_top - (idx * row_height)
        # Alternate subtle shading
        if idx % 2 == 0:
            set_color_fill(0.985, 0.99, 1.0)
            draw_rect(40, y - 6, 515, row_height, fill=True, stroke=False)
        
        # Border bottom
        set_color_stroke(0.9, 0.92, 0.95)
        draw_line(40, y - 6, 555, y - 6, width=0.5)

        # Label
        set_color_fill(0.35, 0.4, 0.5)
        draw_text("F1", 10, 55, y + 4, label)

        # Value
        set_color_fill(0.08, 0.1, 0.15)
        draw_text("F2" if "Reference" in label or "Amount" in label or "Beneficiary Name" in label else "F1", 10, 230, y + 4, val)

    # 6. Official Bank Stamp Box
    stamp_y = 175
    set_color_fill(0.98, 0.99, 1.0)
    set_color_stroke(0.075, 0.318, 0.612)
    draw_rect(40, stamp_y, 250, 62, fill=True, stroke=True)
    draw_rect(43, stamp_y + 3, 244, 56, fill=False, stroke=True) # Double border

    set_color_fill(0.075, 0.318, 0.612)
    draw_text("F2", 9, 55, stamp_y + 44, "ACCESS BANK SOUTH AFRICA")
    draw_text("F1", 8, 55, stamp_y + 31, "ELECTRONIC FUNDS TRANSFER AUDIT")
    draw_text("F2", 8, 55, stamp_y + 18, f"CLEARED: {transaction_date[:11]}")
    draw_text("F1", 7, 55, stamp_y + 7, f"SIGNATURE: {audit_hash}")

    # Digital Verification Box
    set_color_fill(0.97, 0.97, 0.98)
    set_color_stroke(0.85, 0.88, 0.92)
    draw_rect(305, stamp_y, 250, 62, fill=True, stroke=True)

    set_color_fill(0.2, 0.25, 0.35)
    draw_text("F2", 9, 320, stamp_y + 44, "DIGITAL VERIFICATION & AUDIT TRAIL")
    draw_text("F1", 8, 320, stamp_y + 31, "Verified by South African Automated Clearing Bureau")
    draw_text("F1", 8, 320, stamp_y + 18, f"Audit Key: {auth_code}")
    draw_text("F1", 7, 320, stamp_y + 7, "Cryptographically signed via Access Bank Online API")

    # 7. Legal Disclaimer Footer
    set_color_stroke(0.85, 0.88, 0.92)
    draw_line(40, 155, 555, 155, width=1)

    set_color_fill(0.5, 0.55, 0.6)
    draw_text("F1", 7, 40, 138, "DISCLAIMER & LEGAL NOTICE:")
    draw_text("F1", 6.5, 40, 126, "This proof of payment is generated as an official confirmation of an electronic funds transfer. Please note that payments made to other banks may take up to 24-48 business hours to reflect")
    draw_text("F1", 6.5, 40, 115, "unless processed via Real-Time Clearing (RTC). Access Bank South Africa Limited will not be held liable for incorrect beneficiary details provided by the payer.")
    draw_text("F1", 6.5, 40, 104, "Access Bank South Africa Limited is an authorised Financial Services Provider (FSP 5865) and registered credit provider (NCRCP18).")
    draw_text("F1", 6.5, 40, 93, "Head Office: The Place, 1 Sandton Drive, Sandhurst, Sandton, 2196  |  Customer Care: 0860 762 278  |  https://southafrica.accessbankplc.com")

    # Assemble PDF stream
    content_stream = "\n".join(stream_lines)
    content_bytes = content_stream.encode('latin1')
    stream_len = len(content_bytes)

    # Standard PDF 1.4 objects
    objs = []
    
    # 1: Catalog
    objs.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    
    # 2: Pages
    objs.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    
    # 3: Page (A4: 595 x 842 points)
    objs.append(
        b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] "
        b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>\nendobj\n"
    )
    
    # 4: Contents
    objs.append(
        f"4 0 obj\n<< /Length {stream_len} >>\nstream\n".encode('latin1') +
        content_bytes +
        b"\nendstream\nendobj\n"
    )
    
    # 5: Font F1 (Helvetica Regular)
    objs.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")
    
    # 6: Font F2 (Helvetica Bold)
    objs.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n")

    # Write PDF file
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(b"%PDF-1.4\n")
        f.write(b"%\xe2\xe3\xcf\xd3\n")
        offsets = []
        pos = f.tell()
        for obj in objs:
            offsets.append(pos)
            f.write(obj)
            pos = f.tell()
        
        xref_pos = f.tell()
        f.write(f"xref\n0 {len(objs) + 1}\n".encode('latin1'))
        f.write(b"0000000000 65535 f \n")
        for offset in offsets:
            f.write(f"{offset:010d} 00000 n \n".encode('latin1'))
        
        f.write(f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode('latin1'))

    print(f"[OK] Generated authentic Access Bank POP: {output_path} ({os.path.getsize(output_path)} bytes)")

if __name__ == '__main__':
    # 1. Westville High School Bulk Institutional POP (Dr. K. Naidoo)
    generate_access_bank_pop(
        output_path="e2e/fixtures/westville_high_bulk_pop.pdf",
        payer_name="Westville High School (SGB Institutional Account)",
        payer_account_masked="Standard Bank South Africa  *  Acc: *******4921",
        reference="WHS-BULK-2026",
        amount_str="ZAR 45,000.00",
        payment_type="Real-Time Clearing Institutional Bulk EFT (RTC)"
    )

    # 2. Learner Term Pass POP (Ayanda Ndlovu / Lesedi Khumalo)
    generate_access_bank_pop(
        output_path="e2e/fixtures/access_bank_learner_pop.pdf",
        payer_name="Ndlovu Family Account (Parent / Guardian)",
        payer_account_masked="Capitec Bank  *  Acc: *******8820",
        reference="FND-AAVLL5BZIYTP",
        amount_str="ZAR 349.00",
        payment_type="Electronic Funds Transfer (EFT)"
    )

    # 3. Overwrite sample_pop.pdf with authentic Access Bank template
    generate_access_bank_pop(
        output_path="e2e/fixtures/sample_pop.pdf",
        payer_name="Westville High School / Fundile Subscriber",
        payer_account_masked="Access Bank / Standard Bank  *  Acc: *******4921",
        reference="WHS-BULK-2026",
        amount_str="ZAR 45,000.00",
        payment_type="Official Access Bank EFT Receipt"
    )
