import streamlit as st
from  PIL import Image
st.title("HP Skin Scanner")
a=st.file_uploader("Photo pao")
if a:
 st.image(Image.open(a))
 st.success("Glow 85% - Sadi cream best aa!")
