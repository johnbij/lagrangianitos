import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import pytz
from datetime import datetime

# Evita errores de renderizado
matplotlib.use('Agg')

st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")

# --- EL FIX MAESTRO PARA CELULARES ---
st.markdown("""
    <style>
    /* Forza a que las columnas NO se apilen hacia abajo en celulares */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: center !important;
    }
    
    /* Ajusta el tamaño de los botones para que quepan todos en la pantalla del celu */
    [data-testid="stHorizontalBlock"] .stButton > button {
        width: 100% !important;
        padding: 5px 2px !important;
        font-size: 14px !important;
        min-height: 45px !important;
    }

    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; font-weight: bold; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; font-weight: bold; }
    .clase-box { background-color: white; padding: 20px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    </style>
    """, unsafe_allow_html=True)

# Estados de navegación
if 'eje' not in st.session_state: st.session_state.eje = None
if 'clase' not in st.session_state: st.session_state.clase = None

# --- HEADER ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 Lagrangianitos PAES M1</div>', unsafe_allow_html=True)
st.markdown(f'<div class="header-rojo">⏳ Días: 108 | Hrs: 20</div>', unsafe_allow_html=True)

st.write("")

# --- NAVEGACIÓN (FORZADA HORIZONTAL) ---
cols = st.columns(5)
if cols[0].button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if cols[1].button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()
if cols[2].button("A"): st.session_state.eje = "Álgebra"; st.rerun()
if cols[3].button("G"): st.session_state.eje = "Geometría"; st.rerun()
if cols[4].button("D"): st.session_state.eje = "Datos"; st.rerun()

st.divider()

# --- LÓGICA DE CONTENIDO ---
if st.session_state.eje == "Números":
    st.markdown("### 🔢 Eje Números")
    # Sub-ejes en horizontal (radio button es más estable en móvil)
    sub = st.radio("Subejes:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    
    if sub == "Conjuntos":
        # Botones de clase también forzados en horizontal
        c1, c2 = st.columns(2)
        if c1.button("📘 N01"): st.session_state.clase = "N01"
        if c2.button("📘 N02"): st.session_state.clase = "N02"

# --- RENDER DE LAS CLASES (TEXTO ÍNTEGRO) ---
if st.session_state.clase == "N01":
    st.markdown('<div class="clase-box"><h1>N01: Teoría de Conjuntos</h1><p>Tu contenido aquí...</p></div>', unsafe_allow_html=True)
elif st.session_state.clase == "N02":
    st.markdown('<div class="clase-box"><h1>N02: Números Naturales</h1><p>Tu contenido aquí...</p></div>', unsafe_allow_html=True)
    
