import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

st.set_page_config(page_title="H&P LUXE", page_icon="✨", layout="centered")

st.markdown("<h1 style='text-align:center; color:#B76E79;'>H&P LUXE ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>ਸਕਿਨ ਸਕੈਨਰ - ਸੁਨਾਮ</h3>", unsafe_allow_html=True)
st.divider()

st.subheader("📝 ਪਹਿਲਾ ਪੜਾਅ: 4 ਸਵਾਲ")
q1 = st.selectbox("1. ਤੁਹਾਡੀ ਸਕਿਨ ਦਿਨ ਚ ਕਿਵੇਂ ਰਹਿੰਦੀ ਏ?", ["2-3 ਘੰਟੇ ਚ ਤੇਲ ਆ ਜਾਂਦਾ", "ਪੂਰਾ ਦਿਨ ਖੁਸ਼ਕ", "ਨੱਕ ਤੇ ਤੇਲ, ਗੱਲਾਂ ਸੁੱਕੀਆਂ", "ਨੋਰਮਲ"])
q2 = st.selectbox("2. ਪਾਣੀ ਕਿੰਨਾ ਪੀਂਦੇ ਹੋ?", ["1-2 ਲੀਟਰ", "3-4 ਲੀਟਰ", "ਬਹੁਤ ਘੱਟ"])
q3 = st.selectbox("3. ਨੀਂਦ ਕਿੰਨੀ ਲੈਂਦੇ ਹੋ?", ["7-8 ਘੰਟੇ", "5-6 ਘੰਟੇ", "4 ਤੋਂ ਘੱਟ"])
q4 = st.selectbox("4. ਮੁਹਾਸੇ ਕਿੰਨੇ ਨਿਕਲਦੇ ਨੇ?", ["ਕਦੇ ਕਦੇ 1-2", "ਹਰ ਮਹੀਨੇ 3-4", "ਹਮੇਸ਼ਾ", "ਬਿਲਕੁਲ ਨਹੀਂ"])

st.divider()
st.subheader("📸 ਦੂਜਾ ਪੜਾਅ: ਫੋਟੋ ਪਾਓ")
uploaded = st.file_uploader("ਆਪਣੀ ਸਾਫ ਫੋਟੋ ਪਾਓ", type=["jpg","jpeg","png"])

