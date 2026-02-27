import streamlit as st
from datetime import datetime
import pytz
import time
from streamlit_autorefresh import st_autorefresh

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

if 'ir_a_pdf' not in st.session_state:
    st.session_state.ir_a_pdf = False

# --- ESTADOS DEL CRONÓMETRO ---
if 'cronometro_activo' not in st.session_state:
    st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state:
    st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. DICCIONARIO DE CONTENIDOS :::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def render_N01():
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle, Rectangle

    # ── TÍTULO ──────────────────────────────────────────────────────────────
    st.markdown("""
# Eje Números
## N01: Teoría de Conjuntos - El Lenguaje Maestro

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás. A menudo, nos enseñan que las matemáticas son un conjunto de reglas para calcular el vuelto o aprobar un examen, pero eso es como decir que la música es solo saber apretar teclas. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.

Este eje de **Números** no se trata de hacer cuentas rápidas; se trata de aprender a clasificar el caos. Durante las próximas unidades, descubriremos que los números no están "tirados" en el espacio, sino que habitan en estructuras organizadas llamadas **Conjuntos**. Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer fronteras y a entender que todo gran sistema se basa en quién pertenece a qué y bajo qué reglas. Prepárate para una apertura de mente donde el infinito deja de ser un concepto místico y se convierte en un terreno que podemos cartografiar.

### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
A finales del siglo XIX, un hombre decidió desafiar a la teología y a la ciencia de su tiempo. **Georg Cantor** se atrevió a decir que el infinito no era un muro infranqueable, sino un jardín que podía ser medido. Cantor demostró que los conjuntos nos permiten comparar tamaños de infinitos que parecen imposibles. Su valentía permitió que hoy podamos definir con precisión quirúrgica qué es un número. En la PAES, este lenguaje es tu escudo: si dominas los conjuntos, dominas las instrucciones de la prueba.

### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
Para que exista el orden, debe existir un límite y una jerarquía clara:

* **El Universo ($\\mathcal{U}$):** Es el contexto total que contiene todos los elementos de un problema. Nada existe fuera del universo.
* **El Vacío ($\\emptyset$ o $\\{\\}$):** Un conjunto sin elementos. Es la representación de la nada matemática y es subconjunto de cualquier conjunto por definición.
* **Pertenencia ($\\in$):** Relación de un **elemento** hacia un conjunto. (Ej: Manzana $\\in$ Frutas).
* **Subconjunto o Inclusión ($\\subset$):** Se dice que $A$ es subconjunto de $B$ ($A \\subset B$) si **todos** los elementos de $A$ están también en $B$.

> **💡 Tip:** Si $A \\subset B$, entonces la intersección es el más pequeño ($A \\cap B = A$) y la unión es el más grande ($A \\cup B = B$).
""")

    # ── FIGURA 1: Inclusión ──────────────────────────────────────────────────
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.add_patch(plt.Rectangle((0, 0), 10, 8, color='#f0f0f0', ec='black', lw=2))
    ax1.add_patch(plt.Circle((5, 4), 3, color='#3498db', alpha=0.3, ec='blue', lw=2))
    ax1.text(5, 6.5, "Conjunto B", fontsize=12, fontweight='bold', color='blue', ha='center')
    ax1.add_patch(plt.Circle((5, 4), 1.2, color='#2980b9', alpha=0.8, ec='navy', lw=2))
    ax1.text(5, 4, "A ⊂ B", fontsize=12, fontweight='bold', color='white', ha='center', va='center')
    ax1.set_xlim(-1, 11)
    ax1.set_ylim(-1, 9)
    ax1.axis('off')
    fig1.suptitle("Relación de Inclusión (Subconjuntos)", fontsize=15, fontweight='bold')
    st.pyplot(fig1)
    plt.close(fig1)

    # ── SECCIONES 4 Y 5 ─────────────────────────────────────────────────────
    st.markdown("""
### 🛡️ 4. Operaciones de "1000 Puntos"
Estas operaciones son las que "mueven" los elementos entre conjuntos:

| Operación | Símbolo | Significado Lógico | Carpintería Técnica |
| :--- | :---: | :--- | :--- |
| **Unión** | $\\cup$ | $x \\in A$ **o** $x \\in B$ | Agrupar todos los elementos de ambos. |
| **Intersección** | $\\cap$ | $x \\in A$ **y** $x \\in B$ | Solo los elementos que se repiten. |
| **Diferencia** | $-$ | $x \\in A$ pero $x \\notin B$ | Al primer conjunto le borras lo que sea del segundo. |
| **Complemento** | $A^c$ | $x \\in \\mathcal{U}$ pero $x \\notin A$ | Todo lo que le falta a A para ser el Universo. |

### 🛡️ 5. Cardinalidad y Conjunto Potencia
* **Cardinalidad ($n$):** Llamamos cardinalidad al número de elementos únicos de un conjunto. Se denota como $\\#A = n$ o $n(A)$.
* **Regla de Oro de la Unión:** $\\#(A \\cup B) = \\#A + \\#B - \\#(A \\cap B)$.
* **Conjunto Potencia:** Es el conjunto formado por todos los subconjuntos posibles de $A$.
* **Total de Subconjuntos:** Si la cardinalidad de un conjunto es $n$, el total de subconjuntos que se pueden formar es:
$$2^n$$
> **💡 Tip:** El total de subconjuntos siempre incluye al **Vacío** y al **propio conjunto $A$**. Si agregas un elemento a la bolsa, el conjunto potencia crece al doble.

### 🛡️ 6. Cartografía Visual (Diagramas de Venn-Euler)
Para dominar la PAES, debes "ver" la operación antes de calcularla. Aquí se presentan las estructuras visuales para tu análisis:
""")

    # ── FIGURA 2: Lámina de operaciones ─────────────────────────────────────
    color_a = '#e74c3c'
    color_b = '#3498db'
    color_u = '#f1c40f'

    fig2, axs = plt.subplots(2, 4, figsize=(20, 10))
    fig2.patch.set_facecolor('white')
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    # 1. Vacío
    axs[0,0].add_patch(Rectangle((0.1, 0.1), 0.8, 0.8, color='#f9f9f9', ec='black', lw=2))
    axs[0,0].text(0.9, 0.9, "U", fontweight='bold', ha='right')
    axs[0,0].text(0.5, 0.5, "Ø", fontsize=40, ha='center', va='center', alpha=0.3)
    axs[0,0].set_title("1. Conjunto Vacío", fontweight='bold')

    # 2. Intersección
    axs[0,1].add_patch(Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.3, ec='red'))
    axs[0,1].add_patch(Circle((0.6, 0.5), 0.25, color=color_b, alpha=0.3, ec='blue'))
    axs[0,1].text(0.25, 0.5, "A", fontweight='bold', fontsize=12)
    axs[0,1].text(0.75, 0.5, "B", fontweight='bold', fontsize=12)
    axs[0,1].text(0.5, 0.5, "A∩B", ha='center', fontweight='bold', color='black')
    axs[0,1].set_title("2. Intersección", fontweight='bold')

    # 3. Unión
    axs[0,2].add_patch(Circle((0.4, 0.5), 0.25, color='purple', alpha=0.6))
    axs[0,2].add_patch(Circle((0.6, 0.5), 0.25, color='purple', alpha=0.6))
    axs[0,2].text(0.25, 0.5, "A", fontweight='bold', color='white')
    axs[0,2].text(0.75, 0.5, "B", fontweight='bold', color='white')
    axs[0,2].set_title("3. Unión (A ∪ B)", fontweight='bold')

    # 4. Diferencia
    axs[0,3].add_patch(Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.8, ec='red'))
    axs[0,3].add_patch(Circle((0.6, 0.5), 0.25, color='white', alpha=1.0))
    axs[0,3].add_patch(Circle((0.6, 0.5), 0.25, color=color_b, alpha=0.1, ec='blue', ls='--'))
    axs[0,3].text(0.2, 0.5, "A", fontweight='bold')
    axs[0,3].text(0.75, 0.5, "B", fontweight='bold', alpha=0.5)
    axs[0,3].set_title("4. Diferencia (A - B)", fontweight='bold')

    # 5. Complemento
    axs[1,0].add_patch(Rectangle((0.1, 0.1), 0.8, 0.8, color=color_u, alpha=0.3, ec='black'))
    axs[1,0].add_patch(Circle((0.5, 0.5), 0.25, color='white', ec='black'))
    axs[1,0].text(0.5, 0.5, "A", ha='center', va='center', fontweight='bold')
    axs[1,0].text(0.15, 0.8, "Aᶜ", fontsize=15, fontweight='bold')
    axs[1,0].set_title("5. Complemento de A", fontweight='bold')

    # 6. Disjuntos
    axs[1,1].add_patch(Circle((0.25, 0.5), 0.2, color=color_a, alpha=0.5, ec='red'))
    axs[1,1].add_patch(Circle((0.75, 0.5), 0.2, color=color_b, alpha=0.5, ec='blue'))
    axs[1,1].text(0.25, 0.5, "A", ha='center', fontweight='bold')
    axs[1,1].text(0.75, 0.5, "B", ha='center', fontweight='bold')
    axs[1,1].set_title("6. Disjuntos (A ∩ B = Ø)", fontweight='bold')

    # 7. Unión Disjunta
    axs[1,2].add_patch(Circle((0.25, 0.5), 0.2, color='gray', alpha=0.8))
    axs[1,2].add_patch(Circle((0.75, 0.5), 0.2, color='gray', alpha=0.8))
    axs[1,2].text(0.25, 0.5, "A", ha='center', fontweight='bold', color='white')
    axs[1,2].text(0.75, 0.5, "B", ha='center', fontweight='bold', color='white')
    axs[1,2].set_title("7. Unión Disjunta", fontweight='bold')

    # 8. Subconjunto
    axs[1,3].add_patch(Circle((0.5, 0.5), 0.35, color=color_b, alpha=0.3, ec='blue'))
    axs[1,3].add_patch(Circle((0.5, 0.5), 0.15, color=color_a, alpha=0.8, ec='red'))
    axs[1,3].text(0.5, 0.75, "B", color='blue', fontweight='bold')
    axs[1,3].text(0.5, 0.5, "A", color='white', fontweight='bold', ha='center', va='center')
    axs[1,3].set_title("8. Inclusión (A ⊂ B)", fontweight='bold')

    for ax in axs.flat:
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

    fig2.suptitle("LÁMINA TÉCNICA: OPERACIONES DE CONJUNTOS", fontsize=20, fontweight='bold')
    st.pyplot(fig2)
    plt.close(fig2)

    # ── CITA FINAL ───────────────────────────────────────────────────────────
    st.markdown("""
---
> *"En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".*
>
> — **Georg Cantor**
""")

