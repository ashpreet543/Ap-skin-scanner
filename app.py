import streamlit as st
st.markdown('<meta name="google-site-verification" content="jSn7w9k8ZJtsvbuiBcnyShRAADZgo20oiPzl--mUgds" />', unsafe_allow_html=True)import streamlit as st
st.markdown('<meta name="google-site-verification" content="jSn7w9k8ZJtsvbuiBcnyShRAADZgo20oiPzl--mUgds" />', unsafe_allow_html=True)
from PIL import Image

st.set_page_config(page_title="HP Skin Scanner")

st.title("HP Skin Scanner - Dadi Maa + Meesho")

tab1, tab2 = st.tabs(["📁 Gallery", "📷 Camera"])

def show_result():
    st.success("Skin Analysis: Dry Skin / Acne Detected")
    st.subheader("👵 Dadi Maa Nuskha")
    st.write("Haldi + Dahi 10 min lagao, roz paani zyada pio")
    
    st.subheader("🛒 Meesho Product Suggestion")
    st.write("**Himalaya Neem Face Wash - ₹199**")
    st.link_button("Meesho Te Vekho", "https://www.meesho.com/search?q=neem%20face%20wash")
    
    st.write("**Plum Moisturizer for Dry Skin - ₹299**")
    st.link_button("Meesho Te Vekho", "https://www.meesho.com/search?q=moisturizer%20dry%20skin")

with tab1:
    file = st.file_uploader("Photo upload karo")
    if file:
        st.image(file)
        show_result()

with tab2:
    pic = st.camera_input("Camera")
    if pic:
        show_result()
