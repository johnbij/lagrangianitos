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
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    div.stButton > button { 
        min-height: 85px !important; 
        border-radius: 12px !important; 
        border: 1px solid #e0e0e0 !important; 
        color: #31333F !important;
        font-weight: bold !important;
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

    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # ::: PANTALLA DE LOS 4 EJES ::::::::::::::::::::::::::::::::::::::::::::::
    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    if st.session_state.eje_actual is None:
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números\nConjuntos y operatoria", key="btn_num", use_container_width=True):
            st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra\nFunciones y más", key="btn_alg", use_container_width=True):
            st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría\nÁreas y Volúmenes", key="btn_geo", use_container_width=True):
            st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if c4.button("📊 Datos y Azar\nProbabilidad y Estadística", key="btn_dat", use_container_width=True):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # ::: NAVEGACIÓN DENTRO DE NÚMEROS ::::::::::::::::::::::::::::::::::::::::
    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    else:
        if st.button("⬅️ Volver al Inicio", use_container_width=True):
            st.session_state.eje_actual = None
            st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Categorías de Números")
                
                # Botón 1: Conjuntos
                if st.button("📦 Conjuntos Numéricos (N01)", use_container_width=True):
                    st.session_state.sub_seccion_actual = "N01"; st.rerun()
                
                # Botón 2: Operatoria
                if st.button("➕ Operatoria", use_container_width=True): pass
                
                # Botón 3: Ejercitación (EL QUE FALTABA)
                if st.button("📝 Ejercitación", use_container_width=True): pass
            
            # ::: CLASE N01 :::::::::::::::::::::::::::::::::::::::::::::::::::
            elif st.session_state.sub_seccion_actual == "N01":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("""
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>
---
### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
... Contenido ...
""", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca")
    
