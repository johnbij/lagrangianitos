import streamlit as st


def render_N15():
    with st.expander("📚 Teoría", expanded=False):
        st.title("N15: Herramientas de Inspección - El ADN de los Números")

        st.markdown(r"""
    ### 🏛️ Contexto Histórico: El Tamiz de Eratóstenes y los Ladrillos del Universo
    Hace más de 2.200 años, Eratóstenes (el mismo que midió la Tierra con una sombra) se dio cuenta de que había números que eran "especiales". Algunos números se podían desarmar en otros más chicos, pero otros eran como átomos: imposibles de dividir. A estos los llamó **Números Primos**.

    En el taller de la matemática, los números primos son los **ladrillos fundamentales**. Todo número que no es primo (compuesto) es simplemente una construcción hecha de primos. Entender esto es tener "visión de rayos X": cuando ves un 60, un maestro no ve un 60, ve $2 \cdot 2 \cdot 3 \cdot 5$. Esta técnica permitió a los antiguos simplificar cálculos astronómicos que hoy nos parecerían imposibles.

    ---

    ### 🛡️ El Teorema Fundamental: Factorización Prima
    Cualquier número entero mayor que 1 puede expresarse como un producto único de números primos. Es su **huella digital**.

    ### 🛠️ Cómo desarmar el motor (Árbol de Factores):
    Para encontrar los factores primos de un número (como el 40), lo dividimos sucesivamente por los primos más chicos (2, 3, 5, 7...):
    * 40 es $2 \cdot 20$
    * 20 es $2 \cdot 10$
    * 10 es $2 \cdot 5$
    * **Resultado:** $40 = 2^3 \cdot 5$

    **¿Para qué sirve esto?** Para simplificar fracciones. Si tienes $\frac{40}{60}$, y sabes que $60 = 2^2 \cdot 3 \cdot 5$, solo "tallas" los factores que se repiten arriba y abajo y llegas a $\frac{2}{3}$ sin dudar.

    ---

    ### 🛡️ Las Reglas de Inspección (Divisibilidad)
    No pierdas tiempo dividiendo. Usa estos atajos de "maestro pillo" para saber si el resto será cero:

    1. **Por 2:** Si termina en cifra par (0, 2, 4, 6, 8).
    2. **Por 3:** Si al **sumar sus dígitos**, el resultado está en la tabla del 3.
        * *Ejemplo:* 123 $\rightarrow 1+2+3 = 6$. ¡Es divisible por 3!
    3. **Por 4:** Si sus últimas dos cifras son 00 o un múltiplo de 4.
    4. **Por 5:** Si termina en 0 o 5.
    5. **Por 6:** Si es divisible por 2 y por 3 al mismo tiempo.
    6. **Por 9:** Si al sumar sus dígitos, el resultado es múltiplo de 9.
    7. **Por 10:** Si termina en 0.

    ---

    ### 🛡️ El MCD y el mcm: La Gestión de Repuestos
    * **MCD (Máximo Común Divisor):** Es el molde más grande que cabe exactamente en varios números. Se obtiene multiplicando los factores primos comunes con su **menor** exponente.
    * **mcm (mínimo común múltiplo):** Es el primer número donde se encuentran varios múltiplos. Se obtiene multiplicando todos los factores (comunes y no comunes) con su **mayor** exponente.

    ---

    ### 🛡️ La Densidad Racional: El espacio infinito
    A diferencia de los números naturales, donde entre el 5 y el 6 no hay nada, en los racionales **siempre hay espacio**.
    Si tienes $\frac{1}{2}$ y $\frac{3}{4}$, siempre puedes encontrar un número justo al medio (el promedio).
    **Técnica:** Sumas las fracciones y divides por 2. Esto demuestra que los números racionales son "densos": no importa cuánto te acerques, siempre hay más números en medio.

    > **Típ:** Si en la PAES te piden simplificar una fracción gigante, no empieces a dividir a lo loco. Suma los dígitos para ver si es divisible por 3 o 9, o mira la última cifra. Usa las reglas de inspección primero; ahorran tiempo y errores de cálculo.

    ---

    > "Los números primos son los átomos de la aritmética, las piezas indivisibles con las que se construye toda la realidad numérica".
    > — **Marcus du Sautoy**
    """)


    with st.expander("❓ Cuestionario N15", expanded=False):
        from utils import render_multiple_choice_quiz
        import json as _json
        _quiz_data = [
            {
                        "question": "¿Cuál de los siguientes números es primo?",
                        "options": {
                                    "A": "1",
                                    "B": "9",
                                    "C": "13",
                                    "D": "15"
                        },
                        "answer": "C",
                        "explanation": "13 solo es divisible por 1 y por sí mismo. El 1 no es primo, el 9 = 3×3, el 15 = 3×5."
            },
            {
                        "question": "La descomposición en factores primos de 12 es:",
                        "options": {
                                    "A": "$2 \\times 6$",
                                    "B": "$3 \\times 4$",
                                    "C": "$2^2 \\times 3$",
                                    "D": "$2 \\times 3^2$"
                        },
                        "answer": "C",
                        "explanation": "$12 = 4 \\times 3 = 2^2 \\times 3$."
            },
            {
                        "question": "El Mínimo Común Múltiplo (mcm) de 4 y 6 es:",
                        "options": {
                                    "A": "2",
                                    "B": "12",
                                    "C": "24",
                                    "D": "6"
                        },
                        "answer": "B",
                        "explanation": "Factores: $4 = 2^2$ y $6 = 2 \\times 3$. mcm $= 2^2 \\times 3 = 12$."
            },
            {
                        "question": "El Máximo Común Divisor (MCD) de 18 y 24 es:",
                        "options": {
                                    "A": "4",
                                    "B": "72",
                                    "C": "6",
                                    "D": "3"
                        },
                        "answer": "C",
                        "explanation": "$18 = 2 \\times 3^2$ y $24 = 2^3 \\times 3$. MCD $= 2 \\times 3 = 6$."
            },
            {
                        "question": "¿Cuál de los siguientes números es divisible por 3?",
                        "options": {
                                    "A": "124",
                                    "B": "211",
                                    "C": "132",
                                    "D": "145"
                        },
                        "answer": "C",
                        "explanation": "Un número es divisible por 3 si la suma de sus dígitos lo es. $1+3+2=6$, que es divisible por 3."
            },
            {
                        "question": "¿Cuántos divisores tiene el número 12?",
                        "options": {
                                    "A": "3",
                                    "B": "4",
                                    "C": "5",
                                    "D": "6"
                        },
                        "answer": "D",
                        "explanation": "Los divisores de 12 son: 1, 2, 3, 4, 6, 12. En total 6 divisores."
            },
            {
                        "question": "El criterio de divisibilidad por 9 establece que la suma de sus dígitos debe ser divisible por:",
                        "options": {
                                    "A": "3",
                                    "B": "6",
                                    "C": "9",
                                    "D": "18"
                        },
                        "answer": "C",
                        "explanation": "Si la suma de los dígitos es divisible por 9, el número también lo es."
            },
            {
                        "question": "¿Cuál es el mcm de 3, 4 y 6?",
                        "options": {
                                    "A": "12",
                                    "B": "24",
                                    "C": "72",
                                    "D": "6"
                        },
                        "answer": "A",
                        "explanation": "$3=3$, $4=2^2$, $6=2\\times3$. mcm $= 2^2 \\times 3 = 12$."
            },
            {
                        "question": "Un número par siempre es divisible por:",
                        "options": {
                                    "A": "4",
                                    "B": "2",
                                    "C": "6",
                                    "D": "3"
                        },
                        "answer": "B",
                        "explanation": "Por definición, un número par es divisible exactamente por 2."
            },
            {
                        "question": "Si el MCD de dos números es 1, entonces son:",
                        "options": {
                                    "A": "Múltiplos",
                                    "B": "Primos entre sí (coprimos)",
                                    "C": "Iguales",
                                    "D": "Primos absolutos"
                        },
                        "answer": "B",
                        "explanation": "Cuando MCD(a, b) = 1, se dice que a y b son coprimos o primos entre sí."
            }
]
        render_multiple_choice_quiz(_quiz_data, key_prefix="n15_quiz")
