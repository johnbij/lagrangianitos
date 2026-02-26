import streamlit as st
from datetime import datetime
import pytz
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state: st.session_state.eje_actual = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. CSS NUCLEAR (ELIMINA CAJAS Y ARREGLA MÓVIL) :::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* 1. ELIMINAR CUALQUIER MARGEN DE STREAMLIT */
    .block-container { padding-top: 1rem !important; padding-bottom: 0rem !important; max-width: 100% !important; }
    
    /* 2. MATAR LAS CAJAS VACÍAS (Lo que rayaste en azul) */
    [data-testid="stVerticalBlock"] > div:empty { display: none !important; margin: 0 !important; padding: 0 !important; }
    div[data-testid="stVerticalBlock"] > div:has(div[class*="stMarkdown"] > p:empty) { display: none !important; }
    
    /* 3. HEADERS RESPONSIVOS */
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; margin-bottom: 20px; font-weight: bold; }

    /* 4. BOTONES NAVEGACIÓN (Fix para que no se pongan uno arriba del otro) */
    .stButton > button {
        width: 100% !important;
        border-radius: 10px !important;
        height: 50px !important;
        font-weight: bold !important;
    }

    /* 5. CAJA DE CLASE LIMPIA */
    .clase-box {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #eee;
        margin-top: -10px; /* Elimina el aire blanco */
    }

    /* Ocultar elementos innecesarios de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. DASHBOARD :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# Cabecera
zona_cl = pytz.timezone('America/Santiago')
ahora = datetime.now(zona_cl)
st.markdown(f'<div class="header-azul">🐉 <b>Lagrangianitos. Tus recursos PAES M1</b></div>', unsafe_allow_html=True)
dias_paes = (datetime(2026, 6, 15, tzinfo=zona_cl) - ahora).days
st.markdown(f'<div class="header-rojo">⏳ Días para PAES: {dias_paes} </div>', unsafe_allow_html=True)

# Cronómetro y Botones Superiores
c1, c2, c3, c4, c5 = st.columns([1,1,1,1,1])
with c1: 
    if st.button("🏠"): st.session_state.eje_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
with c2: 
    if st.button("N"): st.session_state.eje_actual = "Números"; st.session_state.clase_seleccionada = None; st.rerun()
with c3: st.button("A")
with c4: st.button("G")
with c5: st.button("D")

st.divider()

# --- LÓGICA DE NAVEGACIÓN ---
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
    
    # Contenedor de la clase que "mata" el espacio blanco
    st.markdown('<div class="clase-box">', unsafe_allow_html=True)
    st.markdown("""
# <span style="color:darkblue">N01: Teoría de Conjuntos</span>
## <span style="color:darkblue">El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás. Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer fronteras y a entender que todo gran sistema se basa en quién pertenece a qué y bajo qué reglas.

---

### 🛡️ 2. El Marco de Referencia
* **El Universo ($\mathcal{U}$):** El contexto total.
* **El Vacío ($\emptyset$):** Sin elementos.
* **Pertenencia ($\in$):** Relación elemento-conjunto.

> **Típ:** ... Si $A \subset B$, entonces $A \cap B = A$ y $A \cup B = B$.

---

### 🛡️ 3. Operaciones de "1000 Puntos"
* **Unión ($\cup$):** Agrupar todos los elementos.
* **Intersección ($\cap$):** Solo los que se repiten.
* **Diferencia ($-$):** Al primero le borras lo que sea del segundo.

---

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".  
> — **Georg Cantor**
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Selecciona el eje **N** arriba para ver las clases.")
    
