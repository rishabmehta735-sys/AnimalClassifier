from PIL import Image
import os

for folders in ["dataset/train","dataset/val","dataset/test"]:
    for root,dirs,files in os.walk(folders):
# for root, dirs, files in [os.walk('dataset/train'),os.walk('dataset/val'),os.walk('dataset/test')]:
        for fname in files:
            fpath = os.path.join(root, fname)
            try:
                img = Image.open(fpath)
                if img.mode != 'RGB':
                    print(f"Converting {img.mode} -> RGB: {fpath}")
                    img.convert('RGB').save(fpath)
            except Exception as e:
                print(f"ERROR: {fpath} — {e}")