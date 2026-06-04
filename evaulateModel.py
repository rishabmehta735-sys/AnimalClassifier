# We are plotting the accuracy and loss for both train and validation dataset
# Testing it with test dataset then the classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,classification_report
import numpy as np
# from trainModel import history
from getDataset import getDatasets
from model import model

print("hello")
_, _, test_ds = getDatasets()
print("Dataset loaded")

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
        print("INSIDE")
        preds = model.predict(images)
        y_true.extend(np.argmax(labels.numpy(), axis=1))
        y_pred.extend(np.argmax(preds, axis=1))

    # print(confusion_matrix(y_true,y_pred))
    print(classification_report(y_true, y_pred, target_names=['cat','dog','horse']))
except:
    print("An error occurred")
