
import streamlit as st
from datetime import datetime
import pytz

# Configuración de la página
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🚀", layout="wide")

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    st.title("📌 Navegación")
    
    # Aquí pones tu link real de Instagram
    st.markdown("""
    ### 🔗 Mis Redes
    * [📸 Sígueme en Instagram](https://instagram.com/tu_usuario_aqui) 
    * [📚 Apuntes PAES M1](https://google.com)
    
    ---
    **Seba**
    *Estudiante de Ingeniería*
    """)
    
    st.divider()
    st.info("**Típ**: El éxito en la PAES M1 depende de la constancia, no de la velocidad.")

# --- CUERPO PRINCIPAL ---
st.title("🚀 Lagrangianitos: Centro de Recursos")

# Sistema de pestañas para organizar el contenido
tab1, tab2, tab3 = st.tabs(["🏠 Inicio", "📅 Contador PAES", "🌍 Reloj Global"])

with tab1:
    st.header("¡Bienvenidos!")
    st.write("Hola, soy Seba. Este es mi espacio donde comparto recursos para ingeniería y la PAES M1.")
    st.success("Explora las herramientas usando las pestañas de arriba.")

with tab2:
    st.header("⏳ Cuenta regresiva: PAES de Invierno")
    # Fecha: Lunes 15 de junio de 2026
    zona_cl = pytz.timezone('America/Santiago')
    fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    ahora = datetime.now(zona_cl)
    faltan = fecha_paes - ahora
    
    if faltan.days > 0:
        c1, c2, c3 = st.columns(3)
        c1.metric("Días restantes", faltan.days)
        c2.metric("Horas", faltan.seconds // 3600)
        c3.metric("Minutos", (faltan.seconds // 60) % 60)
    else:
        st.balloons()
        st.success("¡Llegó el gran día!")

with tab3:
    st.header("🌍 Reloj Mundial")
    tz_name = st.selectbox("Selecciona una zona horaria:", pytz.all_timezones, index=pytz.all_timezones.index('America/Santiago'))
    now = datetime.now(pytz.timezone(tz_name))
    st.metric(f"Hora en {tz_name}", now.strftime("%H:%M:%S"))
    st.write(f"Fecha: {now.strftime('%d/%m/%Y')}")
