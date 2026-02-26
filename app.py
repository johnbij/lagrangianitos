import streamlit as st
from datetime import datetime
import pytz
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state: st.session_state.eje_actual = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. CSS PARA MATAR LA CAJA Y ARREGLAR BOTONES :::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* 1. ELIMINAR ESPACIOS BLANCOS Y CAJAS VACÍAS */
    .block-container { padding-top: 1rem !important; }
    [data-testid="stVerticalBlock"] > div:empty { display: none !important; }
    [data-testid="stMarkdownContainer"] > p:empty { display: none !important; }
    
    /* 2. HEADERS */
    .header-azul { background-color: #3b71ca; padding: 10px; border-radius: 12px 12px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 8px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 12px 12px; margin-bottom: 10px; font-weight: bold; }

    /* 3. BOTONES EN FILA (MÓVIL Y PC) */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 5px !important;
    }
    
    .stButton > button {
        width: 100% !important;
        min-width: 45px !important;
        height: 45px !important;
        border-radius: 10px !important;
        padding: 0 !important;
    }

    /* 4. CAJA DE CLASE SIN AIRE ARRIBA */
    .clase-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #eee;
        margin-top: -30px; /* Sube la clase para matar el espacio que marcaste */
    }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. INTERFAZ ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Cabecera
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 <b>Lagrangianitos. PAES M1</b></div>', unsafe_allow_html=True)
dias_paes = (datetime(2026, 6, 15, tzinfo=zona_cl) - ahora).days
st.markdown(f'<div class="header-rojo">⏳ Días: {dias_paes} </div>', unsafe_allow_html=True)

# Botones de navegación forzados en fila
cols = st.columns(5)
with cols[0]: 
    if st.button("🏠"): 
        st.session_state.eje_actual = None
        st.session_state.clase_seleccionada = None
        st.rerun()
with cols[1]: 
    if st.button("N"): 
        st.session_state.eje_actual = "Números"
        st.session_state.clase_seleccionada = None
        st.rerun()
with cols[2]: st.button("A")
with cols[3]: st.button("G")
with cols[4]: st.button("D")

st.divider()

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. CONTENIDO :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if st.session_state.eje_actual == "Números" and st.session_state.clase_seleccionada is None:
    st.markdown("### 📚 Clases de Conjuntos")
    if st.button("📖 N01: Teoría de Conjuntos"):
        st.session_state.clase_seleccionada = "N01"
        st.rerun()
    if st.button("🔙 Volver"):
        st.session_state.eje_actual = None
        st.rerun()

elif st.session_state.clase_seleccionada == "N01":
    if st.button("🔙 Volver al listado"):
        st.session_state.clase_seleccionada = None
        st.rerun()
    
    # La caja que matará el espacio en blanco
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""
# <span style="color:darkblue">N01: Teoría de Conjuntos</span>
## <span style="color:darkblue">El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal
Aprender Teoría de Conjuntos es aprender a clasificar el caos. Todo gran sistema se basa en quién pertenece a qué bajo reglas claras.

---

### 🛡️ 2. El Marco de Referencia
* **El Universo ($\mathcal{U}$):** El contexto total.
* **El Vacío ($\emptyset$):** Sin elementos.
* **Pertenencia ($\in$):** Relación elemento-conjunto.

> **Típ:** ... Si $A \subset B$, entonces $A \cap B = A$ y $A \cup B = B$.

---

### 🛡️ 3. Operaciones Clave
* **Unión ($\cup$):** Agrupar todos los elementos.
* **Intersección ($\cap$):** Solo los que se repiten.

---

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".  
> — **Georg Cantor**
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Presiona el botón **N** para empezar.")
        
