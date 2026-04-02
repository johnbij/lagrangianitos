import streamlit as st


def render_N24():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("## N24: Proporciones - La Igualdad entre Razones")
        st.markdown("---")

        st.markdown("### 🏛️ Contexto Histórico: El Reparto Justo y la Regla de Tres")
        st.markdown("""
    Históricamente, antes de que existiera el álgebra moderna, los mercaderes de la Ruta de la Seda necesitaban sistemas rápidos para calcular precios y trueques. Si 3 sacos de especias valían 10 monedas, ¿cuánto valían 15 sacos? No usaban fórmulas complejas, sino que entendían que la relación entre el producto y el precio debía mantenerse constante. Esa búsqueda de una "cuarta cantidad" a partir de tres conocidas permitió el desarrollo de lo que hoy llamamos **proporción**. Fue la herramienta que permitió que el comercio global funcionara de manera justa mucho antes de que se inventaran las calculadoras.
        """)
        st.markdown("---")

        st.markdown("""
    <div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1565C0; margin-top: 0;">¿Qué es una Proporción?</h2>
        Es la <b>igualdad</b> entre dos o más razones. Cuando comparamos dos razones y ambas nos entregan exactamente el mismo valor <b>k</b>, decimos que estamos en presencia de una proporción.
        $$\\frac{a}{b} = k \\quad \\text{y} \\quad \\frac{c}{d} = k \\quad \\implies \\quad \\frac{a}{b} = \\frac{c}{d}$$
        Se lee: <b>"a es a b como c es a d"</b>.
    </div>
    """, unsafe_allow_html=True)

        st.markdown("### 🛡️ Teorema Fundamental de las Proporciones")
        st.markdown("""
    En toda proporción, el producto de los **extremos** es igual al producto de los **medios**. Es lo que conocemos comúnmente como "multiplicar cruzado":
    $$a \\cdot d = b \\cdot c$$
        """)

        st.markdown("### 🛡️ Hacia las Ecuaciones")
        st.markdown("""
    Fíjate que al tener esta igualdad de razones que comparten el valor $k$, si nos falta un dato, podemos despejarlo. Esto que estás haciendo ahora de buscar un valor desconocido en una igualdad es el corazón de las **ecuaciones**, la herramienta reina de este eje y que estudiaremos a fondo muy pronto.
        """)

        st.markdown("---")
        st.markdown("""
    **Típ:** Una proporción solo existe si ambas razones valen lo mismo ($k$). Si multiplicas cruzado y los resultados son iguales, la proporción es real. Si te falta un dato, despeja la igualdad multiplicando los que están cruzados y dividiendo por el que quedó solo.
        """)
        st.markdown("---")
        st.info('*"Donde hay medida hay número, y donde hay número hay proporción."*  \n— **San Agustín**')

        st.markdown("---")

    with st.expander("📝 Guía de Ejemplos: Proporciones e Igualdad de k", expanded=False):
        st.markdown("""
**1. Hallar el término desconocido.** En la proporción $x : 4 = 15 : 6$, ¿cuál es el valor de $x$?

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Plantear la igualdad como fracciones | $\\frac{x}{4} = \\frac{15}{6}$ |
| 2 | Aplicar teorema fundamental (cruzar) | $6 \\cdot x = 4 \\cdot 15$ |
| 3 | Resolver la multiplicación y despejar | $x = 60 / 6$ |
| 4 | Resultado final | $x = 10$ |

**2. Verificación mediante el valor k.** ¿Forman una proporción las razones $12 : 4$ y $30 : 10$?

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Calcular valor $k$ de la primera razón | $12 / 4 = 3$ |
| 2 | Calcular valor $k$ de la segunda razón | $30 / 10 = 3$ |
| 3 | Comparar los valores de $k$ | $3 = 3$ |
| 4 | Conclusión | Al ser el mismo valor $k$, es una proporción válida. |

**3. Uso de la constante k en igualdades.** Si $a/b = 2/3$ y $a + b = 20$, hallar el valor de $a$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Definir con constante $k$ | $a = 2k, b = 3k$ |
| 2 | Plantear la igualdad de la suma | $2k + 3k = 20 \\implies 5k = 20$ |
| 3 | Hallar el valor de $k$ | $k = 4$ |
| 4 | Calcular el valor real de $a$ | $2 \\cdot 4 = 8$ |

**4. Proporción con decimales.** Hallar el valor de $y$ en la igualdad $y : 0,5 = 10 : 2$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Plantear como igualdad de razones | $\\frac{y}{0,5} = \\frac{10}{2}$ |
| 2 | Multiplicar cruzado | $2 \\cdot y = 10 \\cdot 0,5$ |
| 3 | Resolver la multiplicación | $2y = 5$ |
| 4 | Resultado final | $y = 2,5$ |

**5. Incógnita en el consecuente.** Hallar $n$ en la igualdad $10 : 5 = 14 : n$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Plantear como igualdad de razones | $\\frac{10}{5} = \\frac{14}{n}$ |
| 2 | Multiplicar cruzado | $10 \\cdot n = 5 \\cdot 14$ |
| 3 | Resolver y despejar | $10n = 70 \\implies n = 7$ |
| 4 | Verificación del valor $k$ | $10/5=2$ y $14/7=2$. ✓ |
        """)

    with st.expander("❓ Cuestionario N24", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': 'En la proporción $\\frac{x}{12} = \\frac{3}{4}$, el valor de $x$ es:', 'options': {'A': '9', 'B': '16', 'C': '36', 'D': '6'}, 'answer': 'A', 'explanation': 'Multiplicamos cruzado: $4x = 36 \\implies x = 9$.'},
            {'question': 'Si se cumple que $2 : 7 = 10 : x$, ¿cuál es el valor de la incógnita $x$?', 'options': {'A': '14', 'B': '35', 'C': '70', 'D': '20'}, 'answer': 'B', 'explanation': 'Aplicamos el teorema fundamental: $2x = 70 \\implies x = 35$.'},
            {'question': '¿Cuál de las siguientes parejas de razones forma una proporción?', 'options': {'A': '$2:3$ y $4:5$', 'B': '$3:4$ y $9:12$', 'C': '$5:2$ y $10:5$', 'D': '$1:8$ y $2:10$'}, 'answer': 'B', 'explanation': 'Al dividir $3/4 = 0,75$ y $9/12 = 0,75$. Como el valor $k$ es el mismo, es proporción.'},
            {'question': 'Si $a/b = 5/3$ y se sabe que $a = 30$, ¿cuál es el valor de $b$?', 'options': {'A': '18', 'B': '10', 'C': '50', 'D': '15'}, 'answer': 'A', 'explanation': '$\\frac{30}{b} = \\frac{5}{3} \\implies 5b = 90 \\implies b = 18$.'},
            {'question': 'En una proporción, los medios son 8 y 15. Si uno de los extremos es 12, ¿cuál es el otro extremo?', 'options': {'A': '10', 'B': '120', 'C': '5', 'D': '20'}, 'answer': 'A', 'explanation': 'Producto de medios ($8 \\cdot 15 = 120$) = producto de extremos ($12 \\cdot x = 120$), por ende $x = 10$.'},
            {'question': 'Si $x$ e $y$ están en razón $3:5$ y su suma es 40, ¿cuál es el valor de $x$?', 'options': {'A': '15', 'B': '25', 'C': '8', 'D': '24'}, 'answer': 'A', 'explanation': 'Usando $k$: $3k + 5k = 40 \\implies 8k = 40 \\implies k = 5$. Por tanto $x = 3 \\cdot 5 = 15$.'},
            {'question': 'La cuarta proporcional entre los números 3, 6 y 10 es:', 'options': {'A': '5', 'B': '20', 'C': '30', 'D': '18'}, 'answer': 'B', 'explanation': 'Planteamos la igualdad $\\frac{3}{6} = \\frac{10}{x} \\implies 3x = 60 \\implies x = 20$.'},
            {'question': 'Si se cumple la igualdad $\\frac{18}{x} = \\frac{x}{2}$, ¿cuál es el valor positivo de $x$?', 'options': {'A': '6', 'B': '9', 'C': '36', 'D': '18'}, 'answer': 'A', 'explanation': 'Multiplicamos cruzado: $x^2 = 36$. El valor positivo es 6.'},
            {'question': 'Si por 3 lápices se pagan \$900, ¿cuánto se pagaría por 7 lápices?', 'options': {'A': '\$2.100', 'B': '\$1.800', 'C': '\$2.700', 'D': '\$300'}, 'answer': 'A', 'explanation': 'Planteamos la proporción $\\frac{3}{900} = \\frac{7}{x} \\implies 3x = 6.300 \\implies x = 2.100$.'},
            {'question': 'Si el producto de los extremos de una proporción es 72 y uno de los medios es 9, ¿cuál es el valor del otro medio?', 'options': {'A': '81', 'B': '63', 'C': '8', 'D': '648'}, 'answer': 'C', 'explanation': 'El producto de medios = producto de extremos (72). Si un medio es 9, el otro debe ser 8.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n24_quiz")

