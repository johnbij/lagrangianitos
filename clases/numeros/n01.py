import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle


def render_N01():
    with st.expander("📚 Teoría", expanded=False):

        # ── TÍTULO Y SECCIONES 1-3 ───────────────────────────────────────────────
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

        # ── FIGURA 1: Relación de Inclusión ─────────────────────────────────────
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

        # ── SECCIONES 4 y 5 ─────────────────────────────────────────────────────
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
        axs[0, 0].add_patch(Rectangle((0.1, 0.1), 0.8, 0.8, color='#f9f9f9', ec='black', lw=2))
        axs[0, 0].text(0.9, 0.9, "U", fontweight='bold', ha='right')
        axs[0, 0].text(0.5, 0.5, "Ø", fontsize=40, ha='center', va='center', alpha=0.3)
        axs[0, 0].set_title("1. Conjunto Vacío", fontweight='bold')

        # 2. Intersección
        axs[0, 1].add_patch(Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.3, ec='red'))
        axs[0, 1].add_patch(Circle((0.6, 0.5), 0.25, color=color_b, alpha=0.3, ec='blue'))
        axs[0, 1].text(0.25, 0.5, "A", fontweight='bold', fontsize=12)
        axs[0, 1].text(0.75, 0.5, "B", fontweight='bold', fontsize=12)
        axs[0, 1].text(0.5, 0.5, "A∩B", ha='center', fontweight='bold', color='black')
        axs[0, 1].set_title("2. Intersección", fontweight='bold')

        # 3. Unión
        axs[0, 2].add_patch(Circle((0.4, 0.5), 0.25, color='purple', alpha=0.6))
        axs[0, 2].add_patch(Circle((0.6, 0.5), 0.25, color='purple', alpha=0.6))
        axs[0, 2].text(0.25, 0.5, "A", fontweight='bold', color='white')
        axs[0, 2].text(0.75, 0.5, "B", fontweight='bold', color='white')
        axs[0, 2].set_title("3. Unión (A ∪ B)", fontweight='bold')

        # 4. Diferencia
        axs[0, 3].add_patch(Circle((0.4, 0.5), 0.25, color=color_a, alpha=0.8, ec='red'))
        axs[0, 3].add_patch(Circle((0.6, 0.5), 0.25, color='white', alpha=1.0))
        axs[0, 3].add_patch(Circle((0.6, 0.5), 0.25, color=color_b, alpha=0.1, ec='blue', ls='--'))
        axs[0, 3].text(0.2, 0.5, "A", fontweight='bold')
        axs[0, 3].text(0.75, 0.5, "B", fontweight='bold', alpha=0.5)
        axs[0, 3].set_title("4. Diferencia (A - B)", fontweight='bold')

        # 5. Complemento
        axs[1, 0].add_patch(Rectangle((0.1, 0.1), 0.8, 0.8, color=color_u, alpha=0.3, ec='black'))
        axs[1, 0].add_patch(Circle((0.5, 0.5), 0.25, color='white', ec='black'))
        axs[1, 0].text(0.5, 0.5, "A", ha='center', va='center', fontweight='bold')
        axs[1, 0].text(0.15, 0.8, "Aᶜ", fontsize=15, fontweight='bold')
        axs[1, 0].set_title("5. Complemento de A", fontweight='bold')

        # 6. Disjuntos
        axs[1, 1].add_patch(Circle((0.25, 0.5), 0.2, color=color_a, alpha=0.5, ec='red'))
        axs[1, 1].add_patch(Circle((0.75, 0.5), 0.2, color=color_b, alpha=0.5, ec='blue'))
        axs[1, 1].text(0.25, 0.5, "A", ha='center', fontweight='bold')
        axs[1, 1].text(0.75, 0.5, "B", ha='center', fontweight='bold')
        axs[1, 1].set_title("6. Disjuntos (A ∩ B = Ø)", fontweight='bold')

        # 7. Unión Disjunta
        axs[1, 2].add_patch(Circle((0.25, 0.5), 0.2, color='gray', alpha=0.8))
        axs[1, 2].add_patch(Circle((0.75, 0.5), 0.2, color='gray', alpha=0.8))
        axs[1, 2].text(0.25, 0.5, "A", ha='center', fontweight='bold', color='white')
        axs[1, 2].text(0.75, 0.5, "B", ha='center', fontweight='bold', color='white')
        axs[1, 2].set_title("7. Unión Disjunta", fontweight='bold')

        # 8. Subconjunto
        axs[1, 3].add_patch(Circle((0.5, 0.5), 0.35, color=color_b, alpha=0.3, ec='blue'))
        axs[1, 3].add_patch(Circle((0.5, 0.5), 0.15, color=color_a, alpha=0.8, ec='red'))
        axs[1, 3].text(0.5, 0.75, "B", color='blue', fontweight='bold')
        axs[1, 3].text(0.5, 0.5, "A", color='white', fontweight='bold', ha='center', va='center')
        axs[1, 3].set_title("8. Inclusión (A ⊂ B)", fontweight='bold')

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


    with st.expander("❓ Cuestionario N01", expanded=False):
        from utils import render_multiple_choice_quiz
        import json as _json
        _quiz_data = [
            {
                        "question": "¿Cuál de las siguientes opciones es un conjunto BIEN DEFINIDO?",
                        "options": {
                                    "A": "Los números bonitos",
                                    "B": "Los números pares entre 1 y 10",
                                    "C": "Las personas altas",
                                    "D": "Las cosas grandes"
                        },
                        "answer": "B",
                        "explanation": "Un conjunto bien definido permite saber sin ambigüedad si un elemento pertenece o no. Los pares entre 1 y 10 son: {2, 4, 6, 8, 10}."
            },
            {
                        "question": "El símbolo $\\in$ significa:",
                        "options": {
                                    "A": "No pertenece",
                                    "B": "Es subconjunto de",
                                    "C": "Pertenece a",
                                    "D": "Es igual a"
                        },
                        "answer": "C",
                        "explanation": "$a \\in A$ se lee 'a pertenece al conjunto A'."
            },
            {
                        "question": "Si $A = \\{1, 2, 3\\}$ y $B = \\{3, 4, 5\\}$, entonces $A \\cap B$ es:",
                        "options": {
                                    "A": "$\\{1, 2, 3, 4, 5\\}$",
                                    "B": "$\\{3\\}$",
                                    "C": "$\\emptyset$",
                                    "D": "$\\{1, 2\\}$"
                        },
                        "answer": "B",
                        "explanation": "La intersección son los elementos comunes: solo el 3 está en ambos conjuntos."
            },
            {
                        "question": "Si $A = \\{1, 2, 3\\}$ y $B = \\{3, 4, 5\\}$, entonces $A \\cup B$ es:",
                        "options": {
                                    "A": "$\\{3\\}$",
                                    "B": "$\\{1, 2\\}$",
                                    "C": "$\\{1, 2, 3, 4, 5\\}$",
                                    "D": "$\\{4, 5\\}$"
                        },
                        "answer": "C",
                        "explanation": "La unión junta todos los elementos sin repetir: {1, 2, 3, 4, 5}."
            },
            {
                        "question": "El conjunto vacío se denota por:",
                        "options": {
                                    "A": "$\\{0\\}$",
                                    "B": "$\\emptyset$ o $\\{\\}$",
                                    "C": "$\\infty$",
                                    "D": "$\\{\\emptyset\\}$"
                        },
                        "answer": "B",
                        "explanation": "El conjunto vacío no contiene ningún elemento. Se escribe $\\emptyset$ o $\\{\\}$. Ojo: $\\{0\\}$ tiene un elemento (el cero)."
            },
            {
                        "question": "Si $A \\subset B$, significa que:",
                        "options": {
                                    "A": "A y B son iguales",
                                    "B": "Todos los elementos de A están en B",
                                    "C": "B está contenido en A",
                                    "D": "A y B son disjuntos"
                        },
                        "answer": "B",
                        "explanation": "La inclusión $A \\subset B$ significa que cada elemento de A también pertenece a B."
            },
            {
                        "question": "La diferencia $A - B$ contiene:",
                        "options": {
                                    "A": "Los elementos de B que no están en A",
                                    "B": "Los elementos comunes de A y B",
                                    "C": "Los elementos de A que no están en B",
                                    "D": "Todos los elementos de A y B"
                        },
                        "answer": "C",
                        "explanation": "$A - B$ es el conjunto de elementos que están en A pero NO en B."
            },
            {
                        "question": "Si el universo $U = \\{1,2,3,4,5\\}$ y $A = \\{1,3,5\\}$, el complemento $A^c$ es:",
                        "options": {
                                    "A": "$\\{1,3,5\\}$",
                                    "B": "$\\{2,4\\}$",
                                    "C": "$\\{1,2,3,4,5\\}$",
                                    "D": "$\\emptyset$"
                        },
                        "answer": "B",
                        "explanation": "El complemento de A contiene todo lo del universo que NO está en A: {2, 4}."
            },
            {
                        "question": "¿Cuántos subconjuntos tiene el conjunto $\\{a, b\\}$?",
                        "options": {
                                    "A": "2",
                                    "B": "3",
                                    "C": "4",
                                    "D": "8"
                        },
                        "answer": "C",
                        "explanation": "Un conjunto con n elementos tiene $2^n$ subconjuntos. Con 2 elementos: $2^2 = 4$. Son: $\\emptyset$, {a}, {b}, {a,b}."
            },
            {
                        "question": "Dos conjuntos son DISJUNTOS si:",
                        "options": {
                                    "A": "Son iguales",
                                    "B": "Uno es subconjunto del otro",
                                    "C": "Su intersección es el vacío",
                                    "D": "Su unión es el vacío"
                        },
                        "answer": "C",
                        "explanation": "Conjuntos disjuntos no comparten ningún elemento: $A \\cap B = \\emptyset$."
            }
]
        render_multiple_choice_quiz(_quiz_data, key_prefix="n01_quiz")
