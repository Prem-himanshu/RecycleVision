import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = "model_6_class.h5"

model = tf.keras.models.load_model(MODEL_PATH)

CLASSES = [
    "cardboard",
    "glass",
    "metal",
    "paper",
    "plastic",
    "trash"
]

def predict_6(image):
    img = image.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    preds = model.predict(img)
    class_id = np.argmax(preds)
    confidence = preds[0][class_id]

    return CLASSES[class_id], float(con_]()

