
import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Lagrangianitos Dash", page_icon="🚀")

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/blue-rocket-icon-png-17.png", width=100)
    st.title("Perfil")
    st.markdown("""
    **Seba**
    *Estudiante de Ingeniería*
    
    **Redes Sociales:**
    * [📸 Instagram: @lagrangianitos](https://instagram.com/lagrangianitos)
    
    **Proyectos:**
    - Libro Digital PAES M1 📚
    - Dashboard de Datos 📊
    """)
    st.divider()
    st.write("Típ: Estudia al menos 30 min al día de álgebra para asegurar la M1.")

# --- CUERPO PRINCIPAL ---
st.title("Hola, bienvenidos a la página de Lagrangianitos 👋")
st.write("Estás en el centro de recursos para la PAES M1 y herramientas de ingeniería.")

st.divider()

# --- CONTADOR PAES DE INVIERNO ---
st.header("⏳ Cuenta regresiva: PAES de Invierno")

# Configurar fecha objetivo: 15 de junio de 2026
zona_cl = pytz.timezone('America/Santiago')
fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
ahora = datetime.now(zona_cl)

faltan = fecha_paes - ahora

if faltan.days > 0:
    col1, col2, col3 = st.columns(3)
    col1.metric("Días", faltan.days)
    col2.metric("Horas", faltan.seconds // 3600)
    col3.metric("Minutos", (faltan.seconds // 60) % 60)
    st.write(f"Faltan **{faltan.days} días** para el inicio de la prueba.")
else:
    st.success("¡Llegó el día!")

st.divider()

# --- RELOJ GLOBAL ---
st.header("⏰ Reloj Global")
timezone_name = st.selectbox("Cambia la zona horaria para comparar:", pytz.all_timezones, index=pytz.all_timezones.index('America/Santiago'))

now_global = datetime.now(pytz.timezone(timezone_name))
c1, c2 = st.columns(2)
c1.metric(label="Fecha Actual", value=now_global.strftime("%d/%m/%Y"))
c2.metric(label="Hora Local", value=now_global.strftime("%H:%M:%S"))
