
import streamlit as st
from custom_style import eurogenius_css
import time

st.set_page_config(page_title="🎰 EuroGenius", layout="centered")
st.markdown(eurogenius_css(), unsafe_allow_html=True)

# Sound-Effekt beim Starten
st.audio("https://www.myinstants.com/media/sounds/casino-slot-machine.mp3", autoplay=True)

# Branding-Header
st.markdown("## 💎 Willkommen bei **EuroGenius**")
st.markdown("### Die einzige Lotto-App mit Strategie + Gefühl")
st.markdown("<div style='font-size:60px; text-align:center;'>🎯🎲🔮</div>", unsafe_allow_html=True)

# Spielmodus-Buttons mit Animationseffekt
st.markdown("#### Wähle deinen Modus:")

step = st.radio("Dein Spielweg", ["🎲 Intuition", "📊 Statistik", "🤖 KI"], horizontal=True)

if step == "🎲 Intuition":
    st.markdown("##### 🔥 Folge deinem Bauchgefühl – wähle heiße Zahlen")
    if st.button("💡 Intuitiv starten"):
        st.success("🎉 Strategie geladen... viel Glück!")
        time.sleep(1)
        st.switch_page("pages/strategie.py")

elif step == "📊 Statistik":
    st.markdown("##### 📈 Nutze Ziehungsdaten für deine Analyse")
    if st.button("📂 Statistik ansehen"):
        st.success("📊 Statistiken bereit!")
        time.sleep(1)
        st.switch_page("pages/meine_strategien.py")

elif step == "🤖 KI":
    st.markdown("##### 🧠 Lass unsere KI deinen besten Tipp finden")
    if st.button("🤖 KI aktivieren"):
        st.success("🧠 KI denkt...")
        time.sleep(2)
        st.switch_page("pages/dashboard_demo.py")

# Ladeeffekt-Animation
st.markdown("##### ⏳ Glücksenergie wird geladen...")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.004)
    progress.progress(i + 1)

st.markdown("---")
st.info("🔐 Tipp: Logge dich ein, um Strategien zu speichern & Premium zu nutzen")
