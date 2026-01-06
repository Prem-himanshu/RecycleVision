import streamlit as st
from PIL import Image

import predict_6
import predict_10
import predict_12

st.set_page_config(page_title="RecycleVision", layout="centered")

st.title("♻️ RecycleVision – Garbage Classification")

model_choice = st.selectbox(
    "Select classification model",
    ("6 Classes", "10 Classes", "12 Classes")
)

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        if model_choice == "6 Classes":
            label, confidence = predict_6.predict_6(image)
        elif model_choice == "10 Classes":
            label, confidence = predict_10.predict_10(image)
        else:
            label, confidence = predict_12.predict_12(image)

        st.success(f"Prediction: **{label}**")
        st.info(f"Confidence: **{confidence:.2f}**")
