import streamlit as st
from datetime import datetime
import pytz
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

# Inicialización de estados de navegación para que no se pierdan
if 'eje_actual' not in st.session_state: st.session_state.eje_actual = None
if 'sub_eje_actual' not in st.session_state: st.session_state.sub_eje_actual = None
if 'sub_seccion_actual' not in st.session_state: st.session_state.sub_seccion_actual = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None

# Estados del cronómetro
if 'cronometro_activo' not in st.session_state: st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state: st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS (REPARACIÓN TOTAL) ::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* 1. Limpieza de márgenes superiores de Streamlit */
    .block-container { padding-top: 1.5rem !important; }

    /* 2. Headers */
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; margin-bottom: 20px; }
    
    /* 3. Cronómetro Digital */
    .crono-container-barton { background-color: white; padding: 10px; border-radius: 10px; text-align: center; border: 2px solid #3b71ca; }
    .crono-digital-azul { font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; color: #3b71ca; }
    
    /* 4. Botones de Navegación (Cuadrados y Ordenados) */
    [data-testid="stHorizontalBlock"] button { 
        width: 100% !important; 
        min-height: 50px !important; 
        font-weight: bold !important; 
        border-radius: 8px !important; 
    }

    /* 5. ELIMINAR LA CAJA BLANCA FANTASMA */
    /* Este selector mata específicamente el contenedor vacío que aparece antes de los títulos */
    [data-testid="stVerticalBlock"] > div:empty { display: none !important; }
    [data-testid="stMarkdownContainer"] > p:empty { display: none !important; }

    /* 6. Caja de Clase Unificada */
    .clase-container {
        background-color: white;
        padding: 10px 30px 30px 30px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. DASHBOARD :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    # Cabecera con Reloj
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div style="font-size: 20px; font-weight: bold;">🐉 Lagrangianitos. Tus recursos PAES M1</div><div style="font-size: 14px; opacity: 0.9;">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    dias_paes = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    st.markdown(f'<div class="header-rojo">⏳ Días para PAES: {dias_paes} </div>', unsafe_allow_html=True)

    # Cronómetro Digital
    st.write("")
    c1, c2 = st.columns([1, 3])
    with c1:
        if not st.session_state.cronometro_activo:
            if st.button("▶️ Iniciar"): st.session_state.tiempo_inicio = time.time(); st.session_state.cronometro_activo = True; st.rerun()
        else:
            if st.button("⏹️ Detener"): st.session_state.cronometro_activo = False; st.session_state.tiempo_inicio = None; st.rerun()
    with c2:
        if st.session_state.cronometro_activo:
            t = int(time.time() - st.session_state.tiempo_inicio)
            st.markdown(f'<div class="crono-container-barton"><span class="crono-digital-azul">{t//60:02d}:{t%60:02d}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="crono-container-barton" style="border: 2px dashed #e0e0e0;"><span style="color:#e0e0e0; font-size:32px; font-family:Courier New; font-weight:bold;">00:00</span></div>', unsafe_allow_html=True)

    st.write("")

    # Barra de navegación rápida (N, A, G, D)
    nav_cols = st.columns(5)
    if nav_cols[0].button("🏠"): st.session_state.eje_actual = None; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if nav_cols[1].button("N"): st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if nav_cols[2].button("A"): st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if nav_cols[3].button("G"): st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if nav_cols[4].button("D"): st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()

    st.divider()

    # --- FLUJO DE PANTALLAS (RECUPERADO) ---
    if st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        e_col1, e_col2 = st.columns(2)
        if e_col1.button("🔢 Números"): st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if e_col2.button("📉 Álgebra"): st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        e_col3, e_col4 = st.columns(2)
        if e_col3.button("📐 Geometría"): st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if e_col4.button("📊 Datos y Azar"): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()
    
    elif st.session_state.sub_eje_actual is None:
        st.markdown(f"## {st.session_state.eje_actual}")
        if st.session_state.eje_actual == "🔢 Números":
            if st.button("🛡️ 1. Conjuntos"): st.session_state.sub_eje_actual = "Conjuntos"; st.rerun()
            if st.button("⚙️ 2. Operatoria"): st.session_state.sub_eje_actual = "Operatoria"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.eje_actual = None; st.rerun()

    elif st.session_state.sub_seccion_actual is None:
        st.markdown(f"## {st.session_state.sub_eje_actual}")
        if st.button("📘 Teoría y Conceptos"): st.session_state.sub_seccion_actual = "Teoria"; st.rerun()
        if st.button("📝 Ejercitación"): st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.sub_eje_actual = None; st.rerun()

    elif st.session_state.clase_seleccionada is None:
        st.subheader("📖 Clases Disponibles")
        if st.session_state.sub_seccion_actual == "Teoria" and st.session_state.sub_eje_actual == "Conjuntos":
            if st.button("📖 N01: Teoría de Conjuntos"): st.session_state.clase_seleccionada = "N01"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.sub_seccion_actual = None; st.rerun()

    else:
        # --- CLASE N01 INTEGRAL ---
        if st.button("🔙 Volver al listado"): 
            st.session_state.clase_seleccionada = None
            st.rerun()

        st.markdown('<div class="clase-container">', unsafe_allow_html=True)
        st.markdown("""
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.

---

### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
A finales del siglo XIX, **Georg Cantor** demostró que los conjuntos nos permiten comparar tamaños de infinitos que parecen imposibles.

---

### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
* **El Universo ($\mathcal{U}$):** Contexto total que contiene todos los elementos.
* **El Vacío ($\emptyset$):** Un conjunto sin elementos.
* **Pertenencia ($\in$):** Relación de un elemento hacia un conjunto.
* **Subconjunto ($\subset$):** $A \subset B$ si todos los elementos de $A$ están en $B$.

> **Típ:** ... Si $A \subset B$, entonces la intersección es el más pequeño ($A \cap B = A$).

---

### 🛡️ 4. Operaciones de "1000 Puntos"
| Operación | Símbolo | Significado Lógico | |
| :--- | :---: | :--- | :--- |
| **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ | Agrupar todos los elementos. |
| **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ | Solo los que se repiten. |

---

### 🛡️ 5. Cardinalidad y Conjunto Potencia
* **Cardinalidad ($n$):** Número de elementos únicos.
* **Total de Subconjuntos:** $2^n$

> **Típ:** ... El total de subconjuntos siempre incluye al **Vacío** y al **propio conjunto $A$**.

---

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".  
> — **Georg Cantor**
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Actualización del cronómetro
if st.session_state.cronometro_activo:
    time.sleep(1)
    st.rerun()
        
