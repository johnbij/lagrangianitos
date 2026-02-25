
import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Lagrangianitos Dash", page_icon="🚀")

# --- PRESENTACIÓN ---
st.title("Hola, bienvenidos a la página de Lagrangianitos 👋")
st.markdown("Soy estudiante de ingeniería en la universidad y estoy creando mi proyecto **Libro Digital PAES M1**.")

st.divider()

# --- CONTADOR PAES DE INVIERNO ---
st.header("⏳ Cuenta regresiva: PAES de Invierno")

# Configurar fecha objetivo: 15 de junio de 2026
zona_cl = pytz.timezone('America/Santiago')
fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
ahora = datetime.now(zona_cl)

# Calcular diferencia
faltan = fecha_paes - ahora

if faltan.days > 0:
    col1, col2, col3 = st.columns(3)
    col1.metric("Días", faltan.days)
    col2.metric("Horas", faltan.seconds // 3600)
    col3.metric("Minutos", (faltan.seconds // 60) % 60)
    st.write(f"Faltan exactamente **{faltan.days} días** para el Lunes 15 de junio de 2026.")
else:
    st.success("¡Llegó el día de la PAES! ¡Mucho éxito!")

st.divider()

# --- RELOJ GLOBAL ---
st.header("⏰ Reloj Global")
timezone_name = st.selectbox("Zona horaria:", pytz.all_timezones, index=pytz.all_timezones.index('America/Santiago'))

now_global = datetime.now(pytz.timezone(timezone_name))
c1, c2 = st.columns(2)
c1.metric(label="Fecha Actual", value=now_global.strftime("%d/%m/%Y"))
c2.metric(label="Hora Local", value=now_global.strftime("%H:%M:%S"))

st.divider()
st.info("Típ: Recuerda que la PAES de Invierno es una gran oportunidad para asegurar tu puntaje temprano.")
