import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import pytz
import time
from datetime import datetime
matplotlib.use('Agg')

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. FUNCIONES DE GRÁFICOS (MODULARIZADOS) :::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def graficar_inclusion():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.add_patch(plt.Rectangle((0, 0), 10, 8, color='#f0f0f0', ec='black', lw=2))
    ax.add_patch(plt.Circle((5, 4), 3, color='#3498db', alpha=0.3, ec='blue', lw=2))
    ax.add_patch(plt.Circle((5, 4), 1.2, color='#2980b9', alpha=0.8, ec='navy', lw=2))
    ax.text(5, 4, "A ⊂ B", fontsize=12, fontweight='bold', color='white', ha='center', va='center')
    ax.set_xlim(-1, 11); ax.set_ylim(-1, 9); ax.axis('off')
    st.pyplot(fig)

def graficar_lamina_operaciones():
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    # ... (Aquí va tu código completo de los 8 subplots que me pasaste)
    # Por brevedad en este bloque, asumo que el código de los axs está aquí
    plt.suptitle("LÁMINA TÉCNICA: OPERACIONES DE CONJUNTOS", fontsize=20, fontweight='bold')
    st.pyplot(fig)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. CONTENIDO DE LAS CLASES (MÓDULOS) :::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def mostrar_n01():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""# Eje Números
## N01: Teoría de Conjuntos - El Lenguaje Maestro
---
### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
(Aquí va todo tu texto de la N01)...""")
    
    st.write("### 🎨 Cartografía Visual")
    graficar_inclusion()
    
    st.markdown("### 🛡️ 4. Operaciones de '1000 Puntos'")
    # ... tabla de operaciones ...
    
    st.write("### 🖼️ Lámina Técnica")
    graficar_lamina_operaciones()
    
    st.markdown("""---
> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def mostrar_n02():
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""# Eje Números
## N02: Los Números Naturales (N) - El Génesis del Conteo
---
(Aquí va todo tu texto completo de la N02 que me pasaste)...
---
> "El número es la sustancia de todas las cosas".
> — **Pitágoras**""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. CONFIGURACIÓN Y ESTILOS CSS :::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# Estilos CSS (Iguales a tu versión filete)
st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .crono-digital { font-family: 'Courier New', monospace; font-size: 35px; font-weight: bold; color: #3b71ca; text-align: center; width: 100%; display: block; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# Estados de sesión
for key in ['eje_actual', 'sub_seccion_actual', 'clase_seleccionada', 'cronometro_activo', 'tiempo_inicio']:
    if key not in st.session_state: st.session_state[key] = None if key != 'cronometro_activo' else False

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. LÓGICA DE NAVEGACIÓN Y SUBEJES ::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca"])

if menu == "🏠 Dashboard PAES":
    # Header y Cronómetro (Aprovechando la caja blanca)
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul">🐉 Lagrangianitos Hub | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)
    
    with st.container(border=True):
        c1, c2 = st.columns([1, 2])
        if c1.button("▶️/⏹️ Cronómetro"):
            st.session_state.cronometro_activo = not st.session_state.cronometro_activo
            if st.session_state.cronometro_activo: st.session_state.tiempo_inicio = time.time()
            st.rerun()
        if st.session_state.cronometro_activo:
            secs = int(time.time() - st.session_state.tiempo_inicio)
            c2.markdown(f'<span class="crono-digital">{secs//60:02d}:{secs%60:02d}</span>', unsafe_allow_html=True)
        else:
            c2.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

    # Navegación Superior (Botones rápidos)
    cols = st.columns(5)
    if cols[0].button("🏠"): st.session_state.eje_actual = None; st.rerun()
    if cols[1].button("N"): st.session_state.eje_actual = "Números"; st.session_state.sub_seccion_actual = None; st.rerun()
    if cols[2].button("A"): st.session_state.eje_actual = "Álgebra"; st.session_state.sub_seccion_actual = None; st.rerun()
    if cols[3].button("G"): st.session_state.eje_actual = "Geometría"; st.session_state.sub_seccion_actual = None; st.rerun()
    if cols[4].button("D"): st.session_state.eje_actual = "Datos"; st.session_state.sub_seccion_actual = None; st.rerun()

    st.divider()

    # Lógica de Ejes y Sub-ejes
    if st.session_state.eje_actual == "Números":
        sub = st.selectbox("Selecciona Sub-eje:", ["Conjuntos", "Operatoria", "Razones y Proporciones", "Ejercitación"])
        if sub == "Conjuntos":
            c1, c2 = st.columns(2)
            if c1.button("📖 N01: Teoría de Conjuntos"): st.session_state.clase_seleccionada = "N01"
            if c2.button("📖 N02: Números Naturales"): st.session_state.clase_seleccionada = "N02"
    
    elif st.session_state.eje_actual == "Álgebra":
        st.selectbox("Selecciona Sub-eje:", ["Álgebra", "Funciones", "Ejercitación"])
        
    elif st.session_state.eje_actual == "Geometría":
        st.selectbox("Selecciona Sub-eje:", ["Formas y Figuras", "Perímetros, Áreas y Volúmenes", "Vectores", "Ejercitación"])
        
    elif st.session_state.eje_actual == "Datos":
        st.selectbox("Selecciona Sub-eje:", ["Estadística", "Probabilidad"])

    # RENDER DE CLASES
    if st.session_state.clase_seleccionada == "N01": mostrar_n01()
    elif st.session_state.clase_seleccionada == "N02": mostrar_n02()

# Auto-refresh crono
if st.session_state.cronometro_activo:
    time.sleep(1); st.rerun()
    