def render_proximamente(codigo):
    st.info(f"🚀 La clase {codigo} está en desarrollo.")

CONTENIDOS = {
    "🔢 Números": {
        "Teoria": {
            "N01": {"label": "📖 N01: Teoría de Conjuntos",    "render": render_N01},
            "N02": {"label": "📖 N02: Próximamente",            "render": lambda: render_proximamente("N02")},
            "N03": {"label": "📖 N03: Próximamente",            "render": lambda: render_proximamente("N03")},
        },
        "Ejercitacion": {
            "NE01": {"label": "📝 NE01: Ejercicios Conjuntos",  "render": lambda: render_proximamente("NE01")},
        },
    },
    "📉 Álgebra": {
        "Teoria": {
            "A01": {"label": "📖 A01: Expresiones Algebraicas", "render": lambda: render_proximamente("A01")},
            "A02": {"label": "📖 A02: Ecuaciones",              "render": lambda: render_proximamente("A02")},
        },
        "Ejercitacion": {
            "AE01": {"label": "📝 AE01: Ejercicios Álgebra",    "render": lambda: render_proximamente("AE01")},
        },
    },
    "📐 Geometría": {
        "Teoria": {
            "G01": {"label": "📖 G01: Geometría Plana",         "render": lambda: render_proximamente("G01")},
            "G02": {"label": "📖 G02: Geometría del Espacio",   "render": lambda: render_proximamente("G02")},
        },
        "Ejercitacion": {
            "GE01": {"label": "📝 GE01: Ejercicios Geometría",  "render": lambda: render_proximamente("GE01")},
        },
    },
    "📊 Datos y Azar": {
        "Teoria": {
            "D01": {"label": "📖 D01: Estadística Descriptiva", "render": lambda: render_proximamente("D01")},
            "D02": {"label": "📖 D02: Probabilidades",          "render": lambda: render_proximamente("D02")},
        },
        "Ejercitacion": {
            "DE01": {"label": "📝 DE01: Ejercicios Datos",      "render": lambda: render_proximamente("DE01")},
        },
    },
}

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. ESTILOS CSS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* --- BARRA DE NAVEGACIÓN 🏠 / N / A / G / D --- */
    [data-testid="stHorizontalBlock"] { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 4px !important; }
    [data-testid="stHorizontalBlock"] > div { flex: 1 1 0% !important; min-width: 0 !important; }
    [data-testid="stHorizontalBlock"] button {
        width: 100% !important;
        min-height: 70px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        background-color: #1a1a2e !important;
        color: white !important;
        border: none !important;
    }

    /* --- BOTONES DE CATEGORÍA (Teoría / Ejercitación / Clases) --- */
    .cat-container div.stButton > button {
        min-height: 85px !important; border-radius: 15px !important; margin-bottom: 15px !important;
        width: 100% !important; font-size: 18px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important; box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }

    /* --- BOTÓN PDF --- */
    .pdf-btn div.stButton > button {
        background-color: #4a0e8f !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 65px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* --- CRONÓMETRO --- */
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
# :::: 4. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 5. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":

    # --- AUTO REFRESH solo cuando el cronómetro está activo ---
    if st.session_state.cronometro_activo:
        st_autorefresh(interval=1000, limit=None, key="crono_refresh")

    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)

    paes_date = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    delta = paes_date - ahora
    dias = delta.days
    horas = delta.seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    st.write("")

    # --- BOTONES DE EJES ---
    if st.session_state.get('ir_a_pdf'):
        st.session_state.ir_a_pdf = False
        st.header("📂 Biblioteca de Recursos en PDF")
        st.info("🚀 Aquí irán los materiales descargables. Próximamente.")
        if st.button("🔙 Volver al inicio", key="volver_pdf"):
            st.rerun()

    elif st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números",      key="m_n", use_container_width=True): st.session_state.eje_actual = "🔢 Números";      st.rerun()
        if c2.button("📉 Álgebra",      key="m_a", use_container_width=True): st.session_state.eje_actual = "📉 Álgebra";      st.rerun()
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría",    key="m_g", use_container_width=True): st.session_state.eje_actual = "📐 Geometría";    st.rerun()
        if c4.button("📊 Datos y Azar", key="m_d", use_container_width=True): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

        # --- BOTÓN PDFs CENTRADO ---
        st.write("")
        col_iz, col_pdf, col_der = st.columns([1, 4, 1])
        with col_pdf:
            st.markdown('<div class="pdf-btn">', unsafe_allow_html=True)
            if st.button("📄 Materiales descargables en PDF", key="m_pdf", use_container_width=True):
                st.session_state.ir_a_pdf = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        # --- BARRA DE NAVEGACIÓN SUPERIOR ---
        n_cols = st.columns(5)
        if n_cols[0].button("🏠", key="n_h"):
            st.session_state.eje_actual = None
            st.session_state.sub_seccion_actual = None
            st.session_state.clase_seleccionada = None
            st.session_state.rama_datos = None
            st.rerun()
        if n_cols[1].button("N", key="n_n"):
            st.session_state.eje_actual = "🔢 Números";      st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[2].button("A", key="n_a"):
            st.session_state.eje_actual = "📉 Álgebra";      st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[3].button("G", key="n_g"):
            st.session_state.eje_actual = "📐 Geometría";    st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[4].button("D", key="n_d"):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.session_state.rama_datos = None; st.rerun()

        st.write("---")

        # --- CRONÓMETRO ---
        with st.container(border=True):
            col_btn, col_crono = st.columns([1, 2])
            with col_btn:
                if not st.session_state.cronometro_activo:
                    if st.button("▶️ Iniciar", key="btn_start_crono"):
                        st.session_state.tiempo_inicio = time.time()
                        st.session_state.cronometro_activo = True
                        st.rerun()
                else:
                    if st.button("⏹️ Detener", key="btn_stop_crono"):
                        st.session_state.cronometro_activo = False
                        st.rerun()
            with col_crono:
                if st.session_state.cronometro_activo and st.session_state.tiempo_inicio:
                    secs = int(time.time() - st.session_state.tiempo_inicio)
                    st.markdown(f'<span class="crono-digital">{secs//60:02d}:{secs%60:02d}</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

        # --- NAVEGACIÓN DE CONTENIDO BASADA EN DICCIONARIO ---
        eje = st.session_state.eje_actual
        clases_del_eje = CONTENIDOS.get(eje, {})

        if st.session_state.sub_seccion_actual is None:
            st.markdown(f"## {eje}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📘 Teoría y Conceptos",      key="bt_t"): st.session_state.sub_seccion_actual = "Teoria";       st.rerun()
            if st.button("📝 Ejercitación y Práctica", key="bt_e"): st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.clase_seleccionada is None:
            sub = st.session_state.sub_seccion_actual
            st.subheader(f"📚 Clases de {eje}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            clases = clases_del_eje.get(sub, {})
            for codigo, datos in clases.items():
                if st.button(datos["label"], key=f"cls_{codigo}"):
                    st.session_state.clase_seleccionada = codigo
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("🔙 Volver", key="volver_sub"):
                st.session_state.sub_seccion_actual = None
                st.rerun()

        else:
            sub    = st.session_state.sub_seccion_actual
            codigo = st.session_state.clase_seleccionada
            clase  = clases_del_eje.get(sub, {}).get(codigo)

            # Sin caja envolvente — contenido directo, sin cajita blanca
            if clase:
                clase["render"]()
            else:
                st.warning(f"Clase {codigo} no encontrada.")

            if st.button("🔙 Volver al listado de clases", key="volver_lista"):
                st.session_state.clase_seleccionada = None
                st.rerun()

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos")
