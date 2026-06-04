# This ia a cnn based neural network 
from tensorflow.keras import models,layers # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore
model = models.Sequential([
    # 32 filters and each filter is of 3 * 3 size and polling is of 2 * 2
    layers.Conv2D(32,(3,3) ,activation = "relu" , input_shape = (128,128,3)),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(64,(3,3) ,activation = "relu" ),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    layers.Conv2D(128,(3,3) ,activation = "relu" ),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2,2),

    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    # Dropout means drop half od the total neurons in the last layer 
    # so that each neuron becomes independent and strong and it prevents overfitting
    layers.Dropout(0.45),
    layers.Dense(3, activation='softmax')  # 3 = cat, dog, horse

])

model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)
model.summary()
