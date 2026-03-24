import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from pathlib import Path
import pytz
[span_2](start_span)import yaml  # Requiere PyYAML en requirements.txt[span_2](end_span)
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Importaciones de tus módulos locales
from contenidos import CONTENIDOS
from styles import aplicar_estilos
from logros import registrar_clase
from visitas import registrar_visita, obtener_visitas

# =============================================================================
# 0. CONFIGURACIÓN DE PÁGINA Y AUTENTICACIÓN
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

# [span_3](start_span)Cargar configuración desde config.yaml[span_3](end_span)
# Nota: Asegúrate de que el archivo en GitHub se llame 'config.yaml' y no 'config.yaml.txt'
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Archivo 'config.yaml' no encontrado. Verifica el nombre en tu repositorio.")
    st.stop()

# [span_4](start_span)Inicializar el autenticador[span_4](end_span)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Renderizar Login
name, authentication_status, username = authenticator.login('Login', 'main')

# =============================================================================
# 1. LÓGICA POST-AUTENTICACIÓN
# =============================================================================

if authentication_status:
    # Logout en la Sidebar
    with st.sidebar:
        st.markdown(f"### 🐉 Bienvenido, {name}")
        authenticator.logout('Cerrar Sesión', 'sidebar')
        st.divider()

    # [span_5](start_span)Inicialización de estados (Tu lógica original)[span_5](end_span)
    if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
    if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual      = None
    if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None
    if 'menu_actual'        not in st.session_state: st.session_state.menu_actual        = "🐉 Bienvenida"
    if 'ultimo_visto'       not in st.session_state: st.session_state.ultimo_visto       = None
    if 'nick_usuario'      not in st.session_state: st.session_state.nick_usuario       = username

    # Registrar visita
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    aplicar_estilos()

    # --- NAVEGACIÓN ---
    if "nav_radio" not in st.session_state:
        st.session_state.nav_radio = st.session_state.menu_actual
    
    with st.sidebar:
        visitas_total = obtener_visitas()
        st.markdown(f'<div style="text-align:center;">👁️ <b>{visitas_total:,}</b> visitas</div>', unsafe_allow_html=True)
        menu = st.radio("Ir a:", ["🐉 Bienvenida", "🏠 Dashboard PAES", "📂 Biblioteca de PDFs"], key="nav_radio")
        st.session_state.menu_actual = menu

    # [Aquí sigue todo el resto de tu código de Dashboard y Biblioteca...]
    if menu == "🏠 Dashboard PAES":
        st.title("🚀 Dashboard PAES M1")
        # [span_6](start_span)Pega aquí el bloque del Dashboard que tienes en tu app.py original[span_6](end_span)
        
    elif menu == "📂 Biblioteca de PDFs":
        st.title("📂 Biblioteca")
        # [span_7](start_span)Pega aquí el bloque de PDFs[span_7](end_span)

    elif menu == "🐉 Bienvenida":
        st.title("Bienvenido a Lagrangianitos")

elif authentication_status == False:
    st.error('Usuario o contraseña incorrectos.')
elif authentication_status == None:
    st.warning('Ingresa tus credenciales para acceder al contenido.')

