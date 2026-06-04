from PIL import Image
import os

print("=== Scanning test folder ===")
for root, dirs, files in os.walk("dataset/test"):
    for fname in files:
        path = os.path.join(root, fname)
        try:
            img = Image.open(path)
            img.load()  # forces full decode, not just header
            print(f"OK | {img.mode} | {img.size} | {path}")
        except Exception as e:
            print(f"BAD | {path} | {e}")