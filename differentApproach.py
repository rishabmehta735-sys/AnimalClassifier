import tensorflow as tf
import numpy as np

test_ds = tf.keras.utils.image_dataset_from_directory(
    'dataset/test',
    image_size=(128, 128),
    batch_size=1,
    label_mode='categorical',
    color_mode="rgb",
    shuffle=False
)

print("Dataset built, converting to numpy...")

images_list = []
labels_list = []

# Use as_numpy_iterator to bypass the threading issue
for images, labels in test_ds.as_numpy_iterator():
    images_list.append(images)
    labels_list.append(labels)
    
print(f"Loaded {len(images_list)} images")