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
    /* Barras superiores */
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* NAVEGACIÓN RÁPIDA (🏠 N A G D) */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 4px !important;
    }
    
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    [data-testid="stHorizontalBlock"] button {
        width: 100% !important;
        min-height: 55px !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }

    /* BOTONES DE CATEGORÍAS (Teoría y Ejercitación) */
    .cat-container div.stButton > button { 
        min-height: 85px !important; 
        border-radius: 15px !important; 
        margin-bottom: 15px !important;
        width: 100% !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        text-align: left !important;
        padding-left: 20px !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
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
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    
    dias = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    horas = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    st.write("") 

    # ::: PANTALLA DE INICIO (4 EJES) :::
    if st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
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
        n_cols = st.columns(5)
        if n_cols[0].button("🏠", key="n_h"):
            st.session_state.eje_actual = None; st.session_state.sub_seccion_actual = None; st.rerun()
        if n_cols[1].button("N", key="n_n"):
            st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n_cols[2].button("A", key="n_a"):
            st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n_cols[3].button("G", key="n_g"):
            st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n_cols[4].button("D", key="n_d"):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        # ::: CONTENIDO DINÁMICO POR EJE :::
        st.markdown(f"## {st.session_state.eje_actual}")

        if st.session_state.sub_seccion_actual is None:
            # Botones de Teoría y Ejercitación para el eje seleccionado
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            
            if st.button("📘 Teoría y Conceptos", key="btn_teoria"):
                st.session_state.sub_seccion_actual = "Teoria"; st.rerun()
                
            if st.button("📝 Ejercitación y Práctica", key="btn_ejercitacion"):
                st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
                
            st.markdown('</div>', unsafe_allow_html=True)
            st.info("🚀 Selecciona una modalidad para comenzar.")
            
        else:
            # Vista cuando ya seleccionaste Teoría o Ejercitación
            if st.session_state.sub_seccion_actual == "Teoria":
                st.subheader(f"📚 Teoría: {st.session_state.eje_actual}")
                st.info("Aquí irán las clases y explicaciones paso a paso.")
            else:
                st.subheader(f"📝 Ejercitación: {st.session_state.eje_actual}")
                st.info("Aquí irán los cuestionarios y pautas explicativas.")
            
            if st.button("🔙 Volver a opciones"):
                st.session_state.sub_seccion_actual = None; st.rerun()

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos")
