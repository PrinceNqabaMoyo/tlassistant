path = "caps-ai-backend/app/utils/mathematical_literacy/gr11_probability_generator.py"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Replace all mangled unicode characters
text = text.replace("o\"", "✓")
text = text.replace("^c", "∩")
text = text.replace("^.", "∅")
text = text.replace("", "")

# Replace all escaped curly braces in f-strings
text = text.replace(r"$\\{\\{1; 3; 5; 7; 9; 11; 13; 15; 17; 19\\}\\}$", "{1; 3; 5; 7; 9; 11; 13; 15; 17; 19}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{2; 4; 6; 8; 10; 12; 14; 16; 18; 20\\}\\}$", "{2; 4; 6; 8; 10; 12; 14; 16; 18; 20}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{1; 2; 3; 4; 5; 6\\}\\}$", "{1; 2; 3; 4; 5; 6}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{2; 4; 6\\}\\}$", "{2; 4; 6}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{3; 6\\}\\}$", "{3; 6}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{6\\}\\}$", "{6}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{2; 3; 4; 6\\}\\}$", "{2; 3; 4; 6}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{(H, H); (H, T); (T, H); (T, T)\\}\\}$", "{(H, H); (H, T); (T, H); (T, T)}".replace("{", "{{").replace("}", "}}"))
text = text.replace(r"$\\{\\{(H, H); (H, T); (T, H)\\}\\}$", "{(H, H); (H, T); (T, H)}".replace("{", "{{").replace("}", "}}"))

# Any remaining \{{ or \}}
text = text.replace(r"\\{\\{", "{{").replace(r"\\}\\}", "}}")
text = text.replace(r"\\{", "{{").replace(r"\\}", "}}")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaned up unicode and braces.")
