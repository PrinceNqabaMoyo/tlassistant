import re
import os

source_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "source_plates", "male_internal_organs.svg")
target_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public", "diagrams", "male_reproductive_cleaned.svg")

with open(source_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add a <style> block at the beginning of the svg to cleanly hide all <text> elements
# and pointer lines that have stroke="#000" and stroke-width="3"
style_block = """
<style>
  text { display: none !important; }
  line[stroke="#000"][stroke-width="3"] { display: none !important; }
  line[stroke="#000"] { display: none !important; }
  polygon[points*="157.19"], polygon[points*="187.89"], polygon[points*="210.38"], 
  polygon[points*="565.44"], polygon[points*="437.89"], polygon[points*="533.33"], 
  polygon[points*="192.55"] { display: none !important; }
</style>
"""

# Insert style_block after opening <svg ...>
svg_open_end = content.find('>') + 1
clean_content = content[:svg_open_end] + style_block + content[svg_open_end:]

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(clean_content)

print(f"Created {target_path} ({os.path.getsize(target_path)} bytes)")
