import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="H&P LUXE", page_icon="✨", layout="centered")
st.title("✨ H&import streamlit as st
from PIL import Image

# Home Page
st.set_page_config(page_title="H&P LUXE", layout="wide")

st.title("H&P LUXE ✨")
st.subheader("Natural Glow, Punjabi Touch")

# MODEL PHOTO - Hero Banner
st.image("model.jpg", use_container_width=True, caption="H&P LUXE Muse - Evleen Style 🧡")

st.markdown("---")
st.write("Welcome to H&P LUXE - Your Luxury Skincare Brand")

# Tere baaki products da code ethe ayuP LUXE - AI Skin Scanner")
st.caption("Parneet Khangura")

# Quiz
st.subheader("1. Smart Quiz")
q1 = st.selectbox("Skin Type?", ["Oily", "Dry", "Combination"])
q2 = st.selectbox("Main Problem?", ["Acne", "Dark Spots", "Dullness"])
q3 = st.selectbox("Age Group?", ["15-20", "21-25", "26+"])
q4 = st.selectbox("Daily Water?", ["1-2L", "3-4L"])

# Photos
st.subheader("2. Before Photo")
before = st.file_uploader("Upload Before", type=["jpg","png"])
if before:
    st.image(before, width=200)

st.subheader("3. After Photo")
after = st.file_uploader("Upload After", type=["jpg","png"])
if after:
    st.image(after, width=200)

# Scores
st.subheader("4. AI Scores (Demo)")
glow = 78
hydrated = 65
acne = 20
age = 22
st.metric("Glow Score", f"{glow}%")
st.metric("Hydration", f"{hydrated}%")
st.metric("Acne Risk", f"{acne}%")
st.metric("Skin Age", f"{age} years")

# 5 Age
st.info(f"Detected Skin Age: {age} years")

# 6 Dadi Nuskha
st.subheader("6. Dadi Maa Nuskha")
if q2=="Acne":
    st.success("Haldi + Besan + Gulab Jal - daily 10 min")
else:
    st.success("Dahi + Shahad + Nimbu - 15 min")

# 7 Meesho
st.subheader("7. Best Product")
st.link_button("Buy on Meesho - Under 199", "https://www.meesho.com")

# 8 Punjabi Voice
st.subheader("8. Punjabi Voice Tip")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 9 Challenge
st.subheader("9. 7 Day Glow Challenge")
days = ["Day 1 - Water", "Day 2 - No Taleya", "Day 3 - Face Pack", "Day 4 - Sleep 8hr", "Day 5 - Sunscreen", "Day 6 - Fruits", "Day 7 - Glow Check"]
for d in days:
    st.checkbox(d)

# 10 Diary Graph
st.subheader("10. Skin Diary Graph")
chart_data = pd.DataFrame({"Glow": [60,65,70,78]})
st.line_chart(chart_data)

# 11 Diet
st.subheader("11. Diet Chart")
diet = {
    "Khao": ["Fruits", "Green Veg", "Water 3L"],
    "Na Khao": ["Tala Hoya", "Cold Drink", "Junk Food"]
}
st.table(pd.DataFrame(diet))

# 12 Weather + PDF
st.subheader("12. Weather + Report")
st.write("Sunam Weather: 32C - Use Sunscreen")
if st.button("Download PDF Report"):
    st.balloons()
    st.success("Report Ready! PPT ch screenshot le lo")
