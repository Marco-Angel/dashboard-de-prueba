# app.py
import streamlit as st
import os

st.set_page_config(page_title="Pepper Dashboard", layout="wide", initial_sidebar_state="collapsed")

# ---------------------------
# CSS para estilo mejorado
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
    .msg-user {
        background-color:#D5F5E3;
        padding:10px;
        border-radius:10px;
        margin:6px 0;
        text-align:right;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }
    .msg-bot {
        background-color:#F2F3F4;
        padding:10px;
        border-radius:10px;
        margin:6px 0;
        text-align:left;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
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
# Layout: tres columnas
# ---------------------------
col1, col2, col3 = st.columns([1.3, 1.3, 0.8])  # derecha más angosta

# ---------------------------
# Columna 1: Video
# ---------------------------
with col1:
    st.subheader("🤖 Pepper")
    video_path = "pepper_video.mp4"
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.warning("⚠️ No encontré el archivo `pepper_video.mp4`. Súbelo en la carpeta del proyecto.")

    if st.button("▶️ INICIO VIDEO"):
        st.experimental_rerun()

# ---------------------------
# Columna 2: Solo texto de novedades (centrado)
# ---------------------------
with col2:
    st.markdown("<div class='card'><h4>Novedad Tecnológica 1</h4><p>Breve Descripción</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>Novedad Tecnológica 2</h4><p>Breve Descripción</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>Novedad Tecnológica 3</h4><p>Breve Descripción</p></div>", unsafe_allow_html=True)

# ---------------------------
# Columna 3: Solo Chatbot
# ---------------------------
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [("bot", "Hola 👋, soy el chatbot de Pepper. Pregúntame lo que quieras.")]

def get_bot_reply(user_text: str) -> str:
    if "video" in user_text.lower():
        return "El video de Pepper lo puedes ver en la columna izquierda 👉"
    if "novedad" in user_text.lower():
        return "Las novedades están en la parte central, ¿quieres más detalles de alguna en particular?"
    return "🤖 Soy un chatbot demo. Pregúntame sobre el video o las novedades."

with col3:
    st.markdown("### 💬 Chatbot de confianza")
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"<div class='msg-user'><b>Tú:</b> {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='msg-bot'><b>PepperBot:</b> {msg}</div>", unsafe_allow_html=True)

    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Escribe tu mensaje aquí...")
        submitted = st.form_submit_button("Enviar")
        if submitted and user_input:
            st.session_state.chat_history.append(("user", user_input))
            reply = get_bot_reply(user_input)
            st.session_state.chat_history.append(("bot", reply))
            st.experimental_rerun()

