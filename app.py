import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from pathlib import Path
import pytz
import yaml
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

# Cargar configuración desde config.yaml
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Error: No se encontró el archivo 'config.yaml'. Verifica el nombre en tu repositorio.")
    st.stop()

# Inicializar el autenticador
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Renderizar Login con argumentos con nombre para evitar el ValueError
# Si quieres el login en la sidebar, cambia location='main' por location='sidebar'
login_result = authenticator.login(location='main')

# La nueva versión devuelve un objeto o tupla según la sub-versión, 
# pero authentication_status sigue estando en st.session_state
authentication_status = st.session_state.get("authentication_status")
name = st.session_state.get("name")
username = st.session_state.get("username")

# =============================================================================
# 1. LÓGICA SEGÚN ESTADO DE AUTENTICACIÓN
# =============================================================================

if authentication_status:
    # --- CONTENIDO PROTEGIDO ---
    
    with st.sidebar:
        st.markdown(f"### 🐉 Bienvenido, {name}")
        authenticator.logout('Cerrar Sesión', 'sidebar')
        st.divider()

    # Inicialización de estados de sesión (Tu lógica original)
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

    # Navegación
    with st.sidebar:
        visitas_total = obtener_visitas()
        st.markdown(f'<div style="text-align:center;">👁️ <b>{visitas_total:,}</b> visitas</div>', unsafe_allow_html=True)
        menu = st.radio("Ir a:", ["🐉 Bienvenida", "🏠 Dashboard PAES", "📂 Biblioteca de PDFs"], key="nav_radio_main")
        st.session_state.menu_actual = menu

    # --- RENDERIZADO DE SECCIONES ---

    if menu == "🏠 Dashboard PAES":
        zona_cl = pytz.timezone('America/Santiago')
        ahora   = datetime.now(zona_cl)

        st.markdown(f'<div class="header-azul">🐉 Lagrangianitos — PAES M1 | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)

        if st.session_state.eje_actual is None:
            st.subheader("Selecciona un Eje Temático")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔢 Números", use_container_width=True):
                    st.session_state.eje_actual = "🔢 Números"; st.rerun()
            with c2:
                if st.button("📉 Álgebra", use_container_width=True):
                    st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        else:
            if st.button("🔙 Volver a los Ejes"):
                st.session_state.eje_actual = None; st.rerun()

    elif menu == "📂 Biblioteca de PDFs":
        st.title("📂 Biblioteca de Recursos")
        st.info("Próximamente: Guías y ensayos descargables.")

    elif menu == "🐉 Bienvenida":
        st.title("🐉 Bienvenidos a Lagrangianitos")
        st.write(f"Hola {name}, ya tienes acceso total al material de ingeniería y PAES.")
        if st.button("🚀 Ir al Dashboard", type="primary"):
            st.session_state.menu_actual = "🏠 Dashboard PAES"; st.rerun()

elif authentication_status == False:
    st.error('Usuario o contraseña incorrectos.')
    
elif authentication_status == None:
    st.warning('Ingresa tus credenciales para acceder.')
    st.info("¿Eres nuevo? Contacta al administrador para obtener tu acceso.")
