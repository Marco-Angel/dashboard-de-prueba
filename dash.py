# app.py
import streamlit as st
import os
import chatbot_component  # 👈 tu chatbot está en este archivo separado

st.set_page_config(page_title="Pepper Dashboard", layout="wide", initial_sidebar_state="collapsed")

# ---------------------------
# CSS
# ---------------------------
st.markdown(
    """
    <style>
    .header {
        background: linear-gradient(90deg, #FFC300, #FF5733);
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        font-weight: 700;
        font-size: 22px;
        color: black;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
    }
    .card {
        background-color: white;
        padding: 18px;
        border-radius: 15px;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# Header
# ---------------------------
st.markdown("<div class='header'>PRESENTANDO NOVEDADES TECNOLÓGICAS CON PEPPER</div>", unsafe_allow_html=True)

# ---------------------------
# Layout
# ---------------------------
col1, col2, col3 = st.columns([1, 1.3, 1.1])

# ---------------------------

# Columna 1: Video
with col1:
    st.subheader("🤖 Pepper")
    video_path = "pepper_video.mp4"
    if os.path.exists(video_path):
        st.video(video_path)  # 👈 siempre aparece
    else:
        st.warning("⚠️ No encontré el archivo `pepper_video.mp4`. Súbelo en la carpeta del proyecto.")


# ---------------------------
# Columna 2: Novedades
# ---------------------------
with col2:
    st.markdown("<div class='card'><h4>Novedad Tecnológica 1</h4><p>Breve Descripción</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>Novedad Tecnológica 2</h4><p>Breve Descripción</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>Novedad Tecnológica 3</h4><p>Breve Descripción</p></div>", unsafe_allow_html=True)

# ---------------------------
# Columna 3: Tu Chatbot
# ---------------------------
with col3:
    chatbot_component.show_chatbot()  # 👈 aquí se ejecuta tu chatbot

