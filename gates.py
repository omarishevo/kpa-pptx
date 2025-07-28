import streamlit as st
from PIL import Image
import os

# Set the path to your slide images folder
SLIDES_DIR = "slides"

# Load all slide images
image_files = sorted([
    os.path.join(SLIDES_DIR, f)
    for f in os.listdir(SLIDES_DIR)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
])

total_slides = len(image_files)

st.title("🚦 Vehicle Traffic and Congestion at KPA Gates")
st.subheader("📊 Slide-by-Slide Viewer (Image Mode)")

if total_slides == 0:
    st.error("❌ No slide images found. Please place your .png/.jpg slides in the 'slides' folder.")
else:
    slide_num = st.slider("Select slide number", 1, total_slides, 1)
    st.image(Image.open(image_files[slide_num - 1]), caption=f"Slide {slide_num}", use_column_width=True)
