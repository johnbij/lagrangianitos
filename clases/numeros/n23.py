import streamlit as st


def render_N23():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("## N23: Razones - ¿Cómo comparamos dos magnitudes?")
        st.markdown("---")

        st.markdown("### 🏛️ Contexto Histórico: El Canon de Policleto y la Belleza Matemática")
        st.markdown("""
    En la antigua Grecia, la belleza no era una opinión, era una proporción. El escultor **Policleto** escribió un tratado llamado *El Canon*, donde explicaba que para que un cuerpo humano fuera perfecto, todas sus partes debían estar en una **razón** específica. Por ejemplo, la altura total debía ser exactamente 7 veces la altura de la cabeza. Los griegos entendieron que la armonía de la arquitectura y el arte dependía de estas relaciones numéricas. Hoy, usamos esas mismas razones para todo: desde la mezcla de concreto en una obra hasta la escala de un mapa o la resolución de la pantalla de tu celular (16:9).
        """)
        st.markdown("---")

        st.markdown("""
    <div style="background-color: #E8F5E9; border-left: 8px solid #2E7D32; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1B5E20; margin-top: 0;">¿Qué es una Razón?</h2>
        Una razón es una comparación entre dos cantidades mediante una <b>división</b> (cociente). Nos dice cuántas veces una cantidad contiene a la otra.
        <ul>
            <li><b>Notación:</b> $a : b$ o $\\frac{a}{b}$ (Se lee "a es a b").</li>
            <li><b>Antecedente (a):</b> Lo que estoy comparando.</li>
            <li><b>Consecuente (b):</b> Mi punto de referencia ($b \\neq 0$).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

        st.markdown("### 🛡️ El Valor de la Razón")
        st.markdown("""
    El resultado de la división $a/b = k$ se llama **Valor de la Razón**.
    * Si la razón entre la altura de un edificio y su sombra es $12 : 4$, el valor de la razón es **3**. Esto significa que el edificio es 3 veces más grande que su sombra.
        """)

        st.markdown("### 🛡️ El Concepto Maestro: La Constante $k$")
        st.markdown("""
    Este es el secreto para "programar" cualquier problema de razones. Cuando decimos que dos cantidades están en razón $3 : 5$, estamos diciendo que:
    * La primera cantidad son 3 "partes" iguales ($3k$).
    * La segunda cantidad son 5 "partes" iguales ($5k$).
    * **$k$** es el valor de **una sola parte**.

    **Típ:** Siempre que veas una razón, agrégale la $k$ de inmediato. Si te dan el total, suma las $k$; si te dan la diferencia, réstalas. Es infalible.
        """)

        st.markdown("### 🛡️ Razones Compuestas (Series de razones)")
        st.markdown("""
    Podemos comparar tres o más magnitudes al mismo tiempo:
    * $a : b : c = 2 : 4 : 7$  
    Significa que por cada 2 partes de $a$, hay 4 de $b$ y 7 de $c$. El total de partes es $2k+4k+7k = 13k$.
        """)

        st.markdown("---")
        st.markdown("""
    ### ⚠️ Errores Típicos a Evitar:
    1. **Unidades distintas:** No compares 2 metros con 50 cm. Pasa todo a la misma unidad (200 cm : 50 cm = $4:1$).
    2. **Confundir orden:** La razón $2:3$ no es lo mismo que $3:2$. El que se nombra primero, va arriba.
        """)

        st.markdown("---")
        st.info("*\"La razón es un faro que guía, pero no debe ser la única luz en el camino del descubrimiento.\"*")

        st.markdown("---")

    with st.expander("📝 Guía de Ejemplos: El Poder de la Constante k", expanded=False):
        st.markdown("""
**E01. Hallar cantidades dado el total.** La razón entre hombres y mujeres en una fiesta es $4 : 5$. Si en total hay 180 personas, ¿cuántas mujeres hay?

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Definir las cantidades con $k$ | H = $4k$, M = $5k$ |
| 2 | Plantear la ecuación del total | $4k + 5k = 180 \\implies 9k = 180$ |
| 3 | Hallar el valor de una parte ($k$) | $k = 20$ |
| 4 | Calcular la cantidad solicitada (M) | $5 \\cdot 20 = 100$ mujeres |

**E02. Hallar cantidades dada la diferencia.** Las edades de Juan y Diego están en razón $3 : 7$. Si Diego es 20 años mayor que Juan, ¿qué edad tiene Juan?

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Definir con $k$ | J = $3k$, D = $7k$ |
| 2 | Plantear la diferencia | $7k - 3k = 20 \\implies 4k = 20$ |
| 3 | Hallar $k$ | $k = 5$ |
| 4 | Calcular edad de Juan | $3 \\cdot 5 = 15$ años |

**E03. Razón con unidades distintas.** ¿Cuál es la razón entre un segmento de 12 cm y otro de 3 metros?

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Convertir todo a cm | 12 cm y 300 cm |
| 2 | Escribir como división | $12 / 300$ |
| 3 | Simplificar al máximo | $1 / 25$ |
| 4 | Resultado final | La razón es $1 : 25$ |

**E04. Serie de razones.** En un triángulo, sus ángulos interiores están en razón $2 : 3 : 4$. ¿Cuánto mide el ángulo mayor?

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Definir ángulos con $k$ | $2k, 3k, 4k$ |
| 2 | Recordar que la suma es 180° | $2k + 3k + 4k = 180$ |
| 3 | Resolver $k$ | $9k = 180 \\implies k = 20$ |
| 4 | Calcular ángulo mayor ($4k$) | $4 \\cdot 20 = 80°$ |

**E05. Encontrar la razón.** En un curso de 40 alumnos, 15 son reprobados. ¿Cuál es la razón entre aprobados y el total?

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Calcular aprobados | $40 - 15 = 25$ |
| 2 | Identificar antecedente y consecuente | Aprobados (25) : Total (40) |
| 3 | Simplificar la fracción | $25/40 = 5/8$ |
| 4 | Resultado final | $5 : 8$ |
        """)

    with st.expander("❓ Cuestionario N23", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': 'En un canasto, la razón entre manzanas y peras es $3 : 2$. Si hay 12 manzanas, ¿cuántas peras hay?', 'options': {'A': '8', 'B': '10', 'C': '18', 'D': '24'}, 'answer': 'A', 'explanation': '$3k = 12 \\implies k = 4$. Peras: $2k = 2 \\cdot 4 = 8$.'},
            {'question': 'La razón entre dos números es $5 : 8$ y su suma es 65. ¿Cuál es el número menor?', 'options': {'A': '25', 'B': '40', 'C': '13', 'D': '30'}, 'answer': 'A', 'explanation': '$5k + 8k = 65 \\implies 13k = 65 \\implies k = 5$. Menor: $5 \\cdot 5 = 25$.'},
            {'question': 'Si $a : b = 3 : 4$ y $b = 20$, ¿cuál es el valor de $a$?', 'options': {'A': '12', 'B': '15', 'C': '16', 'D': '27'}, 'answer': 'B', 'explanation': '$b = 4k = 20 \\implies k = 5$. Luego $a = 3 \\cdot 5 = 15$.'},
            {'question': 'En un mapa a escala $1 : 50.000$, dos ciudades están separadas por 4 cm. ¿Cuál es la distancia real?', 'options': {'A': '2 km', 'B': '20 km', 'C': '200 m', 'D': '50 km'}, 'answer': 'A', 'explanation': '$1 : 50.000 \\implies 1 \\text{ cm real es } 50.000 \\text{ cm}$. $4 \\cdot 50.000 = 200.000 \\text{ cm} = 2 \\text{ km}$.'},
            {'question': 'Las edades de un padre y su hijo están en razón $10 : 3$. Si la diferencia de sus edades es 28 años, ¿qué edad tiene el hijo?', 'options': {'A': '12 años', 'B': '15 años', 'C': '18 años', 'D': '40 años'}, 'answer': 'A', 'explanation': '$10k - 3k = 28 \\implies 7k = 28 \\implies k = 4$. Hijo: $3 \\cdot 4 = 12$ años.'},
            {'question': '¿Cuál es la razón entre 500 gramos y 2 kilogramos?', 'options': {'A': '$250 : 1$', 'B': '$1 : 4$', 'C': '$1 : 2$', 'D': '$4 : 1$'}, 'answer': 'B', 'explanation': 'Convertir a gramos: $500 : 2.000$. Simplificando queda $1 : 4$.'},
            {'question': 'Tres socios reparten una ganancia en razón $2 : 3 : 5$. Si el que menos recibe obtiene \$200.000, ¿cuál fue la ganancia total?', 'options': {'A': '\$500.000', 'B': '\$1.000.000', 'C': '\$2.000.000', 'D': '\$400.000'}, 'answer': 'B', 'explanation': 'Menor recibe $2k = 200.000 \\implies k = 100.000$. Total: $(2+3+5)k = 10k = 1.000.000$.'},
            {'question': 'En una mezcla de colores, el azul y el rojo están en razón $3 : 7$. Si se usan 21 litros de rojo, ¿cuántos litros de azul se necesitan?', 'options': {'A': '3 litros', 'B': '9 litros', 'C': '14 litros', 'D': '10 litros'}, 'answer': 'B', 'explanation': 'Rojo: $7k = 21 \\implies k = 3$. Azul: $3k = 3 \\cdot 3 = 9$ litros.'},
            {'question': 'Si el antecedente de una razón es 15 y el valor de la razón es 3, ¿cuál es el consecuente?', 'options': {'A': '45', 'B': '12', 'C': '5', 'D': '18'}, 'answer': 'C', 'explanation': '$15 / b = 3 \\implies 15 = 3b \\implies b = 5$.'},
            {'question': 'Las medidas de los lados de un rectángulo están en razón $2 : 5$. Si el perímetro es 70 cm, ¿cuál es el área?', 'options': {'A': '100 cm²', 'B': '250 cm²', 'C': '700 cm²', 'D': '140 cm²'}, 'answer': 'B', 'explanation': 'Lados: $2k$ y $5k$. Perímetro: $2(2k + 5k) = 70 \\implies 14k = 70 \\implies k = 5$. Lados son 10 y 25. Área: $10 \\cdot 25 = 250$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n23_quiz")

