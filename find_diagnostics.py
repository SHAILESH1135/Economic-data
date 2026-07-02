import os

search_paths = [
    r"C:\SHAILESH\My work space\India economic data analysis",
    r"C:\Users\Rames",
    r"C:\Users\Rames\.gemini\antigravity-ide\brain\f1890fff-ca99-476d-b3e0-b83085c98b05"
]

found = False
for path in search_paths:
    print(f"Scanning {path}...")
    for root, dirs, files in os.walk(path):
        if "diagnostics.txt" in files:
            full_path = os.path.join(root, "diagnostics.txt")
            print(f"FOUND diagnostics.txt at: {full_path}")
            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    print("--- CONTENTS ---")
                    print(f.read())
                    print("----------------")
                found = True
            except Exception as e:
                print(f"Error reading file: {e}")
            break
    if found:
        break
else:
    print("diagnostics.txt not found anywhere!")
