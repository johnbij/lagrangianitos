import streamlit as st
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# Estado para controlar en qué "página" estamos
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None

# --- 2. INYECCIÓN DE CSS (TARJETAS PRO Y BOTONES DE NAVEGACIÓN) ---
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        background-color: white !important;
        padding: 10px !important;
        border-radius: 0 0 15px 15px !important;
    }
    /* Tarjetas Pro Principales */
    div.stButton > button {
        height: 110px !important;
        border-radius: 15px !important;
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        justify-content: center !important;
        padding: 20px !important;
        white-space: pre-wrap !important;
        text-align: left !important;
        margin-bottom: 15px !important;
        color: #31333F !important;
    }
    div.stButton > button:hover {
        border-color: #3b71ca !important;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1) !important;
        transform: translateY(-2px) !important;
    }
    /* Estilo para los mini-botones de navegación superior */
    .nav-container {
        display: flex;
        gap: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería en FCFM Universidad de Chile*")
    st.markdown("### Redes Sociales \n- [📸 Instagram: @lagrangianitos](https://instagram.com/lagrangianitos)")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("""
    Sólo existen dos días en el año en los que no se puede hacer nada. Uno se llama ayer y otro mañana. 
    Por lo tanto, hoy es el día ideal para amar, crecer, hacer y principalmente vivir. 
    Dalai Lama
    """)

# --- 4. LÓGICA DE NAVEGACIÓN ---
if menu == "🏠 Dashboard PAES":
    # Cabecera Azul (Título Centrado y Reloj)
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div style="background-color: #3b71ca; padding: 25px; border-radius: 15px 15px 0 0; color: white; position: relative; display: flex; align-items: center; justify-content: center; min-height: 100px;">
            <div style="font-size: 28px; font-weight: bold; text-align: center; padding: 0 120px; line-height: 1.2;">
                🐉 Lagrangianitos. Tus recursos PAES M1
            </div>
            <div style="position: absolute; right: 25px; text-align: right;">
                <div style="font-size: 14px; opacity: 0.9;">Santiago, Chile</div>
                <div style="font-size: 22px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Cabecera Roja (Countdown)
    fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    faltan = fecha_paes - ahora
    st.markdown(f"""
        <div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center;">
            <div style="font-size: 22px; font-weight: bold;">⏳ Días: {faltan.days}</div>
            <div style="font-size: 22px; font-weight: bold;">Hrs: {faltan.seconds // 3600}</div>
            <div style="font-size: 22px; font-weight: bold;">Min: {(faltan.seconds // 60) % 60}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # Definición de Ejes y Colores
    ejes_info = {
        "🔢 Números": "Conjuntos, operatoria, potencias, raíces y razones.",
        "📉 Álgebra": "Operatoria algebraica y funciones",
        "📐 Geometría": "Teoremas, perímetros, áreas y volúmenes. Vectores",
        "📊 Datos y Azar": "Medidas de tendencia y tablas. Azar, eventos y combinatoria."
    }

    if st.session_state.eje_actual is None:
        # PÁGINA A: MENÚ DE SELECCIÓN PRINCIPAL
        st.subheader("📚 Selecciona un Eje Temático")
        for nombre, desc in ejes_info.items():
            if st.button(f"{nombre}\n{desc}", key=f"btn_{nombre}", use_container_width=True):
                st.session_state.eje_actual = nombre
                st.rerun()
    else:
        # PÁGINA B: CONTENIDO DEL EJE + NAVEGACIÓN SUPERIOR COLORIDA
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        
        with col1:
            if st.button("🏠 Inicio", use_container_width=True):
                st.session_state.eje_actual = None
                st.rerun()
        with col2:
            if st.button("🔢 Números", key="nav_num", use_container_width=True):
                st.session_state.eje_actual = "🔢 Números"
                st.rerun()
        with col3:
            if st.button("📉 Álgebra", key="nav_alg", use_container_width=True):
                st.session_state.eje_actual = "📉 Álgebra"
                st.rerun()
        with col4:
            if st.button("📐 Geometría", key="nav_geo", use_container_width=True):
                st.session_state.eje_actual = "📐 Geometría"
                st.rerun()
        with col5:
            if st.button("📊 Datos", key="nav_dat", use_container_width=True):
                st.session_state.eje_actual = "📊 Datos y Azar"
                st.rerun()

        st.write("---")
        eje_selec = st.session_state.eje_actual
        st.header(eje_selec)
        
        with st.expander(f"📂 Sesiones de {eje_selec[2:]}", expanded=True):
            st.info(f"Contenido de {eje_selec}. Listado de clases en desarrollo.")

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos PDF")
    # ... (Lógica de archivos)
