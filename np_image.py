import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Buttefly Image Processor", layout="wide")

# Title
st.title("Butterfly Image - Multi-Color Channel Visualizer")

# Load image from URL
@st.cache_data
def load_image():
    url = "https://i.pinimg.com/474x/2a/1d/42/2a1d424fe1ada838fb3d46f42a0365fd.jpg"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGB")

# Load and display image
butterfly = load_image()
st.image(butterfly, caption="Original Butterfly Image", use_container_width=True)

# Convert to NumPy array
butterfly_np = np.array(butterfly)
R, G, B = butterfly_np[:, :, 0], butterfly_np[:, :, 1], butterfly_np[:, :, 2]

# Create channel images
red_img = np.zeros_like(butterfly_np)
green_img = np.zeros_like(butterfly_np)
blue_img = np.zeros_like(butterfly_np)

red_img[:, :, 0] = R
green_img[:, :, 1] = G
blue_img[:, :, 2] = B

# Display RGB channels
st.subheader("RGB Channel Visualization")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(red_img, caption="Red Channel", use_container_width=True)

with col2:
    st.image(green_img, caption="Green Channel", use_container_width=True)

with col3:
    st.image(blue_img, caption="Blue Channel", use_container_width=True)

# Grayscale + Colormap
st.subheader("Colormapped Grayscale Image")

colormap = st.selectbox(
    "Choose a Matplotlib colormap",
    ["viridis", "plasma", "inferno", "magma", "cividis", "hot", "cool", "gray"]
)

butterfly_gray = butterfly.convert("L")
butterfly_gray_np = np.array(butterfly_gray)

# Plot using matplotlib with colormap
fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(butterfly_gray_np, cmap=colormap)
plt.axis("off")

# DO NOT USE: plt.show()
# USE THIS INSTEAD:
st.pyplot(fig)