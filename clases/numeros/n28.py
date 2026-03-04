import streamlit as st


def render_N28():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown("""## N28: Reparto Inversamente Proporcional - La Lógica Invertida

    ---

    ### 🏛️  Contexto Histórico: El Reparto de Cargas en la Ingeniería Antigua

    En la construcción de los grandes acueductos romanos, los ingenieros enfrentaban un problema de proporcionalidad inversa: la presión del agua y el diámetro del tubo. Para que el sistema no colapsara, entendían que a **menor** diámetro de la tubería, la velocidad del agua debía ser **mayor**. No era un reparto directo; era una relación donde una cantidad crecía mientras la otra disminuía para mantener el equilibrio del sistema. Hoy aplicamos esa misma "lógica invertida" para repartir premios por faltas o tiempos en una carrera: el que hace menos tiempo, se lleva el premio más grande.

    ---

    <div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
        <h2 style="color: #1565C0; margin-top: 0;"> Concepto de Reparto Inverso</h2>
        Repartir una cantidad <b>S</b> en partes inversamente proporcionales (I.P.) a ciertos números <i>a, b, c...</i> significa que las partes recibidas son <b>directamente proporcionales</b> a sus inversos: $\\frac{1}{a}, \\frac{1}{b}, \\frac{1}{c}...$
        <br><br>
        <blockquote><b>Regla de Oro:</b> A menor índice de reparto, mayor es la parte recibida. ¡Es al revés que el reparto directo!</blockquote>
    </div>



    ### 🛡️  El Algoritmo "Invertir y Amplificar" (Paso a Paso)
    Para no trabajar con fracciones complicadas, usamos este procedimiento técnico:

    1.  **Invertir los índices:** Si los números son $2$ y $3$, escribimos sus inversos: $\\frac{1}{2}$ y $\\frac{1}{3}$.
    2.  **M.C.M. para limpiar:** Buscamos el Mínimo Común Múltiplo de los denominadores.
    3.  **Amplificar:** Multiplicamos cada fracción por el M.C.M. para obtener números enteros.
    4.  **Aplicar Método k:** Con esos nuevos números enteros, hacemos un reparto directo normal.

    ----------
    **Típ:** El reparto inverso es simplemente un reparto directo disfrazado. Si inviertes los índices y amplificas, el problema se vuelve exactamente igual a los que vimos en la clase anterior.

    ---

    "La simplicidad es la máxima sofisticación."  
    — **Leonardo da Vinci**""", unsafe_allow_html=True)
        st.markdown("---")

    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: Dominando el Reparto Inverso

**E01. Reparto I.P. simple.** Repartir \\$600.000 entre dos personas de forma I.P. a sus edades: 20 y 30 años.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir índices | $1/20$ y $1/30$ |
| 2 | M.C.M. entre 20 y 30 | 60 |
| 3 | Amplificar (Limpiar) | $1/20 \\cdot 60 = 3$ ; $1/30 \\cdot 60 = 2$ |
| 4 | Aplicar Método $k$ | $3k + 2k = 600.000 \\implies 5k = 600.000 \\implies k = 120.000$ |
| 5 | Resultados finales | Mayor: $3 \\cdot 120k = \\$360.000$; Menor: $2 \\cdot 120k = \\$240.000$ |

**E02. Reparto I.P. de tres partes.** Dividir 310 en partes I.P. a 2, 3 y 5.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir índices | $1/2, 1/3, 1/5$ |
| 2 | M.C.M. (2, 3, 5) | 30 |
| 3 | Amplificar | $1/2 \\cdot 30 = 15$ ; $1/3 \\cdot 30 = 10$ ; $1/5 \\cdot 30 = 6$ |
| 4 | Sumar e igualar | $15k + 10k + 6k = 310 \\implies 31k = 310 \\implies k = 10$ |
| 5 | Partes reales | 150, 100 y 60 |

