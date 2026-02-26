import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import pytz
import time
from datetime import datetime

# Configuración para que Matplotlib no explote en la nube
matplotlib.use('Agg')

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. FUNCIONES DE GRÁFICOS (MÓDULOS VISUALES) ::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def graficar_inclusion():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.add_patch(plt.Rectangle((0, 0), 10, 8, color='#f0f0f0', ec='black', lw=2))
    ax.add_patch(plt.Circle((5, 4), 3, color='#3498db', alpha=0.3, ec='blue', lw=2))
    ax.add_patch(plt.Circle((5, 4), 1.2, color='#2980b9', alpha=0.8, ec='navy', lw=2))
    ax.text(5, 6.5, "Conjunto B", fontsize=12, fontweight='bold', color='blue', ha='center')
    ax.text(5, 4, "A ⊂ B", fontsize=12, fontweight='bold', color='white', ha='center', va='center')
    ax.set_xlim(-1, 11); ax.set_ylim(-1, 9); ax.axis('off')
    st.pyplot(fig)

def graficar_lamina_operaciones():
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    fig.patch.set_facecolor('white')
    # Aquí va la lógica de tus 8 mini-gráficos (Vacío, Unión, etc.)
    # ... (Omitido por brevedad, pero mantén tu código de los axs aquí)
    for ax in axs.flat: ax.axis('off')
    plt.suptitle("LÁMINA TÉCNICA: OPERACIONES DE CONJUNTOS", fontsize=20, fontweight='bold')
    st.pyplot(fig)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. MÓDULOS DE CLASES (CONTENIDO) :::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def mostrar_n01():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""# Eje Números
## N01: Teoría de Conjuntos - El Lenguaje Maestro
---
Aprender Teoría de Conjuntos es aprender a pensar con orden... (Texto completo N01)""")
    st.write("### 🎨 Cartografía Visual")
    graficar_inclusion()
    st.write("### 🖼️ Lámina Técnica")
    graficar_lamina_operaciones()
    st.markdown("""---
> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**""")
    st.markdown('</div>', unsafe_allow_html=True)

def mostrar_n02():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""# Eje Números
## N02: Los Números Naturales (N) - El Génesis del Conteo
---
(Texto completo N02)...
---
> "El número es la sustancia de todas las cosas".
> — **Pitágoras**""")
    st.markdown('</div>', unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. INTERFAZ Y LÓGICA DE NAVEGACIÓN :::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")

# Estilos CSS
st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 35px; font-weight: bold; color: #3b71ca; text-align: center; display: block; }
    </style>
    """, unsafe_allow_html=True)

# Inicialización de estados
for key in ['eje', 'sub_eje', 'clase', 'crono_on', 't_inicio']:
    if key not in st.session_state: st.session_state[key] = None if key != 'crono_on' else False

# HEADER
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 Lagrangianitos Hub | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="header-rojo">⏳ Días para PAES: 108</div>', unsafe_allow_html=True)

# CRONÓMETRO
with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    if col1.button("▶️/⏹️ Crono"):
        st.session_state.crono_on = not st.session_state.crono_on
        if st.session_state.crono_on: st.session_state.t_inicio = time.time()
        st.rerun()
    if st.session_state.crono_on:
        s = int(time.time() - st.session_state.t_inicio)
        col2.markdown(f'<span class="crono-digital">{s//60:02d}:{s%60:02d}</span>', unsafe_allow_html=True)
    else:
        col2.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

# BARRA DE NAVEGACIÓN (BOTONES EJE)
st.write("")
nav = st.columns(5)
if nav[0].button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if nav[1].button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()
if nav[2].button("A"): st.session_state.eje = "Álgebra"; st.session_state.clase = None; st.rerun()
if nav[3].button("G"): st.session_state.eje = "Geometría"; st.session_state.clase = None; st.rerun()
if nav[4].button("D"): st.session_state.eje = "Datos"; st.session_state.clase = None; st.rerun()

st.divider()

# LÓGICA DE FILTRADO (Aquí matamos los fantasmas)
if st.session_state.eje == "Números":
    seccion = st.radio("Sub-ejes Números:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    if seccion == "Conjuntos":
        if st.button("📖 N01: Teoría de Conjuntos"): st.session_state.clase = "N01"
        if st.button("📖 N02: Números Naturales"): st.session_state.clase = "N02"

elif st.session_state.eje == "Álgebra":
    st.radio("Sub-ejes Álgebra:", ["Álgebra", "Funciones", "Ejercitación"], horizontal=True)

elif st.session_state.eje == "Geometría":
    st.radio("Sub-ejes Geometría:", ["Formas", "Perímetros/Áreas", "Vectores", "Ejercitación"], horizontal=True)

elif st.session_state.eje == "Datos":
    # El botón "Datos y Azar" ahora solo vive en esta rama
    st.radio("Sub-ejes Datos y Azar:", ["Estadística", "Probabilidad", "Ejercitación"], horizontal=True)

# RENDER DE CLASE
if st.session_state.clase == "N01": mostrar_n01()
elif st.session_state.clase == "N02": mostrar_n02()

if st.session_state.crono_on: time.sleep(1); st.rerun()
    
