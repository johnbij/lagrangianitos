import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import pytz
import time
from datetime import datetime

matplotlib.use('Agg')

# --- GRÁFICOS ---
def graficar_inclusion():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.add_patch(plt.Rectangle((0, 0), 10, 8, color='#f0f0f0', ec='black', lw=2))
    ax.add_patch(plt.Circle((5, 4), 3, color='#3498db', alpha=0.3, ec='blue', lw=2))
    ax.add_patch(plt.Circle((5, 4), 1.2, color='#2980b9', alpha=0.8, ec='navy', lw=2))
    ax.set_xlim(-1, 11); ax.set_ylim(-1, 9); ax.axis('off')
    st.pyplot(fig)

# --- CLASES (Pega aquí tu contenido original) ---
def mostrar_clase_n01():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # PEGA AQUÍ TODO EL TEXTO DE LA CLASE N01 (CONJUNTOS)
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    st.markdown("""# AQUÍ VA TU TEXTO ORIGINAL N01""")
    graficar_inclusion() # El gráfico se queda donde tú lo pongas
    st.markdown('</div>', unsafe_allow_html=True)

def mostrar_clase_n02():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # PEGA AQUÍ TODO EL TEXTO DE LA CLASE N02 (NATURALES)
    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    st.markdown("""# AQUÍ VA TU TEXTO ORIGINAL N02""")
    st.markdown('</div>', unsafe_allow_html=True)

# --- INTERFAZ (Tu diseño original de las fotos) ---
st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")
st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de navegación (Corregida sin fantasmas)
if 'eje' not in st.session_state: st.session_state.eje = None
if 'clase' not in st.session_state: st.session_state.clase = None

# Header y Botones
cols = st.columns(5)
if cols[0].button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if cols[1].button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()

if st.session_state.eje == "Números":
    sub = st.radio("Subejes:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    if sub == "Conjuntos":
        if st.button("📖 N01"): st.session_state.clase = "N01"
        if st.button("📖 N02"): st.session_state.clase = "N02"

if st.session_state.clase == "N01": mostrar_clase_n01()
elif st.session_state.clase == "N02": mostrar_clase_n02()
