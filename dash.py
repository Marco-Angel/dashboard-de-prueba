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
        background: linear-gradient(90deg, #FFC300, #1E90FF);
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        font-weight: 700;
        font-size: 22px;
        color: black;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
    }
    .card {
        background: linear-gradient(90deg, #87CEEB, #FF5733);;
        padding: 20px;
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
st.markdown("<div class='header'>UN POCO DE NOVEDADES TECNOLÓGICAS</div>", unsafe_allow_html=True)

# ---------------------------
# Layout
# ---------------------------
col1, col2, col3 = st.columns([0.9, 1.6, 0.9])

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
    st.markdown("<div class='card'><h4>Impacto de los sistemas digitales en implantes cerebrales adaptativos</h4><p>Los implantes cerebrales adaptativos digitales permiten monitorear la actividad cerebral y ajustar la estimulación en tiempo real, mejorando tratamientos neurológicos y la calidad de vida, aunque plantean retos éticos y de seguridad.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4> Biocombustibles de algas genéticamente editadas</h4><p>Los biocombustibles de algas genéticamente editadas se producen al modificar algas para aumentar su eficiencia en la generación de lípidos y energía renovable, ofreciendo una alternativa sostenible a los combustibles fósiles, aunque con desafíos técnicos y ambientales.n</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>Computación reversible y su impacto en los sistemas digitales</h4><p>La computación reversible busca procesar información sin pérdida de energía al invertir las operaciones lógicas, lo que podría reducir el consumo energético y transformar la eficiencia de los sistemas digitales.</p></div>", unsafe_allow_html=True)

# ---------------------------
# Columna 3: Tu Chatbot
# ---------------------------
with col3:
    chatbot_component.show_chatbot()  # 👈 aquí se ejecuta tu chatbot

