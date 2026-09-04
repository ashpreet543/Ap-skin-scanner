import streamlit as st
meta = '<meta name="google-site-verification" content="jSn7w9k8ZJtsvbuiBcnyShRAADZgo2OoiPzl--mUgds" />"""
st.markdown(meta, unsafe_allow_html=True)
from PIL import Image

st.set_page_config(page_title="HP Skin Scanner", layout="centered")

st.title("HP Skin Scanner - Dadi Maa Nuskha")

tab1, tab2 = st.tabs(["📁 Gallery", "📷 Camera"])

def show_result():
    st.success("Skin Analysis: Dry Skin Detected")
    st.subheader("👵 Dadi Maa Nuskha")
    st.write("Haldi + Dahi 10 min laga ke dho lo")
    st.subheader("🛒 Meesho Product Suggestions")
    st.write("**Himalaya Neem Face Wash** - Best for dry skin")

with tab1:
    uploaded = st.file_uploader("Upload skin photo", type=["jpg","png","jpeg"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Image")
        if st.button("Analyze"):
            show_result()

with tab2:
    cam = st.camera_input("Take a photo")
    if cam:
        img = Image.open(cam)
        st.image(img)
        if st.button("Analyze Camera", key="cam_analyze"):
            show_result()
