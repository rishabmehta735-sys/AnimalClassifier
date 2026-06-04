from PIL import Image
import os

modes = {}

for root, dirs, files in os.walk('dataset/train'):
    for fname in files:
        fpath = os.path.join(root, fname)
        try:
            img = Image.open(fpath)
            mode = img.mode  # e.g. 'RGB', 'RGBA', 'L', 'P'
            modes[mode] = modes.get(mode, 0) + 1
            if mode != 'RGB':
                print(f"{mode}: {fpath}")
        except Exception as e:
            print(f"ERROR: {fpath} — {e}")

print("\nSummary:", modes)