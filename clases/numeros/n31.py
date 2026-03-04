import streamlit as st


def render_N31():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("""## N31: Proporcionalidad Directa - El Efecto Espejo

    ---

    ### 🏛️ Contexto Histórico: El Origen del Valor

    Desde que el primer comerciante cambió granos de sal por pieles en Mesopotamia, la proporcionalidad directa ha regido la economía. Los matemáticos griegos, como **Euclides**, formalizaron esto como la "Teoría de las Magnitudes". Ellos entendieron que el universo tiene reglas de escala: si duplicas el tamaño de una columna, necesitas el doble de material. Esta relación lineal es la base de toda la ingeniería y la contabilidad moderna: es la seguridad de saber que el sistema es predecible y justo.

    ---

    <div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1565C0; margin-top: 0;"> 🛡️ Definición: Los Partners</h2>
        Dos variables $x$ e $y$ son <b>directamente proporcionales</b> si son "compañeras totales": lo que le pase a una, le pasa a la otra en la misma intensidad.
        <br><br>
        <ul>
            <li>Si duplicas $x$, entonces $y$ se duplica.</li>
            <li>Si $x$ baja a la tercera parte, $y$ también baja a la tercera parte.</li>
        </ul>
        <b>Regla de Oro:</b> Siempre se mueven en la misma dirección y con la misma fuerza.
    </div>

    ### 🛡️ La Constante de Proporcionalidad ($k$)
    En este tipo de relación, el **cociente** (la división) entre las dos variables es siempre el mismo. Es como el "ADN" de la relación:

    $$\\frac{y}{x} = k \\quad \\implies \\quad y = k \\cdot x$$

    * **$k$** es la constante. Si conoces un punto $(x, y)$, conoces a $k$ para siempre.
    * **Típ:** En física y economía, $k$ suele representar un precio unitario, una velocidad constante o una densidad.

    ### 🛡️ Representación Gráfica: El Camino Recto
    El gráfico es **siempre una línea recta que pasa obligatoriamente por el origen $(0,0)$**.
    * Si la recta parte más arriba o más abajo del punto $(0,0)$, **no es proporcionalidad directa** (aunque sea una recta).
    * La inclinación (pendiente) de la recta es el valor de $k$.



    ### 🛡️ Identificación en Tablas
    Para pillar una proporción directa en una tabla, solo divide $y$ por $x$. Si el número se repite, ¡bingo!

    | $x$ (Litros) | $y$ (Precio) | $y / x = k$ |
    | :--- | :--- | :--- |
    | 2 | 10 | $10/2 = 5$ |
    | 5 | 25 | $25/5 = 5$ |
    | 10 | 50 | $50/10 = 5$ |

    ---

    "Donde hay medida y proporción, hay lugar para la razón."  
    — **Anónimo**""", unsafe_allow_html=True)
        st.markdown("---")

    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: Dominando la Directa

**E01. Encontrar valores faltantes usando la constante $k$.**
Si $x$ e $y$ son directamente proporcionales, y sabemos que cuando $x = 4$, $y = 20$. ¿Cuánto vale $y$ cuando $x = 9$?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Calcular la constante $k$ | $k = 20 / 4 = 5$ |
| 2 | Plantear la ecuación con el nuevo $x$ | $y = 5 \\cdot 9$ |
| 3 | Resultado final | $y = 45$ |

**E02. Identificar si una tabla es Directa.**
| x | 3 | 6 | 10 |
| :--- | :--- | :--- | :--- |
| y | 12 | 24 | 40 |
**Análisis:** $12/3 = 4$; $24/6 = 4$; $40/10 = 4$. Como el cociente es constante ($k=4$), es **Directa**.

**E03. Problema de aplicación PAES.**
Un auto recorre 180 km con 12 litros de bencina. ¿Cuántos kilómetros recorrerá con 20 litros?
| Magnitud A (Litros) | Magnitud B (Km) | Razón ($k$) |
| :--- | :--- | :--- |
| 12 | 180 | $180/12 = 15$ |
| 20 | $x$ | $x = 20 \\cdot 15$ |
**Resultado:** Recorrerá 300 km.

**E04. Reconocimiento gráfico.**
¿Cuál de estos puntos pertenece a una proporción directa que pasa por $(2, 8)$?
1. $(3, 12)$
2. $(5, 15)$
**Análisis:** Si pasa por $(2, 8)$, entonces $k = 8/2 = 4$.
* En el punto 1: $12/3 = 4$ (Sí pertenece).
* En el punto 2: $15/5 = 3$ (No pertenece).

