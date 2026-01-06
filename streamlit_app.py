import streamlit as st
from PIL import Image

# ✅ IMPORT FUNCTIONS (THIS FIXES YOUR ERROR)
from predict_6 import predict_6
from predict_10 import predict_10
from predict_12 import predict_12

st.set_page_config(page_title="RecycleVision", layout="centered")

st.title("♻️ RecycleVision – Garbage Classification")
st.write("Upload an image to classify garbage")

# Select model
model_choice = st.selectbox(
    "Choose classification model",
    ["6 Classes", "10 Classes", "12 Classes"]
)

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Predicting..."):
            if model_choice == "6 Classes":
                label, confidence = predict_6(image)
            elif model_choice == "10 Classes":
                label, confidence = predict_10(image)
            else:
                label, confidence = predict_12(image)

        st.success(f"Prediction: **{label}**")
        st.info(f"Confidence: **{confidence**


