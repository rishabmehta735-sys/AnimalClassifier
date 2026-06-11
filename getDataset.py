# We are loading and changing rgb values from 0-255 to 0-1 so that neural networks can function in a better way
import tensorflow as tf

IMG_SIZE = (128,128)
BATCH_SIZE = 32



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
        shuffle=True
    )

    print("Dataset built")

    


    train_ds = train_ds.map(lambda x, y: (x / 255.0, y))
    val_ds = val_ds.map(lambda x, y: (x / 255.0, y))
    test_ds = test_ds.map(lambda x, y: (x / 255.0, y))

    augment = tf.keras.Sequential([
        tf.keras.layers.RandomFlip("horizontal"),
        tf.keras.layers.RandomRotation(0.15),
        tf.keras.layers.RandomZoom(0.1),
    ])
    train_ds = train_ds.map(lambda x, y: (augment(x, training=True), y))

    return train_ds, val_ds, test_ds