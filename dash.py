import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Pepper Dashboard",
    layout="wide"
)

# Título principal
st.markdown(
    "<h2 style='text-align:center; color:black; background-color:#FFC300; padding:10px; border-radius:10px;'>PRESENTANDO NOVEDADES TECNOLÓGICAS CON PEPPER</h2>",
    unsafe_allow_html=True
)

# Crear tres columnas: imagen - novedades - espacio contenido
col1, col2, col3 = st.columns([1,1.2,2])

# ---- Columna 1: Imagen de Pepper ----
with col1:
    st.image("47cdade8-32dd-417c-95ce-b76fe0b58a5a.png", use_column_width=True)
    st.markdown(
        "<div style='text-align:center;'>"
        "<button style='background-color:#FFC300; color:black; font-weight:bold; padding:10px 20px; border-radius:8px;'>INICIO VIDEO</button>"
        "</div>",
        unsafe_allow_html=True
    )

# ---- Columna 2: Botones de novedades ----
with col2:
    st.markdown("<div style='background-color:#E67E22; padding:8px; border-radius:8px; text-align:center; color:white; font-weight:bold;'>Novedad Tecnológica 1</div>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#F5B7B1; padding:8px; border-radius:8px; text-align:center;'>Breve Descripción</div>", unsafe_allow_html=True)

    st.markdown("<div style='background-color:#5DADE2; padding:8px; border-radius:8px; text-align:center; color:white; font-weight:bold;'>Novedad Tecnológica 2</div>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#AED6F1; padding:8px; border-radius:8px; text-align:center;'>Breve Descripción</div>", unsafe_allow_html=True)

    st.markdown("<div style='background-color:#239B56; padding:8px; border-radius:8px; text-align:center; color:white; font-weight:bold;'>Novedad Tecnológica 3</div>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:#A9DFBF; padding:8px; border-radius:8px; text-align:center;'>Breve Descripción</div>", unsafe_allow_html=True)

    st.markdown("<div style='background-color:#58D68D; padding:8px; border-radius:8px; text-align:center; font-weight:bold;'>¿Tienes dudas?, consulta con tu chatbot de confianza !!!</div>", unsafe_allow_html=True)

# ---- Columna 3: Área de contenido dinámico ----
with col3:
    st.markdown(
        "<div style='background: linear-gradient(to bottom, #AED6F1, #D6EAF8); padding:20px; border-radius:20px; min-height:400px;'>"
        "<h4 style='text-align:center; color:black;'>Aquí aparecerá el contenido dinámico según la novedad seleccionada</h4>"
        "</div>",
        unsafe_allow_html=True
    )
