import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import pytz
import time
from datetime import datetime

# Bloquea el renderizado para que funcione en la nube
matplotlib.use('Agg')

st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")

# --- CSS PARA FORZAR EL DISEÑO ---
st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; font-weight: bold; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; font-weight: bold; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 35px; font-weight: bold; color: #3b71ca; text-align: center; width: 100%; display: block; }
    
    /* FUERZA QUE LOS BOTONES NO SE VAYAN HACIA ABAJO */
    [data-testid="stHorizontalBlock"] {
        align-items: center;
    }
    button {
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Estados
if 'eje' not in st.session_state: st.session_state.eje = None
if 'clase' not in st.session_state: st.session_state.clase = None

# --- HEADER (IGUAL A TU FOTO) ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 Lagrangianitos. Tus recursos PAES M1 | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="header-rojo">⏳ Días: 108 | Hrs: 20</div>', unsafe_allow_html=True)

# --- CRONÓMETRO ---
with st.container(border=True):
    c_btn, c_rel = st.columns([1, 3])
    c_btn.button("▶️ Iniciar/Parar")
    c_rel.markdown('<span class="crono-digital">00:00</span>', unsafe_allow_html=True)

# --- NAVEGACIÓN PRINCIPAL (FILA HORIZONTAL) ---
st.write("")
nav = st.columns(5) # Esto obliga a que los 5 botones estén en la misma línea
if nav[0].button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if nav[1].button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()
if nav[2].button("A"): st.session_state.eje = "Álgebra"; st.rerun()
if nav[3].button("G"): st.session_state.eje = "Geometría"; st.rerun()
if nav[4].button("D"): st.session_state.eje = "Datos"; st.rerun()

st.divider()

# --- LÓGICA DE EJES ---
if st.session_state.eje == "Números":
    st.markdown("### 🔢 Eje Números")
    sub = st.radio("Subejes:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    
    if sub == "Conjuntos":
        # BOTONES DE CLASE EN FILA
        clase_cols = st.columns(2)
        if clase_cols[0].button("📘 Teoría N01"): st.session_state.clase = "N01"
        if clase_cols[1].button("📘 Naturales N02"): st.session_state.clase = "N02"

# --- ÁREA DE CLASE ---
if st.session_state.clase == "N01":
    st.markdown('<div class="clase-box"><h1>N01: Teoría de Conjuntos</h1><p>Contenido completo...</p></div>', unsafe_allow_html=True)
elif st.session_state.clase == "N02":
    st.markdown('<div class="clase-box"><h1>N02: Los Números Naturales</h1><p>Contenido completo...</p></div>', unsafe_allow_html=True)
    
