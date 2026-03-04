import streamlit as st


def render_N21():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("## N21: Racionalización Básica - El Arte de Limpiar el Denominador")
        st.markdown("---")

        st.markdown("### 🏛️ Contexto Histórico: La obsesión por la forma estándar")
        st.markdown("""
    Durante siglos, el cálculo manual era un dolor de cabeza, y dividir por un número irracional (como $\\sqrt{2}$) era el equivalente a tratar de escribir con un lápiz sin punta. Los matemáticos de la época renacentista buscaban formas **\"canónicas\"** o estándar para los números. Descubrieron que si multiplicaban el numerador y el denominador por el mismo radical, el valor de la fracción no cambiaba, pero el denominador se convertía en un número entero agradable y fácil de usar para dividir. La racionalización nace no solo por estética, sino por una necesidad pura de velocidad y precisión en el cálculo.
        """)
        st.markdown("---")

        st.markdown("""
    <div style="background-color: #E8F5E9; border-left: 8px solid #2E7D32; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1B5E20; margin-top: 0;">¿Qué es Racionalizar?</h2>
        Racionalizar es un proceso algebraico que consiste en eliminar las raíces del denominador de una fracción. El objetivo es obtener una fracción equivalente cuyo denominador sea un número racional (entero o fracción entera).
    </div>
    """, unsafe_allow_html=True)

        st.markdown("### 🛡️ El Procedimiento Maestro")
        st.markdown("""
    Para racionalizar una raíz simple del tipo $\\dfrac{A}{\\sqrt[n]{b^m}}$, multiplicamos tanto el numerador como el denominador por otra raíz que **\"complete\"** la potencia del denominador para que el índice se cancele.

    $$\\frac{A}{\\sqrt[n]{b^m}} \\cdot \\frac{\\sqrt[n]{b^{n-m}}}{\\sqrt[n]{b^{n-m}}} = \\frac{A \\cdot \\sqrt[n]{b^{n-m}}}{b}$$
        """)

        st.markdown("### 🛡️ Casos Básicos")
        st.markdown("""
    | Denominador | Factor Racionalizante | Resultado en Denominador |
    | :--- | :--- | :--- |
    | $\\sqrt{a}$ | $\\sqrt{a}$ | $a$ |
    | $\\sqrt[3]{a}$ | $\\sqrt[3]{a^2}$ | $a$ |
    | $\\sqrt[4]{a^3}$ | $\\sqrt[4]{a}$ | $a$ |

    **Típ:** ¡No te olvides de multiplicar arriba también! Si solo multiplicas abajo, estás cambiando el valor de la fracción, no racionalizándola.
        """)
        st.markdown("---")


    with st.expander("📝 Guía de Ejemplos Paso a Paso - Racionalización Básica"):
        st.markdown("""
**E01. Racionalizar una raíz cuadrada simple.** Racionalizar $\\dfrac{1}{\\sqrt{2}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante | $\\sqrt{2}$ |
| 2 | Multiplicar arriba y abajo | $\\dfrac{1 \\cdot \\sqrt{2}}{\\sqrt{2} \\cdot \\sqrt{2}}$ |
| 3 | Resolver producto | $\\dfrac{\\sqrt{2}}{2}$ |

---

**E02. Racionalizar con coeficiente en el denominador.** Racionalizar $\\dfrac{3}{\\sqrt{3}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante | $\\sqrt{3}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{3 \\cdot \\sqrt{3}}{\\sqrt{3} \\cdot \\sqrt{3}}$ |
| 3 | Resolver y simplificar | $\\dfrac{3\\sqrt{3}}{3} = \\sqrt{3}$ |

---

**E03. Racionalizar con número entero en el numerador.** Racionalizar $\\dfrac{2}{3\\sqrt{5}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante (solo la raíz) | $\\sqrt{5}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{2 \\cdot \\sqrt{5}}{3\\sqrt{5} \\cdot \\sqrt{5}}$ |
| 3 | Resolver producto en denominador | $\\dfrac{2\\sqrt{5}}{3 \\cdot 5} = \\dfrac{2\\sqrt{5}}{15}$ |

---

**E04. Racionalizar raíz cúbica.** Racionalizar $\\dfrac{1}{\\sqrt[3]{2}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor para completar exponente 3 | $\\sqrt[3]{2^2}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{1 \\cdot \\sqrt[3]{2^2}}{\\sqrt[3]{2} \\cdot \\sqrt[3]{2^2}}$ |
| 3 | Resolver denominador | $\\dfrac{\\sqrt[3]{4}}{\\sqrt[3]{2^3}} = \\dfrac{\\sqrt[3]{4}}{2}$ |

---

**E05. Racionalizar raíz sobre raíz.** Racionalizar $\\dfrac{\\sqrt{2}}{\\sqrt{3}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante | $\\sqrt{3}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{\\sqrt{2} \\cdot \\sqrt{3}}{\\sqrt{3} \\cdot \\sqrt{3}}$ |
| 3 | Resolver productos | $\\dfrac{\\sqrt{6}}{3}$ |
        """)

    with st.expander("❓ Cuestionario N21", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿Cuál es el resultado de racionalizar $\\dfrac{1}{\\sqrt{5}}$?', 'options': {'A': '$\\dfrac{\\sqrt{5}}{5}$', 'B': '$\\sqrt{5}$', 'C': '$\\dfrac{1}{5}$', 'D': '$\\dfrac{5}{\\sqrt{5}}$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál es el factor racionalizante para $\\dfrac{A}{\\sqrt{7}}$?', 'options': {'A': '$7$', 'B': '$\\sqrt{7}$', 'C': '$\\sqrt{49}$', 'D': '$\\dfrac{\\sqrt{7}}{7}$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Racionaliza la expresión $\\dfrac{2}{\\sqrt{2}}$:', 'options': {'A': '$2\\sqrt{2}$', 'B': '$\\dfrac{\\sqrt{2}}{2}$', 'C': '$\\sqrt{2}$', 'D': '$2$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Al racionalizar $\\dfrac{1}{\\sqrt[3]{3}}$, el denominador resultante es:', 'options': {'A': '$3$', 'B': '$9$', 'C': '$\\sqrt[3]{3}$', 'D': '$\\sqrt[3]{9}$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El resultado de $\\dfrac{\\sqrt{2}}{\\sqrt{6}}$ tras racionalizar es:', 'options': {'A': '$\\dfrac{\\sqrt{12}}{6}$', 'B': '$\\dfrac{\\sqrt{3}}{3}$', 'C': '$\\dfrac{1}{\\sqrt{3}}$', 'D': '$\\dfrac{2}{6}$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Cuál es el resultado de racionalizar $\\dfrac{4}{3\\sqrt{2}}$?', 'options': {'A': '$\\dfrac{4\\sqrt{2}}{3}$', 'B': '$\\dfrac{2\\sqrt{2}}{3}$', 'C': '$\\dfrac{2\\sqrt{2}}{6}$', 'D': '$\\dfrac{\\sqrt{2}}{3}$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Racionaliza $\\dfrac{1}{\\sqrt[4]{2^2}}$:', 'options': {'A': '$\\dfrac{\\sqrt[4]{2}}{2}$', 'B': '$\\dfrac{\\sqrt[4]{4}}{2}$', 'C': '$\\sqrt[4]{2}$', 'D': '$\\dfrac{1}{2}$'}, 'answer': 'A', 'explanation': ''},
            {'question': '¿Qué expresión es equivalente a $\\dfrac{10}{2\\sqrt{5}}$?', 'options': {'A': '$5\\sqrt{5}$', 'B': '$2\\sqrt{5}$', 'C': '$\\sqrt{5}$', 'D': '$\\dfrac{\\sqrt{5}}{5}$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'Al racionalizar $\\dfrac{\\sqrt{3}}{\\sqrt{5}}$, ¿qué numerador obtienes?', 'options': {'A': '$\\sqrt{3}$', 'B': '$\\sqrt{5}$', 'C': '$\\sqrt{15}$', 'D': '$15$'}, 'answer': 'A', 'explanation': ''},
            {'question': 'El factor racionalizante de $\\dfrac{1}{\\sqrt[5]{x^2}}$ es:', 'options': {'A': '$\\sqrt[5]{x}$', 'B': '$\\sqrt[5]{x^2}$', 'C': '$\\sqrt[5]{x^3}$', 'D': '$\\sqrt[5]{x^5}$'}, 'answer': 'A', 'explanation': ''}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n21_quiz")


    st.markdown("---")
    st.markdown("> *\"La matemática es la reina de las ciencias.\"*")
