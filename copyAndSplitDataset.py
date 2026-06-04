# We are creating copy of the original dataset and splitting
#  it into three components train 70%,validation 15% and test 15 %
import os
import random
import shutil

def copyAndSplitDataset(animal,train = 0.7,val = 0.15):
    parent_dirs = f'rawData/{animal}'
    
    allFiles =[os.path.join(parent_dirs,f) for f in os.listdir(parent_dirs)] 
    random.shuffle(allFiles)
    length = len(allFiles)
   
    split_dataset = {
        "train": allFiles[:int(length * train)],
        "val": allFiles[int(length * train) : int(length *(train + val))],
        "test" : allFiles[int(length * (train + val)) :]

    }
    print("train dataset length ",len(split_dataset["train"]))
    print("val dataset length ",len(split_dataset["val"]))
    for split,files in split_dataset.items():
        dest = f'dataset/{split}/{animal}'
        os.makedirs(dest,exist_ok=True)
        for f in files:
            shutil.copy(f,dest)
   


for animal in ["cat","dog","horse"]:
    copyAndSplitDataset(animal)