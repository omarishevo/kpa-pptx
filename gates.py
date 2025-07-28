import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import os

# Constants
PDF_PATH = "OMARPPTX.pdf"
SLIDES_DIR = "pdf_slides"

# Convert PDF pages to images (only once)
@st.cache_resource
def convert_pdf_to_images(pdf_path):
    if not os.path.exists(SLIDES_DIR):
        os.makedirs(SLIDES_DIR)
    
    pages = convert_from_path(pdf_path, dpi=200)
    images = []

    for i, page in enumerate(pages):
        image_path = os.path.join(SLIDES_DIR, f"slide_{i+1}.png")
        page.save(image_path, "PNG")
        images.append(image_path)

    return images

# Load and convert the PDF
slide_images = convert_pdf_to_images(PDF_PATH)
total_slides = len(slide_images)

# UI
st.title("🚦 Vehicle Traffic and Congestion at KPA Gates")
st.subheader("📑 Slide-by-Slide Viewer (PDF-Based)")

slide_num = st.slider("Select Slide", 1, total_slides, 1)
image_path = slide_images[slide_num - 1]

st.image(Image.open(image_path), caption=f"Slide {slide_num} of {total_slides}", use_column_width=True)
