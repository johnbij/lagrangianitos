import streamlit as st


def render_N26():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("""## N26: Composición y Descomposición de Proporciones

    ---

    ### 🏛️ Contexto Histórico: Los Agrimensores y el Reparto de Tierras

    En el antiguo Egipto, cuando el río Nilo se desbordaba, borraba los límites de los terrenos. Los agrimensores debían repartir la tierra de nuevo manteniendo las proporciones originales, pero basándose en el **área total** disponible después de la inundación. Para no calcular cada parcela desde cero, usaban la lógica de la **composición**: si conocían la razón de las partes, podían proyectar cuánto le correspondía a cada uno respecto al total sumado. Esta técnica permitió que la paz social se mantuviera gracias a un cálculo rápido y transparente.

    ---

    <div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1565C0; margin-top: 0;"> Componer una Proporción</h2>
        Componer significa <b>sumar el consecuente al antecedente</b> en ambos lados de la igualdad. Se usa cuando el problema te entrega la <b>suma total</b> de dos cantidades.
        <br><br>
        Si $\\frac{a}{b} = \\frac{c}{d}$, entonces:
        $$\\frac{a + b}{b} = \\frac{c + d}{d} \\quad \\text{o} \\quad \\frac{a}{a + b} = \\frac{c}{c + d}$$
    </div>

    ### 🛡️ Descomponer una Proporción
    Descomponer consiste en <b>restar el consecuente al antecedente</b>. Es la herramienta ideal cuando el dato del problema es la <b>diferencia</b> entre las cantidades.
    $$\\frac{a - b}{b} = \\frac{c - d}{d} \\quad \\text{o} \\quad \\frac{a}{a - b} = \\frac{c}{c - d}$$

    ### 🛡️ Suma de Antecedentes y Consecuentes
    Si tienes una serie de razones iguales: $\\frac{a}{b} = \\frac{c}{d} = \\frac{e}{f} = k$
    Entonces, la suma de todos los "arriba" partida por la de todos los "abajo" mantiene la misma constante:
    $$\\frac{a + c + e}{b + d + f} = k$$

    -----------------
    **Típ:** Si el problema te da el "total", usa composición sumando los términos de la razón. Si te dice "cuánto más" tiene uno que otro, usa descomposición restándolos. ¡Te ahorras todo el despeje de la $k$!

    ---

    "La arquitectura es una música de proporciones hecha piedra."  
    — **Le Corbusier**""", unsafe_allow_html=True)
        st.markdown("---")

    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: Componer y Descomponer

**E01. Composición con suma total.** Dos números están en razón $3 : 7$ y su suma es 100. Hallar el menor.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Plantear proporción original | $\\frac{a}{b} = \\frac{3}{7}$ |
| 2 | Componer (sumar razón) | $\\frac{a + b}{a} = \\frac{3 + 7}{3} \\implies \\frac{100}{a} = \\frac{10}{3}$ |
| 3 | Despejar $a$ (Simetría) | $\\frac{a}{100} = \\frac{3}{10} \\implies a = 30$ |
| 4 | Resultado final | El menor es 30. |

**E02. Descomposición con diferencia.** La razón entre dos sueldos es $5 : 2$. Si uno gana \\$300.000 más que el otro, ¿cuál es el sueldo menor?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Plantear proporción | $\\frac{a}{b} = \\frac{5}{2}$ |
| 2 | Descomponer (restar razón) | $\\frac{a - b}{b} = \\frac{5 - 2}{2} \\implies \\frac{300.000}{b} = \\frac{3}{2}$ |
| 3 | Despejar $b$ | $b = \\frac{300.000 \\cdot 2}{3}$ |
| 4 | Resultado final | \\$200.000 |

**E03. Componer y Descomponer a la vez.** Si $a/b = 5/4$, ¿cuánto vale $\\frac{a+b}{a-b}$?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Aplicar la propiedad mixta | $\\frac{a + b}{a - b} = \\frac{5 + 4}{5 - 4}$ |
| 2 | Resolver las operaciones | $9 / 1$ |
| 3 | Resultado final | 9 |

**E04. Serie de razones.** Si $\\frac{a}{2} = \\frac{b}{3} = \\frac{c}{5}$ y $a+b+c = 50$, hallar $c$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Sumar antecedentes y consecuentes | $\\frac{a+b+c}{2+3+5} = k \\implies \\frac{50}{10} = k$ |
| 2 | Hallar valor de $k$ | $k = 5$ |
| 3 | Despejar $c$ desde su razón | $\\frac{c}{5} = 5 \\implies c = 25$ |
| 4 | Resultado final | 25 |

