import streamlit as st
from datetime import datetime
import pytz

# Configuración de la página
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

# --- ESTADO DE NAVEGACIÓN ---
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = "🔢 Números"

# --- ESTILOS CSS PARA INTEGRAR BOTONES ---
st.markdown("""
    <style>
    /* Estilo para que los botones se vean limpios dentro de la barra */
    .stButton > button {
        width: 100%;
        border-radius: 5px;
        height: 50px;
        background-color: #f8f9fa;
        color: #333;
        border: 1px solid #ddd;
    }
    .stButton > button:hover {
        border-color: #3b71ca;
        color: #3b71ca;
    }
    /* Contenedor de la barra blanca */
    .barra-blanca {
        background-color: white;
        padding: 20px;
        border-radius: 0 0 10px 10px;
        border: 1px solid #dddddd;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/blue-rocket-icon-png-17.png", width=100)
    st.title("Perfil")
    st.markdown('''**Seba** \n*Estudiante de Ingeniería* \n\n[📸 Instagram](https://instagram.com/lagrangianitos)''')
    st.divider()
    st.write("Típ: El orden en los ejes es clave.")

# --- DISEÑO DE BANDERAS ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
faltan = fecha_paes - ahora

# 1. BARRA AZUL
st.markdown(f"""
    <div style="background-color: #3b71ca; padding: 20px; border-radius: 10px 10px 0 0; color: white; height: 100px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid white;">
        <div style="font-size: 26px; font-weight: bold;">🚀 Centro de Recursos: PAES M1</div>
        <div style="text-align: right;">
            <div style="font-size: 12px; opacity: 0.9;">⏰ Hora Actual</div>
            <div style="font-size: 20px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. BARRA ROJA
st.markdown(f"""
    <div style="background-color: #cc0000; padding: 20px; color: white; height: 100px; display: flex; justify-content: space-around; align-items: center; border-bottom: 1px solid #eee;">
        <div style="font-size: 18px; font-weight: bold;">⏳ Días: {faltan.days}</div>
        <div style="font-size: 18px; font-weight: bold;">Horas: {faltan.seconds // 3600}</div>
        <div style="font-size: 18px; font-weight: bold;">Minutos: {(faltan.seconds // 60) % 60}</div>
    </div>
    """, unsafe_allow_html=True)

# 3. BARRA BLANCA INTEGRADA (Con botones dentro)
with st.container():
    # Abrimos el div blanco con HTML
    st.markdown('<div class="barra-blanca">', unsafe_allow_html=True)
    cols = st.columns(4)
    with cols[0]:
        if st.button("🔢 Números"): st.session_state.eje_actual = "🔢 Números"
    with cols[1]:
        if st.button("📉 Álgebra"): st.session_state.eje_actual = "📉 Álgebra"
    with cols[2]:
        if st.button("📐 Geometría"): st.session_state.eje_actual = "📐 Geometría"
    with cols[3]:
        if st.button("📊 Estadística"): st.session_state.eje_actual = "📊 Estadística"
    # Cerramos el div
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# --- CONTENIDO ---
eje = st.session_state.eje_actual
if eje == "📉 Álgebra":
    st.markdown("<h1 style='color: blue;'>Eje Álgebra</h1>", unsafe_allow_html=True)
    st.info("Típ: Anota: tip ... El lenguaje algebraico es la base de toda la prueba.")
else:
    st.header(eje)
    st.write(f"Recursos para el eje de {eje[2:]}")
