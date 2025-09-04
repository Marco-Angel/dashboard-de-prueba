# app.py
import streamlit as st
import os

st.set_page_config(page_title="Pepper Dashboard", layout="wide", initial_sidebar_state="collapsed")

# ---------------------------
# CSS
# ---------------------------
st.markdown(
    """
    <style>
    .header {
        background-color: #FFC300;
        padding: 10px 12px;
        border-radius: 10px;
        text-align: center;
        font-weight: 700;
        font-size: 20px;
    }
    .box-desc {background-color:#F5B7B1; padding:10px; border-radius:10px; text-align:center; margin-bottom:8px;}
    .blue-desc {background: linear-gradient(#AED6F1,#D6EAF8); padding:10px; border-radius:10px; text-align:center; margin-bottom:8px;}
    .green-desc {background: linear-gradient(#A9DFBF,#D4EFDF); padding:10px; border-radius:10px; text-align:center; margin-bottom:8px;}
    .content-area {background: linear-gradient(to bottom, #AED6F1, #D6EAF8); padding:18px; border-radius:20px; min-height:360px;}
    .chat-box {background-color:#58D68D; padding:12px; border-radius:12px; color:black; font-weight:700; text-align:center;}
    .msg-user {background-color:#E8F8F5; padding:8px; border-radius:8px; margin:6px 0;}
    .msg-bot {background-color:#F2F3F4; padding:8px; border-radius:8px; margin:6px 0;}
    </style>
    """, unsafe_allow_html=True
)

# ---------------------------
# Header
# ---------------------------
st.markdown("<div class='header'>PRESENTANDO NOVEDADES TECNOLÓGICAS CON PEPPER</div>", unsafe_allow_html=True)

# ---------------------------
# Layout: tres columnas
# ---------------------------
col1, col2, col3 = st.columns([1, 0.9, 1.8])

# ---------------------------
# Columna 1: Video
# ---------------------------
with col1:
    st.markdown("<h4 style='text-align:center;'>Pepper</h4>", unsafe_allow_html=True)
    video_path = "pepper_video.mp4"
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.warning(f"⚠️ No encontré '{video_path}'. Sube tu video en esta carpeta.")

    if st.button("INICIO VIDEO"):
        st.experimental_rerun()

# ---------------------------
# Columna 2: Botones de novedades
# ---------------------------
if 'selected' not in st.session_state:
    st.session_state.selected = "n1"

with col2:
    if st.button("Novedad Tecnológica 1"):
        st.session_state.selected = "n1"
    st.markdown("<div class='box-desc'>Breve Descripción</div>", unsafe_allow_html=True)

    if st.button("Novedad Tecnológica 2"):
        st.session_state.selected = "n2"
    st.markdown("<div class='blue-desc'>Breve Descripción</div>", unsafe_allow_html=True)

    if st.button("Novedad Tecnológica 3"):
        st.session_state.selected = "n3"
    st.markdown("<div class='green-desc'>Breve Descripción</div>", unsafe_allow_html=True)

    st.markdown("<div class='chat-box'>¿Tienes dudas? Consulta con tu chatbot de confianza !!!</div>", unsafe_allow_html=True)

# ---------------------------
# Columna 3: Contenido + Chatbot
# ---------------------------
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [("bot", "Hola, soy el chatbot de Pepper. ¿En qué puedo ayudarte?")]

def get_bot_reply(user_text: str) -> str:
    if "video" in user_text.lower():
        return "Puedes ver el video en la columna izquierda."
    if "novedad 1" in user_text.lower():
        return "Detalles ampliados de la Novedad Tecnológica 1..."
    if "novedad 2" in user_text.lower():
        return "Detalles ampliados de la Novedad Tecnológica 2..."
    if "novedad 3" in user_text.lower():
        return "Detalles ampliados de la Novedad Tecnológica 3..."
    return "Soy un chatbot demo 🤖, pregúntame sobre las novedades o el video."

with col3:
    st.markdown("<div class='content-area'>", unsafe_allow_html=True)
    if st.session_state.selected == "n1":
        st.subheader("Novedad Tecnológica 1")
        st.write("Aquí va la información detallada de la novedad 1.")
    elif st.session_state.selected == "n2":
        st.subheader("Novedad Tecnológica 2")
        st.write("Aquí va la información detallada de la novedad 2.")
    else:
        st.subheader("Novedad Tecnológica 3")
        st.write("Aquí va la información detallada de la novedad 3.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Chatbot")
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"<div class='msg-user'><b>Tú:</b> {msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='msg-bot'><b>Bot:</b> {msg}</div>", unsafe_allow_html=True)

    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Escribe tu mensaje")
        submitted = st.form_submit_button("Enviar")
        if submitted and user_input:
            st.session_state.chat_history.append(("user", user_input))
            reply = get_bot_reply(user_input)
            st.session_state.chat_history.append(("bot", reply))
            st.experimental_rerun()

