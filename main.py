
import streamlit as st
from custom_style import eurogenius_css
import time

st.set_page_config(page_title="🎰 EuroGenius", layout="centered")
st.markdown(eurogenius_css(), unsafe_allow_html=True)

# Big Intro Style
st.markdown("## 🎯 Willkommen bei **EuroGenius** – Deine smarte Lotto-Reise")
st.markdown("### 🧠 Statistik. 🎰 Gefühl. 🤖 KI. Alles in einer App.")
st.markdown("---")

# Visual impact
st.markdown("<div style='font-size:80px; text-align:center;'>💎🎲🔮</div>", unsafe_allow_html=True)

st.markdown("#### Starte deine Reise und wähle deinen Spielmodus:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔥 Intuition"):
        st.switch_page("pages/strategie.py")

with col2:
    if st.button("📊 Statistik"):
        st.switch_page("pages/meine_strategien.py")

with col3:
    if st.button("🤖 KI"):
        st.switch_page("pages/dashboard_demo.py")

st.markdown("---")
st.markdown("#### 💌 Tipp: Erstelle ein Profil und sichere deine Strategien!")
st.markdown("➡️ Login über die Sidebar")

# Optional: animiertes Fortschrittsgefühl
st.markdown("##### ⏳ Lade deine Glücksfrequenz...")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.007)
    progress.progress(i + 1)

st.success("🎉 Bereit! Dein Weg zum Millionen-Code beginnt jetzt.")
