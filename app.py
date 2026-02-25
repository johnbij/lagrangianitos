import streamlit as st
from datetime import datetime
import pytz

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS (UI/UX) :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* Barras superiores fijas */
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* FORZAR FILA HORIZONTAL PARA LOS 5 BOTONES EN MÓVIL */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: center !important;
        justify-content: space-between !important;
    }
    
    [data-testid="stHorizontalBlock"] .stButton > button {
        width: 100% !important;
        min-height: 45px !important;
        padding: 2px !important;
        font-size: 16px !important;
    }

    /* Botones de categorías (grandes y verticales) */
    .cat-btn div.stButton > button { 
        min-height: 80px !important; 
        border-radius: 12px !important; 
        margin-bottom: 10px;
    }
    
    .clase-box { max-width: 900px; margin: 0 auto; padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    
    dias = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    horas = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    st.write("") 

    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # ::: PANTALLA INICIAL (LOS 4 EJES) :::::::::::::::::::::::::::::::::::::::
    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    if st.session_state.eje_actual is None:
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números\nConjuntos y operatoria", key="main_n", use_container_width=True):
            st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra\nFunciones y más", key="main_a", use_container_width=True):
            st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría\nÁreas y Volúmenes", key="main_g", use_container_width=True):
            st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if c4.button("📊 Datos y Azar\nProbabilidad y Estadística", key="main_d", use_container_width=True):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # ::: BARRA DE NAVEGACIÓN RÁPIDA (FILA DE 5) ::::::::::::::::::::::::::::::
    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else:
        # Esto ahora se mantendrá horizontal gracias al CSS de arriba
        nav_cols = st.columns(5)
        
        if nav_cols[0].button("🏠", key="nav_h"):
            st.session_state.eje_actual = None
            st.session_state.sub_seccion_actual = None; st.rerun()
        
        if nav_cols[1].button("N", key="nav_n"):
            st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_seccion_actual = None; st.rerun()
            
        if nav_cols[2].button("A", key="nav_a"):
            st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_seccion_actual = None; st.rerun()
            
        if nav_cols[3].button("G", key="nav_g"):
            st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_seccion_actual = None; st.rerun()
            
        if nav_cols[4].button("D", key="nav_d"):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        # ::: SECCIÓN NÚMEROS :::::::::::::::::::::::::::::::::::::::::::::::::
        # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Categorías de Números")
                
                # Usamos un contenedor con clase propia para que NO hereden el estilo horizontal
                st.markdown('<div class="cat-btn">', unsafe_allow_html=True)
                if st.button("📦 Conjuntos Numéricos (N01)", use_container_width=True):
                    st.session_state.sub_seccion_actual = "N01"; st.rerun()
                
                if st.button("➕ Operatoria", use_container_width=True): pass
                
                if st.button("📝 Ejercitación", use_container_width=True): pass
                st.markdown('</div>', unsafe_allow_html=True)
            
            # ::: CONTENIDO CLASE N01 :::::::::::::::::::::::::::::::::::::::::
            elif st.session_state.sub_seccion_actual == "N01":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("# <span style='color:darkblue'>N01: Teoría de Conjuntos</span>", unsafe_allow_html=True)
                st.write("Bienvenido al lenguaje maestro...")
                st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca")
    
