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
# 0. CONFIGURACIÓN DE PÁGINA Y SEGURIDAD
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

# Carga de configuración desde config.yaml
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("⚠️ Error: No se encontró el archivo 'config.yaml'.")
    st.stop()

# Inicialización del autenticador
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Render del Login
authenticator.login(location='main')

# =============================================================================
# 1. LÓGICA SEGÚN ESTADO DE AUTENTICACIÓN
# =============================================================================

if st.session_state["authentication_status"]:
    
    # --- INICIALIZACIÓN DE ESTADOS (Movido arriba para que el radio los use) ---
    if 'menu_actual' not in st.session_state: 
        st.session_state.menu_actual = "🐉 Bienvenida"
    if 'eje_actual' not in st.session_state: 
        st.session_state.eje_actual = None

    # --- BARRA LATERAL ---
    with st.sidebar:
        st.markdown(f"### 🐉 Bienvenido, {st.session_state['name']}")
        authenticator.logout('Cerrar Sesión', 'sidebar')
        st.divider()

        visitas_total = obtener_visitas()
        st.markdown(f'<div style="text-align:center; font-size:12px;">👁️ <b>{visitas_total:,}</b> visitas</div>', unsafe_allow_html=True)
        
        modo_detective = False
        if st.session_state["username"] == "admin":
            st.divider()
            modo_detective = st.toggle("🕵️ Modo Detective")
        
        if not modo_detective:
            st.divider()
            
            # --- LA CORRECCIÓN ESTÁ AQUÍ ---
            opciones_menu = ["🐉 Bienvenida", "🏠 Dashboard PAES", "📂 Biblioteca de PDFs"]
            
            # Calculamos en qué posición está el menú actual para que el radio no se resetee solo
            if st.session_state.menu_actual in opciones_menu:
                indice_previo = opciones_menu.index(st.session_state.menu_actual)
            else:
                indice_previo = 0

            menu = st.radio(
                "Ir a:", 
                opciones_menu, 
                index=indice_previo, # Esto sincroniza el radio con el botón
                key="nav_radio"
            )
            st.session_state.menu_actual = menu
            
        st.divider()
        st.caption("💬 \"Sólo existen dos días en el año en los que no se puede hacer nada.\" — Dalai Lama")

    # Registrar visita
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    aplicar_estilos()

    # =============================================================================
    # 2. RENDERIZADO DE SECCIONES
    # =============================================================================

    # A. VISTA DETECTIVE (SEGURIDAD)
    if modo_detective:
        st.title("🕵️ Panel de Monitoreo (Admin)")
        st.info("Vigilancia de accesos y comportamiento.")
        # ... (Tu lógica de detective) ...

    # B. DASHBOARD PAES
    elif st.session_state.menu_actual == "🏠 Dashboard PAES":
        st.title("🏠 Dashboard PAES M1")
        # Aquí pones el código que genera la segunda foto que me mostraste
        st.write("Selecciona una unidad para comenzar.")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔢 Números", use_container_width=True):
                st.session_state.eje_actual = "🔢 Números"; st.rerun()
        with c2:
            if st.button("📉 Álgebra", use_container_width=True):
                st.session_state.eje_actual = "📉 Álgebra"; st.rerun()

    # C. BIBLIOTECA
    elif st.session_state.menu_actual == "📂 Biblioteca de PDFs":
        st.title("📂 Biblioteca")
        # ... (Tu lógica de PDFs) ...

    # D. BIENVENIDA
    elif st.session_state.menu_actual == "🐉 Bienvenida":
        st.title("🐉 Bienvenidos a Lagrangianitos")
        st.write(f"Hola **{st.session_state['name']}**.")
        
        # EL BOTÓN AHORA SÍ FUNCIONARÁ
        if st.button("🚀 Ir al Dashboard ahora", type="primary"):
            st.session_state.menu_actual = "🏠 Dashboard PAES"
            st.rerun()

# =============================================================================
# 3. MANEJO DE ACCESO DENEGADO
# =============================================================================

elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrectos.')
elif st.session_state["authentication_status"] is None:
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos Hub</h1>", unsafe_allow_html=True)
