import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import pytz
import time
from datetime import datetime

# Bloqueo de renderizado para evitar errores en la nube
matplotlib.use('Agg')

st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")

# --- CSS SEGURO (Solo lo estético, sin romper columnas) ---
st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 20px; border-radius: 15px 15px 0 0; color: white; text-align: center; font-size: 20px; font-weight: bold; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; font-weight: bold; }
    .clase-box { background-color: white; padding: 25px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; margin-top: 20px; }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; color: #3b71ca; }
    
    /* Esto ayuda a que en el celu los botones no se vean gigantes */
    .stButton button { width: 100%; min-height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# Estados de la sesión
if 'eje' not in st.session_state: st.session_state.eje = None
if 'clase' not in st.session_state: st.session_state.clase = None

# --- HEADER (Restaurado como la foto 14:28) ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 Lagrangianitos. Tus recursos PAES M1</div>', unsafe_allow_html=True)
st.markdown(f'<div class="header-rojo"><span>⏳ Días: 108</span><span>Hrs: 20</span></div>', unsafe_allow_html=True)

# --- NAVEGACIÓN PRINCIPAL ---
# Usamos columnas estándar de Streamlit para que sea estable
st.write("")
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if c2.button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()
if c3.button("A"): st.session_state.eje = "Álgebra"; st.rerun()
if c4.button("G"): st.session_state.eje = "Geometría"; st.rerun()
if c5.button("D"): st.session_state.eje = "Datos"; st.rerun()

st.divider()

# --- CRONÓMETRO (En su caja original) ---
with st.container(border=True):
    col_izq, col_der = st.columns([1, 1])
    col_izq.button("▶️ Parar/Iniciar")
    col_der.markdown('<div class="crono-digital">01:16</div>', unsafe_allow_html=True)

# --- LÓGICA DE CONTENIDO ---
if st.session_state.eje == "Números":
    st.markdown("## 🔢 Números")
    sub = st.radio("Subejes:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    
    if sub == "Conjuntos":
        col_n1, col_n2 = st.columns(2)
        if col_n1.button("📘 Teoría (N01)"): st.session_state.clase = "N01"
        if col_n2.button("📘 Naturales (N02)"): st.session_state.clase = "N02"

# Mostrar la clase seleccionada
if st.session_state.clase == "N01":
    st.markdown('<div class="clase-box"><h1>N01: Teoría de Conjuntos</h1><p>Tu texto aquí...</p></div>', unsafe_allow_html=True)
elif st.session_state.clase == "N02":
    st.markdown('<div class="clase-box"><h1>N02: Números Naturales</h1><p>Tu texto aquí...</p></div>', unsafe_allow_html=True)
    