DIET = {
    "ਤੇਲ ਵਾਲੀ": [["ਦਿਨ 1","ਨਿੰਬੂ ਪਾਣੀ + 5 ਬਦਾਮ","ਦਾਲ + ਰੋਟੀ + ਦਹੀਂ","ਸਲਾਦ + ਸੂਪ"],["ਦਿਨ 2","ਗਰੀਨ ਟੀ + ਪਪੀਤਾ","ਖਿਚੜੀ","ਭੁੰਨੇ ਛੋਲੇ"],["ਦਿਨ 3","ਐਲੋਵੇਰਾ ਜੂਸ","ਲੌਕੀ ਸਬਜ਼ੀ + ਰੋਟੀ","ਦਲੀਆ"],["ਦਿਨ 4","ਮੇਥੀ ਪਾਣੀ","ਦਹੀਂ ਚਾਵਲ","ਮੂੰਗ ਦਾਲ"],["ਦਿਨ 5","ਨਾਰੀਅਲ ਪਾਣੀ","ਭਿੰਡੀ + ਰੋਟੀ","ਸੂਪ"],["ਦਿਨ 6","ਗਰੀਨ ਟੀ","ਉਪਮਾ","ਸਲਾਦ"],["ਦਿਨ 7","ਨਿੰਬੂ ਪਾਣੀ","ਦਾਲ ਚਾਵਲ","ਹਲਕਾ ਭੋਜਨ"]],
    "ਖੁਸ਼ਕ": [["ਦਿਨ 1","ਬਦਾਮ ਦੁੱਧ + ਖਜੂਰ","ਘਿਓ ਵਾਲੀ ਦਾਲ + ਰੋਟੀ","ਪਨੀਰ + ਦੁੱਧ"],["ਦਿਨ 2","ਕੇਲਾ + ਦੁੱਧ","ਰਾਜਮਾ ਚਾਵਲ","ਸੂਪ"],["ਦਿਨ 3","7 ਭਿੱਜੇ ਬਦਾਮ","ਰੋਟੀ + ਦਹੀਂ","ਖੀਰ"],["ਦਿਨ 4","ਅੰਜੀਰ + ਦੁੱਧ","ਦਾਲ ਚਾਵਲ ਘਿਓ ਨਾਲ","ਭੁਰਜੀ"],["ਦਿਨ 5","ਕੇਲਾ ਸ਼ੇਕ","ਸਬਜ਼ੀ + ਰੋਟੀ","ਦਲੀਆ ਦੁੱਧ"],["ਦਿਨ 6","ਨਾਰੀਅਲ ਪਾਣੀ","ਖਿਚੜੀ","ਦੁੱਧ ਰੋਟੀ"],["ਦਿਨ 7","ਸ਼ਹਿਦ + ਗਰਮ ਪਾਣੀ","ਰਾਜਮਾ ਚਾਵਲ","ਸਲਾਦ"]],
    "ਮਿਕਸ": [["ਦਿਨ 1","ਜੀਰਾ ਪਾਣੀ","ਦਾਲ ਰੋਟੀ ਦਹੀਂ","ਸੂਪ"],["ਦਿਨ 2","ਪਪੀਤਾ","ਸਬਜ਼ੀ ਰੋਟੀ","ਦਲੀਆ"],["ਦਿਨ 3","ਗਰੀਨ ਟੀ","ਖਿਚੜੀ","ਪਨੀਰ ਸਲਾਦ"],["ਦਿਨ 4","ਨਿੰਬੂ ਪਾਣੀ","ਚਾਵਲ ਦਾਲ","ਛੋਲੇ"],["ਦਿਨ 5","ਬਦਾਮ 5","ਉਪਮਾ","ਸੂਪ"],["ਦਿਨ 6","ਐਲੋਵੇਰਾ","ਭਿੰਡੀ ਰੋਟੀ","ਦਹੀਂ"],["ਦਿਨ 7","ਨਾਰੀਅਲ ਪਾਣੀ","ਦਾਲ ਚਾਵਲ","ਹਲਕਾ"]],
    "ਨੋਰਮਲ": [["ਦਿਨ 1","ਸ਼ਹਿਦ ਗਰਮ ਪਾਣੀ","ਥਾਲੀ","ਸਲਾਦ"],["ਦਿਨ 2","ਫਲ","ਰੋਟੀ ਸਬਜ਼ੀ","ਸੂਪ"],["ਦਿਨ 3","ਬਦਾਮ","ਖਿਚੜੀ","ਪਨੀਰ"],["ਦਿਨ 4","ਨਿੰਬੂ ਪਾਣੀ","ਚਾਵਲ ਦਾਲ","ਦਲੀਆ"],["ਦਿਨ 5","ਗਰੀਨ ਟੀ","ਸਬਜ਼ੀ ਰੋਟੀ","ਦੁੱਧ"],["ਦਿਨ 6","ਪਪੀਤਾ","ਰਾਜਮਾ ਚਾਵਲ","ਸਲਾਦ"],["ਦਿਨ 7","ਨਾਰੀਅਲ ਪਾਣੀ","ਦਾਲ ਚਾਵਲ","ਹਲਕਾ"]]
}
CHALLENGE = {
    "ਤੇਲ ਵਾਲੀ": ["ਦਿਨ 1: ਮੁਲਤਾਨੀ ਮਿੱਟੀ + ਗੁਲਾਬ ਜਲ ਪੈਕ","ਦਿਨ 2: ਤਲਿਆ ਭੋਜਨ ਬੰਦ, 5 ਵਾਰ ਮੂੰਹ ਧੋਵੋ","ਦਿਨ 3: ਬਰਫ ਨਾਲ 2 ਮਿੰਟ ਸਿਕਾਈ","ਦਿਨ 4: ਨਿੰਮ ਵਾਲੇ ਪਾਣੀ ਨਾਲ ਮੂੰਹ ਧੋਵੋ","ਦਿਨ 5: ਗਰੀਨ ਟੀ + ਪੈਕ","ਦਿਨ 6: ਰਾਤ ਨੂੰ ਐਲੋਵੇਰਾ ਜੈੱਲ","ਦਿਨ 7: ਫੋਟੋ ਚ ਫਰਕ ਵੇਖੋ"],
    "ਖੁਸ਼ਕ": ["ਦਿਨ 1: ਦਹੀਂ + ਸ਼ਹਿਦ + ਬਦਾਮ ਤੇਲ ਪੈਕ","ਦਿਨ 2: ਦਿਨ ਚ 3 ਵਾਰ ਕਰੀਮ ਲਾਓ","ਦਿਨ 3: ਦੁੱਧ ਨਾਲ ਮੂੰਹ ਧੋਵੋ","ਦਿਨ 4: ਬਦਾਮ ਤੇਲ ਨਾਲ ਮਾਲਿਸ਼","ਦਿਨ 5: ਕੇਲਾ ਪੈਕ","ਦਿਨ 6: 3 ਲੀਟਰ ਪਾਣੀ + ਨਾਰੀਅਲ ਪਾਣੀ","ਦਿਨ 7: ਫੋਟੋ ਚ ਫਰਕ ਵੇਖੋ"],
    "ਮਿਕਸ": ["ਦਿਨ 1: ਨੱਕ ਤੇ ਮੁਲਤਾਨੀ, ਗੱਲਾਂ ਤੇ ਦਹੀਂ","ਦਿਨ 2: 3 ਲੀਟਰ ਪਾਣੀ","ਦਿਨ 3: ਵੇਸਣ ਪੈਕ","ਦਿਨ 4: ਗੁਲਾਬ ਜਲ ਸਪਰੇਅ","ਦਿਨ 5: ਦਹੀਂ ਖਾਓ","ਦਿਨ 6: ਧੁੱਪ ਤੋਂ ਬਚੋ","ਦਿਨ 7: ਫੋਟੋ ਚ ਫਰਕ ਵੇਖੋ"],
    "ਨੋਰਮਲ": ["ਦਿਨ 1: ਹਲਦੀ ਵੇਸਣ ਪੈਕ","ਦਿਨ 2: 3 ਲੀਟਰ ਪਾਣੀ","ਦਿਨ 3: ਫਲ ਖਾਓ","ਦਿਨ 4: 8 ਘੰਟੇ ਨੀਂਦ","ਦਿਨ 5: ਗੁਲਾਬ ਜਲ","ਦਿਨ 6: ਸੀਰਮ ਲਾਓ","ਦਿਨ 7: ਫੋਟੋ ਚ ਫਰਕ ਵੇਖੋ"],
}

