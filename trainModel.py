# here we are training the model using training dataset and validing it with the validation dataset
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from model import model
from getDataset import getDatasets

# Here ealry stopping means if model keeps perfroming bad (validation loss keeps increasing ) then after
#  5 epochs which is patience it will stop and it will restore the best weights
# Simply because if val_loss is increasing it means model is memorizing overfitting
callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ModelCheckpoint('model/best_model.keras', save_best_only=True)
]
train_ds,val_ds,_ = getDatasets()
print("Dataset loaded. Starting training...")
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=40,
    callbacks=callbacks
)