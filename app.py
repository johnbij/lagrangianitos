import streamlit as st
from datetime import datetime
import pytz

# Configuración de la página
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

# --- ESTADO DE NAVEGACIÓN ---
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = "🔢 Números"

# --- INYECCIÓN DE CSS PARA LA NAVEGACIÓN ---
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        background-color: white !important;
        padding: 15px !important;
        border: 1px solid #dddddd !important;
        border-radius: 0 0 15px 15px !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.05) !important;
    }
    .stButton > button {
        border-radius: 8px !important;
        border: 1px solid #3b71ca !important;
        color: #3b71ca !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (RESTAURADA CON LINKS) ---
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/blue-rocket-icon-png-17.png", width=100)
    st.title("Perfil")
    st.markdown('''
**Seba**
*Estudiante de Ingeniería*

**Redes Sociales:**
* [📸 Instagram: @lagrangianitos](https://instagram.com/lagrangianitos)

**Proyectos:**
- Libro Digital PAES M1 📚
- Dashboard de Datos 📊
''')
    st.divider()
    st.write("Típ: El orden en los ejes es clave para un buen puntaje.")

# --- DISEÑO DE BANDERAS (AZUL - ROJO - BLANCO) ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
faltan = fecha_paes - ahora

# 1. BARRA AZUL
st.markdown(f"""
    <div style="background-color: #3b71ca; padding: 20px; border-radius: 15px 15px 0 0; color: white; height: 100px; display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid white;">
        <div style="font-size: 26px; font-weight: bold;">🚀 Centro de Recursos: PAES M1</div>
        <div style="text-align: right;">
            <div style="font-size: 11px; opacity: 0.9;">⏰ Hora Actual</div>
            <div style="font-size: 20px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. BARRA ROJA
st.markdown(f"""
    <div style="background-color: #cc0000; padding: 20px; color: white; height: 100px; display: flex; justify-content: space-around; align-items: center; border-bottom: 1px solid white;">
        <div style="font-size: 18px; font-weight: bold;">⏳ Días: {faltan.days}</div>
        <div style="font-size: 18px; font-weight: bold;">Horas: {faltan.seconds // 3600}</div>
        <div style="font-size: 18px; font-weight: bold;">Minutos: {(faltan.seconds // 60) % 60}</div>
    </div>
    """, unsafe_allow_html=True)

# 3. BARRA BLANCA (Navegación)
cols = st.columns(4)
if cols[0].button("🔢 Números", use_container_width=True): st.session_state.eje_actual = "🔢 Números"
if cols[1].button("📉 Álgebra", use_container_width=True): st.session_state.eje_actual = "📉 Álgebra"
if cols[2].button("📐 Geometría", use_container_width=True): st.session_state.eje_actual = "📐 Geometría"
if cols[3].button("📊 Estadística", use_container_width=True): st.session_state.eje_actual = "📊 Estadística"

st.write("---")

# --- LÓGICA DE CONTENIDO ---
eje = st.session_state.eje_actual

if eje == "📉 Álgebra":
    st.header("📉 Álgebra")
    st.write("Contenidos de expresiones algebraicas, ecuaciones y funciones.")

elif eje == "🔢 Números":
    st.header("🔢 Números")
    st.write("Contenidos de potencias, raíces y porcentajes.")

elif eje == "📐 Geometría":
    st.header("📐 Geometría")
    st.write("Contenidos de geometría plana y espacial.")

elif eje == "📊 Estadística":
    st.header("📊 Estadística")
    st.write("Análisis de datos y probabilidad.")
