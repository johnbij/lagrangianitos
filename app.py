import streamlit as st
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

# Inicializamos el estado como None para que no aparezca nada al principio
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None

# --- 2. INYECCIÓN DE CSS (TARJETAS PRO) ---
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        background-color: white !important;
        padding: 10px !important;
        border-radius: 0 0 15px 15px !important;
    }
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
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería*")
    st.markdown("### Redes Sociales \n- [📸 Instagram: @lagrangianitos](https://instagram.com/lagrangianitos)")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    # Típ: Aquí puedes poner recordatorios cortos para tus alumnos
    st.write("Típ: Selecciona un eje temático para comenzar tu sesión de estudio.")

# --- 4. LÓGICA DE NAVEGACIÓN ---
if menu == "🏠 Dashboard PAES":
    # Cabeceras (Reloj y Countdown)
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div style="background-color: #3b71ca; padding: 20px; border-radius: 15px 15px 0 0; color: white; display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 22px; font-weight: bold;">🚀 Centro de Recursos PAES</div>
            <div style="text-align: right;">
                <div style="font-size: 18px; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    faltan = fecha_paes - ahora
    st.markdown(f"""
        <div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center;">
            <div style="font-size: 16px; font-weight: bold;">⏳ Días: {faltan.days}</div>
            <div style="font-size: 16px; font-weight: bold;">Hrs: {faltan.seconds // 3600}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("📚 Ejes Temáticos")

    ejes_info = {
        "🔢 Números": "Conjuntos, operatoria, potencias, raíces y razones.",
        "📉 Álgebra": "Operatoria algebraica y funciones.",
        "📐 Geometría": "Teoremas, perímetros, áreas y volúmenes. Vectores.",
        "📊 Datos y Azar": "Medidas de tendencia, tablas, azar y combinatoria."
    }

    # Dibujamos las tarjetas
    for nombre, desc in ejes_info.items():
        if st.button(f"{nombre}\n{desc}", key=f"btn_{nombre}", use_container_width=True):
            st.session_state.eje_actual = nombre

    # --- EL TRUCO PARA OCULTAR ---
    if st.session_state.eje_actual is not None:
        st.write("---")
        eje_selec = st.session_state.eje_actual
        st.header(eje_selec)
        
        with st.expander(f"📂 Sesiones de {eje_selec[2:]}", expanded=True):
            st.info("Aquí aparecerán tus 121 clases organizadas.")
    else:
        # Esto aparece solo cuando no han hecho clic en nada
        st.info("👈 Selecciona uno de los ejes de arriba para ver las clases disponibles.")

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos PDF")
    # ... (Resto del código de descarga igual)
