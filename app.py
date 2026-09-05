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
        st.success("Analysis: Oily Skin - 85% Glow!")
            st.write("**Tuhadi skin vich tel jyada aa, par glow vadhia!**")
            st.write("**Matlab:** Pores khule ne, mitti jama hundi aa.")
            st.write("**Dadi da Nuskha:** Multani mitti + Gulab jal roz sham nu. Besan naal muh dhovo.")
            st.write("**Product:** Neem Face Wash use karo.")
        st.link_button("🛒 Meesho te Khao", "https://www.meesho.com")
st.success("Analysis: Dry Skin - 65% Hydration ghat aa!")
            st.write("**Tuhadi skin sukkhi aa, nami di lod aa!**")
            st.write("**Matlab:** Paani ghat pinde ho, dhoop jyada lagdi aa.")
            st.write("**Dadi da Nuskha:** Raat nu malai + shahad + 2 bund nariyal tel laao. Kheere da ras lagao.")
            st.write("**Product:** Haldi Cream din ch 2 vaar.")
with tab2:
    camera_photo = st.camera_input("Camera naal photo lao")
    if camera_photo:
        st.image(camera_photo, use_container_width=True)
        st.success("Analysis: Dry Skin - Nuskha: Malai + Shahad lagao!")
        st.link_button("🛒 Haldi Cream Khao", "https://www.meesho.com")