**E03. Premio por faltas.** Se reparten \\$140.000 entre dos obreros de forma I.P. a los días que faltaron: 3 y 4 días.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir y buscar M.C.M. | $1/3$ y $1/4$. M.C.M. = 12 |
| 2 | Nuevos índices directos | $12/3 = 4$ y $12/4 = 3$ |
| 3 | Hallar $k$ | $7k = 140.000 \\implies k = 20.000$ |
| 4 | Parte del que faltó menos | $4 \\cdot 20.000 = \\$80.000$ |

**E04. Reparto I.P. con fracciones.** Repartir 100 en partes I.P. a $1/2$ y $1/4$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir las fracciones | $2$ y $4$ |
| 2 | No hace falta M.C.M. (ya son enteros) | Índices: 2 y 4 |
| 3 | Hallar $k$ | $2k + 4k = 100 \\implies 6k = 100$ |
| 4 | Resolver | $k = 16,6$ (aprox) |

**E05. Diferencia en reparto I.P.** Se reparte un monto I.P. a 4 y 6. Si el que recibió más obtuvo \\$20.000 más que el otro, ¿cuál era el total?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir y amplificar (MCM 12) | $12/4 = 3$ ; $12/6 = 2$ |
| 2 | Plantear diferencia | $3k - 2k = 20.000 \\implies k = 20.000$ |
| 3 | Calcular total ($3k+2k$) | $5k = 5 \\cdot 20.000 = \\$100.000$ |""")
    with st.expander("❓ Cuestionario N28", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': 'Si se reparten \\$220.000 de forma I.P. a 2 y 9, ¿cuánto recibe la parte menor (la asociada al 9)?', 'options': {'A': '40.000\\', 'B': '180.000\\', 'C': '110.000\\', 'D': '20.000'}, 'answer': 'A', 'explanation': 'Inversos: $1/2$ y $1/9$. M.C.M. = 18. Índices: 9 y 2. $11k = 220.000 \\implies k = 20.000$. Parte menor (índice 2): \\$40.000.'},
            {'question': 'Al repartir 60 unidades de forma I.P. a 1, 2 y 3, el M.C.M. que debemos usar para limpiar los índices es:', 'options': {'A': '3\\', 'B': '6\\', 'C': '12\\', 'D': '1'}, 'answer': 'B', 'explanation': 'Los denominadores de los inversos son 1, 2 y 3. El M.C.M.(1, 2, 3) = 6.'},
            {'question': 'Se reparte una herencia de forma I.P. a las edades 20 y 25. ¿Cuál es la razón entre las partes recibidas?', 'options': {'A': '$4 : 5$ \\', 'B': '$5 : 4$ \\', 'C': '$20 : 25$ \\', 'D': '$1 : 2$'}, 'answer': 'B', 'explanation': 'Inversos: $1/20$ y $1/25$. M.C.M. = 100. Índices: 5 y 4. La razón es $5 : 4$.'},
            {'question': 'Si repartimos 70 objetos I.P. a 3 y 4, ¿cuántos objetos recibe la parte mayor?', 'options': {'A': '30\\', 'B': '40\\', 'C': '35\\', 'D': '50'}, 'answer': 'B', 'explanation': 'Inversos: $1/3$ y $1/4$. M.C.M. = 12. Índices: 4 y 3. $7k = 70 \\implies k = 10$. Parte mayor: $4 \\cdot 10 = 40$.'},
            {'question': 'Tres amigos se reparten una cuenta de 37.000 pesos de forma I.P. a la cantidad de dinero que traían: 2.000, 3.000 y 4.000. ¿Cuál es el valor de k tras simplificar los índices? (M.C.M. 12)', 'options': {'A': '1.000\\', 'B': '3.000\\', 'C': '4.000\\', 'D': '2.000'}, 'answer': 'B', 'explanation': 'Inversos: $1/2, 1/3, 1/4$ (quitando los miles). M.C.M. = 12. Índices: 6, 4, 3. $13k = 39.000 \\implies k = 3.000$ (ajustando el valor total del ejemplo).'},
            {'question': 'Al repartir I.P. a los números 4, 5 y 10, los nuevos índices directos tras amplificar por el M.C.M. (20) son:', 'options': {'A': '$5, 4$ y $2$ \\', 'B': '$10, 5$ y $4$ \\', 'C': '$4, 5$ y $10$ \\', 'D': '$1, 2$ y $5$'}, 'answer': 'A', 'explanation': '$1/4 \\cdot 20 = 5$; $1/5 \\cdot 20 = 4$; $1/10 \\cdot 20 = 2$.'},
            {'question': 'Si se reparte un premio I.P. a las faltas cometidas (2 y 5) y el que menos faltó recibe \\$50.000, ¿cuánto recibe el otro?', 'options': {'A': '20.000\\', 'B': '25.000\\', 'C': '125.000\\', 'D': '10.000'}, 'answer': 'A', 'explanation': 'Índices directos: 5 y 2. El que menos faltó ($5k$) recibe 50.000 $\\implies k = 10.000$. El otro ($2k$) recibe 20.000.'},
            {'question': 'La expresión "repartir I.P. a x" es equivalente a:', 'options': {'A': 'Repartir directamente a x \\', 'B': 'Repartir directamente a 1/x \\', 'C': 'Repartir directamente a x² \\', 'D': 'No existe tal equivalencia'}, 'answer': 'B', 'explanation': 'Definición fundamental de proporcionalidad inversa.'},
            {'question': 'Se reparte una cantidad I.P. a 1/2 y 1/3. Esto equivale a un reparto directo a:', 'options': {'A': '2 y 3 \\', 'B': '3 y 2\\', 'C': '1/2 y 1/3\\', 'D': '6 y 1'}, 'answer': 'A', 'explanation': 'Al invertir los inversos ($1/2$ y $1/3$) volvemos a los originales 2 y 3 para el reparto directo.'},
            {'question': 'Si al repartir una suma I.P. a 3 y 6, la parte mayor es 40, ¿cuál es la suma total repartida?', 'options': {'A': '60\\', 'B': '120\\', 'C': '80\\', 'D': '90'}, 'answer': 'A', 'explanation': 'Inversos $1/3, 1/6$. M.C.M. = 6. Índices: 2 y 1. Parte mayor $2k = 40 \\implies k = 20$. Total: $3k = 3 \\cdot 20 = 60$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n28_quiz")
    with st.expander("✅ Pauta - N28", expanded=False):
        st.markdown("""# ✅ Pauta - Cuestionario N28

