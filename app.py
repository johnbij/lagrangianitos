import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import pytz
import time
from datetime import datetime

# Configuración crítica para el servidor
matplotlib.use('Agg')

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. TUS GRÁFICOS (MODULARIZADOS) ::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def graficar_inclusion():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.add_patch(plt.Rectangle((0, 0), 10, 8, color='#f0f0f0', ec='black', lw=2, label='Universo (U)'))
    ax.add_patch(plt.Circle((5, 4), 3, color='#3498db', alpha=0.3, ec='blue', lw=2))
    ax.text(5, 6.5, "Conjunto B", fontsize=12, fontweight='bold', color='blue', ha='center')
    ax.add_patch(plt.Circle((5, 4), 1.2, color='#2980b9', alpha=0.8, ec='navy', lw=2))
    ax.text(5, 4, "A ⊂ B", fontsize=12, fontweight='bold', color='white', ha='center', va='center')
    ax.set_xlim(-1, 11); ax.set_ylim(-1, 9); ax.axis('off')
    st.pyplot(fig)

def graficar_lamina_operaciones():
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    fig.patch.set_facecolor('white')
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    color_a, color_b, color_u = '#e74c3c', '#3498db', '#f1c40f'

    # 1. Vacío
    axs[0,0].add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.8, color='#f9f9f9', ec='black', lw=2))
    axs[0,0].text(0.5, 0.5, "Ø", fontsize=40, ha='center', va='center', alpha=0.3)
    axs[0,0].set_title("1. Conjunto Vacío", fontweight='bold')
    # 2. Intersección
    axs[0,1].add_patch(plt.Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.3, ec='red'))
    axs[0,1].add_patch(plt.Circle((0.6, 0.5), 0.25, color=color_b, alpha=0.3, ec='blue'))
    axs[0,1].set_title("2. Intersección", fontweight='bold')
    # 3. Unión
    axs[0,2].add_patch(plt.Circle((0.4, 0.5), 0.25, color='purple', alpha=0.6))
    axs[0,2].add_patch(plt.Circle((0.6, 0.5), 0.25, color='purple', alpha=0.6))
    axs[0,2].set_title("3. Unión (A ∪ B)", fontweight='bold')
    # 4. Diferencia
    axs[0,3].add_patch(plt.Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.8, ec='red'))
    axs[0,3].add_patch(plt.Circle((0.6, 0.5), 0.25, color='white', alpha=1.0))
    axs[0,3].set_title("4. Diferencia (A - B)", fontweight='bold')
    # 5. Complemento
    axs[1,0].add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.8, color=color_u, alpha=0.3, ec='black'))
    axs[1,0].add_patch(plt.Circle((0.5, 0.5), 0.25, color='white', ec='black'))
    axs[1,0].set_title("5. Complemento de A", fontweight='bold')
    # 6. Disjuntos
    axs[1,1].add_patch(plt.Circle((0.25, 0.5), 0.2, color=color_a, alpha=0.5, ec='red'))
    axs[1,1].add_patch(plt.Circle((0.75, 0.5), 0.2, color=color_b, alpha=0.5, ec='blue'))
    axs[1,1].set_title("6. Disjuntos", fontweight='bold')
    # 7. Unión Disjunta
    axs[1,2].add_patch(plt.Circle((0.25, 0.5), 0.2, color='gray', alpha=0.8))
    axs[1,2].add_patch(plt.Circle((0.75, 0.5), 0.2, color='gray', alpha=0.8))
    axs[1,2].set_title("7. Unión Disjunta", fontweight='bold')
    # 8. Inclusión
    axs[1,3].add_patch(plt.Circle((0.5, 0.5), 0.35, color=color_b, alpha=0.3, ec='blue'))
    axs[1,3].add_patch(plt.Circle((0.5, 0.5), 0.15, color=color_a, alpha=0.8, ec='red'))
    axs[1,3].set_title("8. Inclusión (A ⊂ B)", fontweight='bold')

    for ax in axs.flat:
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis('off')
    st.pyplot(fig)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. MÓDULOS DE CLASES :::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def mostrar_clase_n01():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""# Eje Números
