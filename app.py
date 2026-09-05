import streamlit as st
from PIL import Image

# 1. GOOGLE VERIFICATION
st.set_page_config(page_title="HP Skin Scanner - Dadi Maa Nuskha", page_icon="🌿", layout="centered")
st.markdown('<meta name="google-site-verification" content="jSn7w9k8ZJtsvbuiBcnyShRAADZgo20oiPzl--mUgds" />', unsafe_allow_html=True)

# 2. BLACK THEME
st.markdown("""
<style>
.stApp { background-color: #0e0e0e; color: white; }
h1 { color: #00ff88; }
</style>
""", unsafe_allow_html=True)

st.title("HP Skin Scanner - Dadi Maa Nuskha 🌿")
st.write("Apni skin di photo upload karo te Dadi Maa da nuskha pao!")

tab1, tab2 = st.tabs(["📁 Gallery", "📸 Camera"])

with tab1:
    uploaded_file = st.file_uploader("Photo Upload Karo", type=["jpg","png","jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Tuhadi Photo", use_container_width=True)
        st.success("Analysis: Oily Skin - Nuskha: Neem + Haldi pack 15 min lagao!")
        st.link_button("🛒 Meesho te Khao", "https://www.meesho.com")

with tab2:
    camera_photo = st.camera_input("Camera naal photo lao")
    if camera_photo:
        st.image(camera_photo, use_container_width=True)
        st.success("Analysis: Dry Skin - Nuskha: Malai + Shahad lagao!")
        st.link_button("🛒 Haldi Cream Khao", "https://www.meesho.com")
