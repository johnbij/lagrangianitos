import streamlit as st
from datetime import datetime
import pytz

# Configuración de la página
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

# --- ESTADO DE NAVEGACIÓN ---
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = "🔢 Números"

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/blue-rocket-icon-png-17.png", width=100)
    st.title("Perfil")
    st.markdown('''
**Seba**
*Estudiante de Ingeniería*

**Redes Sociales:**
* [📸 Instagram: @lagrangianitos](https://instagram.com/lagrangianitos)
''')
    st.divider()
    st.write("Típ: El orden en los ejes es clave para un buen puntaje.")

# --- DISEÑO DE BANDERAS (LAS 3 BARRAS IGUALES) ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
faltan = fecha_paes - ahora

# 1. BARRA AZUL (Título y Reloj)
st.markdown(f"""
    <div style="background-color: #3b71ca; padding: 20px; border-radius: 10px 10px 0 0; color: white; height: 100px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid white;">
        <div style="font-size: 26px; font-weight: bold;">🚀 Centro de Recursos: PAES M1</div>
        <div style="text-align: right;">
            <div style="font-size: 12px; opacity: 0.9;">⏰ Hora Actual (Chile)</div>
            <div style="font-size: 20px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. BARRA ROJA (Cuenta Regresiva)
st.markdown(f"""
    <div style="background-color: #cc0000; padding: 20px; color: white; height: 100px; display: flex; justify-content: space-around; align-items: center; border-bottom: 2px solid #eeeeee;">
        <div style="font-size: 18px; font-weight: bold;">⏳ Días: {faltan.days}</div>
        <div style="font-size: 18px; font-weight: bold;">Horas: {faltan.seconds // 3600}</div>
        <div style="font-size: 18px; font-weight: bold;">Minutos: {(faltan.seconds // 60) % 60}</div>
    </div>
    """, unsafe_allow_html=True)

# 3. BARRA BLANCA (Navegación)
# Primero creamos el contenedor visual blanco
st.markdown("""
    <div style="background-color: white; padding: 0px; border-radius: 0 0 10px 10px; height: 100px; border: 1px solid #dddddd; display: flex; align-items: center; justify-content: center; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
    </div>
    """, unsafe_allow_html=True)

# Usamos un truco de CSS negativo para meter los botones reales de Streamlit "dentro" del espacio de la barra blanca
st.markdown('<style>div.row-widget.stButton {text-align:center;}</style>', unsafe_allow_html=True)
cols = st.columns(4)
with cols[0]:
    if st.button("🔢 Números", use_container_width=True): st.session_state.eje_actual = "🔢 Números"
with cols[1]:
    if st.button("📉 Álgebra", use_container_width=True): st.session_state.eje_actual = "📉 Álgebra"
with cols[2]:
    if st.button("📐 Geometría", use_container_width=True): st.session_state.eje_actual = "📐 Geometría"
with cols[3]:
    if st.button("📊 Estadística", use_container_width=True): st.session_state.eje_actual = "📊 Estadística"

st.write("---")

# --- LÓGICA DE CONTENIDO ---
eje = st.session_state.eje_actual

if eje == "🔢 Números":
    st.header(eje)
    st.write("Aquí encontrarás recursos sobre conjuntos numéricos, potencias y porcentajes.")

elif eje == "📉 Álgebra":
    st.markdown("<h1 style='color: blue;'>Eje Álgebra</h1>", unsafe_allow_html=True)
    st.write("Contenidos de expresiones algebraicas, ecuaciones y funciones.")
    st.info("Típ: Anota: tip ... Las funciones son el corazón de la PAES.")

elif eje == "📐 Geometría":
    st.header(eje)
    st.write("Recursos de figuras 2D, 3D y transformaciones isométricas.")

elif eje == "📊 Estadística":
    st.header(eje)
    st.write("Análisis de datos, medidas de tendencia central y probabilidades.")
