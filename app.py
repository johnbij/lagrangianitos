import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import pytz
import time
from datetime import datetime

# Evita el error de 'ModuleNotFoundError' y de renderizado en la nube
matplotlib.use('Agg')

# --- CONFIGURACIÓN DE PÁGINA Y ESTILO (RESTAURADO) ---
st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; font-weight: bold; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; font-weight: bold; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 35px; font-weight: bold; color: #3b71ca; text-align: center; width: 100%; display: block; }
    
    /* ESTO ARREGLA LOS BOTONES PARA QUE NO VAYAN HACIA ABAJO */
    div[data-testid="stHorizontalBlock"] button {
        width: 100% !important;
        min-height: 55px !important;
        font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTADOS ---
if 'eje' not in st.session_state: st.session_state.eje = None
if 'clase' not in st.session_state: st.session_state.clase = None
if 'crono' not in st.session_state: st.session_state.crono = False

# --- HEADER ---
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 Lagrangianitos. Tus recursos PAES M1 | 📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="header-rojo">⏳ Días: 108 | Hrs: 20</div>', unsafe_allow_html=True)

# --- CRONÓMETRO ---
with st.container(border=True):
    col_btn, col_reloj = st.columns([1, 2])
    if col_btn.button("▶️ Iniciar/Parar"):
        st.session_state.crono = not st.session_state.crono
        if st.session_state.crono: st.session_state.t_0 = time.time()
        st.rerun()
    if st.session_state.crono:
        s = int(time.time() - st.session_state.t_0)
        col_reloj.markdown(f'<span class="crono-digital">{s//60:02d}:{s%60:02d}</span>', unsafe_allow_html=True)
    else:
        col_reloj.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

# --- NAVEGACIÓN (BOTONES EN FILA, NO HACIA ABAJO) ---
st.write("")
cols_nav = st.columns(5) # Esto fuerza a que sean 5 columnas en una misma fila
if cols_nav[0].button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if cols_nav[1].button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()
if cols_nav[2].button("A"): st.session_state.eje = "Álgebra"; st.rerun()
if cols_nav[3].button("G"): st.session_state.eje = "Geometría"; st.rerun()
if cols_nav[4].button("D"): st.session_state.eje = "Datos"; st.rerun()

st.divider()

# --- LÓGICA DE CONTENIDO ---
if st.session_state.eje == "Números":
    st.markdown("### 🔢 Eje Números")
    # Sub-ejes en horizontal
    sub = st.radio("Subejes:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    
    if sub == "Conjuntos":
        # Botones de clase en una misma fila
        c1, c2 = st.columns(2)
        if c1.button("📘 Teoría N01"): st.session_state.clase = "N01"
        if c2.button("📘 Naturales N02"): st.session_state.clase = "N02"

# --- RENDER DE CLASES ---
if st.session_state.clase == "N01":
    st.markdown('<div class="clase-box"><h1>N01: Teoría de Conjuntos</h1><p>Contenido completo aquí...</p></div>', unsafe_allow_html=True)
elif st.session_state.clase == "N02":
    st.markdown('<div class="clase-box"><h1>N02: Los Números Naturales</h1><p>Contenido completo aquí...</p></div>', unsafe_allow_html=True)

if st.session_state.crono:
    time.sleep(1)
    st.rerun()
    
