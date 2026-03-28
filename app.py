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
    from visitas import registrar_visita
except ImportError:
    from Contenidos import CONTENIDOS
    from Styles import aplicar_estilos
    from Logros import registrar_clase
    from Visitas import registrar_visita

# =============================================================================
# 1. CONFIGURACIÓN Y SESIÓN (COOKIES)
# =============================================================================
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("No se encontró config.yaml")
    st.stop()

# Inicialización con 30 días de sesión desde tu YAML
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

authenticator.login(location='main')

# =============================================================================
# 2. LÓGICA DE NAVEGACIÓN
# =============================================================================
if st.session_state["authentication_status"]:
    
    if 'menu_actual' not in st.session_state: st.session_state.menu_actual = "Bienvenida"
    if 'eje_actual'  not in st.session_state: st.session_state.eje_actual = None

    aplicar_estilos()

    # --- PANTALLA BIENVENIDA ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos</h1>", unsafe_allow_html=True)
        st.write(f"Hola **{st.session_state['name']}**, bienvenido.")
        
        if st.button("🚀 Entrar al Dashboard", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"; st.rerun()
            
        if st.button("📂 Biblioteca de PDFs", use_container_width=True):
            st.session_state.menu_actual = "Biblioteca"; st.rerun()

    # --- DASHBOARD (MOTOR DE CONTENIDOS) ---
    elif st.session_state.menu_actual == "Dashboard":
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"; st.session_state.eje_actual = None; st.rerun()

        if st.session_state.eje_actual is None:
            st.subheader("🎯 Selecciona tu Eje")
            for eje in CONTENIDOS.keys():
                if st.button(eje, use_container_width=True):
                    st.session_state.eje_actual = eje; st.rerun()
        else:
            eje_key = st.session_state.eje_actual
            if st.button(f"🔙 Cambiar de Eje"):
                st.session_state.eje_actual = None; st.rerun()
            
            st.title(f"📍 {eje_key}")
            
            # Navegación en la estructura: CONTENIDOS[eje]["subcategorias"]
            if eje_key in CONTENIDOS:
                subcats = CONTENIDOS[eje_key].get("subcategorias", {})
                
                if subcats:
                    unidades = list(subcats.keys())
                    u_sel = st.selectbox("📚 Unidad:", ["---"] + unidades)
                    
                    if u_sel != "---":
                        clases_dict = subcats[u_sel]
                        mapeo = {v["label"]: k for k, v in clases_dict.items()}
                        c_label = st.selectbox("📖 Clase:", ["---"] + list(mapeo.keys()))
                        
                        if c_label != "---":
                            clase_id = mapeo[c_label]
                            clase_data = clases_dict[clase_id]
                            
                            st.divider()
                            # EJECUCIÓN DEL RENDER
                            if "render" in clase_data:
                                clase_data["render"]()
                                
                            if st.button("✅ Terminar Clase"):
                                registrar_clase(st.session_state['username'], eje_key, u_sel, c_label)
                                st.balloons()
            else:
                st.error("Error de carga.")

    # --- BIBLIOTECA ---
    elif st.session_state.menu_actual == "Biblioteca":
        if st.button("🔙 Volver"):
            st.session_state.menu_actual = "Bienvenida"; st.rerun()
        st.title("📂 PDFs")

    st.divider()
    authenticator.logout('Cerrar Sesión', 'main')

elif st.session_state["authentication_status"] is False:
    st.error('Usuario/Contraseña incorrectos.')
elif st.session_state["authentication_status"] is None:
    st.markdown("<h2 style='text-align:center;'>🐉 Lagrangianitos</h2>", unsafe_allow_html=True)
