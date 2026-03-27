import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from pathlib import Path
import pytz
from datetime import datetime

# =============================================================================
# 0. IMPORTACIONES CRÍTICAS (CON MANEJO DE ERRORES PARA GITHUB)
# =============================================================================

try:
    # Intentamos importar con minúsculas (estándar)
    from contenidos import CONTENIDOS
    from styles import aplicar_estilos
    from logros import registrar_clase
    from visitas import registrar_visita, obtener_visitas
except ImportError:
    try:
        # Si falla, intentamos con Mayúsculas (por si acaso en GitHub están así)
        from Contenidos import CONTENIDOS
        from Styles import aplicar_estilos
        from Logros import registrar_clase
        from Visitas import registrar_visita, obtener_visitas
    except ImportError as e:
        st.error(f"❌ Error crítico: No se encontraron los módulos auxiliares en GitHub. {e}")
        st.stop()

# =============================================================================
# 1. CONFIGURACIÓN DE PÁGINA Y SEGURIDAD
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
# 2. LÓGICA TRAS LA AUTENTICACIÓN
# =============================================================================

if st.session_state["authentication_status"]:
    
    # Inicialización de estados de navegación
    if 'menu_actual' not in st.session_state: st.session_state.menu_actual = "Bienvenida"
    if 'eje_actual'  not in st.session_state: st.session_state.eje_actual = None

    # Registrar visita una vez
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    aplicar_estilos()

    # --- A. PANTALLA DE BIENVENIDA ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos</h1>", unsafe_allow_html=True)
        st.write(f"Hola **{st.session_state['name']}**, listo para el entrenamiento.")
        
        if st.button("🚀 Ir al Dashboard ahora", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"
            st.rerun()
            
        if st.button("📂 Biblioteca de PDFs", use_container_width=True):
            st.session_state.menu_actual = "Biblioteca"
            st.rerun()

    # --- B. DASHBOARD (EL MOTOR QUE FALLABA) ---
    elif st.session_state.menu_actual == "Dashboard":
        
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"
            st.session_state.eje_actual = None
            st.rerun()

        # Selector de Ejes
        if st.session_state.eje_actual is None:
            st.subheader("Selecciona tu Eje:")
            c1, c2 = st.columns(2)
            
            # NOTA: Estas llaves deben existir en tu diccionario CONTENIDOS
            with c1:
                if st.button("🔢 Números", use_container_width=True):
                    st.session_state.eje_actual = "Números"; st.rerun()
                if st.button("📐 Geometría", use_container_width=True):
                    st.session_state.eje_actual = "Geometría"; st.rerun()
            with c2:
                if st.button("📉 Álgebra", use_container_width=True):
                    st.session_state.eje_actual = "Álgebra"; st.rerun()
                if st.button("📊 Datos", use_container_width=True):
                    st.session_state.eje_actual = "Datos"; st.rerun()

        # Visualización de Contenido
        else:
            eje_key = st.session_state.eje_actual
            if st.button("🔙 Cambiar de Eje"):
                st.session_state.eje_actual = None; st.rerun()
            
            st.title(f"📍 {eje_key}")

            # DEBUG PARA GITHUB: Si no aparece nada, esto nos dirá por qué
            if eje_key in CONTENIDOS:
                unidades = list(CONTENIDOS[eje_key].keys())
                unidad_sel = st.selectbox("Selecciona Unidad:", ["--- Elige ---"] + unidades)
                
                if unidad_sel != "--- Elige ---":
                    clases = CONTENIDOS[eje_key][unidad_sel]
                    clase_sel = st.selectbox("Selecciona Clase:", ["--- Elige ---"] + list(clases.keys()))
                    
                    if clase_sel != "--- Elige ---":
                        data = clases[clase_sel]
                        st.divider()
                        st.header(data.get("titulo", clase_sel))
                        
                        if "video" in data:
                            st.video(data["video"])
                        
                        if "descripcion" in data:
                            st.write(data["descripcion"])
                            
                        if st.button("✅ Terminar Clase"):
                            registrar_clase(st.session_state['username'], eje_key, unidad_sel, clase_sel)
                            st.balloons()
            else:
                st.error(f"No se encontró el eje '{eje_key}' en el archivo de contenidos.")
                st.info(f"Llaves detectadas en GitHub: {list(CONTENIDOS.keys())}")

    # --- C. BIBLIOTECA ---
    elif st.session_state.menu_actual == "Biblioteca":
        if st.button("🔙 Volver"):
            st.session_state.menu_actual = "Bienvenida"; st.rerun()
        st.title("📂 PDFs")
        # (Lógica de descarga aquí...)

    # --- PIE DE PÁGINA ---
    st.divider()
    authenticator.logout('Cerrar Sesión', 'main')

# Manejo de Login
elif st.session_state["authentication_status"] is False:
    st.error('Credenciales incorrectas.')
elif st.session_state["authentication_status"] is None:
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos</h1>", unsafe_allow_html=True)
