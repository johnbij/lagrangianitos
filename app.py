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
# :::: 2. ESTILOS CSS (DISEÑO DE LA CASA) :::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* Barras superiores fijas */
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* NAVEGACIÓN RÁPIDA: Forzar fila horizontal y botones robustos */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: center !important;
        gap: 8px !important;
    }
    
    [data-testid="stHorizontalBlock"] > div {
        width: auto !important;
        min-width: 55px !important; /* Evita que se vean flacos */
        flex: 1 1 auto !important;
    }

    [data-testid="stHorizontalBlock"] button {
        min-height: 55px !important; 
        padding: 5px !important;
        font-size: 18px !important; /* Letra grande para N A G D */
        font-weight: bold !important;
        border-radius: 10px !important;
    }

    /* BOTONES DE CATEGORÍAS: Verticales y grandes */
    .cat-container div.stButton > button { 
        min-height: 80px !important; 
        border-radius: 12px !important; 
        margin-bottom: 12px !important;
        width: 100% !important;
        font-size: 16px !important;
        display: block !important;
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
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    # ::: Render de Cabeceras :::
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    
    dias = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    horas = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    st.write("") 

    # ::: PANTALLA DE INICIO (4 EJES) :::
    if st.session_state.eje_actual is None:
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números\nConjuntos y operatoria", key="m_n", use_container_width=True):
            st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra\nFunciones y más", key="m_a", use_container_width=True):
            st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría\nÁreas y Volúmenes", key="m_g", use_container_width=True):
            st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if c4.button("📊 Datos y Azar\nProbabilidad y Estadística", key="m_d", use_container_width=True):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

    # ::: NAVEGACIÓN INTERNA (🏠 N A G D) :::
    else:
        n1, n2, n3, n4, n5 = st.columns(5)
        
        if n1.button("🏠", key="nav_h"):
            st.session_state.eje_actual = None; st.session_state.sub_seccion_actual = None; st.rerun()
        if n2.button("N", key="nav_n"):
            st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n3.button("A", key="nav_a"):
            st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n4.button("G", key="nav_g"):
            st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n5.button("D", key="nav_d"):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        # ::: CONTENIDO EJE NÚMEROS :::
        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Categorías de Números")
                
                st.markdown('<div class="cat-container">', unsafe_allow_html=True)
                if st.button("📦 Conjuntos Numéricos (N01)", key="cat_n01"):
                    st.session_state.sub_seccion_actual = "N01"; st.rerun()
                if st.button("➕ Operatoria", key="cat_op"): pass
                if st.button("📝 Ejercitación", key="cat_ej"): pass
                st.markdown('</div>', unsafe_allow_html=True)
            
            elif st.session_state.sub_seccion_actual == "N01":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("# <span style='color:darkblue'>N01: Teoría de Conjuntos</span>", unsafe_allow_html=True)
                st.write("Bienvenido al lenguaje maestro...")
                st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.header(st.session_state.eje_actual)
            st.info("Contenido en desarrollo.")

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca")
    
