import streamlit as st
from datetime import datetime
import pytz

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

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* Cabeceras */
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* NAVEGACIÓN RÁPIDA (🏠 N A G D) */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 4px !important;
    }
    
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 0% !important;
        min-width: 0 !important;
    }

    [data-testid="stHorizontalBlock"] button {
        width: 100% !important;
        min-height: 55px !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
    }

    /* BOTONES DE CATEGORÍAS */
    .cat-container div.stButton > button { 
        min-height: 85px !important; 
        border-radius: 15px !important; 
        margin-bottom: 15px !important;
        width: 100% !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        text-align: left !important;
        padding-left: 20px !important;
        border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }

    /* Estilo de "Hoja de Clase" */
    .clase-box {
        background-color: white; 
        padding: 30px; 
        border-radius: 15px; 
        border: 1px solid #e0e0e0;
        color: #1a1a1a;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton**")
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
        if c1.button("🔢 Números\nConjuntos y operatoria", key="m_n", use_container_width=True):
            st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra\nFunciones y más", key="m_a", use_container_width=True):
            st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría\nÁreas y Volúmenes", key="m_g", use_container_width=True):
            st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if c4.button("📊 Datos y Azar\nProbabilidad y Estadística", key="m_d", use_container_width=True):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

    else:
        n_cols = st.columns(5)
        if n_cols[0].button("🏠", key="nav_h"):
            st.session_state.eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.rama_datos = None; st.rerun()
        if n_cols[1].button("N", key="nav_n"):
            st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n_cols[2].button("A", key="nav_a"):
            st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n_cols[3].button("G", key="nav_g"):
            st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_seccion_actual = None; st.rerun()
        if n_cols[4].button("D", key="nav_d"):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        # --- Lógica de Datos y Azar ---
        if st.session_state.eje_actual == "📊 Datos y Azar" and st.session_state.rama_datos is None:
            st.markdown(f"## {st.session_state.eje_actual}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📈 Estadística", key="btn_est"):
                st.session_state.rama_datos = "Estadística"; st.rerun()
            if st.button("🎲 Probabilidad", key="btn_prob"):
                st.session_state.rama_datos = "Probabilidad"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # --- Selección de Teoría/Ejercitación ---
        elif st.session_state.sub_seccion_actual is None:
            st.markdown(f"## {st.session_state.eje_actual}")
            if st.session_state.eje_actual == "📊 Datos y Azar":
                st.write(f"Seleccionaste: **{st.session_state.rama_datos}**")
            
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📘 Teoría y Conceptos", key="btn_teoria"):
                st.session_state.sub_seccion_actual = "Teoria"; st.rerun()
            if st.button("📝 Ejercitación y Práctica", key="btn_ejercitacion"):
                st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
            if st.session_state.eje_actual == "📊 Datos y Azar":
                if st.button("⬅️ Cambiar Rama"):
                    st.session_state.rama_datos = None; st.rerun()
        
        # --- CONTENIDO FINAL ---
        else:
            if st.session_state.sub_seccion_actual == "Teoria" and st.session_state.eje_actual == "🔢 Números":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("""
                # <span style="color:darkblue">Eje Números</span>
                ## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

                ---

                ### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
                Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer fronteras y a entender que todo gran sistema se basa en quién pertenece a qué y bajo qué reglas.

                ---

                ### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
                **Georg Cantor** demostró que los conjuntos nos permiten comparar tamaños de infinitos que parecen imposibles. En la PAES, este lenguaje es tu escudo.

                ---

                ### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
                * **El Universo ($\mathcal{U}$):** Es el contexto total que contiene todos los elementos de un problema.
                * **El Vacío ($\emptyset$ o $\{\}$):** Un conjunto sin elementos. Es subconjunto de cualquier conjunto por definición.
                * **Pertenencia ($\in$):** Relación de un **elemento** hacia un conjunto.
                * **Subconjunto o Inclusión ($\subset$):** $A \subset B$ si todos los elementos de $A$ están en $B$.

                > **Típ:** Si $A \subset B$, entonces la intersección es el más pequeño ($A \cap B = A$) y la unión es el más grande ($A \cup B = B$).

                ---

                ### 🛡️ 4. Operaciones de "1000 Puntos"
                | Operación | Símbolo | Significado Lógico | Carpintería Técnica |
                | :--- | :---: | :--- | :--- |
                | **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ | Agrupar todos los elementos. |
                | **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ | Solo los que se repiten. |
                | **Diferencia** | $-$ | $x \in A$ pero $x \notin B$ | Quitar elementos del segundo. |
                | **Complemento** | $A^c$ | $x \in \mathcal{U}$ pero $x \notin A$ | Lo que le falta para ser el Universo. |

                ---

                ### 🛡️ 5. Cardinalidad y Conjunto Potencia
                * **Cardinalidad ($n$):** Número de elementos únicos.
                * **Regla de Oro de la Unión:** $n(A \cup B) = n(A) + n(B) - n(A \cap B)$.
                * **Total de Subconjuntos:** $$2^n$$

                ---

                ### 🛡️ 6. Cartografía Visual (Diagramas de Venn-Euler)
                
                Los diagramas de Venn nos permiten visualizar las relaciones entre conjuntos de manera intuitiva.

                ---
                *"En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla."* — **Georg Cantor**
                """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("🚀 Contenido en desarrollo para esta sección.")
            
            if st.button("🔙 Volver a opciones"):
                st.session_state.sub_seccion_actual = None; st.rerun()

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos")