if st.button("✨ ਮੇਰਾ ਨਤੀਜਾ ਵੇਖੋ", use_container_width=True, type="primary"):
    if not uploaded:
        st.error("ਪਹਿਲਾਂ ਫੋਟੋ ਪਾਓ ਜੀ!")
        st.stop()

    img = Image.open(uploaded).convert("RGB")
    st.image(img, use_column_width=True)

    # Scan
    arr = np.array(img.resize((100,100)))
    brightness = np.mean(arr)
    r_mean, g_mean = np.mean(arr[:,:,0]), np.mean(arr[:,:,1])
    redness = r_mean - g_mean

    if "ਤੇਲ" in q1: detected = "ਤੇਲ ਵਾਲੀ"
    elif "ਖੁਸ਼ਕ" in q1: detected = "ਖੁਸ਼ਕ"
    elif "ਨੱਕ" in q1: detected = "ਮਿਕਸ"
    else: detected = "ਨੋਰਮਲ"

    glow = int((brightness/255)*50 + 30)
    if q2 == "3-4 ਲੀਟਰ": glow+=12
    if q2 == "ਬਹੁਤ ਘੱਟ": glow-=12
    if q3 == "7-8 ਘੰਟੇ": glow+=8
    if q3 == "4 ਤੋਂ ਘੱਟ": glow-=8
    glow = min(95, max(30, glow))

    taravat = 70
    if detected == "ਖੁਸ਼ਕ": taravat = 40
    if q2 == "3-4 ਲੀਟਰ": taravat+=15
    taravat = min(90, max(25, taravat))

    daane = int(abs(redness)/4)
    if "ਹਰ ਮਹੀਨੇ" in q4: daane+=3
    if "ਹਮੇਸ਼ਾ" in q4: daane+=5
    daane = min(9, max(0, daane))

    # --- SARA RESULT PUNJABI CH ---
    st.divider()
    st.markdown(f"<h2 style='text-align:center;'>🔍 ਤੁਹਾਡੀ ਰਿਪੋਰਟ: {detected} ਸਕਿਨ</h2>", unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    c1.metric("✨ ਨੂਰ", f"{glow}%")
    c2.metric("💧 ਤਰਾਵਟ", f"{taravat}%")
    c3.metric("🔴 ਦਾਣੇ", f"{daane}")

    if glow < 50:
        st.warning("⚠️ ਨੂਰ ਘੱਟ ਏ! ਤੁਸੀਂ ਪਾਣੀ ਘੱਟ ਪੀਂਦੇ ਹੋ ਤੇ ਨੀਂਦ ਪੂਰੀ ਨਹੀਂ।")
    elif glow > 80:
        st.success("🌟 ਵਾਹ! ਤੁਹਾਡਾ ਨੂਰ ਬਹੁਤ ਵਧੀਆ ਏ!")

    if daane > 4:
        st.error(f"😟 ਦਾਣੇ {daane} ਨੇ, ਹੱਥ ਨਾ ਲਾਓ ਤੇ ਤਲੀਆਂ ਚੀਜ਼ਾਂ ਬੰਦ ਕਰੋ।")
    else:
        st.success("✅ ਦਾਣੇ ਕੰਟਰੋਲ ਚ ਨੇ!")

    st.divider()
    st.subheader(f"👵 ਦਾਦੀ ਮਾਂ ਦਾ ਨੁਸਖਾ - {detected} ਸਕਿਨ ਲਈ")

    if detected == "ਤੇਲ ਵਾਲੀ":
        st.markdown("**ਤੇਲ ਵਾਲੀ ਸਕਿਨ ਲਈ:** ਮੁਲਤਾਨੀ ਮਿੱਟੀ + ਗੁਲਾਬ ਜਲ + ਨਿੰਬੂ ਦੀਆਂ 2 ਬੂੰਦਾਂ। ਹਫਤੇ ਚ 2 ਵਾਰ 15 ਮਿੰਟ ਲਾਓ। ਤੇਲ ਬਿਲਕੁਲ ਖਤਮ।")
        prod, link = "ਤੇਲ ਵਾਲੀ ਸਕਿਨ ਲਈ ਚਾਰਕੋਲ ਫੇਸ ਵਾਸ਼", "https://www.meesho.com/search?q=charcoal%20face%20wash"
        karan = "ਤੇਲ ਵਾਲੀ ਸਕਿਨ ਚ ਤੇਲ ਜ਼ਿਆਦਾ ਬਣਦਾ, ਇਸ ਲਈ ਚਾਰਕੋਲ ਤੇਲ ਸੋਖ ਲੈਂਦਾ।"
    elif detected == "ਖੁਸ਼ਕ":
        st.markdown("**ਖੁਸ਼ਕ ਸਕਿਨ ਲਈ:** ਦਹੀਂ + ਸ਼ਹਿਦ + 2 ਬੂੰਦਾਂ ਬਦਾਮ ਤੇਲ। 20 ਮਿੰਟ ਲਾ ਕੇ ਧੋ ਲਓ। ਸਕਿਨ ਨਰਮ ਤੇ ਤਰਾਵਟ 2 ਗੁਣਾ।")
        prod, link = "ਖੁਸ਼ਕ ਸਕਿਨ ਲਈ ਹਾਈਡਰਾ ਕਰੀਮ", "https://www.meesho.com/search?q=hydra%20moisturizer"
        karan = "ਖੁਸ਼ਕ ਸਕਿਨ ਚ ਪਾਣੀ ਦੀ ਘਾਟ ਏ, ਇਸ ਲਈ ਹਾਈਡਰਾ ਕਰੀਮ ਤਰਾਵਟ ਦਿੰਦੀ ਏ।"
    elif detected == "ਮਿਕਸ":
        st.markdown("**ਮਿਕਸ ਸਕਿਨ ਲਈ:** ਨੱਕ ਤੇ ਮੁਲਤਾਨੀ ਮਿੱਟੀ, ਗੱਲਾਂ ਤੇ ਦਹੀਂ + ਸ਼ਹਿਦ। 2 ਵੱਖਰੇ ਪੈਕ!")
        prod, link = "ਮਿਕਸ ਸਕਿਨ ਲਈ ਵਿਟਾਮਿਨ C ਸੀਰਮ", "https://www.meesho.com/search?q=vitamin%20c%20serum"
        karan = "ਮਿਕਸ ਸਕਿਨ ਲਈ ਸੰਤੁਲਨ ਚਾਹੀਦਾ।"
    else:
        st.markdown("**ਨੋਰਮਲ ਸਕਿਨ ਲਈ:** ਵੇਸਣ + ਹਲਦੀ + ਕੱਚਾ ਦੁੱਧ। ਰੋਜ਼ 10 ਮਿੰਟ, ਨੂਰ ਬਣਿਆ ਰਹੂ।")
        prod, link = "ਨੂਰ ਲਈ ਉਬਟਨ ਕਿੱਟ", "https://www.meesho.com/search?q=ubtan"
        karan = "ਨੋਰਮਲ ਸਕਿਨ ਦਾ ਨੂਰ ਬਣਾਈ ਰੱਖਣ ਲਈ ਉਬਟਨ ਬੈਸਟ ਏ।"

    st.divider()
    st.subheader(f"🛍️ ਤੁਹਾਡੇ ਲਈ ਪ੍ਰੋਡਕਟ - {detected} ਸਕਿਨ ਮੁਤਾਬਕ")
    st.markdown(f"**ਨਾਮ:** {prod}")
    st.markdown(f"**ਕਿਉਂ?:** {karan}")
    st.link_button(f"👉 ਮੀਸ਼ੋ ਤੇ {prod} ਵੇਖੋ", link, use_container_width=True)

    st.divider()
    st.subheader(f"🥗 ਤੁਹਾਡੀ ਸਕਿਨ ਲਈ 7 ਦਿਨਾਂ ਦਾ ਖਾਣ-ਪੀਣ ਚਾਰਟ")
    st.markdown(f"ਇਹ ਚਾਰਟ ਤੁਹਾਡੀ **{detected} ਸਕਿਨ** ਤੇ **{q2} ਪਾਣੀ** ਪੀਣ ਦੀ ਆਦਤ ਮੁਤਾਬਕ ਬਣਿਆ ਏ।")
    df = pd.DataFrame(DIET[detected], columns=["ਦਿਨ", "ਸਵੇਰ ਦਾ ਨਾਸ਼ਤਾ", "ਦੁਪਹਿਰ ਦਾ ਖਾਣਾ", "ਸ਼ਾਮ ਦਾ ਖਾਣਾ"])
    st.table(df)

    st.divider()
    st.subheader(f"🔥 {detected} ਸਕਿਨ ਲਈ 7 ਦਿਨਾਂ ਦਾ ਚੈਲੇਂਜ")
    st.markdown("ਰੋਜ਼ ਇੱਕ ਕੰਮ ਕਰੋ ਤੇ ਟਿੱਕ ਕਰੋ, 7ਵੇਂ ਦਿਨ ਫਰਕ ਵੇਖੋ!")
    for i, task in enumerate(CHALLENGE[detected], 1):
        st.checkbox(f"{task}", key=f"ch_{detected}_{i}")

    st.balloons()
    st.success("🎉 ਵਧਾਈਆਂ! 7 ਦਿਨ ਇਹ ਚੈਲੇਂਜ ਪੂਰਾ ਕਰੋ, ਨੂਰ 100% ਵਧੂ!")

    st.divider()
    st.subheader("🔄 ਪਹਿਲਾਂ ਤੇ ਬਾਅਦ ਦੀ ਫੋਟੋ")
    col1, col2 = st.columns(2)
    with col1:
        b = st.file_uploader("ਪਹਿਲਾਂ ਵਾਲੀ ਫੋਟੋ", key="before")
        if b: st.image(Image.open(b), use_container_width=True)
    with col2:
        a = st.file_uploader("7 ਦਿਨਾਂ ਬਾਅਦ ਵਾਲੀ ਫੋਟੋ", key="after")
        if a: st.image(Image.open(a), use_container_width=True)

    st.info(f"🔊 ਬੋਲ ਕੇ ਸੁਣੋ: 'ਸਤ ਸ੍ਰੀ ਅਕਾਲ ਜੀ! ਤੁਹਾਡੀ ਸਕਿਨ {detected} ਏ। ਨੂਰ {glow}% ਏ, ਤਰਾਵਟ {taravat}% ਏ। {prod} ਵਰਤੋ ਤੇ 7 ਦਿਨ ਚਮਕੋ!'")

st.caption("ਬਣਾਇਆ: ਅਸ਼ਪ੍ਰੀਤ ਕੌਰ | ਸੁਨਾਮ | H&P LUXE")
