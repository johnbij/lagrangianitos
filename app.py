import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from pathlib import Path
import pytz
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Importaciones de tus módulos locales (Asegúrate de que existan en tu repo)
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

# Render del Login en la pantalla principal (Ideal para móvil)
authenticator.login(location='main')

# =============================================================================
# 1. LÓGICA TRAS EL LOGIN
# =============================================================================

if st.session_state["authentication_status"]:
    
    # --- INICIALIZACIÓN DE ESTADOS (La "memoria" del Entrenador) ---
    if 'menu_actual'        not in st.session_state: st.session_state.menu_actual = "Bienvenida"
    if 'eje_actual'         not in st.session_state: st.session_state.eje_actual = None
    if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual = None
    if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None

    # Registrar visita (una sola vez)
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    # Aplicar tus estilos CSS personalizados (Colores, bordes, etc)
    aplicar_estilos()

    # =============================================================================
    # 2. RENDERIZADO DE SECCIONES (FLUJO PRINCIPAL)
    # =============================================================================

    # --- A. PANTALLA DE BIENVENIDA ---
    if st.session_state.menu_actual == "Bienvenida":
        st.markdown("<h1 style='text-align:center;'>🐉 Bienvenidos a Lagrangianitos</h1>", unsafe_allow_html=True)
        st.write(f"Hola **{st.session_state['name']}**, prepárate para el entrenamiento de élite.")
        
        st.divider()
        st.markdown("### ¿Qué quieres entrenar hoy?")
        
        # Botones de navegación central
        if st.button("🏠 Ir al Dashboard de Clases", type="primary", use_container_width=True):
            st.session_state.menu_actual = "Dashboard"
            st.rerun()
            
        if st.button("📂 Abrir Biblioteca de PDFs", use_container_width=True):
            st.session_state.menu_actual = "Biblioteca"
            st.rerun()
        
        st.info("💡 Consejo del Profe: La constancia le gana al talento. Dale átomos.")

    # --- B. DASHBOARD (EL CORAZÓN DE LA APP) ---
    elif st.session_state.menu_actual == "Dashboard":
        
        # Botón para volver al Inicio siempre arriba
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"
            st.session_state.eje_actual = None
            st.rerun()

        # 1. SI NO HA ELEGIDO EJE: Mostramos las tarjetas de la segunda foto
        if st.session_state.eje_actual is None:
            st.markdown("<h2 style='text-align:center;'>🎯 Selección de Eje</h2>", unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                # Los nombres aquí deben coincidir con las llaves de tu dict CONTENIDOS
                if st.button("🔢 Números\nConjuntos • Operatoria", use_container_width=True, key="card_num"):
                    st.session_state.eje_actual = "🔢 Números"; st.rerun()
                if st.button("📐 Geometría\nFiguras • Área • Vectores", use_container_width=True, key="card_geo"):
                    st.session_state.eje_actual = "📐 Geometría"; st.rerun()
            
            with col2 if 'col2' in locals() else c2: # Parche por si acaso
                if st.button("📉 Álgebra\nÁlgebra • Funciones", use_container_width=True, key="card_alg"):
                    st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
                if st.button("📊 Datos y Azar\nEstadística • Probabilidad", use_container_width=True, key="card_dat"):
                    st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()
            
            st.divider()
            st.subheader("🟣 Contenido de Física")
            f1, f2 = st.columns(2)
            with f1:
                if st.button("🌊 Ondas", use_container_width=True): st.info("Próximamente")
            with f2:
                if st.button("⚙️ Mecánica", use_container_width=True): st.info("Próximamente")

        # 2. SI YA ELIGIÓ EJE: Cargamos las clases desde contenidos.py
        else:
            eje = st.session_state.eje_actual
            if st.button(f"🔙 Volver a Selección de Ejes"):
                st.session_state.eje_actual = None; st.rerun()
            
            st.title(f"📍 {eje}")
            
            if eje in CONTENIDOS:
                # Selector de Unidad/Subcategoría
                subcategorias = list(CONTENIDOS[eje].keys())
                subcat = st.selectbox("Selecciona la Unidad:", ["--- Elige ---"] + subcategorias)
                
                if subcat != "--- Elige ---":
                    # Selector de Clase
                    clases = CONTENIDOS[eje][subcat]
                    clase_nom = st.selectbox("Elige la Clase:", ["--- Elige ---"] + list(clases.keys()))
                    
                    if clase_nom != "--- Elige ---":
                        datos_clase = clases[clase_nom]
                        st.divider()
                        st.header(f"📖 {clase_nom}")
                        
                        # Render de Video
                        if "video" in datos_clase and datos_clase["video"]:
                            st.video(datos_clase["video"])
                        
                        # Render de Contenido/Texto
                        if "descripcion" in datos_clase:
                            st.write(datos_clase["descripcion"])
                        
                        # Logros / Guardado en DB (Próximamente Sheets)
                        if st.button("✅ Marcar como completada"):
                            registrar_clase(st.session_state['username'], eje, subcat, clase_nom)
                            st.balloons()
                            st.success("¡Clase registrada en tu historial!")
            else:
                st.warning("Aún no hay contenido en este eje. ¡Sigue entrenando los otros!")

    # --- C. BIBLIOTECA ---
    elif st.session_state.menu_actual == "Biblioteca":
        if st.button("🔙 Volver al Inicio"):
            st.session_state.menu_actual = "Bienvenida"; st.rerun()
            
        st.title("📂 Biblioteca de Recursos")
        st.write("Descarga tus guías y ensayos personalizados.")
        
        pdf_dir = Path("pdfs")
        if pdf_dir.exists():
            for pdf in pdf_dir.glob("*.pdf"):
                with open(pdf, "rb") as f:
                    st.download_button(label=f"⬇️ Descargar {pdf.name}", data=f, file_name=pdf.name, use_container_width=True)
        else:
            st.info("Sube tus archivos a la carpeta /pdfs para verlos aquí.")

    # =============================================================================
    # 3. PIE DE PÁGINA (CONTROL DE ACCESOS Y ADMIN)
    # =============================================================================
    st.divider()
    c_out, c_det = st.columns([1, 1])
    
    with c_out:
        authenticator.logout('Cerrar Sesión', 'main')
    
    with c_det:
        if st.session_state["username"] == "admin":
            if st.toggle("🕵️ Modo Detective"):
                vt = obtener_visitas()
                st.write(f"Visitas totales: **{vt}**")
                st.caption("Recuerda: Si hay muchas visitas de un mismo user, lo están compartiendo.")

# =============================================================================
# 4. MANEJO DE LOGIN FALLIDO O VACÍO
# =============================================================================

elif st.session_state["authentication_status"] is False:
    st.error('Usuario o contraseña incorrectos.')
elif st.session_state["authentication_status"] is None:
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos Hub</h1>", unsafe_allow_html=True)
    st.info("Ingresa tus credenciales para acceder al entrenamiento.")
