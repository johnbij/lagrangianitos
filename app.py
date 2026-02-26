import streamlit as st
from datetime import datetime
import pytz
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None
if 'rama_datos' not in st.session_state:
    st.session_state.rama_datos = None
if 'clase_seleccionada' not in st.session_state:
    st.session_state.clase_seleccionada = None

if 'cronometro_activo' not in st.session_state:
    st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state:
    st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    [data-testid="stHorizontalBlock"] { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 4px !important; }
    [data-testid="stHorizontalBlock"] > div { flex: 1 1 0% !important; min-width: 0 !important; }
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; }

    .cat-container div.stButton > button { 
        min-height: 85px !important; border-radius: 15px !important; margin-bottom: 15px !important;
        width: 100% !important; font-size: 18px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important; box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    
    .crono-digital {
        font-family: 'Courier New', monospace;
        font-size: 35px;
        font-weight: bold;
        color: #3b71ca;
        text-align: center;
        width: 100%;
        display: block;
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
# :::: 4. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    
    dias = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    horas = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    st.write("") 

    if st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números", key="m_n"): st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra", key="m_a"): st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría", key="m_g"): st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if c4.button("📊 Datos y Azar", key="m_d"): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

    else:
        n_cols = st.columns(5)
        if n_cols[0].button("🏠", key="n_h"): st.session_state.eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[1].button("N", key="n_n"): st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[2].button("A", key="n_a"): st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[3].button("G", key="n_g"): st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[4].button("D", key="n_d"): st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()

        st.write("---")

        with st.container(border=True):
            col_btn, col_crono = st.columns([1, 2])
            with col_btn:
                if not st.session_state.cronometro_activo:
                    if st.button("▶️ Iniciar", key="btn_start"):
                        st.session_state.tiempo_inicio = time.time()
                        st.session_state.cronometro_activo = True
                        st.rerun()
                else:
                    if st.button("⏹️ Parar", key="btn_stop"):
                        st.session_state.cronometro_activo = False
                        st.rerun()
            with col_crono:
                if st.session_state.cronometro_activo:
                    secs = int(time.time() - st.session_state.tiempo_inicio)
                    st.markdown(f'<span class="crono-digital">{secs//60:02d}:{secs%60:02d}</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)
        
        if st.session_state.sub_seccion_actual is None:
            st.markdown(f"## {st.session_state.eje_actual}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📘 Teoría y Conceptos", key="bt_t"): st.session_state.sub_seccion_actual = "Teoria"; st.rerun()
            if st.button("📝 Ejercitación", key="bt_e"): st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.clase_seleccionada is None:
            st.subheader(f"📚 Clases de {st.session_state.eje_actual}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📖 N01: Teoría de Conjuntos", key="n01"): st.session_state.clase_seleccionada = "N01"; st.rerun()
            if st.button("📖 N02: Los Números Naturales", key="n02"): st.session_state.clase_seleccionada = "N02"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("🔙 Volver"): st.session_state.sub_seccion_actual = None; st.rerun()

        else:
            if st.session_state.clase_seleccionada == "N01":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("""
# Eje Números
## N01: Teoría de Conjuntos - El Lenguaje Maestro

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.

Este eje de **Números** no se trata de hacer cuentas rápidas; se trata de aprender a clasificar el caos. Durante las próximas unidades, descubriremos que los números no están "tirados" en el espacio, sino que habitan en estructuras organizadas llamadas **Conjuntos**. Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer fronteras y a entender que todo gran sistema se basa en quién pertenece a qué y bajo qué reglas.

### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
A finales del siglo XIX, **Georg Cantor** se atrevió a decir que el infinito no era un muro infranqueable, sino un jardín que podía ser medido. Cantor demostró que los conjuntos nos permiten comparar tamaños de infinitos que parecen imposibles. Su valentía permitió que hoy podamos definir con precisión quirúrgica qué es un número.

### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
* **El Universo ($\mathcal{U}$):** Es el contexto total que contiene todos los elementos.
* **El Vacío ($\emptyset$):** Un conjunto sin elementos.
* **Pertenencia ($\in$):** Relación de un **elemento** hacia un conjunto.
* **Subconjunto ($\subset$):** $A \subset B$ si **todos** los elementos de $A$ están también en $B$.

> **Típ:** Anota: tip ... Si $A \subset B$, entonces la intersección es el más pequeño ($A \cap B = A$) y la unión es el más grande ($A \cup B = B$).

### 🛡️ 4. Operaciones de "1000 Puntos"
| Operación | Símbolo | Significado Lógico | Carpintería Técnica |
| :--- | :---: | :--- | :--- |
| **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ | Agrupar todos los elementos de ambos. |
| **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ | Solo los elementos que se repiten. |
| **Diferencia** | $-$ | $x \in A$ pero $x \notin B$ | Al primer conjunto le borras lo que sea del segundo. |
| **Complemento** | $A^c$ | $x \in \mathcal{U}$ pero $x \notin A$ | Todo lo que le falta a A para ser el Universo. |

### 🛡️ 5. Cardinalidad y Conjunto Potencia
* **Cardinalidad ($n$):** Número de elementos únicos.
* **Regla de Oro de la Unión:** $\#(A \cup B) = \#A + \#B - \#(A \cap B)$.
* **Conjunto Potencia:** Todos los subconjuntos posibles de $A$.
* **Total de Subconjuntos:** $2^n$

> **Típ:** Anota: tip ... El total de subconjuntos siempre incluye al **Vacío** y al **propio conjunto $A$**.

### 🛡️ 6. Cartografía Visual (Diagramas de Venn-Euler)
Para dominar la PAES, debes "ver" la operación antes de calcularla.
                


> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**
                """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            elif st.session_state.clase_seleccionada == "N02":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("""
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N02: Los Números Naturales ($\mathbb{N}$) - El Génesis del Conteo</span>

---

### 🛡️ 1. El Portal: El Instinto de Cuantificar
Los Números Naturales fueron descubiertos como la herramienta de supervivencia definitiva para contar presas, días y ciclos.

---

### 🛡️ 2. Crónica del Origen: El Hueso de Ishango y Peano
**Giuseppe Peano** demostró que solo necesitábamos un punto de partida (el 1) y un sucesor para construir todo el universo matemático.

---

### 🛡️ 3. Definición y Características Formales
$$\mathbb{N} = \{1, 2, 3, 4, 5, 6, 7, ...\}$$

* **Primer Elemento:** El **1** es el inicio absoluto.
* **Infinitud:** No existe un número máximo.
* **Discretitud:** Entre el 4 y el 5 **no hay nada**.

---

### 🛡️ 4. La Ley de Tricotomía
Establece que para $a, b \in \mathbb{N}$, solo una es posible: $a < b$, $a > b$, o $a = b$.

---

### 🛡️ 5. Relaciones de Vecindad
* **El Sucesor:** $(n + 1)$.
* **El Antecesor:** $(n - 1)$, con excepción del 1.

> **Típ:** Anota: tip ... Si el antecesor de $n$ es natural, $n$ no puede ser 1.

---

### 🛡️ 6. Las Reglas del Juego: Propiedades
* **Clausura:** Cerrado en Adición y Multiplicación. No en Resta ni División.
* **Conmutativa, Asociativa y Distributiva.**

> "El número es la sustancia de todas las cosas". — **Pitágoras**
                """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            if st.button("🔙 Volver al listado"): st.session_state.clase_seleccionada = None; st.rerun()

if st.session_state.cronometro_activo:
    time.sleep(1)
    st.rerun()
    