**E05. Diferencia en serie de razones.** Si $x/10 = y/4$ y $x - y = 12$, hallar $x$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Descomponer la serie | $\\frac{x - y}{10 - 4} = k$ |
| 2 | Reemplazar valores | $12 / 6 = 2 \\implies k = 2$ |
| 3 | Calcular $x$ | $x / 10 = 2 \\implies x = 20$ |
| 4 | Resultado final | 20 |""")
    with st.expander("❓ Cuestionario N26", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': 'Si $a : b = 5 : 4$ y $a + b = 18$, ¿cuál es el valor de $a$ usando composición?', 'options': {'A': '10\\', 'B': '8\\', 'C': '9\\', 'D': '12'}, 'answer': 'A', 'explanation': 'Componiendo: $\\frac{a + b}{a} = \\frac{5 + 4}{5} \\implies \\frac{18}{a} = \\frac{9}{5} \\implies a = 10$.'},
            {'question': 'En la proporción $\\frac{x}{y} = \\frac{7}{3}$, la expresión compuesta $\\frac{x + y}{y}$ equivale a:', 'options': {'A': '$10 / 3$\\', 'B': '$10 / 7$\\', 'C': '$4 / 3$\\', 'D': '$7 / 10$'}, 'answer': 'A', 'explanation': 'Por definición de composición: $\\frac{7 + 3}{3} = 10 / 3$.'},
            {'question': 'Dos números están en razón $9 : 5$. Si su diferencia es 12, ¿cuál es el número mayor?', 'options': {'A': '15\\', 'B': '27\\', 'C': '20\\', 'D': '45'}, 'answer': 'B', 'explanation': 'Descomponiendo: $\\frac{a - b}{a} = \\frac{9 - 5}{9} \\implies \\frac{12}{a} = \\frac{4}{9} \\implies a = 27$.'},
            {'question': 'Si $\\frac{a}{b} = \\frac{3}{2}$, ¿cuál es el valor de la expresión $\\frac{a + b}{a - b}$?', 'options': {'A': '5\\', 'B': '1\\', 'C': '1,5\\', 'D': '6'}, 'answer': 'A', 'explanation': 'Aplicando la propiedad mixta: $\\frac{3 + 2}{3 - 2} = 5 / 1 = 5$.'},
            {'question': 'En una serie de razones $\\frac{a}{3} = \\frac{b}{4} = \\frac{c}{5} = k$, si $a+b+c = 60$, el valor de $k$ es:', 'options': {'A': '5\\', 'B': '12\\', 'C': '10\\', 'D': '15\\'}, 'answer': 'A', 'explanation': 'Suma de antecedentes (60) entre suma de consecuentes ($3+4+5=12$): $60 / 12 = 5$.'},
            {'question': 'Si $x : y = 11 : 8$ y se sabe que $x - y = 9$, el valor de $y$ es:', 'options': {'A': '33\\', 'B': '24\\', 'C': '3\\', 'D': '11\\'}, 'answer': 'B', 'explanation': 'Descomponiendo respecto a $y$: $\\frac{x - y}{y} = \\frac{11 - 8}{8} \\implies \\frac{9}{y} = \\frac{3}{8} \\implies y = 24$.'},
            {'question': 'La propiedad $\\frac{a}{a - b} = \\frac{c}{c - d}$ se conoce como:', 'options': {'A': 'Composición\\', 'B': 'Descomposición\\', 'C': 'Alternar medios\\', 'D': 'Inversión\\'}, 'answer': 'B', 'explanation': 'Se trata de una variante de la descomposición al restar el consecuente.'},
            {'question': 'Si $\\frac{a}{b} = \\frac{5}{2}$, entonces $\\frac{a - b}{a + b}$ es igual a:', 'options': {'A': '$3 / 7$\\', 'B': '$7 / 3$\\', 'C': '$3 / 5$\\', 'D': '$2 / 5$'}, 'answer': 'A', 'explanation': '$\\frac{5 - 2}{5 + 2} = 3 / 7$.'},
            {'question': 'En un curso, la razón aprobados/reprobados es $7 : 2$. Si el curso tiene 36 alumnos, ¿cuántos aprobaron?', 'options': {'A': '28\\', 'B': '8\\', 'C': '14\\', 'D': '30'}, 'answer': 'A', 'explanation': 'Componiendo: $\\frac{Aprob}{Total} = \\frac{7}{7 + 2} \\implies \\frac{Aprob}{36} = \\frac{7}{9} \\implies Aprob = 28$.'},
            {'question': 'Si $\\frac{x}{2} = \\frac{y}{5} = \\frac{z}{3}$ y $x+y+z = 100$, ¿cuál es el valor de $y$?', 'options': {'A': '20\\', 'B': '50\\', 'C': '30\\', 'D': '10'}, 'answer': 'B', 'explanation': '$k = 100 / (2+5+3) = 10$. Luego $y = 5 \\cdot 10 = 50$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n26_quiz")
    with st.expander("✅ Pauta - N26", expanded=False):
        st.markdown("""# ✅ Pauta - Cuestionario N26

1. **A.** Componiendo: $\\frac{a + b}{a} = \\frac{5 + 4}{5} \\implies \\frac{18}{a} = \\frac{9}{5} \\implies a = 10$.
2. **A.** Por definición de composición: $\\frac{7 + 3}{3} = 10 / 3$.
3. **B.** Descomponiendo: $\\frac{a - b}{a} = \\frac{9 - 5}{9} \\implies \\frac{12}{a} = \\frac{4}{9} \\implies a = 27$.
4. **A.** Aplicando la propiedad mixta: $\\frac{3 + 2}{3 - 2} = 5 / 1 = 5$.
5. **A.** Suma de antecedentes (60) entre suma de consecuentes ($3+4+5=12$): $60 / 12 = 5$.
6. **B.** Descomponiendo respecto a $y$: $\\frac{x - y}{y} = \\frac{11 - 8}{8} \\implies \\frac{9}{y} = \\frac{3}{8} \\implies y = 24$.
7. **B.** Se trata de una variante de la descomposición al restar el consecuente.
8. **A.** $\\frac{5 - 2}{5 + 2} = 3 / 7$.
9. **A.** Componiendo: $\\frac{Aprob}{Total} = \\frac{7}{7 + 2} \\implies \\frac{Aprob}{36} = \\frac{7}{9} \\implies Aprob = 28$.
10. **B.** $k = 100 / (2+5+3) = 10$. Luego $y = 5 \\cdot 10 = 50$.""")