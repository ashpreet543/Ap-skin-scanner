import streamlit as st
st.markdown('<meta name="google-site-verification" content="jSn7w9k8ZJtsvbuiBcnyShRAADZgo20oiPzl--mUgds" />', unsafe_allow_html=True)
from PIL import Image
st.set_page_config(page_title="HP Skin Scanner", layout="wide")
st.title("HP Skin Scanner - Dadi Maa Nuskha")
tab1, tab2 = st.tabs(["Gallery", "Camera"])
def show_result():
    st.success("Skin Analysis: Dry Skin Detected")
    st.subheader("Dadi Maa Nuskha")
    st.write("Haldi + Dahi 10 min lagao")
    st.subheader("Meesho Product Suggestion")
    st.write("Himalaya Neem Face Wash")
with tab1:
    uploaded = st.file_uploader("Upload Skin Photo")
    if uploaded:
        img = Image.open(uploaded)
        st.image(img)
        show_result()
with tab2:
    cam = st.camera_input("Camera")
    if cam:
        img = Image.open(cam)
        st.image(img)
        show_result()
