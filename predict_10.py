import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = "model_10_class.h5"

model = tf.keras.models.load_model(MODEL_PATH)

CLASSES = [
    "battery",
    "biological",
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "shoes",
    "trash",
    "clothes"
]

def predict_10(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)
    class_id = np.argmax(preds)
    confidence = preds[0][class_id]

    return CLASSES[class_id], float(confidence)

