import streamlit as st
from PIL import Image

st.title("HP Skin Scanner - Dadi Maa Nuskha")

a = st.file_uploader("Photo pao", type=["jpg","png"])

if a:
    img = Image.open(a)
    st.image(img)
    st.success("Glow 85% - Sadi Dadi kehndi:")
    st.write("✨ Haldi + Besan + Dahi - Roz lao")
    st.write("🛒 Meesho to: Neem Face Wash")
    st.link_button("Meesho te kharido", "https://www.meesho.com/search?q=neem+face+wash")
