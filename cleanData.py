# Here we are cleaning the data if there is any file which is invalid we are removing it
from PIL import Image
import os

def cleanImages(folder):
    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        try:
            img = Image.open(fpath)
            img.verify()  # catches corrupt files
        except Exception:
            print(f"Removing bad file: {fpath}")
            os.remove(fpath)

for animal in ['cat', 'dog', 'horse']:
    cleanImages(f'rawData/{animal}')
