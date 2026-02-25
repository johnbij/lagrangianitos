
import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Dashboard de Seba", page_icon="🚀")

# --- PRESENTACIÓN ---
st.title("Hola, bienvenidos a la página de Lagrangianitos 👋")
st.markdown("""
### Estudiante de Ingeniería
Bienvenido a mi espacio de datos. Soy estudiante de ingeniería y este dashboard
es parte de mi proyecto de libro digital.
""" )

st.divider()

# --- DASHBOARD DE TIEMPO ---
st.header("⏰ Reloj Global")
st.write("Selecciona una zona horaria para ver la hora exacta:")

# Selección de Zona Horaria
timezone = st.selectbox("Zona horaria:", pytz.all_timezones, index=pytz.all_timezones.index('America/Santiago'))

# Obtener datos
now = datetime.now(pytz.timezone(timezone))
fecha_actual = now.strftime("%d/%m/%Y")
hora_actual = now.strftime("%H:%M:%S")

# Mostrar en métricas
col1, col2 = st.columns(2)
col1.metric(label="Fecha Actual", value=fecha_actual)
col2.metric(label="Hora Local", value=hora_actual)

st.divider()

# Típ: Esto ayuda a que el usuario sepa qué hacer
st.info("**Típ**: Refresca la página para ver los cambios en el código que subas a GitHub.")
