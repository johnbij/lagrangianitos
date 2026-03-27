import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from pathlib import Path

# =============================================================================
# 0. IMPORTACIONES (CON SOPORTE PARA GITHUB)
# =============================================================================
try:
    from contenidos import CONTENIDOS
    from styles import aplicar_estilos
    from logros import registrar_clase
    from visitas import registrar_visita, obtener_visitas
except ImportError:
    from Contenidos import CONTENIDOS
    from Styles import aplicar_estilos
    from Logros import registrar_clase
    from Visitas import registrar_visita, obtener_visitas

# =============================================================================
# 1. CONFIGURACIÓN Y COOKIE (PARA NO LOGEARSE SIEMPRE)
# =============================================================================
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Falta config.yaml")
    st.stop()

# Aumentamos la duración de la cookie a 30 días en el autenticador
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    cookie_expiry_days=30 # <--- ¡Sesión abierta por un mes!
)

authenticator.login(location='main')

# =============================================================================
# 2. LÓGICA DE CONTENIDOS
# =============================================================================
if st.session_state["authentication_status"]:
    
    if 'menu_actual' not in st.session_state: st.session_state.menu_actual = "Bienvenida"
    if 'eje_actual'  not in st.session_state: st.session_state.eje_actual = None

    aplicar_estilos()

    # --- PANTALLA BIENVENIDA ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos</h1>", unsafe_allow_html=True)
        if st.button("🚀 Entrar al Dashboard", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"; st.rerun()

    # --- DASHBOARD (CORREGIDO SEGÚN TU CAPTURA) ---
    elif st.session_state.menu_actual == "Dashboard":
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"; st.session_state.eje_actual = None; st.rerun()

        if st.session_state.eje_actual is None:
            st.subheader("Selecciona tu Eje:")
            c1, c2 = st.columns(2)
            
            # USAMOS LAS LLAVES EXACTAS QUE SALIERON EN TU CAJA AZUL
            with c1:
                if st.button("🔢 Números", use_container_width=True):
                    st.session_state.eje_actual = "1️⃣2️⃣3️⃣ Números"; st.rerun()
                if st.button("📐 Geometría", use_container_width=True):
                    st.session_state.eje_actual = "📐 Geometría"; st.rerun()
                if st.button("⚛️ Física", use_container_width=True):
                    st.session_state.eje_actual = "⚛️ Física"; st.rerun()
            with c2:
                if st.button("📉 Álgebra", use_container_width=True):
                    st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
                if st.button("📊 Datos", use_container_width=True):
                    st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()
                if st.button("🧬 Biología", use_container_width=True):
                    st.session_state.eje_actual = "🔬 Biología"; st.rerun()

        else:
            eje_key = st.session_state.eje_actual
            if st.button("🔙 Cambiar de Eje"):
                st.session_state.eje_actual = None; st.rerun()
            
            # Si el eje existe, mostramos clases
            if eje_key in CONTENIDOS:
                unidades = list(CONTENIDOS[eje_key].keys())
                u_sel = st.selectbox("Unidad:", ["---"] + unidades)
                if u_sel != "---":
                    clases = CONTENIDOS[eje_key][u_sel]
                    c_sel = st.selectbox("Clase:", ["---"] + list(clases.keys()))
                    if c_sel != "---":
                        data = clases[c_sel]
                        st.header(c_sel)
                        if "video" in data: st.video(data["video"])
                        if "descripcion" in data: st.write(data["descripcion"])
            else:
                st.error(f"Error con la llave: {eje_key}")
                st.info(f"Detectadas: {list(CONTENIDOS.keys())}")

    st.divider()
    authenticator.logout('Cerrar Sesión', 'main')

elif st.session_state["authentication_status"] is False:
    st.error('Error de usuario/pass')
