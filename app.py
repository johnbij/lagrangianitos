import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from pathlib import Path

# =============================================================================
# 0. IMPORTACIONES (SOPORTE GITHUB/LINUX)
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
# 1. CONFIGURACIÓN Y SESIÓN (COOKIES)
# =============================================================================
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

# Cargar el YAML que ya tienes configurado con 30 días
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("No se encontró config.yaml")
    st.stop()

# Inicializar autenticador con los parámetros de tu YAML
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    cookie_expiry_days=config['cookie']['expiry_days']
)

# Login en pantalla principal
authenticator.login(location='main')

# =============================================================================
# 2. LÓGICA DE NAVEGACIÓN
# =============================================================================
if st.session_state["authentication_status"]:
    
    # Estados de memoria
    if 'menu_actual' not in st.session_state: st.session_state.menu_actual = "Bienvenida"
    if 'eje_actual'  not in st.session_state: st.session_state.eje_actual = None

    # Registrar visita (opcional, si tienes el módulo visitas.py)
    try:
        if 'visita_registrada' not in st.session_state:
            st.session_state.visita_registrada = True
            registrar_visita()
    except:
        pass

    aplicar_estilos()

    # --- SECCIÓN: BIENVENIDA ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos</h1>", unsafe_allow_html=True)
        st.write(f"Hola **{st.session_state['name']}**, bienvenido al entrenamiento.")
        
        if st.button("🚀 Entrar al Dashboard", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"
            st.rerun()
            
        if st.button("📂 Biblioteca de PDFs", use_container_width=True):
            st.session_state.menu_actual = "Biblioteca"
            st.rerun()

    # --- SECCIÓN: DASHBOARD (MAPEO DE EMOJIS SEGÚN CAPTURA) ---
    elif st.session_state.menu_actual == "Dashboard":
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"
            st.session_state.eje_actual = None
            st.rerun()

        if st.session_state.eje_actual is None:
            st.markdown("### 🎯 Selecciona tu Eje")
            c1, c2 = st.columns(2)
            
            with c1:
                # LLAVES EXACTAS DE TU CONTENIDOS.PY (Vistas en el debug azul)
                if st.button("🔢 Números", use_container_width=True):
                    st.session_state.eje_actual = "1️⃣2️⃣3️⃣ Números"; st.rerun()
                if st.button("📐 Geometría", use_container_width=True):
                    st.session_state.eje_actual = "📐 Geometría"; st.rerun()
                if st.button("⚛️ Física", use_container_width=True):
                    st.session_state.eje_actual = "⚛️ Física"; st.rerun()
            with c2:
                if st.button("📉 Álgebra", use_container_width=True):
                    st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
                if st.button("📊 Datos y Azar", use_container_width=True):
                    st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()
                if st.button("🧬 Biología/Química", use_container_width=True):
                    st.session_state.eje_actual = "🔬 Biología"; st.rerun()

        else:
            eje_key = st.session_state.eje_actual
            if st.button("🔙 Cambiar de Eje"):
                st.session_state.eje_actual = None; st.rerun()
            
            st.title(f"📍 {eje_key}")
            
            # Verificación del Diccionario
            if eje_key in CONTENIDOS:
                unidades = list(CONTENIDOS[eje_key].keys())
                u_sel = st.selectbox("Unidad:", ["--- Seleccionar ---"] + unidades)
                
                if u_sel != "--- Seleccionar ---":
                    clases = CONTENIDOS[eje_key][u_sel]
                    c_sel = st.selectbox("Clase:", ["--- Seleccionar ---"] + list(clases.keys()))
                    
                    if c_sel != "--- Seleccionar ---":
                        data = clases[c_sel]
                        st.divider()
                        st.header(c_sel)
                        
                        # Mostrar Video
                        if "video" in data and data["video"]:
                            st.video(data["video"])
                        
                        # Mostrar Descripción
                        if "descripcion" in data:
                            st.write(data["descripcion"])
                            
                        # Registrar Progreso
                        if st.button("✅ Marcar como completada"):
                            registrar_clase(st.session_state['username'], eje_key, u_sel, c_sel)
                            st.balloons()
            else:
                st.error(f"No encontré el eje '{eje_key}'")
                st.info(f"Llaves en tu archivo: {list(CONTENIDOS.keys())}")

    # --- SECCIÓN: BIBLIOTECA ---
    elif st.session_state.menu_actual == "Biblioteca":
        if st.button("🔙 Volver"):
            st.session_state.menu_actual = "Bienvenida"; st.rerun()
        st.title("📂 Biblioteca")
        st.write("Aquí aparecerán tus archivos PDF.")

    # --- PIE DE PÁGINA ---
    st.divider()
    authenticator.logout('Cerrar Sesión', 'main')

# Manejo de Login Fallido
elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrectos.')
elif st.session_state["authentication_status"] is None:
    st.markdown("<h2 style='text-align:center;'>🐉 Lagrangianitos Hub</h2>", unsafe_allow_html=True)
    st.info("Ingresa tus credenciales para acceder.")
