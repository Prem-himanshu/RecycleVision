import streamlit as st

st.set_page_config(page_title="RecycleVision", layout="centered")

st.title("♻️ RecycleVision – Garbage Classification")
st.write("App is starting...")

try:
    import predict_6
    import predict_10
    import predict_12
    st.success("Models loaded successfully")
except Exception as e:
    st.error("❌ Model loading failed")
    st.exception(e)
    st.stop()

