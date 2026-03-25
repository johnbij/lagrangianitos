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
    
    # --- BARRA LATERAL (Logout y Bienvenida) ---
    with st.sidebar:
        st.markdown(f"### 🐉 Bienvenido, {st.session_state['name']}")
        authenticator.logout('Cerrar Sesión', 'sidebar')
        st.divider()

    # --- INICIALIZACIÓN DE ESTADOS ---
    if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
    if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual      = None
    if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None
    if 'menu_actual'        not in st.session_state: st.session_state.menu_actual        = "🐉 Bienvenida"
    if 'ultimo_visto'       not in st.session_state: st.session_state.ultimo_visto       = None
    if 'nick_usuario'       not in st.session_state: st.session_state.nick_usuario       = st.session_state['username']

    # Registrar visita
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    aplicar_estilos()

    # --- NAVEGACIÓN Y PANEL DETECTIVE ---
    with st.sidebar:
        visitas_total = obtener_visitas()
        st.markdown(f'<div style="text-align:center; font-size:12px;">👁️ <b>{visitas_total:,}</b> visitas</div>', unsafe_allow_html=True)
        
        # OPCIÓN DE ADMIN: Solo visible para el usuario "admin"
        modo_detective = False
        if st.session_state["username"] == "admin":
            st.divider()
            modo_detective = st.toggle("🕵️ Modo Detective")
        
        if not modo_detective:
            st.divider()
            menu = st.radio("Ir a:", ["🐉 Bienvenida", "🏠 Dashboard PAES", "📂 Biblioteca de PDFs"], key="nav_radio")
            st.session_state.menu_actual = menu
        st.divider()
        st.caption("💬 \"Sólo existen dos días en el año en los que no se puede hacer nada.\" — Dalai Lama")

    # =============================================================================
    # 2. RENDERIZADO DE SECCIONES
    # =============================================================================

    # A. VISTA DETECTIVE (SEGURIDAD)
    if modo_detective:
        st.title("🕵️ Panel de Monitoreo (Admin)")
        st.info("Aquí puedes vigilar si hay comportamientos sospechosos (múltiples IPs o accesos rápidos).")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Sesiones", f"{visitas_total}")
        with col2:
            st.metric("Usuario Actual", st.session_state["username"])
        
        st.subheader("Registro de Actividad")
        st.write("Historial de clases vistas por tus alumnos:")
        # Aquí puedes llamar a una función que lea tus logs
        # st.dataframe(obtener_logs_completos())
        st.warning("Consejo: Si notas que un alumno entra a 10 clases en 1 minuto, está compartiendo la cuenta.")

    # B. DASHBOARD PAES
    elif st.session_state.menu_actual == "🏠 Dashboard PAES":
        zona_cl = pytz.timezone('America/Santiago')
        ahora = datetime.now(zona_cl)
        st.markdown(f'<div class="header-azul">🐉 Lagrangianitos — PAES M1 | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)

        if st.session_state.eje_actual is None:
            st.subheader("Selecciona un Eje para estudiar:")
            c1, c2 = st.columns(2)
            with c1:
                if st.button("🔢 Números", key="btn_num", use_container_width=True):
                    st.session_state.eje_actual = "🔢 Números"; st.rerun()
            with c2:
                if st.button("📉 Álgebra", key="btn_alg", use_container_width=True):
                    st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        else:
            if st.button("🔙 Volver a los Ejes"):
                st.session_state.eje_actual = None; st.rerun()
            
            eje = st.session_state.eje_actual
            st.title(f"Estudiando: {eje}")
            # El contenido se carga desde CONTENIDOS[eje]

    # C. BIBLIOTECA
    elif st.session_state.menu_actual == "📂 Biblioteca de PDFs":
        st.title("📂 Biblioteca de Recursos")
        st.write("Descarga aquí tus ensayos y guías personalizadas.")
        # Lógica de escaneo de carpeta /pdfs
        pdf_dir = Path("pdfs")
        if pdf_dir.exists():
            for pdf in pdf_dir.glob("*.pdf"):
                with open(pdf, "rb") as f:
                    st.download_button(label=f"⬇️ {pdf.name}", data=f, file_name=pdf.name)
        else:
            st.info("Sube tus PDFs a la carpeta /pdfs para que aparezcan aquí.")

    # D. BIENVENIDA
    elif st.session_state.menu_actual == "🐉 Bienvenida":
        st.title("🐉 Bienvenidos a Lagrangianitos")
        st.write(f"Hola **{st.session_state['name']}**, prepárate para dominar la PAES M1.")
        st.markdown("""
        ### ¿Qué quieres hacer hoy?
        1. **Revisar clases** en el Dashboard.
        2. **Descargar material** en la Biblioteca.
        3. **Ver tus progresos** (Próximamente).
        """)
        if st.button("🚀 Ir al Dashboard ahora", type="primary"):
            st.session_state.menu_actual = "🏠 Dashboard PAES"; st.rerun()

# =============================================================================
# 3. MANEJO DE ACCESO DENEGADO
# =============================================================================

elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrectos.')
elif st.session_state["authentication_status"] is None:
    st.markdown("""
        <div style="text-align:center; padding: 40px;">
            <h1>🐉 Lagrangianitos Hub</h1>
            <p>Acceso restringido a alumnos matriculados.</p>
        </div>
    """, unsafe_allow_html=True)
    st.info("Ingresa tus credenciales en el formulario de arriba.")