## N01: Teoría de Conjuntos - El Lenguaje Maestro
---
### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Aprender Teoría de Conjuntos es aprender a pensar con orden...""")
    
    st.write("### 🎨 Cartografía Visual")
    graficar_inclusion()
    
    st.markdown("""### 🛡️ 4. Operaciones de '1000 Puntos'
| Operación | Símbolo | Significado Lógico |
| :--- | :---: | :--- |
| **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ |
| **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ |""")
    
    st.write("### 🖼️ Lámina Técnica de Operaciones")
    graficar_lamina_operaciones()
    
    st.markdown("""---
> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**""")
    st.markdown('</div>', unsafe_allow_html=True)

def mostrar_clase_n02():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""# Eje Números
## N02: Los Números Naturales ($\mathbb{N}$) - El Génesis del Conteo
---
### 🛡️ 1. El Portal: El Instinto de Cuantificar
Mucho antes de que existieran las pizarras o los computadores...
(Aquí va el resto de tu texto N02)
---
> "El número es la sustancia de todas las cosas".
> — **Pitágoras**""")
    st.markdown('</div>', unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. INTERFAZ PRINCIPAL ::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", layout="wide")

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 35px; font-weight: bold; color: #3b71ca; text-align: center; width: 100%; display: block; }
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# Estados iniciales
for key in ['eje', 'clase', 'crono_on', 't_inicio']:
    if key not in st.session_state: st.session_state[key] = None if key != 'crono_on' else False

# HEADER
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 Lagrangianitos Hub | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="header-rojo">⏳ Días: 108 | Hrs: 22</div>', unsafe_allow_html=True)

# CRONÓMETRO
with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    if col1.button("▶️/⏹️"):
        st.session_state.crono_on = not st.session_state.crono_on
        if st.session_state.crono_on: st.session_state.t_inicio = time.time()
        st.rerun()
    if st.session_state.crono_on:
        s = int(time.time() - st.session_state.t_inicio)
        col2.markdown(f'<span class="crono-digital">{s//60:02d}:{s%60:02d}</span>', unsafe_allow_html=True)
    else:
        col2.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

# NAVEGACIÓN SUPERIOR
cols = st.columns(5)
if cols[0].button("🏠"): st.session_state.eje = None; st.session_state.clase = None; st.rerun()
if cols[1].button("N"): st.session_state.eje = "Números"; st.session_state.clase = None; st.rerun()
if cols[2].button("A"): st.session_state.eje = "Álgebra"; st.session_state.clase = None; st.rerun()
if cols[3].button("G"): st.session_state.eje = "Geometría"; st.session_state.clase = None; st.rerun()
if cols[4].button("D"): st.session_state.eje = "Datos"; st.session_state.clase = None; st.rerun()

st.divider()

# LÓGICA DE SUB-EJES (SIN FANTASMAS)
if st.session_state.eje == "Números":
    sub = st.radio("Sub-ejes:", ["Conjuntos", "Operatoria", "Razones", "Ejercitación"], horizontal=True)
    if sub == "Conjuntos":
        if st.button("📖 N01: Teoría de Conjuntos"): st.session_state.clase = "N01"
        if st.button("📖 N02: Números Naturales"): st.session_state.clase = "N02"

elif st.session_state.eje == "Álgebra":
    st.radio("Sub-ejes:", ["Álgebra", "Funciones", "Ejercitación"], horizontal=True)

elif st.session_state.eje == "Geometría":
    st.radio("Sub-ejes:", ["Formas", "Perímetros/Áreas", "Vectores", "Ejercitación"], horizontal=True)

elif st.session_state.eje == "Datos":
    st.radio("Sub-ejes:", ["Estadística", "Probabilidad", "Ejercitación"], horizontal=True)

# RENDER DE CLASES
if st.session_state.clase == "N01": mostrar_clase_n01()
elif st.session_state.clase == "N02": mostrar_clase_n02()

if st.session_state.crono_on:
    time.sleep(1); st.rerun()
    
