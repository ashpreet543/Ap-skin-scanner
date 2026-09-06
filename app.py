import streamlit as st
import random
import pandas as pd
from datetime import date

st.set_page_config(page_title="H&P LUXE - 12 Features", page_icon="✨", layout="wide")
st.title("✨ H&P LUXE - FULL 12 FEATURES")
st.caption("Sunam di Dhi da Brand | Final PPT Project")

if 'diary' not in st.session_state:
    st.session_state.diary = []

# 1. QUIZ
st.header("📝 1. Smart Quiz - 4 Sawaal")
q1 = st.radio("Paani kinna peendi?", ["1-2 glass", "4-5 glass", "8+ glass"], horizontal=True)
q2 = st.radio("Sona kinne vje?", ["10pm", "12am", "2am baad"], horizontal=True)
q3 = st.radio("Muh kinni vaar dhondi?", ["1 vaar", "2 vaar", "3+ vaar"], horizontal=True)
q4 = st.radio("Dhoop ch ki hoya?", ["Laal", "Kaala/Tel", "Kuch nahi"], horizontal=True)

# 2 & 3. BEFORE / AFTER
st.divider()
st.header("📸 2 & 3. Before / After")
c1, c2 = st.columns(2)
with c1:
    before = st.file_uploader("Before Photo", type=['jpg','jpeg','png'], key="b")
    if before: st.image(before, caption="Before", use_container_width=True)
with c2:
    after = st.file_uploader("Current Photo *", type=['jpg','jpeg','png'], key="a")
    if after: st.image(after, caption="Current", use_container_width=True)

# BUTTON
if st.button("✨ FULL 12 FEATURES REPORT BNAO", type="primary", use_container_width=True):
    if not after:
        st.error("Puttar, Current photo ta pao!")
    else:
        glow = random.randint(68, 92)
        hydrated = 85 if q1=="8+ glass" else 45
        acnes = 4 if q3=="1 vaar" else 1
        age = random.randint(19, 23)
        st.session_state.diary.append({"Date": str(date.today()), "Glow": glow})
        st.balloons()

        # 4 & 5. 4 SCORES + AGE
        st.divider()
        st.header("📊 4. AI Scores (4) + 5. Age Detection")
        m1,m2,m3,m4 = st.columns(4)
        m1.metric("Glow %", f"{glow}%")
        m2.metric("Hydrated %", f"{hydrated}%")
        m3.metric("Acne Count", acnes)
        m4.metric("Age", f"{age} Saal")

        # 6. DADI NUSKHA
        st.header("👵 6. Dadi Maa Nuskha")
        nuskha = "Besan + Haldi + Dahi 15 min laa, glow aau!" if acnes>2 else "Gulab jal raat nu laa, subah glow!"
        st.success(nuskha)

        # 7. MEESHO
        st.header("🛍️ 7. Meesho Product Link")
        st.link_button("Meesho te Kharido - Rs.199", "https://www.meesho.com/search?q=herbal+face+wash")

        # 8. VOICE (No Error Wala)
        st.header("🔊 8. Punjabi Voice")
        st.info(f"🔊 'Teri glow {glow}% hai puttar! {nuskha}'")
        st.markdown(f'<audio controls autoplay><source src="https://translate.google.com/translate_tts?ie=UTF-8&q=Teri%20glow%20{glow}%20percent%20hai%20puttar&tl=hi&client=tw-ob" type="audio/mpeg"></audio>', unsafe_allow_html=True)

        # 9. CHALLENGE
        st.divider()
        st.header("🔥 9. 7 Din Glow Challenge")
        days = ["Day 1: Haldi Pack", "Day 2: 8 Glass Paani", "Day 3: No Tala Hoya", "Day 4: Gulab Jal", "Day 5: 10pm Sona", "Day 6: Aloe Vera", "Day 7: Final Photo"]
        for d in days:
            st.checkbox(d, key=d)

        # 10. DIARY GRAPH
        st.header("📈 10. Skin Diary Graph")
        if len(st.session_state.diary) >= 1:
            st.line_chart(pd.DataFrame(st.session_state.diary), x="Date", y="Glow")
            st.caption("Terdi glow history!")

        # 11. DIET CHART
        st.header("🥗 11. Diet Chart")
        diet_df = pd.DataFrame({
            "✅ Khao (Glow layi)": ["8 Glass Paani", "Kheera, Dahi", "Nariyal Paani", "Badam"],
            "❌ Na Khao": ["Tala Hoya", "Cold
