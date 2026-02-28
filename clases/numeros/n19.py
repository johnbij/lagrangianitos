import streamlit as st


def render_N19():
    st.markdown("## N19: Aproximaciones - El Control del Margen")
    st.markdown("---")

    st.markdown("### 🏛️ Contexto Histórico: De las Tablillas de Barro al \"Efecto 2000\"")
    st.markdown("""
Hace casi 4.000 años, los **babilonios** ya se enfrentaban al dilema de la precisión. En sus famosas tablillas de barro, como la *YBC 7289*, calcularon el valor de $\\sqrt{2}$ con una exactitud asombrosa. Sin embargo, como su sistema era sexagesimal y se basaba en fracciones, a menudo debían **aproximar** sus cálculos para que cupieran en sus registros de comercio y astronomía. Miles de años después, el mundo moderno vivió un pánico similar con el **\"Y2K\"**. Para ahorrar memoria, los programadores **truncaron** los años a solo dos dígitos (ej: \"98\" por \"1998\"). Al llegar al año 2000, temieron que las computadoras leyeran \"00\" como 1900, colapsando aeropuertos y bancos. Desde el barro hasta los microchips, la historia de la matemática es, en esencia, la historia de cómo aprendimos a manejar el margen de error.
    """)
    st.markdown("---")

    st.markdown("""
<div style="background-color: #E8F5E9; border-left: 8px solid #2E7D32; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1B5E20; margin-top: 0;">¿Por qué aproximar?</h2>
    A veces no necesitamos el valor exacto de $\\pi$, nos basta con un $3{,}14$. Pero hay reglas para "cortar" los números. En la PAES te dirán exactamente cómo hacerlo: <b>Redondeo</b> o <b>Truncamiento</b>.
</div>
""", unsafe_allow_html=True)

    st.markdown("### 🛡️ Truncamiento (El hachazo)")
    st.markdown("""
Es la forma más fácil. Simplemente se **eliminan** las cifras decimales a partir de la posición indicada, sin mirar lo que viene después.
- **Ejemplo:** Truncar $2{,}71828$ a la centésima:
  - Ubico la centésima: $2{,}71[828]$
  - Corto: $2{,}71$
    """)

    st.markdown("### 🛡️ Redondeo (La regla del 5)")
    st.markdown("""
Aquí sí miramos al vecino de la derecha.
1. Ubicas la posición a la que quieres redondear.
2. Miras la cifra que sigue a la derecha:
   - **Si es menor que 5 (0, 1, 2, 3, 4):** La cifra se mantiene igual.
   - **Si es 5 o mayor (5, 6, 7, 8, 9):** Se le suma 1 a la cifra.
- **Ejemplo:** Redondear $2{,}71828$ a la centésima:
  - Ubico la centésima ($1$). Miro a la derecha: hay un $8$.
  - Como $8 \\ge 5$, el $1$ sube a $2$.
  - Resultado: $2{,}72$
    """)

    st.markdown("### 🛡️ Aproximación por Exceso y por Defecto")
    st.markdown("""
- **Por Defecto:** El número aproximado es **menor** que el original (como el truncamiento en positivos).
- **Por Exceso:** El número aproximado es **mayor** que el original.
    """)

    st.markdown("### 🛡️ Estimaciones y Error")
    st.markdown("""
- **Error Absoluto:** Es la diferencia (en valor absoluto) entre el valor real y el valor aproximado.
$$E_{abs} = |V_{real} - V_{aprox}|$$

**Típ:** Si dice \"redondear a la milésima\" y truncas, la respuesta va a estar en la alternativa A para engañarte. La precisión es lo que separa a un experto de un principiante.
    """)
    st.markdown("---")

    with st.expander("📝 Guía de Ejemplos: Truncamiento, Redondeo y Error"):
        st.markdown("""
**E01. Truncamiento a la décima.** Truncar $3{,}4567$ a la décima.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Ubicar la décima (primera cifra decimal) | $3{,}4[567]$ |
| 2 | Eliminar todo lo que está a la derecha | $3{,}4$ |

**E02. Truncamiento a la milésima.** Truncar $0{,}98765$ a la milésima.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Ubicar la milésima (tercera cifra decimal) | $0{,}987[65]$ |
| 2 | Aplicar el corte | $0{,}987$ |

**E03. Redondeo a la unidad.** Redondear $12{,}54$ a la unidad.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Ubicar la unidad (el 2) | $12[{,}54]$ |
| 2 | Mirar cifra de la derecha | Es un 5 |
| 3 | Aplicar regla (5 o más, sube 1) | $13$ |

**E04. Redondeo a la centésima.** Redondear $4{,}5129$ a la centésima.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Ubicar la centésima (el 1) | $4{,}51[29]$ |
| 2 | Mirar cifra de la derecha | Es un 2 |
| 3 | Aplicar regla (menor que 5, se mantiene) | $4{,}51$ |

**E05. Redondeo con cadena de 9.** Redondear $1{,}999$ a la centésima.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Ubicar centésima (segundo 9) | $1{,}99[9]$ |
| 2 | Mirar derecha (es un 9, sube 1) | $1{,}99 + 0{,}01$ |
| 3 | Resultado final | $2{,}00$ o $2$ |

**E06. Aproximación por exceso.** Aproximar $7{,}12$ a la décima por exceso.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Buscar el número con 1 décima inmediatamente mayor | $7{,}2$ |

**E07. Aproximación por defecto.** Aproximar $8{,}99$ a la décima por defecto.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Buscar el número con 1 décima inmediatamente menor | $8{,}9$ |

**E08. Cálculo de Error Absoluto.** Hallar error si $V_{real} = 5$ y $V_{aprox} = 4{,}8$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Aplicar fórmula $|V_{real} - V_{aprox}|$ | $|5 - 4{,}8|$ |
| 2 | Resultado final | $0{,}2$ |

**E09. Estimación en multiplicación.** Estimar $2{,}9 \\cdot 10{,}2$ redondeando a la unidad.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Redondear cada factor | $3 \\cdot 10$ |
| 2 | Operar | $30$ |

**E10. Diferencia entre truncar y redondear.** Comparar $5{,}67$ a la décima.
| Método | Acción | Resultado |
| :--- | :--- | :--- |
| Truncar | Cortar en el 6 | $5{,}6$ |
| Redondear | Como hay un 7, el 6 sube | $5{,}7$ |
        """)

    with st.expander("❓ Cuestionario N19: Aproximaciones"):
        st.markdown("""
**1. Al truncar el número $5{,}6789$ a la centésima se obtiene:**  
A) $5{,}6$ &nbsp;&nbsp; B) $5{,}67$ &nbsp;&nbsp; C) $5{,}68$ &nbsp;&nbsp; D) $5{,}7$

**2. Si redondeamos $12{,}345$ a la décima, el resultado es:**  
A) $12{,}3$ &nbsp;&nbsp; B) $12{,}4$ &nbsp;&nbsp; C) $12{,}35$ &nbsp;&nbsp; D) $12{,}0$

**3. El número $\\pi \\approx 3{,}14159...$ redondeado a la milésima es:**  
A) $3{,}141$ &nbsp;&nbsp; B) $3{,}142$ &nbsp;&nbsp; C) $3{,}14$ &nbsp;&nbsp; D) $3{,}1416$

**4. Si aproximamos $8{,}42$ por exceso a la décima, obtenemos:**  
A) $8{,}4$ &nbsp;&nbsp; B) $8{,}5$ &nbsp;&nbsp; C) $8{,}43$ &nbsp;&nbsp; D) $9{,}0$

**5. ¿Cuál es el error absoluto si se aproxima $2{,}5$ por el número $2$?**  
A) $0{,}5$ &nbsp;&nbsp; B) $-0{,}5$ &nbsp;&nbsp; C) $2{,}5$ &nbsp;&nbsp; D) $0{,}25$

**6. Al truncar el número $-2{,}456$ a la centésima, resulta:**  
A) $-2{,}45$ &nbsp;&nbsp; B) $-2{,}46$ &nbsp;&nbsp; C) $-2{,}4$ &nbsp;&nbsp; D) $-2{,}5$

**7. Si estimamos el producto $3{,}98 \\cdot 5{,}02$ redondeando ambos números a la unidad, el resultado es:**  
A) $15$ &nbsp;&nbsp; B) $20$ &nbsp;&nbsp; C) $19$ &nbsp;&nbsp; D) $20{,}5$

**8. El número $0{,}0099$ redondeado a la milésima es:**  
A) $0{,}009$ &nbsp;&nbsp; B) $0{,}01$ &nbsp;&nbsp; C) $0{,}001$ &nbsp;&nbsp; D) $0{,}010$

**9. Aproximar por defecto a la unidad el número $7{,}89$ da como resultado:**  
A) $7$ &nbsp;&nbsp; B) $8$ &nbsp;&nbsp; C) $7{,}8$ &nbsp;&nbsp; D) $7{,}9$

**10. Si un ejercicio pide redondear a la centésima el valor de $2/3$, el resultado es:**  
A) $0{,}66$ &nbsp;&nbsp; B) $0{,}67$ &nbsp;&nbsp; C) $0{,}6$ &nbsp;&nbsp; D) $0{,}7$
        """)

    with st.expander("✅ Pauta Explicativa - Cuestionario N19"):
        st.markdown("""
1. **B.** Truncar es simplemente cortar. En la centésima (segundo decimal) cortamos y queda $5{,}67$.
2. **A.** El vecino del 3 (la décima) es un 4. Como es menor que 5, el 3 se mantiene. Resulta $12{,}3$.
3. **B.** La milésima es el 1 ($3{,}141$). El vecino de la derecha es un 5, por lo que el 1 sube a 2. Resulta $3{,}142$.
4. **B.** Por exceso buscamos la décima inmediatamente mayor a $8{,}42$, que es $8{,}5$.
5. **A.** Error Absoluto = $|2{,}5 - 2| = |0{,}5| = 0{,}5$.
6. **A.** El truncamiento no mira el valor ni el signo, solo corta en la posición indicada: $-2{,}45$.
7. **B.** Redondeando a la unidad: $3{,}98 \\to 4$ y $5{,}02 \\to 5$. El producto estimado es $4 \\cdot 5 = 20$.
8. **D.** La milésima es el primer 9. El vecino es otro 9, así que el primer 9 sube a 10, transformando el número en $0{,}010$.
9. **A.** Por defecto buscamos la unidad inmediatamente menor o igual al número, que es $7$.
10. **B.** $2 : 3 = 0{,}666...$ Al redondear a la centésima, el vecino del segundo 6 es otro 6, por lo que sube a $0{,}67$.
        """)

    st.markdown("---")
    st.markdown("> *\"No hay nada tan engañoso como un hecho obvio.\"*  \n> — **Arthur Conan Doyle**")
