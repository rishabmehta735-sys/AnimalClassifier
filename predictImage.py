# This file is predicting an image being uploaded by the user using the model
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('model/best_model.keras')


def predict(file):
    
        img = Image.open(file).convert("RGB").resize((128, 128))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)  # model expects (1, 128, 128, 3)

        probs = model.predict(img_array, verbose=0)[0]
        probabilities = []

        for prob in (probs):
            probabilities.append(prob)
           
        return probabilities
