import streamlit as st
from datetime import datetime
import pytz

# Configuración de la página
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

# --- BARRA LATERAL (SIDEBAR) ---
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

# --- ENCABEZADO COMPACTO (TÍTULO + RELOJ) ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)

# Usamos HTML/CSS para crear la franja azul con columnas internas
st.markdown(f"""
    <div style="background-color: #3b71ca; padding: 15px; border-radius: 10px; margin-bottom: 20px; color: white;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="font-size: 28px; font-weight: bold;">
                🚀 Centro de Recursos: PAES M1
            </div>
            <div style="text-align: right;">
                <div style="font-size: 14px; opacity: 0.9;">⏰ Hora Actual (Chile)</div>
                <div style="font-size: 24px; font-weight: bold; font-family: monospace;">
                    {ahora.strftime("%H:%M:%S")}
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- CONTADOR PAES (DEBAJO DEL ENCABEZADO) ---
st.subheader("⏳ Cuenta regresiva: PAES de Invierno")
fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
faltan = fecha_paes - ahora

if faltan.days > 0:
    c1, c2, c3 = st.columns(3)
    c1.metric("Días", faltan.days)
    c2.metric("Horas", faltan.seconds // 3600)
    c3.metric("Minutos", (faltan.seconds // 60) % 60)
else:
    st.success("¡Llegó el día!")

st.divider()

# --- SISTEMA DE PESTAÑAS ---
tab1, tab2, tab3, tab4 = st.tabs(["🔢 Números", "📉 Álgebra", "📐 Geometría", "📊 Estadística"])

with tab1:
    st.header("Eje: Números")
    st.write("Contenidos de potencias, raíces y porcentajes.")

with tab2:
    st.markdown("<h1 style='color: blue;'>Eje Álgebra</h1>", unsafe_allow_html=True)
    st.write("Ecuaciones, funciones y sistemas lineales.")
    st.info("Típ: Anota: tip ... El lenguaje algebraico es la base de toda la prueba.")

with tab3:
    st.header("Eje: Geometría")
    st.write("Teoremas, áreas, volúmenes y vectores.")

with tab4:
    st.header("Eje: Estadística y Probabilidad")
    st.write("Análisis de datos, medidas de tendencia central y probabilidades.")