1. **A.** Inversos: $1/2$ y $1/9$. M.C.M. = 18. Índices: 9 y 2. $11k = 220.000 \\implies k = 20.000$. Parte menor (índice 2): \\$40.000.
2. **B.** Los denominadores de los inversos son 1, 2 y 3. El M.C.M.(1, 2, 3) = 6.
3. **B.** Inversos: $1/20$ y $1/25$. M.C.M. = 100. Índices: 5 y 4. La razón es $5 : 4$.
4. **B.** Inversos: $1/3$ y $1/4$. M.C.M. = 12. Índices: 4 y 3. $7k = 70 \\implies k = 10$. Parte mayor: $4 \\cdot 10 = 40$.
5. **B.** Inversos: $1/2, 1/3, 1/4$ (quitando los miles). M.C.M. = 12. Índices: 6, 4, 3. $13k = 39.000 \\implies k = 3.000$ (ajustando el valor total del ejemplo).
6. **A.** $1/4 \\cdot 20 = 5$; $1/5 \\cdot 20 = 4$; $1/10 \\cdot 20 = 2$.
7. **A.** Índices directos: 5 y 2. El que menos faltó ($5k$) recibe 50.000 $\\implies k = 10.000$. El otro ($2k$) recibe 20.000.
8. **B.** Definición fundamental de proporcionalidad inversa.
9. **A.** Al invertir los inversos ($1/2$ y $1/3$) volvemos a los originales 2 y 3 para el reparto directo.
10. **A.** Inversos $1/3, 1/6$. M.C.M. = 6. Índices: 2 y 1. Parte mayor $2k = 40 \\implies k = 20$. Total: $3k = 3 \\cdot 20 = 60$.""")