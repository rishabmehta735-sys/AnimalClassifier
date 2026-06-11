# We are plotting the accuracy and loss for both train and validation dataset
# Testing it with test dataset then the classification_report
#import matplotlib.pyplot as plt
from sklearn.metrics import classification_report

import tensorflow as tf
import numpy as np
# from trainModel import history
from getDataset import getDatasets



model = tf.keras.models.load_model('model/best_model.keras')
_, _, test_ds = getDatasets()




# Can be used to plot a graph
# for images, labels in test_ds.as_numpy_iterator():
#     print(images.shape)
#     print(labels.shape)
# plt.figure(figsize=(12, 4))

# plt.subplot(1, 2, 1)
# plt.plot(history.history['accuracy'], label='Train')
# plt.plot(history.history['val_accuracy'], label='Val')
# plt.title('Accuracy')
# plt.legend()

# plt.subplot(1, 2, 2)
# plt.plot(history.history['loss'], label='Train')
# plt.plot(history.history['val_loss'], label='Val')
# plt.title('Loss')
# plt.legend()

# plt.show()

y_true, y_pred = [], []
try:
    for images, labels in test_ds:
   
        preds = model.predict(images)
        y_true.extend(np.argmax(labels.numpy(), axis=1))
        y_pred.extend(np.argmax(preds, axis=1))

    print(classification_report(y_true, y_pred, target_names=['cat','dog','horse']))
except Exception as e:
    print("An error occurred:",e)
