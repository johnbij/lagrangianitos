
import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

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
    st.write("Tip: El orden en los ejes es clave para un buen puntaje.")

# --- CUERPO PRINCIPAL ---
st.title("🚀 Centro de Recursos: PAES M1")

# Definición de las 4 pestañas solicitadas
tab1, tab2, tab3, tab4 = st.tabs(["🔢 Números", "📉 Álgebra", "📐 Geometría", "📊 Estadística y Probabilidad"])

with tab1:
    st.header("Eje: Números")
    st.write("Aquí encontrarás recursos sobre conjuntos numéricos, potencias y porcentajes.")
    # Espacio para futuro contenido
    st.info("Tip: Asegúrate de dominar bien la operatoria básica antes de pasar a álgebra.")

with tab2:
    # Aplicando tu preferencia: Título en azul para el Eje Álgebra
    st.markdown("<h1 style='color: blue;'>Eje Álgebra</h1>", unsafe_allow_html=True)
    st.write("Contenidos de expresiones algebraicas, ecuaciones y funciones.")
    st.info("Tip: Anota: tip ... las funciones son el corazón de la PAES.")

with tab3:
    st.header("Eje: Geometría")
    st.write("Recursos de figuras 2D, 3D y transformaciones isométricas.")

with tab4:
    st.header("Eje: Estadística y Probabilidad")
    st.write("Análisis de datos, medidas de tendencia central y probabilidades.")
    
    st.divider()
    # Mantenemos el contador PAES en esta sección o al final como prefieras
    st.subheader("⏳ Cuenta regresiva: PAES de Invierno")
    zona_cl = pytz.timezone('America/Santiago')
    fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    ahora = datetime.now(zona_cl)
    faltan = fecha_paes - ahora
    
    if faltan.days > 0:
        c1, c2, c3 = st.columns(3)
        c1.metric("Días", faltan.days)
        c2.metric("Horas", faltan.seconds // 3600)
        c3.metric("Minutos", (faltan.seconds // 60) % 60)
    else:
        st.success("¡Llegó el día!")

st.divider()
# Reloj Global al final de la página
with st.expander("🌍 Ver Reloj Global"):
    tz_name = st.selectbox("Zona horaria:", pytz.all_timezones, index=pytz.all_timezones.index('America/Santiago'))
    now_g = datetime.now(pytz.timezone(tz_name))
    st.metric(f"Hora en {tz_name}", now_g.strftime("%H:%M:%S"))
