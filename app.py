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

# Render del Login en la pantalla principal
authenticator.login(location='main')

# =============================================================================
# 1. LÓGICA TRAS LA AUTENTICACIÓN
# =============================================================================

if st.session_state["authentication_status"]:
    
    # --- INICIALIZACIÓN DE ESTADOS ---
    if 'menu_actual'   not in st.session_state: st.session_state.menu_actual = "Bienvenida"
    if 'eje_actual'    not in st.session_state: st.session_state.eje_actual = None
    if 'subcat_actual' not in st.session_state: st.session_state.subcat_actual = None

    # Registrar visita
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    aplicar_estilos()

    # =============================================================================
    # 2. RENDERIZADO DE SECCIONES (SIN SIDEBAR PARA MÓVIL)
    # =============================================================================

    # --- A. BIENVENIDA ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Bienvenidos a Lagrangianitos</h1>", unsafe_allow_html=True)
        st.write(f"Hola **{st.session_state['name']}**, prepárate para el entrenamiento de élite.")
        
        st.divider()
        st.markdown("### ¿Qué quieres hacer hoy?")
        
        if st.button("🚀 Ir al Dashboard de Clases ahora", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"
            st.rerun()
            
        if st.button("📂 Abrir Biblioteca de PDFs", use_container_width=True):
            st.session_state.menu_actual = "Biblioteca"
            st.rerun()

    # --- B. DASHBOARD (EL MOTOR DE CLASES) ---
    elif st.session_state.menu_actual == "Dashboard":
        
        # Botón para volver al Inicio
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"
            st.session_state.eje_actual = None
            st.rerun()

        # 1. SELECTOR DE EJES (Las tarjetas)
        if st.session_state.eje_actual is None:
            st.markdown("<h2 style='text-align:center;'>🎯 Selección de Eje</h2>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔢 Números\nConjuntos • Operatoria", use_container_width=True):
                    st.session_state.eje_actual = "Números"; st.rerun()
                if st.button("📐 Geometría\nFiguras • Áreas", use_container_width=True):
                    st.session_state.eje_actual = "Geometría"; st.rerun()
            with c2:
                if st.button("📉 Álgebra\nÁlgebra • Funciones", use_container_width=True):
                    st.session_state.eje_actual = "Álgebra"; st.rerun()
                if st.button("📊 Datos y Azar\nProbabilidades", use_container_width=True):
                    st.session_state.eje_actual = "Datos"; st.rerun()

        # 2. CARGA DINÁMICA DE CONTENIDOS
        else:
            eje_key = st.session_state.eje_actual
            if st.button(f"🔙 Volver a Selección de Ejes"):
                st.session_state.eje_actual = None
                st.rerun()
            
            st.title(f"📍 {eje_key}")
            
            # --- LÓGICA DE BÚSQUEDA INTELIGENTE EN CONTENIDOS.PY ---
            llaves_reales = list(CONTENIDOS.keys())
            
            # Si no hay match exacto, buscamos el parecido (ignore case/tildes básico)
            eje_final = next((k for k in llaves_reales if eje_key.lower() in k.lower() or k.lower() in eje_key.lower()), eje_key)
            
            if eje_final in CONTENIDOS:
                subcategorias = list(CONTENIDOS[eje_final].keys())
                subcat = st.selectbox("Selecciona la Unidad:", ["--- Elige ---"] + subcategorias)
                
                if subcat != "--- Elige ---":
                    clases = CONTENIDOS[eje_final][subcat]
                    clase_nom = st.selectbox("Elige la Clase:", ["--- Elige ---"] + list(clases.keys()))
                    
                    if clase_nom != "--- Elige ---":
                        datos_clase = clases[clase_nom]
                        st.divider()
                        st.header(f"📖 {clase_nom}")
                        
                        if "video" in datos_clase and datos_clase["video"]:
                            st.video(datos_clase["video"])
                        
                        if "descripcion" in datos_clase:
                            st.write(datos_clase["descripcion"])
                        
                        if st.button("✅ Marcar clase como terminada"):
                            registrar_clase(st.session_state['username'], eje_final, subcat, clase_nom)
                            st.balloons()
            else:
                st.error(f"❌ No encontré contenido para '{eje_key}'")
                st.info(f"Las llaves disponibles en tu archivo son: {llaves_reales}")
                st.warning("Asegúrate de que los nombres en el Dashboard coincidan con tu diccionario.")

    # --- C. BIBLIOTECA ---
    elif st.session_state.menu_actual == "Biblioteca":
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"; st.rerun()
        st.title("📂 Biblioteca")
        pdf_dir = Path("pdfs")
        if pdf_dir.exists():
            for pdf in pdf_dir.glob("*.pdf"):
                with open(pdf, "rb") as f:
                    st.download_button(label=f"⬇️ {pdf.name}", data=f, file_name=pdf.name, use_container_width=True)

    # =============================================================================
    # 3. PIE DE PÁGINA
    # =============================================================================
    st.divider()
    c_out, c_det = st.columns(2)
    with c_out:
        authenticator.logout('Cerrar Sesión', 'main')
    with c_det:
        if st.session_state["username"] == "admin":
            if st.toggle("🕵️ Modo Detective"):
                st.write(f"Visitas totales: **{obtener_visitas()}**")

# Manejo de accesos
elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrectos.')
elif st.session_state["authentication_status"] is None:
    st.markdown("<h2 style='text-align:center;'>🐉 Lagrangianitos Hub</h2>", unsafe_allow_html=True)
    st.info("Ingresa tus credenciales para continuar.")
