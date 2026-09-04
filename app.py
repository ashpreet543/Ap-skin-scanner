
import streamlit as st
from PIL import Image
st.title("HP Skin Scanner - Dadi Maa + Meesho")
tab1, tab2 = st.tabs(["📁 Gallery", "📷 Camera"])
with tab1:
    a = st.file_uploader("Photo", type=["jpg","png"])
with tab2:
    b = st.camera_input("Camera")
photo = a or b
if photo:
    img = Image.open(photo)
    st.image(img, width=300)
    st.success("Glow 85% - Dadi kehndi vadia!")
    st.write("✨ Haldi + Besan + Dahi")
    st.link_button("Meesho Neem Wash ₹129", "https://www.meesho.com/search?q=neem+face+wash")
