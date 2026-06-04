from PIL import Image
import os

def clean_dataset(root_dir="dataset"):
    fixed = 0
    deleted = 0

    for root, dirs, files in os.walk(root_dir):
        for fname in files:
            path = os.path.join(root, fname)
            try:
                img = Image.open(path)
                
                # Convert anything that isn't RGB
                if img.mode != "RGB":
                    print(f"Converting {img.mode} -> RGB: {path}")
                    img = img.convert("RGB")
                    img.save(path)
                    fixed += 1
                    
            except Exception as e:
                # Corrupted/unreadable - delete it
                print(f"Deleting corrupt file: {path} ({e})")
                os.remove(path)
                deleted += 1

    print(f"\nDone. Fixed: {fixed}, Deleted: {deleted}")

clean_dataset()