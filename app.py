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
# 0. CONFIGURACIÓN DE PÁGINA Y SEGURIDAD (SIN SIDEBAR)
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
# 1. LÓGICA SEGÚN ESTADO DE AUTENTICACIÓN
# =============================================================================

if st.session_state["authentication_status"]:
    
    # --- INICIALIZACIÓN DE ESTADOS (La "memoria" de navegación) ---
    if 'menu_actual'        not in st.session_state: st.session_state.menu_actual        = "Bienvenida"
    if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
    if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual      = None
    if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None

    # Registrar visita (una sola vez por sesión)
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    # Aplicar tus estilos CSS personalizados
    aplicar_estilos()

    # =============================================================================
    # 2. RENDERIZADO DE SECCIONES (TODO EN PANTALLA PRINCIPAL)
    # =============================================================================

    # --- SECCIÓN A: BIENVENIDA (Home) ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Bienvenidos a Lagrangianitos</h1>", unsafe_allow_html=True)
        st.write(f"Hola **{st.session_state['name']}**, prepárate para dominar la PAES M1.")
        
        st.markdown("""
        ### ¿Qué quieres hacer hoy?
        """)
        
        # BOTONES DE NAVEGACIÓN PRINCIPAL (Sustituyen a la barra lateral en móvil)
        if st.button("🏠 Ir al Dashboard de Clases ahora", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"
            st.rerun()
            
        if st.button("📂 Abrir Biblioteca de PDFs", use_container_width=True):
            st.session_state.menu_actual = "Biblioteca"
            st.rerun()
        
        st.info("💡 Consejo: Revisa tus progresos en el Dashboard cada semana.")

    # --- SECCIÓN B: DASHBOARD (M1 y FÍSICA) ---
    elif st.session_state.menu_actual == "Dashboard":
        # Botón para volver al inicio siempre arriba
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"
            st.session_state.eje_actual = None
            st.rerun()

        zona_cl = pytz.timezone('America/Santiago')
        ahora = datetime.now(zona_cl)
        st.markdown(f'<div class="header-azul">🐉 Dashboard — PAES M1 | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)

        if st.session_state.eje_actual is None:
            st.subheader("Selecciona un Eje para estudiar:")
            
            # Aquí recreamos las tarjetas de tu segunda foto
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔢 Números\nConjuntos • Operatoria", use_container_width=True, key="d_num"):
                    st.session_state.eje_actual = "Números"; st.rerun()
                if st.button("📐 Geometría\nFiguras • Área • Vectores", use_container_width=True, key="d_geo"):
                    st.session_state.eje_actual = "Geometría"; st.rerun()
            
            with col2:
                if st.button("📉 Álgebra\nÁlgebra • Funciones", use_container_width=True, key="d_alg"):
                    st.session_state.eje_actual = "Álgebra"; st.rerun()
                if st.button("📊 Datos y Azar\nEstadística • Probabilidad", use_container_width=True, key="d_dat"):
                    st.session_state.eje_actual = "Datos"; st.rerun()
            
            st.divider()
            st.subheader("🟣 Contenido de Física")
            f1, f2 = st.columns(2)
            with f1:
                st.button("🌊 Ondas", use_container_width=True)
                st.button("⚡ Energía", use_container_width=True)
            with f2:
                st.button("⚙️ Mecánica", use_container_width=True)
                st.button("🔌 Electricidad", use_container_width=True)

        else:
            # Vista dentro de un Eje seleccionado
            if st.button("🔙 Volver a los Ejes"):
                st.session_state.eje_actual = None; st.rerun()
            st.title(f"Estudiando: {st.session_state.eje_actual}")
            # Aquí iría el cargador de clases que ya tenías

    # --- SECCIÓN C: BIBLIOTECA ---
    elif st.session_state.menu_actual == "Biblioteca":
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"; st.rerun()
            
        st.title("📂 Biblioteca de Recursos")
        st.write("Descarga aquí tus ensayos y guías.")
        
        pdf_dir = Path("pdfs")
        if pdf_dir.exists():
            for pdf in pdf_dir.glob("*.pdf"):
                with open(pdf, "rb") as f:
                    st.download_button(label=f"⬇️ {pdf.name}", data=f, file_name=pdf.name, use_container_width=True)
        else:
            st.info("No hay PDFs disponibles todavía.")

    # =============================================================================
    # 3. PIE DE PÁGINA (CONTROL DE ADMIN Y LOGOUT)
    # =============================================================================
    st.divider()
    
    # El Logout ahora está visible al final para que sea fácil salir en el cel
    col_out, col_admin = st.columns([1, 1])
    
    with col_out:
        authenticator.logout('Cerrar Sesión', 'main')
    
    with col_admin:
        # Solo el admin ve el interruptor del modo detective
        if st.session_state["username"] == "admin":
            modo_detective = st.toggle("🕵️ Modo Detective")
            if modo_detective:
                visitas_total = obtener_visitas()
                st.write(f"👁️ Visitas: **{visitas_total}**")
                st.warning("Panel Admin activo")

# =============================================================================
# 4. MANEJO DE ACCESOS
# =============================================================================

elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrectos.')
    
elif st.session_state["authentication_status"] is None:
    st.markdown("<h2 style='text-align:center;'>🐉 Lagrangianitos Hub</h2>", unsafe_allow_html=True)
    st.info("Entrenador de Élite: Ingresa tus credenciales para continuar.")
