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

# Inicializar el autenticador (Versión actualizada sin preauthorized)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Renderizar Login
name, authentication_status, username = authenticator.login('Login', 'main')

# =============================================================================
# 1. LÓGICA SEGÚN ESTADO DE AUTENTICACIÓN
# =============================================================================

if authentication_status:
    # --- CONTENIDO PROTEGIDO ---
    
    with st.sidebar:
        st.markdown(f"### 🐉 Bienvenido, {name}")
        authenticator.logout('Cerrar Sesión', 'sidebar')
        st.divider()

    # Inicialización de estados de sesión
    if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
    if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual      = None
    if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None
    if 'ir_a_pdf'           not in st.session_state: st.session_state.ir_a_pdf           = False
    if 'bienvenida_vista'   not in st.session_state: st.session_state.bienvenida_vista   = False
    if 'menu_actual'        not in st.session_state: st.session_state.menu_actual        = "🐉 Bienvenida"
    if 'ultimo_visto'       not in st.session_state: st.session_state.ultimo_visto       = None
    if 'nick_usuario'      not in st.session_state: st.session_state.nick_usuario       = username
    if 'crono_running'     not in st.session_state: st.session_state.crono_running      = False
    if 'crono_inicio'      not in st.session_state: st.session_state.crono_inicio       = None

    # Registrar visita
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    COLORES = {
        "rojo":      "#c0392b",
        "verde":     "#1b5e20",
        "morado":    "#7b1fa2",
        "naranja":   "#e65100",
        "cian":      "#006064",
        "verde_bio": "#33691e",
        "ambar":     "#ff8f00",
    }

    aplicar_estilos()

    # Sincronización de navegación
    if "nav_radio" not in st.session_state:
        st.session_state.nav_radio = st.session_state.menu_actual
    elif (st.session_state.get("prev_nav_radio") == st.session_state.nav_radio and
          st.session_state.nav_radio != st.session_state.menu_actual):
        st.session_state.nav_radio = st.session_state.menu_actual

    with st.sidebar:
        visitas_total = obtener_visitas()
        st.markdown(
            f'<div style="background:#eef2ff; border-radius:8px; padding:8px; font-size:12px; color:#3730a3; margin-top:4px; text-align:center;">'
            f'👁️ <b>{visitas_total:,}</b> visitas</div>',
            unsafe_allow_html=True
        )
        if st.session_state.ultimo_visto:
            st.markdown(
                f'<div style="background:#f0f0f0; border-radius:8px; padding:8px; font-size:12px; color:#555; margin-top:4px;">'
                f'🕐 Último visto:<br><b>{st.session_state.ultimo_visto}</b></div>',
                unsafe_allow_html=True
            )
        st.divider()
        menu = st.radio("Ir a:", ["🐉 Bienvenida", "🏠 Dashboard PAES", "📂 Biblioteca de PDFs"],
                        key="nav_radio")
        st.session_state.menu_actual = menu
        st.divider()
        st.caption("💬 Solo existen dos días en el año en los que no se puede hacer nada. — Dalai Lama")

    st.session_state.prev_nav_radio = st.session_state.nav_radio

    # --- RENDERIZADO DE SECCIONES ---

    if menu == "🏠 Dashboard PAES":
        zona_cl = pytz.timezone('America/Santiago')
        ahora   = datetime.now(zona_cl)

        st.markdown(
            f'<div class="header-azul">'
            f'<div class="titulo-header">🐉 Lagrangianitos — PAES M1</div>'
            f'<div class="info-header">📍 Santiago · 🕒 {ahora.strftime("%H:%M")}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        paes_date = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
        delta = paes_date - ahora
        dias  = delta.days
        horas = delta.seconds // 3600
        st.markdown(
            f'<div class="header-rojo">'
            f'<div class="timer-item">⏳ Días: {dias}</div>'
            f'<div class="timer-item">Hrs: {horas}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        if st.session_state.eje_actual is None:
            st.markdown('<div class="eje-select">', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔢 Números", key="m_n", use_container_width=True):
                    st.session_state.eje_actual = "🔢 Números"; st.rerun()
            with c2:
                if st.button("📉 Álgebra", key="m_a", use_container_width=True):
                    st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button("🔙 Volver al inicio", key="back_home"):
                st.session_state.eje_actual = None; st.rerun()

    elif menu == "📂 Biblioteca de PDFs":
        st.title("📂 Biblioteca de Recursos")
        st.write("Aquí puedes descargar tus guías y ensayos.")

    elif menu == "🐉 Bienvenida":
        st.markdown('<div class="seccion-titulo">🐉 Bienvenidos a Lagrangianitos</div>', unsafe_allow_html=True)
        st.write("Tu plataforma interactiva para dominar la PAES M1.")
        if st.button("🚀 Ir al Dashboard PAES", type="primary"):
            st.session_state.menu_actual = "🏠 Dashboard PAES"; st.rerun()

elif authentication_status == False:
    st.error('Usuario o contraseña incorrectos.')
    
elif authentication_status == None:
    st.warning('Ingresa tus credenciales para acceder al contenido Premium.')
