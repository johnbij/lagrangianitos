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
    st.write("Típ: El orden en los ejes es clave.")

# --- CUERPO PRINCIPAL (ESTILO BANDERA) ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)

# 1. BARRA AZUL (Título y Reloj)
st.markdown(f"""
    <div style="background-color: #3b71ca; padding: 15px; border-radius: 10px 10px 0 0; color: white; border-bottom: 2px solid white;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 26px; font-weight: bold;">🚀 Centro de Recursos: PAES M1</div>
            <div style="text-align: right;">
                <div style="font-size: 11px; opacity: 0.9;">⏰ Hora Actual (Chile)</div>
                <div style="font-size: 20px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. BARRA ROJA (Cuenta Regresiva)
fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
faltan = fecha_paes - ahora
st.markdown(f"""
    <div style="background-color: #cc0000; padding: 12px; color: white; border-bottom: 2px solid #eeeeee;">
        <div style="display: flex; justify-content: space-around; text-align: center; align-items: center; font-size: 16px; font-weight: bold;">
            <div>⏳ PAES de Invierno: {faltan.days} días</div>
            <div>{faltan.seconds // 3600} Horas</div>
            <div>{(faltan.seconds // 60) % 60} Minutos</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. BARRA BLANCA (Navegación por Ejes)
st.markdown("""
    <div style="background-color: white; padding: 5px 15px; border-radius: 0 0 10px 10px; border: 1px solid #dddddd; box-shadow: 2px 2px 5px rgba(0,0,0,0.05);">
        <p style="margin: 5px 0; font-size: 12px; color: #666; font-weight: bold;">Selecciona tu eje de estudio:</p>
    </div>
    """, unsafe_allow_html=True)

# Botones de navegación dentro de la lógica de Streamlit (aparecen justo debajo de la franja blanca)
col1, col2, col3, col4 = st.columns(4)
if col1.button("🔢 Números"): st.session_state.eje_actual = "🔢 Números"
if col2.button("📉 Álgebra"): st.session_state.eje_actual = "📉 Álgebra"
if col3.button("📐 Geometría"): st.session_state.eje_actual = "📐 Geometría"
if col4.button("📊 Estadística"): st.session_state.eje_actual = "📊 Estadística"

st.divider()

# --- MOSTRAR CONTENIDO SEGÚN EL BOTÓN PRESIONADO ---
eje = st.session_state.eje_actual

if eje == "🔢 Números":
    st.header(eje)
    st.write("Contenidos de conjuntos numéricos y porcentajes.")

elif eje == "📉 Álgebra":
    st.markdown("<h1 style='color: blue;'>Eje Álgebra</h1>", unsafe_allow_html=True)
    st.write("Contenidos de expresiones y funciones.")
    st.info("Típ: Anota: tip ... El lenguaje algebraico es la base de la prueba.")

elif eje == "📐 Geometría":
    st.header(eje)
    st.write("Teoremas de Pitágoras, Tales y transformaciones.")

elif eje == "📊 Estadística":
    st.header(eje)
    st.write("Medidas de tendencia central y probabilidades.")
