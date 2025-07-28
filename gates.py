import streamlit as st
from PIL import Image
import os

st.title("🚦 Vehicle Traffic and Congestion at KPA Gates – Slide Viewer (Image Mode)")

# Folder containing slide images
SLIDES_FOLDER = "slides"

# Get all image files
image_files = sorted([
    os.path.join(SLIDES_FOLDER, file)
    for file in os.listdir(SLIDES_FOLDER)
    if file.lower().endswith((".png", ".jpg", ".jpeg"))
])

total_slides = len(image_files)

if total_slides == 0:
    st.error("No slide images found in the 'slides/' folder.")
else:
    slide_num = st.slider("Select Slide Number", 1, total_slides, 1)
    selected_image = image_files[slide_num - 1]

    st.header(f"📊 Slide {slide_num} of {total_slides}")
    st.image(Image.open(selected_image), use_column_width=True)
