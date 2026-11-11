from PIL import Image
import os

source_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates")

png_path = os.path.join(source_dir, "synapsis_crossing_over_nolabels.png")
if os.path.exists(png_path):
    img = Image.open(png_path)
    print("synapsis_crossing_over_nolabels.png:")
    print("  Size:", img.size)
    print("  Mode:", img.mode)
    print("  Format:", img.format)
