# We are loading and changing rgb values from 0-255 to 0-1 so that neural networks can function in a better way
import tensorflow as tf
import numpy as np
import os
from PIL import Image
IMG_SIZE = (128,128)
BATCH_SIZE = 64


def load_test_manually(test_dir="dataset/test", img_size=(128,128)):
    images, labels, class_names = [], [], sorted(os.listdir(test_dir))
    
    for label_idx, class_name in enumerate(class_names):
        class_dir = os.path.join(test_dir, class_name)
        for fname in os.listdir(class_dir):
            path = os.path.join(class_dir, fname)
            try:
                img = Image.open(path).convert("RGB").resize(img_size)
                images.append(np.array(img) / 255.0)
                labels.append(label_idx)
            except:
                print(f"Skipping: {path}")
    
    return np.array(images), np.array(labels), class_names

def getDatasets():
    train_ds = tf.keras.utils.image_dataset_from_directory(
        'dataset/train',
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode='categorical',
        color_mode="rgb",
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        'dataset/val',
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        label_mode='categorical',
        color_mode="rgb",
    )

    test_ds = tf.keras.utils.image_dataset_from_directory(
        'dataset/test',
        image_size=(128, 128),
        batch_size=1,
        label_mode='categorical',
        color_mode="rgb",
        shuffle=False
    )

    print("Dataset built")

    
    # test_ds = test_ds.prefetch(tf.data.AUTOTUNE)

    # for images, labels in test_ds.as_numpy_iterator():
    #     print(images.shape)
    #     print(labels.shape)

    # print("Done")

    train_ds = train_ds.map(lambda x, y: (x / 255.0, y))
    val_ds = val_ds.map(lambda x, y: (x / 255.0, y))
    test_ds = test_ds.map(lambda x, y: (x / 255.0, y))

    augment = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.15),
        tf.keras.layers.RandomZoom(0.1),
    ])
    train_ds = train_ds.map(lambda x, y: (augment(x, training=True), y))

    return train_ds, val_ds, train_ds