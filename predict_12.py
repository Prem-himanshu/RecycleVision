import numpy as np
import tensorflow as tf

MODEL_PATH = "model_12_class.h5"

model = tf.keras.models.load_model(MODEL_PATH)

CLASSES = [
    "battery",
    "biological",
    "brown-glass",
    "cardboard",
    "clothes",
    "green-glass",
    "metal",
    "paper",
    "plastic",
    "shoes",
    "trash",
    "white-glass"
]

def predict_12(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)
    class_id = np.argmax(preds)
    confidence = float(preds[0][class_id])

    return CLASSES[class_id], confidence
