import streamlit as st
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# Inicialización de estados para navegación profunda
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion' not in st.session_state:
    st.session_state.sub_seccion = None

# --- 2. INYECCIÓN DE CSS (TARJETAS PRO) ---
st.markdown("""
    <style>
    [data-testid="stHorizontalBlock"] {
        background-color: white !important;
        padding: 10px !important;
        border-radius: 0 0 15px 15px !important;
    }
    div.stButton > button {
        height: 100px !important;
        border-radius: 15px !important;
        background-color: white !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.05) !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        margin-bottom: 10px !important;
        color: #31333F !important;
    }
    div.stButton > button:hover {
        border-color: #3b71ca !important;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1) !important;
        transform: translateY(-2px) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería en FCFM Universidad de Chile*")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Típ: Selecciona una sub-sección para ver las clases específicas.")

# --- 4. LÓGICA DE NAVEGACIÓN ---
if menu == "🏠 Dashboard PAES":
    # --- CABECERAS (Dragón y Countdown) ---
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div style="background-color: #3b71ca; padding: 25px; border-radius: 15px 15px 0 0; color: white; position: relative; display: flex; align-items: center; justify-content: center; min-height: 100px;">
            <div style="font-size: 28px; font-weight: bold; text-align: center; padding: 0 120px; line-height: 1.2;">
                🐉 Lagrangianitos. Tus recursos PAES M1
            </div>
            <div style="position: absolute; right: 25px; text-align: right;">
                <div style="font-size: 14px; opacity: 0.9;">Santiago, Chile</div>
                <div style="font-size: 22px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    fecha_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    faltan = fecha_paes - ahora
    st.markdown(f"""
        <div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center;">
            <div style="font-size: 22px; font-weight: bold;">⏳ Días: {faltan.days}</div>
            <div style="font-size: 22px; font-weight: bold;">Hrs: {faltan.seconds // 3600}</div>
            <div style="font-size: 22px; font-weight: bold;">Min: {(faltan.seconds // 60) % 60}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # --- LÓGICA DE PANTALLAS ---
    if st.session_state.eje_actual is None:
        # PANTALLA 1: SELECCIÓN DE EJES
        st.subheader("📚 Selecciona un Eje Temático")
        ejes = {
            "🔢 Números": "Conjuntos, operatoria, potencias, raíces y razones.",
            "📉 Álgebra": "Operatoria algebraica y funciones",
            "📐 Geometría": "Teoremas, perímetros, áreas y volúmenes.",
            "📊 Datos": "Medidas de tendencia, tablas y azar."
        }
        for nombre, desc in ejes.items():
            if st.button(f"{nombre}\n{desc}", key=f"main_{nombre}", use_container_width=True):
                st.session_state.eje_actual = nombre
                st.rerun()

    elif st.session_state.eje_actual == "🔢 Números":
        # PANTALLA 2: SUB-SECCIONES DE NÚMEROS
        # Barra de navegación superior
        nav_cols = st.columns(5)
        if nav_cols[0].button("🏠 Inicio"):
            st.session_state.eje_actual = None
            st.session_state.sub_seccion = None
            st.rerun()
        
        st.header("🔢 Eje Números")
        
        # Solo mostramos los cuadraditos si no se ha elegido una sub-sección
        if st.session_state.sub_seccion is None:
            st.subheader("Selecciona una unidad:")
            sub1, sub2, sub3 = st.columns(3)
            with sub1:
                if st.button("📓 Conjuntos\nNuméricos", use_container_width=True):
                    st.session_state.sub_seccion = "Conjuntos"
                    st.rerun()
            with sub2:
                if st.button("➕ Operatoria", use_container_width=True):
                    st.session_state.sub_seccion = "Operatoria"
                    st.rerun()
            with sub3:
                if st.button("📝 Ejercitación", use_container_width=True):
                    st.session_state.sub_seccion = "Ejercitación"
                    st.rerun()
        else:
            # PANTALLA 3: CONTENIDO FINAL (AQUÍ IRÁ TU CLASE E02)
            st.button("⬅️ Volver a Unidades", on_click=lambda: st.session_state.update({"sub_seccion": None}))
            st.subheader(f"📍 {st.session_state.sub_seccion}")
            
            # Aquí es donde el mensaje de "desarrollo" desaparece y pondremos la materia real
            st.success(f"Cargando material de {st.session_state.sub_seccion}...")

    else:
        # Otros ejes (Álgebra, etc.)
        if st.button("⬅️ Volver al Inicio"):
            st.session_state.eje_actual = None
            st.rerun()
        st.header(st.session_state.eje_actual)
        st.info("Esta sección se configurará igual que Números próximamente.")

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos PDF")