**E05. Situación de escala.**
Si un mapa tiene una escala $1:500.000$. ¿A cuántos km equivalen 4 cm en el mapa?
**Análisis:** Es directa. $1 \\text{ cm} \\rightarrow 500.000 \\text{ cm}$.
$4 \\text{ cm} \\rightarrow 2.000.000 \\text{ cm} = 20 \\text{ km}$.""")
    with st.expander("❓ Cuestionario N31", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': 'Dos variables son directamente proporcionales cuando:', 'options': {'A': 'Al aumentar una, la otra disminuye. \\', 'B': 'Su suma es siempre constante. \\', 'C': 'Al triplicar una, la otra también se triplica. \\', 'D': 'Su gráfico es una curva que no toca el origen.'}, 'answer': 'C', 'explanation': 'Es la definición técnica: el cambio en una se replica exactamente en la misma razón en la otra.'},
            {'question': 'Si $x$ e $y$ son directamente proporcionales y $k=3$, ¿cuál es el valor de $y$ si $x=15$?', 'options': {'A': '5 \\', 'B': '45 \\', 'C': '18 \\', 'D': '12'}, 'answer': 'B', 'explanation': 'Usamos la fórmula $y = k \\cdot x \\implies y = 3 \\cdot 15 = 45$.'},
            {'question': 'El gráfico de una proporción directa se caracteriza por ser una línea recta que:', 'options': {'A': 'Corta al eje Y en el punto (0,5). \\', 'B': 'Es paralela al eje X. \\', 'C': 'Pasa por el origen de coordenadas (0,0). \\', 'D': 'Es una curva descendente.'}, 'answer': 'C', 'explanation': 'Condición esencial: si no pasa por el origen, no hay proporción directa.'},
            {'question': 'Si 5 kg de papas cuestan \\$2.500, ¿cuánto cuestan 8 kg?', 'options': {'A': '\\$3.500 \\', 'B': '\\$4.000 \\', 'C': '\\$4.500 \\', 'D': '\\$5.000'}, 'answer': 'B', 'explanation': 'Calculamos $k = 2500/5 = 500$ por kg. Luego $500 \\cdot 8 = 4000$.'},
            {'question': 'En la tabla siguiente, ¿cuál es el valor de la constante de proporcionalidad $k$?', 'options': {'A': '2 \\', 'B': '0,5 \\', 'C': '4 \\', 'D': '1'}, 'answer': 'B', 'explanation': '$k = y/x$. Entonces $2/4 = 0,5$. (Ojo con el orden de la división).'},
            {'question': 'Si una variable $y$ es directamente proporcional a $x$, ¿cuál de las siguientes expresiones es correcta?', 'options': {'A': '$y = x + k$ \\', 'B': '$x \\cdot y = k$ \\', 'C': '$y/x = k$ \\', 'D': '$y = k/x$'}, 'answer': 'C', 'explanation': 'El cociente constante define la relación directa.'},
            {'question': 'Un corredor recorre 2 km en 10 minutos. Si mantiene su ritmo (velocidad constante), ¿cuánto tardará en recorrer 5 km?', 'options': {'A': '20 minutos \\', 'B': '25 minutos \\', 'C': '30 minutos \\', 'D': '15 minutos'}, 'answer': 'B', 'explanation': '$k = 10/2 = 5$ min por km. Para 5 km: $5 \\cdot 5 = 25$ minutos.'},
            {'question': 'Si $y$ es directamente proporcional a $x$, y cuando $x=10$, $y=2$. ¿Cuánto vale $x$ cuando $y=8$?', 'options': {'A': '40 \\', 'B': '16 \\', 'C': '80 \\', 'D': '4'}, 'answer': 'A', 'explanation': '$k = y/x = 2/10 = 0,2$. Si $y=8$, entonces $8/x = 0,2 \\implies x = 8/0,2 = 40$.'},
            {'question': '¿Cuál de los siguientes gráficos representa una Proporcionalidad Directa?', 'options': {'A': 'Una recta que pasa por (1,2) y (2,4). \\', 'B': 'Una recta que pasa por (0,2) y (2,4). \\', 'C': 'Una curva que pasa por (1,1) y (2,4). \\', 'D': 'Una recta horizontal en $y=3$.'}, 'answer': 'A', 'explanation': 'Comprobamos $k$: $2/1 = 2$ y $4/2 = 2$. Al ser constante y pasar por el origen (implícito), es directa. En la opción B, $k$ cambia ($2/0$ es indefinido y $4/2$ es 2).'},
            {'question': 'Si en una receta para 4 personas se usan 2 huevos, ¿cuántos huevos se necesitan para 10 personas?', 'options': {'A': '4 huevos \\', 'B': '5 huevos \\', 'C': '6 huevos \\', 'D': '8 huevos'}, 'answer': 'B', 'explanation': '$k = 2/4 = 0,5$ huevos por persona. Para 10 personas: $10 \\cdot 0,5 = 5$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n31_quiz")
    with st.expander("✅ Pauta - N31", expanded=False):
        st.markdown("""# ✅ Pauta Explicativa - Cuestionario N31

1. **C.** Es la definición técnica: el cambio en una se replica exactamente en la misma razón en la otra.
2. **B.** Usamos la fórmula $y = k \\cdot x \\implies y = 3 \\cdot 15 = 45$.
3. **C.** Condición esencial: si no pasa por el origen, no hay proporción directa.
4. **B.** Calculamos $k = 2500/5 = 500$ por kg. Luego $500 \\cdot 8 = 4000$.
5. **B.** $k = y/x$. Entonces $2/4 = 0,5$. (Ojo con el orden de la división).
6. **C.** El cociente constante define la relación directa.
7. **B.** $k = 10/2 = 5$ min por km. Para 5 km: $5 \\cdot 5 = 25$ minutos.
8. **A.** $k = y/x = 2/10 = 0,2$. Si $y=8$, entonces $8/x = 0,2 \\implies x = 8/0,2 = 40$.
9. **A.** Comprobamos $k$: $2/1 = 2$ y $4/2 = 2$. Al ser constante y pasar por el origen (implícito), es directa. En la opción B, $k$ cambia ($2/0$ es indefinido y $4/2$ es 2).
10. **B.** $k = 2/4 = 0,5$ huevos por persona. Para 10 personas: $10 \\cdot 0,5 = 5$.""")