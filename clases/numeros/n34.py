import streamlit as st


def render_N34():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("""## N34: De las Proporciones a las Igualdades (El Puente)

    ---

    ### 🏛️ Contexto Histórico: El Arte de la Balanza

    Mucho antes de que existieran los libros de matemáticas, los comerciantes en los mercados de Egipto y Babilonia usaban balanzas de platos. Si ponían una pesa de 1 kilo en un lado, debían poner exactamente 1 kilo de grano en el otro para que la barra se mantuviera horizontal. El término "Álgebra" viene del árabe *Al-Jabr*, que significa "restauración" o "completar". Los antiguos entendieron que una **igualdad** es como una balanza: si haces un cambio en un lado, debes hacer el mismo cambio en el otro para no romper el equilibrio. Lo que hemos estado haciendo con las razones es buscar ese equilibrio.

    ---

    ### ⚖️ ¿Qué es una Igualdad Matemática?
    Hasta ahora, hemos usado razones como $\\frac{x}{10} = 5$. Sin saberlo, ya estabas trabajando con modelos algebraicos. Una igualdad es simplemente una oración matemática que afirma que dos expresiones valen lo mismo.

    **Típ:** Imagina que el signo **"="** es el centro de una balanza.
    * Si en el lado izquierdo sumas 5, la balanza se inclina.
    * Para enderezarla, **debes sumar 5 en el lado derecho**.



    ---

    ### 🛡️ Las Reglas del Movimiento (Despeje)
    Para encontrar el valor de nuestra incógnita (esa $k$ o esa $x$ que tanto hemos buscado), debemos dejarla sola. Para mover los números de un lado a otro del "=" sin romper la balanza, usamos la **operación inversa**:

    1. **Si un número está sumando:** Pasa al otro lado restando.
    2. **Si un número está restando:** Pasa al otro lado sumando.
    3. **Si un número está multiplicando:** Pasa al otro lado dividiendo.
    4. **Si un número está dividiendo:** Pasa al otro lado multiplicando (como hacíamos al resolver $\\frac{x}{4} = 10 \\implies x = 10 \\cdot 4$).

    ---

    ### 🛡️ Relación con las Proporciones
    ¿Te acuerdas de la Proporcionalidad Directa? Teníamos la relación:
    $$\\frac{y}{x} = k$$
    Si queremos saber cuánto vale $y$, el $x$ que está dividiendo pasa al otro lado multiplicando:
    $$y = k \\cdot x$$
    ¡Eso es! Acabas de transformar una **razón** en un **modelo predictivo**. Todo lo que hemos despejado en los problemas de edades, mezclas y móviles seguía esta misma lógica de equilibrio.

    ---

    ### 🛡️ Lenguaje Cotidiano a Lenguaje Matemático
    El gran truco para lo que viene es saber traducir las palabras en símbolos:
    * **"Un número aumentado en 5"** $\\rightarrow x + 5$
    * **"El doble de un número"** $\\rightarrow 2x$
    * **"La tercera parte de algo"** $\\rightarrow \\frac{x}{3}$
    * **"Es igual a" / "Resulta en"** $\\rightarrow =$

    ---

    "La esencia de las matemáticas no es hacer las cosas simples complicadas, sino hacer las cosas complicadas simples."  
    — **S. Gudder**""", unsafe_allow_html=True)
        st.markdown("---")


    with st.expander("❓ Cuestionario N34", expanded=False):
        from utils import render_multiple_choice_quiz
        import json as _json
        _quiz_data = [
            {
                        "question": "Una proporción es una igualdad entre:",
                        "options": {
                                    "A": "Dos sumas",
                                    "B": "Dos razones",
                                    "C": "Dos diferencias",
                                    "D": "Dos productos"
                        },
                        "answer": "B",
                        "explanation": "Una proporción establece que dos razones son iguales: $\\frac{a}{b} = \\frac{c}{d}$."
            },
            {
                        "question": "En la proporción $\\frac{2}{3} = \\frac{x}{12}$, el valor de $x$ es:",
                        "options": {
                                    "A": "6",
                                    "B": "8",
                                    "C": "4",
                                    "D": "18"
                        },
                        "answer": "B",
                        "explanation": "Multiplicando en cruz: $3x = 24$, por lo tanto $x = 8$."
            },
            {
                        "question": "Si $\\frac{a}{b} = \\frac{c}{d}$, entonces por la propiedad de la cruz:",
                        "options": {
                                    "A": "$a + d = b + c$",
                                    "B": "$a \\cdot d = b \\cdot c$",
                                    "C": "$a - d = b - c$",
                                    "D": "$a \\cdot b = c \\cdot d$"
                        },
                        "answer": "B",
                        "explanation": "La propiedad fundamental de las proporciones: el producto de extremos es igual al de medios."
            },
            {
                        "question": "¿Cuál es el valor de $x$ en la ecuación $3x - 5 = 10$?",
                        "options": {
                                    "A": "3",
                                    "B": "5",
                                    "C": "15",
                                    "D": "1"
                        },
                        "answer": "B",
                        "explanation": "$3x = 15$, entonces $x = 5$."
            },
            {
                        "question": "Si 5 lápices cuestan $\\$500$, ¿cuánto cuestan 8 lápices?",
                        "options": {
                                    "A": "$\\$600$",
                                    "B": "$\\$700$",
                                    "C": "$\\$800$",
                                    "D": "$\\$1000$"
                        },
                        "answer": "C",
                        "explanation": "Proporción directa: $\\frac{5}{500} = \\frac{8}{x} \\implies x = 800$."
            },
            {
                        "question": "Una ecuación lineal de una variable tiene:",
                        "options": {
                                    "A": "Infinitas soluciones",
                                    "B": "Ninguna solución",
                                    "C": "Exactamente una solución",
                                    "D": "Dos soluciones"
                        },
                        "answer": "C",
                        "explanation": "Una ecuación lineal ($ax + b = c$, con $a \\neq 0$) tiene exactamente una solución: $x = \\frac{c-b}{a}$."
            },
            {
                        "question": "Si $\\frac{x}{4} = 3$, entonces $x$ es:",
                        "options": {
                                    "A": "$\\frac{3}{4}$",
                                    "B": "7",
                                    "C": "12",
                                    "D": "1"
                        },
                        "answer": "C",
                        "explanation": "Multiplicando ambos lados por 4: $x = 12$."
            },
            {
                        "question": "En una proporción $a:b = c:d$, los elementos $a$ y $d$ se llaman:",
                        "options": {
                                    "A": "Medios",
                                    "B": "Extremos",
                                    "C": "Antecedentes",
                                    "D": "Consecuentes"
                        },
                        "answer": "B",
                        "explanation": "$a$ y $d$ son los términos externos (extremos), mientras que $b$ y $c$ son los internos (medios)."
            },
            {
                        "question": "Despejar $y$ en $2y + 6 = 14$ da:",
                        "options": {
                                    "A": "$y = 10$",
                                    "B": "$y = 4$",
                                    "C": "$y = 7$",
                                    "D": "$y = 3$"
                        },
                        "answer": "B",
                        "explanation": "$2y = 14 - 6 = 8$, entonces $y = 4$."
            },
            {
                        "question": "Si la razón entre dos números es $3:5$ y su suma es 40, el número menor es:",
                        "options": {
                                    "A": "12",
                                    "B": "15",
                                    "C": "24",
                                    "D": "8"
                        },
                        "answer": "B",
                        "explanation": "$3k + 5k = 40 \\implies 8k = 40 \\implies k = 5$. El menor es $3 \\times 5 = 15$."
            }
]
        render_multiple_choice_quiz(_quiz_data, key_prefix="n34_quiz")
