import streamlit as st
from datetime import datetime
import pytz

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None

# --- 2. INYECCIÓN DE CSS (TARJETAS Y CLASE) ---
st.markdown("""
    <style>
    div.stButton > button {
        height: 100px !important;
        border-radius: 12px !important;
        border: 1px solid #e0e0e0 !important;
        transition: all 0.3s ease !important;
        color: #31333F !important;
    }
    .clase-box {
        max-width: 900px;
        margin: 0 auto;
        padding: 20px;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería en FCFM*")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada. Uno se llama ayer y otro mañana. Por lo tanto, hoy es el día ideal para amar, crecer, hacer y principalmente vivir. Dalai Lama")

# --- 4. LÓGICA DE NAVEGACIÓN ---
if menu == "🏠 Dashboard PAES":
    # CABECERAS
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div style="background-color: #3b71ca; padding: 25px; border-radius: 15px 15px 0 0; color: white; position: relative; display: flex; align-items: center; justify-content: center; min-height: 100px;">
            <div style="font-size: 28px; font-weight: bold; text-align: center;">🐉 Lagrangianitos. Tus recursos PAES M1</div>
            <div style="position: absolute; right: 25px; text-align: right;">
                <div style="font-size: 22px; font-weight: bold; font-family: monospace;">{ahora.strftime("%H:%M:%S")}</div>
            </div>
        </div>
        <div style="background-color: #cc0000; padding: 15px; color: white; display: flex; justify-content: space-around; align-items: center; border-radius: 0 0 15px 15px;">
            <div style="font-size: 22px; font-weight: bold;">⏳ Días: {(datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days}</div>
            <div style="font-size: 22px; font-weight: bold;">Hrs: {(datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600}</div>
            <div style="font-size: 22px; font-weight: bold;">Min: {((datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 60) % 60}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    if st.session_state.eje_actual is None:
        st.subheader("📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números\nConjuntos y operatoria", key="main_n", use_container_width=True):
            st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra\nFunciones y más", key="main_a", use_container_width=True):
            st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
    else:
        # Mini Navegación Superior
        c_nav = st.columns(5)
        n_ejes = ["🏠 Inicio", "🔢 Números", "📉 Álgebra", "📐 Geometría", "📊 Datos"]
        for i, n in enumerate(n_ejes):
            if c_nav[i].button(n, key=f"nav_top_{i}", use_container_width=True):
                st.session_state.eje_actual = None if n == "🏠 Inicio" else n
                st.session_state.sub_seccion_actual = None; st.rerun()

        st.write("---")

        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Categorías de Números")
                cs1, cs2, cs3 = st.columns(3)
                if cs1.button("📦 Conjuntos Numéricos", key="cat_conj", use_container_width=True):
                    st.session_state.sub_seccion_actual = "N01"; st.rerun()
                if cs2.button("➕ Operatoria", key="cat_ope", use_container_width=True): pass
                if cs3.button("📝 Ejercitación", key="cat_ejer", use_container_width=True): pass
            
            elif st.session_state.sub_seccion_actual == "N01":
                # CAJITAS DE NAVEGACIÓN INTERNA
                col_back = st.columns(3)
                if col_back[0].button("⬅️ Volver a Menú", key="back_menu", use_container_width=True):
                    st.session_state.sub_seccion_actual = None; st.rerun()
                if col_back[1].button("➕ Ir a Operatoria", key="go_ope", use_container_width=True): pass
                if col_back[2].button("📝 Ir a Ejercitación", key="go_ejer", use_container_width=True): pass
                
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("""
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
""", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.header(st.session_state.eje_actual)
            st.info("Contenido en desarrollo.")

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos PDF")
