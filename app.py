import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import pytz
import time
from datetime import datetime

# Soluciona el error de la primera foto
matplotlib.use('Agg')

# --- FUNCIONES DE GRÁFICOS ---
def graficar_inclusion():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.add_patch(plt.Rectangle((0, 0), 10, 8, color='#f0f0f0', ec='black', lw=2))
    ax.add_patch(plt.Circle((5, 4), 3, color='#3498db', alpha=0.3, ec='blue', lw=2))
    ax.add_patch(plt.Circle((5, 4), 1.2, color='#2980b9', alpha=0.8, ec='navy', lw=2))
    ax.set_xlim(-1, 11); ax.set_ylim(-1, 9); ax.axis('off')
    st.pyplot(fig)

# --- CLASES COMPLETAS (RESTURADAS) ---
def mostrar_clase_n01():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""
    # N01: Teoría de Conjuntos - El Lenguaje Maestro
    ---
    ### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
    Aprender Teoría de Conjuntos es aprender a pensar con orden. No se trata solo de círculos y flechas, sino de la base misma de toda la matemática moderna.
    
    ### 🛡️ 2. El Mapa: Conceptos Fundamentales
    * **Conjunto:** Colección de objetos bien definidos.
    * **Elemento:** Los objetos que pertenecen al conjunto.
    
    ### 🛡️ 3. Representación Visual
    """)
    graficar_inclusion()
    st.markdown("""
    ### 🛡️ 4. Operaciones de '1000 Puntos'
    | Operación | Símbolo | Significado Lógico |
    | :--- | :---: | :--- |
    | **Unión** | $\cup$ | Elementos que están en A **o** en B |
    | **Intersección** | $\cap$ | Elementos que están en A **y** en B |
    
    ---
    > "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
    > — **Georg Cantor**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def mostrar_clase_n02():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""
    # N02: Los Números Naturales ($\mathbb{N}$)
    ---
    ### 🛡️ 1. El Portal: El Instinto de Cuantificar
    Mucho antes de las calculadoras, el ser humano necesitó contar sus pertenencias. Así nacen los Naturales: $\mathbb{N} = \{1, 2, 3, 4, ...\}$.
    
    ### 🛡️ 2. Reglas del Juego
    * **Sucesor:** Todo número $n$ tiene un sucesor $n+1$.
    * **Orden:** Es un conjunto discretamente ordenado.
    
    ### 🛡️ 3. Propiedades
    * **Clausura:** La suma y multiplicación de naturales siempre da otro natural.
    
    ---
    > "El número es la sustancia de todas las cosas".
    > — **Pitágoras**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONFIGURACIÓN Y ESTILO (RESTAURADO) ---
st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; font-weight: bold; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; font-weight: bold; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 35px; font-weight: bold; color: #3b71ca; text-align: center; width: 100%; display: block; }
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; }
    </style>
    """, unsafe_allow_html=True)

# Estados de sesión
if 'eje' not in st.session_state: st.session_state.eje = None
if 'clase' not in st.session_state: st.session_state.clase = None
if 'crono' not in st.session_state: st.session_state.crono = False

# HEADER ORIGINAL
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 Lagrangianitos. Tus recursos PAES M1 | 📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="header-rojo">⏳ Días: 108 | Hrs: 20</div>', unsafe_allow_html=True)

# CRONÓMETRO EN CAJA
with st.container(border=True):
    c1, c2 = st.columns([1, 2])
    if c1.button("▶️ Parar/Iniciar"):
        st.session_state.crono = not st.session_state.crono
        if st.session_state.crono: st.session_state.t_0 = time.time()
        st.rerun()
    if st.session_state.crono:
        s = int(time.time() - st.session_state.t_0)
        c2.markdown(f'<span class="crono-digital">{s//60:02d}:{s%60:02d}</span>', unsafe_allow_html=True)
    else:
        c2.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

# BOTONES DE NAVEGACIÓN
st.write("")
cols = st.columns(5)
if cols[0].button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if cols[1].button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()
if cols[2].button("A"): st.session_state.eje = "Álgebra"; st.rerun()
if cols[3].button("G"): st.session_state.eje = "Geometría"; st.rerun()
if cols[4].button("D"): st.session_state.eje = "Datos"; st.rerun()

st.divider()

# LÓGICA DE CONTENIDO
if st.session_state.eje == "Números":
    st.markdown("### 🔢 Eje Números")
    sub = st.radio("Subejes:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    if sub == "Conjuntos":
        if st.button("📘 Teoría y Conceptos (N01)"): st.session_state.clase = "N01"
        if st.button("📘 Números Naturales (N02)"): st.session_state.clase = "N02"

elif st.session_state.eje == "Datos":
    st.markdown("### 📊 Eje Datos y Azar")
    st.radio("Subejes:", ["Estadística", "Probabilidad", "Ejercitación"], horizontal=True)

# RENDER DE CLASES
if st.session_state.clase == "N01": mostrar_clase_n01()
elif st.session_state.clase == "N02": mostrar_clase_n02()

if st.session_state.crono:
    time.sleep(1); st.rerun()
    
