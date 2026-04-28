import streamlit as st
import matplotlib.pyplot as plt

def render_N03():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(r"""
    ## N03: Los Números Cardinales ($\mathbb{N}_0$) — La Conquista del Vacío

    ---

    ### 🛡️ El Portal: El Descubrimiento de la Nada
    En el capítulo anterior vimos que los Naturales servían para contar lo que "estaba ahí". Pero, ¿cómo representamos la ausencia total? Durante siglos, la humanidad le tuvo miedo al vacío. No fue hasta que civilizaciones como la India y los Mayas entendieron que el "nada" también es una cantidad, que la matemática pudo avanzar hacia el álgebra moderna.[cite: 8]

    Al añadir el **0** a nuestro conjunto de naturales, creamos los **Números Cardinales** (o Naturales Extendidos). Este pequeño cambio redefine las fronteras de lo que podemos calcular.[cite: 8]

    ---

    ### 🛡️ Definición y Notación
    Se denota con la letra $\mathbb{N}_0$ (o a veces $\mathbb{N} \cup \{0\}$) y se define como:[cite: 8]
    $$\mathbb{N}_0 = \{0, 1, 2, 3, 4, 5, ...\}$$

    * **Primer Elemento:** El **0** es ahora el inicio absoluto.[cite: 8]
    * **Cambio de Guardia:** En este conjunto, el **1 ya no es el límite**; ahora el 1 sí tiene un antecesor natural (el 0).[cite: 8]
    * **El Nuevo Muro:** El único número que carece de antecesor en $\mathbb{N}_0$ es el **0**.[cite: 8]
    """)

        # ── FIGURA: Comparativa N vs N0 ───────────────────────────────
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.set_xlim(-1, 7)
        ax.set_ylim(0.5, 2.5)
        ax.axhline(2, xmin=0.25, xmax=0.9, color='black', lw=2, alpha=0.3)
        for x in range(1, 7):
            ax.plot(x, 2, 'ro', markersize=10)
            ax.text(x, 2.15, str(x), ha='center', fontsize=12, fontweight='bold', color='red')
        ax.vlines(1, 1.8, 2.2, color='red', lw=4)
        ax.text(-0.8, 2, "Naturales (N)", fontsize=12, fontweight='bold', va='center')
        ax.axhline(1, xmin=0.125, xmax=0.9, color='black', lw=2, alpha=0.3)
        for x in range(0, 7):
            ax.plot(x, 1, 'go', markersize=10)
            ax.text(x, 0.7, str(x), ha='center', fontsize=12, fontweight='bold', color='green')
        ax.vlines(0, 0.8, 1.2, color='green', lw=4)
        ax.text(-0.8, 1, "Cardinales (N₀)", fontsize=12, fontweight='bold', va='center')
        ax.annotate('', xy=(7, 2), xytext=(6.5, 2), arrowprops=dict(arrowstyle='->', lw=2))
        ax.annotate('', xy=(7, 1), xytext=(6.5, 1), arrowprops=dict(arrowstyle='->', lw=2))
        circle = plt.Circle((0, 1), 0.25, color='yellow', alpha=0.3, ec='green', ls='--')
        ax.add_patch(circle)
        ax.text(0, 1.3, "¡Nuevo elemento!", color='darkgreen', fontsize=9, ha='center', fontweight='bold')
        plt.title("Comparativa de Límites: N vs N₀", fontsize=14, fontweight='bold', pad=20)
        ax.axis('off')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        st.markdown(r"""
    ---

    ### 🛡️ El Cero bajo la Lupa (Protocolo PAES)
    El cero no es un número cualquiera; es un agente especial con reglas propias:[cite: 8]

    1. **Paridad:** El 0 es un **número PAR**.[cite: 8]
    2. **Neutro Aditivo:** Es el elemento que no altera la suma: $a + 0 = a$.[cite: 8]
    3. **Elemento Absorbente:** En la multiplicación: $a \cdot 0 = 0$.[cite: 8]
    4. **La Prohibición:** La división **por cero** ($\frac{a}{0}$) no existe.[cite: 8]

    ---

    ### 🛡️ Diccionario de Supervivencia (Lenguaje Técnico)
    La PAES usará estas frases clave:[cite: 8]

    * **"Enteros positivos":** Se refiere a $\mathbb{N} = \{1, 2, 3, ...\}$.[cite: 8]
    * **"Enteros no negativos":** Se refiere a $\mathbb{N}_0 = \{0, 1, 2, 3, ...\}$.[cite: 8]

    > **Típ:** La palabra **"no negativo"** te obliga a incluir el cero. Si el problema dice "un número no negativo", y tú partes contando desde el 1, perdiste el ejercicio.[cite: 8]

    ---

    ### 🛡️ Propiedades de Clausura en $\mathbb{N}_0$
    * **Adición y Multiplicación:** Siguen siendo **Cerradas**.[cite: 8]
    * **Sustracción:** Sigue **SIN ser cerrada**, pero ganamos el caso: $a - a = 0$.[cite: 8]

    ---

    > "El cero es la mayor invención de la humanidad porque nos permite representar la nada como si fuera algo".
    > — **Anónimo**
    """)


    with st.expander("🚀 Guía de Ejemplos Paso a Paso N03", expanded=False):
        st.markdown(r"""
### 1: La Vecindad del Uno en Diferentes Conjuntos[cite: 8]

| Conjunto | Número | Antecesor ($n-1$) | ¿Existe en el conjunto? |
| :--- | :---: | :---: | :---: |
| Naturales ($\mathbb{N}$) | 1 | 0 | ❌ NO |
| Cardinales ($\mathbb{N}_0$) | 1 | 0 | ✅ SÍ |

---

### 2: El Cero y la Paridad[cite: 8]

| Expresión | Valor | Clasificación |
| :--- | :---: | :--- |
| $x - x$ | 0 | Elemento Neutro / Cardinal |
| $2 \cdot 0$ | 0 | **Número Par** |

---

### 3: Traducción de "Enteros No Negativos"[cite: 8]

| Frase Técnica | Traducción Matemática | Valores |
| :--- | :--- | :--- |
| "Enteros positivos" | $n \in \mathbb{N}$ | $\{1, 2, ...\}$ |
| "Enteros no negativos" | $n \in \mathbb{N}_0$ | $\{0, 1, 2, ...\}$ |

---

### 4: La Absorción y la Indefinición[cite: 8]

| Parte | Operación | Resultado |
| :--- | :--- | :--- |
| Numerador | $10 \cdot 0$ | 0 |
| Denominador | Valor de $x$ (donde $x=0$) | 0 |
| **Total** | **$0 / 0$** | **🚫 Indefinido** |

---

### 5: Clausura Extendida[cite: 8]

| Operación | Conjunto N | Conjunto N0 |
| :--- | :---: | :---: |
| $5 - 5$ | ❌ Se sale | ✅ Clausura (0) |
| $3 - 5$ | ❌ Se sale | ❌ Se sale |
""")

    with st.expander("❓ Cuestionario N03: Números Cardinales", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz_questions = [
            {"question": "¿Cuál es el único número que pertenece a $\\mathbb{N}_0$ pero NO a $\\mathbb{N}$?", "options": {"A": "$1$", "B": "$0$", "C": "$-1$", "D": "No existe tal número"}, "answer": "B", "explanation": "El cero es el único elemento que diferencia ambos conjuntos.[cite: 8]"},
            {"question": "¿Cuál es la condición para que $n \\in \\mathbb{N}_0$ NO tenga antecesor?", "options": {"A": "$n=1$", "B": "$n$ es par", "C": "$n=0$", "D": "Todos los cardinales tienen antecesor"}, "answer": "C", "explanation": "En $\\mathbb{N}_0$ el $0$ es el límite inicial; no hay números menores.[cite: 8]"},
            {"question": "¿Cuál de estas frases representa al conjunto $\\{0,1,2,3,\\ldots\\}$?", "options": {"A": "Enteros positivos", "B": "Enteros no positivos", "C": "Enteros no negativos", "D": "Naturales"}, "answer": "C", "explanation": "No negativos incluye obligatoriamente al cero y todos los positivos.[cite: 8]"},
            {"question": "Respecto al número $0$, ¿cuál afirmación es CORRECTA?", "options": {"A": "Es impar", "B": "Es neutro multiplicativo", "C": "Es par", "D": "Es el sucesor de $1$"}, "answer": "C", "explanation": "El $0$ es par porque $0 = 2 \\cdot 0$.[cite: 8]"},
            {"question": "La expresión $\\frac{5}{k-2}$ no está definida. ¿Cuál es el valor de $k$?", "options": {"A": "$0$", "B": "$2$", "C": "$5$", "D": "$-2$"}, "answer": "B", "explanation": "La división por cero es una indefinición; por tanto $k-2=0$.[cite: 8]"},
            {"question": "Si $A = \\{\\text{enteros no negativos menores que }2\\}$, la cardinalidad de $A$ es:", "options": {"A": "$1$", "B": "$2$", "C": "$3$", "D": "Infinita"}, "answer": "B", "explanation": "$A = \\{0,1\\}$, tiene 2 elementos.[cite: 8]"},
            {"question": "En $1245 \\cdot 0 = 0$, ¿qué propiedad del cero se aplica?", "options": {"A": "Neutro aditivo", "B": "Elemento absorbente", "C": "Clausura", "D": "Distributividad"}, "answer": "B", "explanation": "Propiedad absorbente: cualquier número por 0 da 0.[cite: 8]"},
            {"question": "En $\\mathbb{N}_0$, ¿cuál es el antecesor del sucesor de $0$?", "options": {"A": "$0$", "B": "$1$", "C": "$2$", "D": "No existe"}, "answer": "A", "explanation": "Sucesor de 0 es 1; antecesor de 1 es 0.[cite: 8]"},
            {"question": "Si sumo dos cardinales, el resultado siempre es cardinal. Esto se llama:", "options": {"A": "Conmutatividad", "B": "Asociatividad", "C": "Clausura", "D": "Tricotomía"}, "answer": "C", "explanation": "Clausura: operar elementos del conjunto produce otro del mismo conjunto.[cite: 8]"},
            {"question": "Si $x \\in \\mathbb{N}$, se deduce que:", "options": {"A": "$x$ puede ser $0$", "B": "$x$ es estrictamente mayor que $0$", "C": "$x$ no tiene antecesor en $\\mathbb{N}_0$", "D": "$x$ es entero no positivo"}, "answer": "B", "explanation": "Los naturales parten desde el 1, por lo que todos son mayores que 0.[cite: 8]"},
        ]
        render_multiple_choice_quiz(quiz_questions, key_prefix="n03_quiz")
