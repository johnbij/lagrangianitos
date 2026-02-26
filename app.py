import streamlit as st
from datetime import datetime
import pytz
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# Estados originales
if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None
if 'clase_seleccionada' not in st.session_state:
    st.session_state.clase_seleccionada = None

# NUEVOS ESTADOS PARA EL CRONÓMETRO MANUAL
if 'cronometro_activo' not in st.session_state:
    st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state:
    st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* Estilo para el Cronómetro Manual */
    .crono-container { 
        background-color: #f8f9fa; padding: 10px; border: 2px dashed #cc0000; 
        border-radius: 10px; text-align: center; margin-top: 5px;
    }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 24px; font-weight: bold; color: #cc0000; }

    [data-testid="stHorizontalBlock"] { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 4px !important; }
    [data-testid="stHorizontalBlock"] > div { flex: 1 1 0% !important; min-width: 0 !important; }
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; }

    .cat-container div.stButton > button { 
        min-height: 85px !important; border-radius: 15px !important; margin-bottom: 15px !important;
        width: 100% !important; font-size: 18px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important; box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
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
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días para PAES: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    # --- NUEVA SECCIÓN: CRONÓMETRO MANUAL ACTIVABLE ---
    st.write("")
    crono_col1, crono_col2 = st.columns([1, 3])

    with crono_col1:
        if not st.session_state.cronometro_activo:
            if st.button("⏱️ Iniciar Tiempo"):
                st.session_state.tiempo_inicio = time.time()
                st.session_state.cronometro_activo = True
                st.rerun()
        else:
            if st.button("🛑 Detener/Reset"):
                st.session_state.cronometro_activo = False
                st.session_state.tiempo_inicio = None
                st.rerun()

    with crono_col2:
        if st.session_state.cronometro_activo:
            tiempo_transcurrido = int(time.time() - st.session_state.tiempo_inicio)
            mins, segs = divmod(tiempo_transcurrido, 60)
            st.markdown(f'''
                <div class="crono-container">
                    <span style="color:#cc0000; font-weight:bold;">⏱️ CRONÓMETRO ACTIVO:</span>
                    <span class="crono-digital">{mins:02d}:{segs:02d}</span>
                </div>
            ''', unsafe_allow_html=True)

    st.write("---") 

    if st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números", key="m_n"): st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra", key="m_a"): st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría", key="m_g"): st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if c4.button("📊 Datos y Azar", key="m_d"): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

    else:
        n_cols = st.columns(5)
        if n_cols[0].button("🏠", key="n_h"): st.session_state.eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[1].button("N", key="n_n"): st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[2].button("A", key="n_a"): st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[3].button("G", key="n_g"): st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[4].button("D", key="n_d"): st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()

        st.write("")
        
        if st.session_state.sub_seccion_actual is None:
            st.markdown(f"## {st.session_state.eje_actual}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📘 Teoría y Conceptos", key="bt_t"): st.session_state.sub_seccion_actual = "Teoria"; st.rerun()
            if st.button("📝 Ejercitación y Práctica", key="bt_e"): st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.clase_seleccionada is None:
            st.subheader(f"📚 Clases de {st.session_state.eje_actual}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📖 N01: Teoría de Conjuntos", key="n01"): st.session_state.clase_seleccionada = "N01"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("🔙 Volver"): st.session_state.sub_seccion_actual = None; st.rerun()

        else:
            if st.session_state.clase_seleccionada == "N01":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("""
                # <span style="color:darkblue">N01: Teoría de Conjuntos</span>
                Aprender Teoría de Conjuntos es aprender a pensar con orden...
                """)
                st.markdown('</div>', unsafe_allow_html=True)
            
            if st.button("🔙 Volver al listado"): st.session_state.clase_seleccionada = None; st.rerun()
