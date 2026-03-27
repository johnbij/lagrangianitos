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
# 0. CONFIGURACIÓN DE PÁGINA Y SEGURIDAD (TODO EN PANTALLA PRINCIPAL)
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
    
    # --- INICIALIZACIÓN DE ESTADOS (La "memoria" de navegación) ---
    if 'menu_actual'        not in st.session_state: st.session_state.menu_actual = "Bienvenida"
    if 'eje_actual'         not in st.session_state: st.session_state.eje_actual = None
    if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual = None

    # Registrar visita (solo una vez por sesión)
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    # Aplicar tus estilos CSS (del archivo styles.py)
    aplicar_estilos()

    # =============================================================================
    # 2. RENDERIZADO DE SECCIONES (SIN BARRA LATERAL)
    # =============================================================================

    # --- SECCIÓN A: BIENVENIDA ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Bienvenidos a Lagrangianitos</h1>", unsafe_allow_html=True)
        st.write(f"Hola **{st.session_state['name']}**, prepárate para el entrenamiento de élite.")
        
        st.divider()
        st.markdown("### ¿Qué quieres hacer hoy?")
        
        # BOTONES DE ACCESO RÁPIDO
        if st.button("🚀 Ir al Dashboard de Clases ahora", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"
            st.rerun()
            
        if st.button("📂 Abrir Biblioteca de PDFs", use_container_width=True):
            st.session_state.menu_actual = "Biblioteca"
            st.rerun()
        
        st.info("💡 Consejo: La PAES no se gana con talento, se gana con repetición. ¡Dale átomos!")

    # --- SECCIÓN B: DASHBOARD (EL MOTOR DE LAS CLASES) ---
    elif st.session_state.menu_actual == "Dashboard":
        
        # Botón para volver al Home siempre visible arriba
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"
            st.session_state.eje_actual = None
            st.rerun()

        # 1. SI NO HA ELEGIDO EJE: Mostramos las tarjetas de selección
        if st.session_state.eje_actual is None:
            st.markdown("<h2 style='text-align:center;'>🎯 Elige tu Eje</h2>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                # IMPORTANTE: El texto en "" debe ser IGUAL a la llave en contenidos.py
                if st.button("🔢 Números\nConjuntos • Operatoria", use_container_width=True):
                    st.session_state.eje_actual = "Números"; st.rerun()
                if st.button("📐 Geometría\nFiguras • Áreas", use_container_width=True):
                    st.session_state.eje_actual = "Geometría"; st.rerun()
            with c2:
                if st.button("📉 Álgebra\nÁlgebra • Funciones", use_container_width=True):
                    st.session_state.eje_actual = "Álgebra"; st.rerun()
                if st.button("📊 Datos y Azar\nProbabilidades", use_container_width=True):
                    st.session_state.eje_actual = "Datos"; st.rerun()

        # 2. SI YA ELIGIÓ EJE: Cargamos el contenido dinámico
        else:
            eje_key = st.session_state.eje_actual
            if st.button(f"🔙 Volver a los Ejes"):
                st.session_state.eje_actual = None; st.rerun()
            
            st.title(f"📍 {eje_key}")
            
            # Verificamos si el eje existe en el diccionario CONTENIDOS
            if eje_key in CONTENIDOS:
                subcategorias = list(CONTENIDOS[eje_key].keys())
                subcat = st.selectbox("Selecciona la Unidad:", ["--- Elige ---"] + subcategorias)
                
                if subcat != "--- Elige ---":
                    clases = CONTENIDOS[eje_key][subcat]
                    clase_nom = st.selectbox("Elige la Clase:", ["--- Elige ---"] + list(clases.keys()))
                    
                    if clase_nom != "--- Elige ---":
                        datos_clase = clases[clase_nom]
                        st.divider()
                        st.header(f"📖 {clase_nom}")
                        
                        # RENDER DE VIDEO (Si existe el link en contenidos.py)
                        if "video" in datos_clase and datos_clase["video"]:
                            st.video(datos_clase["video"])
                        
                        # RENDER DE DESCRIPCIÓN
                        if "descripcion" in datos_clase:
                            st.write(datos_clase["descripcion"])
                        
                        # BOTÓN DE PROGRESO (Guarda en logros.py)
                        if st.button("✅ Marcar clase como terminada"):
                            registrar_clase(st.session_state['username'], eje_key, subcat, clase_nom)
                            st.balloons()
                            st.success("¡Progreso guardado, Guerrero!")
            else:
                st.error(f"Error: No encontré contenido para '{eje_key}'")
                st.info(f"Revisa que en contenidos.py la llave sea '{eje_key}'")

    # --- SECCIÓN C: BIBLIOTECA ---
    elif st.session_state.menu_actual == "Biblioteca":
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"; st.rerun()
            
        st.title("📂 Biblioteca de Recursos")
        st.write("Descarga aquí tus guías y ensayos.")
        
        pdf_dir = Path("pdfs")
        if pdf_dir.exists():
            for pdf in pdf_dir.glob("*.pdf"):
                with open(pdf, "rb") as f:
                    st.download_button(label=f"⬇️ {pdf.name}", data=f, file_name=pdf.name, use_container_width=True)
        else:
            st.info("No hay PDFs disponibles aún en la carpeta /pdfs.")

    # =============================================================================
    # 3. PIE DE PÁGINA (LOGOUT Y ADMIN)
    # =============================================================================
    st.divider()
    col_out, col_adm = st.columns(2)
    
    with col_out:
        authenticator.logout('Cerrar Sesión', 'main')
        
    with col_adm:
        if st.session_state["username"] == "admin":
            if st.toggle("🕵️ Modo Detective"):
                vt = obtener_visitas()
                st.write(f"Visitas Totales: **{vt}**")

# =============================================================================
# 4. MANEJO DE ACCESO DENEGADO
# =============================================================================

elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrectos.')
elif st.session_state["authentication_status"] is None:
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos Hub</h1>", unsafe_allow_html=True)
    st.info("Acceso restringido. Por favor, ingresa tus credenciales.")
