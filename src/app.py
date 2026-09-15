"""Streamlit app: cow skin disease screening demo."""

import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

MODEL_PATH = "best.pt"

st.set_page_config(page_title="Cow Skin Disease Screening", layout="centered")
st.title("Cow Skin Disease Screening (Demo)")
st.caption(
    "This tool detects visible skin conditions and flags them for review. "
    "It does not provide a medical diagnosis — always consult a veterinarian."
)


@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)


model = load_model()

uploaded_file = st.file_uploader("Upload a cow image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    with st.spinner("Analyzing..."):
        results = model.predict(np.array(image), conf=0.25)
        result = results[0]

    if len(result.boxes) == 0:
        st.warning("No visible findings detected. REVIEW_REQUIRED: low confidence overall — recommend manual check.")
    else:
        st.subheader("Findings")
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])
            flag = "REVIEW_REQUIRED" if conf < 0.5 else "FINDING_NOTED"
            st.write(f"**{label}** — confidence: {conf:.2f} — `{flag}`")

        annotated = result.plot()
        st.image(annotated, caption="Detected findings", use_container_width=True)

    st.info(
        "This is a screening aid only. All findings should be confirmed by a "
        "qualified veterinarian before any health or treatment decision is made."
    )
    