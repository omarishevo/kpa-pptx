import streamlit as st
from pptx import Presentation
from PIL import Image
from io import BytesIO

# Title
st.title("📊 Vehicle Traffic and Congestion at KPA Gates – Slide Viewer")

# Load your uploaded PowerPoint file
pptx_file = "OMARPPTX.pptx"
prs = Presentation(pptx_file)

# Slide selector
slide_count = len(prs.slides)
slide_num = st.slider("Select slide number", 1, slide_count, 1)
slide = prs.slides[slide_num - 1]

st.subheader(f"Slide {slide_num} of {slide_count}")

# Extract and display text from the slide
slide_text = ""
for shape in slide.shapes:
    if hasattr(shape, "text"):
        slide_text += shape.text + "\n"

if slide_text.strip():
    st.markdown("### 📝 Slide Text Content")
    st.text(slide_text.strip())
else:
    st.info("No text content found on this slide.")

# Extract and display images (charts, visuals, etc.)
has_image = False
for shape in slide.shapes:
    if shape.shape_type == 13:  # Picture type
        image = shape.image
        image_bytes = image.blob
        img = Image.open(BytesIO(image_bytes))
        st.markdown("### 🖼️ Slide Visual/Chart")
        st.image(img, use_column_width=True)
        has_image = True

if not has_image:
    st.warning("No image/chart found on this slide.")
