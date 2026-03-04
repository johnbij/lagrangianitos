import streamlit as st


def render_N09():
    with st.expander("📚 Teoría", expanded=False):
        st.title("N09: El Infinito ♾️ - Más allá de la Cuenta")

        st.markdown(r"""
    **Eje:** Números | **Nivel:** Conceptual y Filosófico

    ---

    ### 🏛️  Contexto Histórico: El Horror al Infinito
    Durante siglos, los matemáticos le tuvieron pánico al infinito. **Aristóteles** decía que el infinito era solo "potencial" (algo que nunca termina de crecer), pero que no existía como algo real. Para los griegos, el infinito era sinónimo de caos, algo que no se podía medir ni controlar.

    La verdadera revolución llegó a finales del siglo XIX con **Georg Cantor**. Él fue el primero en "domar" al infinito, demostrando que no solo era real, sino que había distintos tamaños de infinito. Sus ideas fueron tan revolucionarias (y extrañas para la época) que otros matemáticos lo atacaron ferozmente, llamándolo "corruptor de la juventud". Cantor terminó sus días obsesionado con estas ideas, pero hoy su legado es la base de toda la matemática moderna.

    ---

    ### 🛡️  La Gran Mentira: "¿Es el infinito un número?"
    La respuesta corta es **NO**. En la PAES y en la vida, el infinito no es un número que puedas ubicar en la recta numérica entre el 10 y el 100. Es un **concepto de cantidad sin fin** o un comportamiento de los conjuntos.

    ### 🛡️  ¿Cómo visualizar lo que no termina?
    Imagina una fábrica de ladrillos que nunca cierra y nunca se queda sin material. Si alguien te pregunta "¿cuántos ladrillos hay?", la respuesta no es un número fijo, sino la propiedad de que **siempre habrá uno más**.

    ### 🛡️  Los Niveles de Infinito (La Intuición de Cantor)
    No todos los infinitos son iguales, y esto es lo que vuela la cabeza:

    1. **Infinito "Pequeño" (Contable):** Es el de los Números Naturales ($\mathbb{N} = \{1, 2, 3, ...\}$). Puedes empezar a contarlos y, aunque no termines nunca, llevas un orden.
    2. **Infinito "Gigante" (Incontable):** Es el de los números reales. Entre el 0 y el 1, hay **más** números decimales que todos los números enteros que existen en el universo. Es un infinito mucho más denso.

    ### 🛡️  El Infinito en el Taller de Operaciones
    Cuando te encuentres con el símbolo $\infty$, las reglas de la carpintería normal se rompen:

    * **Inmortalidad:** $\infty + 1000 = \infty$. Al infinito no le haces cosquillas sumándole números finitos.
    * **Absorción:** $\infty \cdot 2 = \infty$. Multiplicar por algo finito no cambia su naturaleza sin fin.
    * **El Peligro:** $\frac{\infty}{\infty}$ o $\infty - \infty$. Estas operaciones son **Indeterminaciones**. No puedes decir que dan 1 o 0, porque depende de qué "infinito" sea más potente que el otro.

    ### 🛡️  ¿Por qué lo estudiamos hoy?
    Sin el infinito, no podríamos entender:
    * **Los Números Primos:** Euclides demostró que son infinitos. Si fueran finitos, la aritmética tendría un techo y se acabaría la creación de números.
    * **Los Decimales:** Las fracciones como $1/3$ generan infinitos decimales ($0,333...$).
    * **El Cálculo:** La base de la ingeniería (Beaucheff) es entender qué pasa cuando algo se acerca al infinito.

    ---

    > **Típ:** Si en una pregunta de suficiencia de datos te dicen que "n es un número muy grande", NO asumas que es infinito. El infinito no es "muy grande", es "sin límite". Hay una diferencia de galaxias entre ambos conceptos.

    ---

    > "Nadie nos expulsará del paraíso que Cantor ha creado para nosotros".
    > — **David Hilbert**
    """)


    with st.expander("❓ Cuestionario N09", expanded=False):
        from utils import render_multiple_choice_quiz
        import json as _json
        _quiz_data = [
            {
                        "question": "¿Cuál es el resultado de $\\frac{1}{2} + \\frac{1}{3} \\cdot \\frac{3}{4}$?",
                        "options": {
                                    "A": "$\\frac{5}{8}$",
                                    "B": "$\\frac{3}{4}$",
                                    "C": "$\\frac{5}{12}$",
                                    "D": "$\\frac{1}{4}$"
                        },
                        "answer": "B",
                        "explanation": "Mult. primero: $\\frac{1}{3} \\cdot \\frac{3}{4} = \\frac{1}{4}$. Luego $\\frac{1}{2} + \\frac{1}{4} = \\frac{2}{4} + \\frac{1}{4} = \\frac{3}{4}$."
            },
            {
                        "question": "Al resolver $\\frac{2}{3} \\div \\frac{4}{3} \\cdot \\frac{1}{2}$, se obtiene:",
                        "options": {
                                    "A": "1",
                                    "B": "$\\frac{1}{4}$",
                                    "C": "$\\frac{4}{9}$",
                                    "D": "$\\frac{1}{2}$"
                        },
                        "answer": "B",
                        "explanation": "Izquierda a derecha: $\\frac{2}{3} \\cdot \\frac{3}{4} = \\frac{1}{2}$. Luego $\\frac{1}{2} \\cdot \\frac{1}{2} = \\frac{1}{4}$."
            },
            {
                        "question": "¿Qué valor resulta de la expresión $\\frac{\\frac{2}{5}}{\\frac{4}{15}}$?",
                        "options": {
                                    "A": "$\\frac{8}{75}$",
                                    "B": "$\\frac{3}{2}$",
                                    "C": "$\\frac{2}{3}$",
                                    "D": "6"
                        },
                        "answer": "B",
                        "explanation": "**Atajo del Pillo:** $(2 \\cdot 15) / (5 \\cdot 4) = 30/20 = 3/2$."
            },
            {
                        "question": "El resultado de $1 - \\left( \\frac{1}{2} - \\frac{1}{4} \\right)$ es:",
                        "options": {
                                    "A": "$\\frac{3}{4}$",
                                    "B": "$\\frac{1}{4}$",
                                    "C": "$\\frac{1}{2}$",
                                    "D": "$\\frac{5}{4}$"
                        },
                        "answer": "A",
                        "explanation": "Paréntesis: $1/2 - 1/4 = 1/4$. Luego $1 - 1/4 = 3/4$."
            },
            {
                        "question": "Si calculamos $\\left( -\\frac{2}{3} \\right) \\cdot \\left( -\\frac{3}{4} \\right)$, el resultado es:",
                        "options": {
                                    "A": "$-\\frac{1}{2}$",
                                    "B": "$\\frac{6}{12}$",
                                    "C": "$\\frac{1}{2}$",
                                    "D": "$-\\frac{5}{12}$"
                        },
                        "answer": "C",
                        "explanation": "Menos por menos es más. Simplificando el 3: $2/4 = 1/2$."
            },
            {
                        "question": "¿Cuál es el valor de $\\frac{1}{2} \\div 2$?",
                        "options": {
                                    "A": "1",
                                    "B": "$\\frac{1}{4}$",
                                    "C": "4",
                                    "D": "$\\frac{1}{2}$"
                        },
                        "answer": "B",
                        "explanation": "Es $\\frac{1}{2} \\cdot \\frac{1}{2} = 1/4$. El entero 2 tiene un 1 abajo."
            },
            {
                        "question": "Al resolver $\\frac{3}{4} - \\frac{1}{2} + \\frac{5}{4}$, el resultado simplificado es:",
                        "options": {
                                    "A": "$\\frac{3}{2}$",
                                    "B": "$\\frac{7}{4}$",
                                    "C": "1",
                                    "D": "$\\frac{9}{4}$"
                        },
                        "answer": "A",
                        "explanation": "mcm es 4: $3/4 - 2/4 + 5/4 = 6/4 = 3/2$."
            },
            {
                        "question": "El valor de la expresión $\\frac{1 + \\frac{1}{3}}{2}$ es:",
                        "options": {
                                    "A": "$\\frac{4}{3}$",
                                    "B": "$\\frac{8}{3}$",
                                    "C": "$\\frac{2}{3}$",
                                    "D": "$\\frac{1}{3}$"
                        },
                        "answer": "C",
                        "explanation": "Numerador: $4/3$. Luego $\\frac{4/3}{2/1}$ (Atajo del Pillo) $= 4/6 = 2/3$."
            },
            {
                        "question": "¿Cuál es el resultado de $\\frac{2}{5} \\cdot \\frac{10}{3} \\div \\frac{4}{3}$?",
                        "options": {
                                    "A": "1",
                                    "B": "$\\frac{16}{25}$",
                                    "C": "$\\frac{4}{3}$",
                                    "D": "$\\frac{8}{15}$"
                        },
                        "answer": "A",
                        "explanation": "Mult: $20/15 = 4/3$. Luego $4/3 \\div 4/3 = 1$."
            },
            {
                        "question": "La expresión del terror: $\\left( \\frac{1}{2} + \\frac{1}{2} \\right) \\cdot \\frac{3}{4} - \\frac{1}{4}$ resulta en:",
                        "options": {
                                    "A": "$\\frac{1}{2}$",
                                    "B": "1",
                                    "C": "$\\frac{3}{4}$",
                                    "D": "0"
                        },
                        "answer": "A",
                        "explanation": "Paréntesis: $1 \\cdot 3/4 = 3/4$. Luego $3/4 - 1/4 = 2/4 = 1/2$."
            },
            {
                        "question": "Según el Algoritmo de la División, si el dividendo es 17 y el divisor es 5, ¿cuál es el valor del resto?",
                        "options": {
                                    "A": "1",
                                    "B": "2",
                                    "C": "3",
                                    "D": "5"
                        },
                        "answer": "B",
                        "explanation": "$17 \\div 5 = 3$ y sobran **2**. ($17 = 5 \\cdot 3 + 2$)."
            },
            {
                        "question": "¿Cuál de las siguientes afirmaciones sobre el Resto (r) es siempre verdadera?",
                        "options": {
                                    "A": "El resto puede ser igual al divisor.",
                                    "B": "El resto debe ser menor que el divisor.",
                                    "C": "El resto debe ser mayor que el cociente.",
                                    "D": "El resto siempre es cero en los números racionales."
                        },
                        "answer": "B",
                        "explanation": "Regla sagrada: El resto $r$ siempre debe cumplir $0 \\le r < d$."
            },
            {
                        "question": "Si un número se puede expresar como $24 = 3 \\cdot 8$, ¿qué nombre técnico reciben el 3 y el 8?",
                        "options": {
                                    "A": "Divisores y múltiplos.",
                                    "B": "Factores.",
                                    "C": "Restos.",
                                    "D": "Dividendos."
                        },
                        "answer": "B",
                        "explanation": "Los números que se multiplican para formar un producto son **factores**."
            },
            {
                        "question": "Al transformar la fracción impropia $\\frac{23}{4}$ a número mixto usando el algoritmo de la división, obtenemos:",
                        "options": {
                                    "A": "$5 \\frac{1}{4}$",
                                    "B": "$4 \\frac{3}{4}$",
                                    "C": "$5 \\frac{3}{4}$",
                                    "D": "$6 \\frac{1}{4}$"
                        },
                        "answer": "C",
                        "explanation": "$23 \\div 4 = 5$ (entero) y sobran **3** (numerador). Resultado: $5 \\frac{3}{4}$."
            },
            {
                        "question": "¿Qué significa que un número sea \"divisible\" por otro?",
                        "options": {
                                    "A": "Que el resultado es un número decimal.",
                                    "B": "Que el resto de la división es cero.",
                                    "C": "Que el cociente es mayor que el dividendo.",
                                    "D": "Que ambos números son primos."
                        },
                        "answer": "B",
                        "explanation": "Divisibilidad implica una división exacta, es decir, resto **cero**."
            },
            {
                        "question": "Si el cociente de una división es 6, el divisor es 4 y el resto es 3, ¿cuál es el dividendo?",
                        "options": {
                                    "A": "24",
                                    "B": "27",
                                    "C": "18",
                                    "D": "13"
                        },
                        "answer": "B",
                        "explanation": "Aplicando $D = d \\cdot q + r \\rightarrow D = 4 \\cdot 6 + 3 = 24 + 3 = 27$."
            },
            {
                        "question": "En la fracción $\\frac{12}{18}$, ¿cuál es el Máximo Común Divisor (MCD) que permite llegar a la fracción irreductible de un solo golpe?",
                        "options": {
                                    "A": "2",
                                    "B": "3",
                                    "C": "6",
                                    "D": "9"
                        },
                        "answer": "C",
                        "explanation": "Los divisores de 12 son {1,2,3,4,6,12} y de 18 {1,2,3,6,9,18}. El mayor común es **6**."
            },
            {
                        "question": "¿Cuál es la principal ventaja de usar la notación de fracción ($\\frac{1}{3}$) en lugar de su forma decimal ($0,333...$)?",
                        "options": {
                                    "A": "Es más fácil de escribir.",
                                    "B": "Representa el valor exacto sin perder información.",
                                    "C": "No requiere conocer el algoritmo de la división.",
                                    "D": "Las fracciones siempre son números enteros."
                        },
                        "answer": "B",
                        "explanation": "La fracción evita el error de aproximación de los decimales infinitos."
            },
            {
                        "question": "Si el resto de una división es 0, podemos afirmar que:",
                        "options": {
                                    "A": "El dividendo es un número primo.",
                                    "B": "El divisor es un factor del dividendo.",
                                    "C": "El cociente es igual al resto.",
                                    "D": "La división no se puede realizar."
                        },
                        "answer": "B",
                        "explanation": "Si la división es exacta, el divisor \"cabe\" justo, por lo tanto es un **factor**."
            },
            {
                        "question": "En el número mixto $7 \\frac{2}{5}$, ¿cuál de los siguientes elementos representa el \"Resto\" del algoritmo original?",
                        "options": {
                                    "A": "7",
                                    "B": "5",
                                    "C": "2",
                                    "D": "35"
                        },
                        "answer": "C",
                        "explanation": "Al pasar de impropia a mixto, el numerador resultante es siempre el **resto**."
            }
]
        render_multiple_choice_quiz(_quiz_data, key_prefix="n09_quiz")
