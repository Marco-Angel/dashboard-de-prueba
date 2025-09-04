# chatbot_component.py
import streamlit as st

def show_chatbot():
    st.write("Aquí va tu chatbot real")
import os
import requests
import streamlit as st
from gtts import gTTS
from dotenv import load_dotenv

# === Cargar variables de entorno (API Key) ===
load_dotenv()
API_URL = "https://api.deepseek.com/v1/chat/completions"

def get_secret(key, default=None):
    if st.secrets and key in st.secrets:
        return st.secrets[key]
    return os.environ.get(key, default)

API_KEY = get_secret("DEEPSEEK_API_KEY")
MODEL = get_secret("MODEL", "deepseek-chat")

if not API_KEY:
    st.error("⚠️ No se encontró la API Key. Configúrala en Streamlit Secrets.")
    st.stop()

# === Configuración de página ===
st.set_page_config(page_title="Chatbot Profesor de Electrónica", page_icon="📡")
st.title("👨‍🏫 Chatbot - Profesor de Ingeniería Electrónica")

if "history" not in st.session_state:
    st.session_state.history = []

# === Función para conversar con DeepSeek ===
def chat_with_deepseek(prompt):
    messages = [
        {"role": "system", "content": "Eres un profesor experto en Ingeniería Electrónica. Explicas los conceptos de manera clara, sencilla y en español, como si estuvieras enseñando a un estudiante universitario."}
    ] + st.session_state.history + [{"role": "user", "content": prompt}]
    
    payload = {"model": MODEL, "messages": messages, "temperature": 0.4}
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    try:
        r = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        r.raise_for_status()
        data = r.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

# === Mostrar historial ===
for msg in st.session_state.history:
    st.markdown(f"**{'Tú' if msg['role']=='user' else 'Profesor'}:** {msg['content']}")

# === Entrada del usuario (Enter para enviar) ===
user_input = st.chat_input("Escribe tu pregunta de Ingeniería Electrónica...")

if user_input:
    # Guardar mensaje del usuario
    st.session_state.history.append({"role": "user", "content": user_input})

    # Obtener respuesta
    response = chat_with_deepseek(user_input)
    st.session_state.history.append({"role": "assistant", "content": response})

    # Mostrar texto
    st.markdown(f"**Profesor:** {response}")

    # Generar voz con gTTS
    try:
        tts = gTTS(text=response, lang='es')
        tts.save("respuesta.mp3")
        st.audio("respuesta.mp3")
    except Exception as e:
        st.error(f"Error generando voz: {e}")

# === Botón para reiniciar ===
if st.button("Reiniciar conversación"):
    st.session_state.history = []
    st.rerun()
