import streamlit as st
from datetime import datetime
import pytz

# =============================================================================
# 📖 CAPÍTULO 0: BIBLIOTECA DE CONTENIDOS (MARKDOWN PURO)
# =============================================================================
# IMPORTANTE: El texto debe estar pegado al margen izquierdo de la pantalla.
# Si hay espacios antes de los "#" o de las tablas, Streamlit rompe el diseño.

CLASE_N01_TEORIA = """
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás. A menudo, nos enseñan que las matemáticas son un conjunto de reglas para calcular el vuelto o aprobar un examen, pero eso es como decir que la música es solo saber apretar teclas. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.

Este eje de **Números** no se trata de hacer cuentas rápidas; se trata de aprender a clasificar el caos. Durante las próximas unidades, descubriremos que los números no están "tirados" en el espacio, sino que habitan en estructuras organizadas llamadas **Conjuntos**. Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer fronteras y a entender que todo gran sistema se basa en quién pertenece a qué y bajo qué reglas. Prepárate para una apertura de mente donde el infinito deja de ser un concepto místico y se convierte en un terreno que podemos cartografiar.

---

### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
A finales del siglo XIX, un hombre decidió desafiar a la teología y a la ciencia de su tiempo. **Georg Cantor** se atrevió a decir que el infinito no era un muro infranqueable, sino un jardín que podía ser medido. Cantor demostró que los conjuntos nos permiten comparar tamaños de infinitos que parecen imposibles. Su valentía permitió que hoy podamos definir con precisión quirúrgica qué es un número. En la PAES, este lenguaje es tu escudo: si dominas los conjuntos, dominas las instrucciones de la prueba.

---

### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
Para que exista el orden, debe existir un límite y una jerarquía clara:

* **El Universo ($\mathcal{U}$):** Es el contexto total que contiene todos los elementos de un problema. Nada existe fuera del universo.
* **El Vacío ($\emptyset$ o $\{\}$):** Un conjunto sin elementos. Es la representación de la nada matemática y es subconjunto de cualquier conjunto por definición.
* **Pertenencia ($\in$):** Relación de un **elemento** hacia un conjunto. (Ej: Manzana $\in$ Frutas).
* **Subconjunto o Inclusión ($\subset$):** Se dice que $A$ es subconjunto de $B$ ($A \subset B$) si **todos** los elementos de $A$ están también en $B$.

> **Típ:** ... Si $A \subset B$, entonces la intersección es el más pequeño ($A \cap B = A$) y la unión es el más grande ($A \cup B = B$).

---

### 🛡️ 4. Operaciones de "1000 Puntos"
Estas operaciones son las que "mueven" los elementos entre conjuntos:

| Operación | Símbolo | Significado Lógico | Carpintería Técnica |
| :--- | :---: | :--- | :--- |
| **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ | Agrupar todos los elementos de ambos. |
| **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ | Solo los elementos que se repiten. |
| **Diferencia** | $-$ | $x \in A$ pero $x \notin B$ | Al primer conjunto le borras lo que sea del segundo. |
| **Complemento** | $A^c$ | $x \in \mathcal{U}$ pero $x \notin A$ | Todo lo que le falta a A para ser el Universo. |

---

### 🛡️ 5. Cardinalidad y Conjunto Potencia
* **Cardinalidad ($n$):** Llamamos cardinalidad al número de elementos únicos de un conjunto. Se denota como $\#A = n$ o $n(A)$.
* **Regla de Oro de la Unión:** $\#(A \cup B) = \#A + \#B - \#(A \cap B)$.
* **Conjunto Potencia:** Es el conjunto formado por todos los subconjuntos posibles de $A$.
* **Total de Subconjuntos:** Si la cardinalidad de un conjunto es $n$, el total de subconjuntos que se pueden formar es:
$$2^n$$

> **Típ:** ... El total de subconjuntos siempre incluye al **Vacío** y al **propio conjunto $A$**. Si agregas un elemento a la bolsa, el conjunto potencia crece al doble.

---

### 🛡️ 6. Cartografía Visual (Diagramas de Venn-Euler)

Para dominar la PAES, debes "ver" la operación antes de calcularla. Los diagramas de Venn-Euler nos permiten visualizar las relaciones entre conjuntos de manera intuitiva. Cada círculo representa un conjunto, y las superposiciones muestran las intersecciones. El rectángulo exterior representa el Universo.

---

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**
"""

# =============================================================================
# 🎨 CAPÍTULO I: FRONT-END Y ESTILOS (RESTAURADOS)
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; }

    .cat-container div.stButton > button { 
        min-height: 85px !important; border-radius: 15px !important; margin-bottom: 15px !important;
        width: 100% !important; font-size: 18px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important; box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }
    .clase-box { 
        background-color: white; padding: 40px; border-radius: 15px; border: 1px solid #e0e0e0; 
        color: #1a1a1a; line-height: 1.6; box-shadow: 0px 4px 10px rgba(0,0,0,0.03);
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# ⚙️ CAPÍTULO II: SISTEMA DE NAVEGACIÓN
# =============================================================================

if 'eje' not in st.session_state: st.session_state.eje = None
if 'sub_seccion' not in st.session_state: st.session_state.sub_seccion = None
if 'clase' not in st.session_state: st.session_state.clase = None

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# =============================================================================
# 🖥️ CAPÍTULO III: RENDERIZADO DEL DASHBOARD (ROLLBACK VISUAL)
# =============================================================================

if menu == "🏠 Dashboard PAES":
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    
    # Header Restaurado
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    
    dias = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    horas = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    st.write("") 

    # Navegación Superior Estilo Iconos
    n_cols = st.columns(5)
    if n_cols[0].button("🏠"): st.session_state.eje = None; st.session_state.sub_seccion = None; st.session_state.clase = None; st.rerun()
    if n_cols[1].button("N"): st.session_state.eje = "🔢 Números"; st.rerun()
    if n_cols[2].button("A"): st.session_state.eje = "📉 Álgebra"; st.rerun()
    if n_cols[3].button("G"): st.session_state.eje = "📐 Geometría"; st.rerun()
    if n_cols[4].button("D"): st.session_state.eje = "📊 Datos y Azar"; st.rerun()

    st.divider()

    if st.session_state.eje is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        # Aquí van tus botones gigantes del inicio
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números"): st.session_state.eje = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra"): st.session_state.eje = "📉 Álgebra"; st.rerun()
    
    elif st.session_state.sub_seccion is None:
        st.markdown(f"## {st.session_state.eje}")
        st.markdown('<div class="cat-container">', unsafe_allow_html=True)
        if st.button("📘 Teoría y Conceptos"): st.session_state.sub_seccion = "Teoria"; st.rerun()
        if st.button("📝 Ejercitación y Práctica"): st.session_state.sub_seccion = "Ejercitacion"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    elif st.session_state.clase is None:
        st.subheader(f"📚 Material de {st.session_state.eje}")
        st.markdown('<div class="cat-container">', unsafe_allow_html=True)
        if st.button("📖 N01: Teoría de Conjuntos"): st.session_state.clase = "N01"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("🔙 Volver"): st.session_state.sub_seccion = None; st.rerun()

    else:
        # PANTALLA DE CLASE FINAL
        if st.session_state.clase == "N01":
            st.markdown('<div class="clase-box">', unsafe_allow_html=True)
            st.markdown(CLASE_N01_TEORIA)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🔙 Volver al listado"): st.session_state.clase = None; st.rerun()

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos")
