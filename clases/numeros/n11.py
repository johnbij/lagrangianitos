import streamlit as st


def render_N11():
    with st.expander("📚 Teoría", expanded=False):
        st.title("N11: Números Racionales I - El Arte de Partir el Entero")

        st.markdown(r"""
    ### 🏛️ 1. Contexto Histórico: El Ojo de Horus y la Herencia del Nilo
    Para los antiguos egipcios, las fracciones no eran solo números; eran una cuestión de supervivencia y justicia. Imagina que el Nilo inundaba las tierras y luego debías repartir el terreno entre 10 familias, pero solo tenías 7 parcelas. No podías simplemente decir "les toca un poco".

    Ellos inventaron un sistema basado en el **Ojo de Horus**. Según la leyenda, el dios Seth despedazó el ojo de Horus y el dios Thot lo reconstruyó, pero faltaba una pieza ($1/64$). Cada parte del ojo representaba una fracción unitaria ($1/2, 1/4, 1/8...$). Los egipcios escribían cualquier fracción como una suma de estas partes. Si un escriba fallaba en el cálculo, alguien se quedaba sin comer. Por eso, los **Racionales ($\mathbb{Q}$)** nacen de la "Razón": la comparación exacta entre lo que tengo y entre cuántos lo reparto.

    ---

    ### 🛡️ 9.1 La Anatomía de la Fracción
    Una fracción $\frac{a}{b}$ es un operador. El **denominador** ($b$) corta la unidad y el **numerador** ($a$) recolecta las piezas.

    ### 🛡️ 9.2 El "Manual de Identidad" y el Entero Oculto
    Es vital saber cuánta "hambre" quita una fracción:

    * **Fracciones Propias:** El numerador es menor que el denominador ($\frac{3}{4}$). **No alcanzan a completar 1 entero.** (Sobra pizza en la caja).
    * **Fracciones Impropias:** El numerador es mayor o igual ($\frac{7}{3}$). **Superan el entero.**
        * **Ejemplo Paso a Paso:** En $\frac{7}{3}$, nos preguntamos: ¿Cuántas veces cabe el 3 en el 7? Cabe **2 veces** y sobra **1**.
        * **Resultado:** $\frac{7}{3} = 2 \frac{1}{3}$ (Tiene 2 enteros completos y un tercio de sobra).

    ---

    ### 🛡️ 9.3 Amplificación y Simplificación: Ajustando el Calibre
    * **Amplificar (Agrandar el formato):** Multiplicas arriba y abajo por el mismo número.
        * **Ejemplo:** $\frac{2}{3}$ amplificado por 4 $\rightarrow \frac{2 \cdot 4}{3 \cdot 4} = \frac{8}{12}$. Sigue siendo la misma cantidad de madera, pero cortada en trozos más chicos.
    * **Simplificar (Achicar el formato):** Divides ambos por su MCD.
        * **Ejemplo:** $\frac{15}{20}$. El MCD entre 15 y 20 es 5.
        * $\frac{15 \div 5}{20 \div 5} = \frac{3}{4}$. Esta es la **Fracción Irreductible**.

    ---

    ### 🛡️ 9.4 Operatoria: El Protocolo de Taller
    Aquí es donde aplicamos la mecánica de precisión:

    1. **Suma/Resta con Simplificación:** $\frac{3}{10} + \frac{1}{10} = \frac{4}{10}$ (¡No lo dejes así! Simplifica por 2) $\rightarrow \frac{2}{5}$.
    2. **Multiplicación (Simplificación Cruzada):**
       $\frac{5}{9} \cdot \frac{3}{10}$. En vez de hacer $15/90$, simplificamos el 5 con el 10 (queda 1 y 2) y el 3 con el 9 (queda 1 y 3).
       $\frac{1}{3} \cdot \frac{1}{2} = \frac{1}{6}$. **¡Mucho más rápido!**
    3. **División:** Mantienes la primera, inviertes la segunda y multiplicas.

    ---

    ### 🛡️ 9.5 Comparación Cruzada: El Puente al Álgebra
    Para saber si $\frac{a}{b} = \frac{c}{d}$, o cuál es mayor, multiplicamos cruzado: $a \cdot d$ y $b \cdot c$.
    * Si $a \cdot d = b \cdot c$, las fracciones son **Equivalentes**.
    * Si $a \cdot d > b \cdot c$, entonces $\frac{a}{b} > \frac{c}{d}$.

    **⚠️ Alerta de Futuro:** Este simple cruce es la base de las **Razones y Proporciones** que veremos más adelante. Además, entender esta igualdad ($a \cdot d = b \cdot c$) es lo que te permitirá resolver **Ecuaciones e Inecuaciones** complejas sin miedo a las fracciones. Si dominas este "baile cruzado", el álgebra será solo un trámite.

    ---

    > **Típ:** En la PAES, si el resultado de tu problema es una fracción, busca siempre simplificarla. Si no está tu resultado en las alternativas, es casi seguro que te falta la **Fracción Irreductible**.

    ---

    > "Los números racionales son los puntos de luz en la recta numérica que nos permiten medir la realidad con precisión".
    > — **Leopold Kronecker**
    """)


    with st.expander("🚀 Guía de Ejemplos: El Taller de Fracciones", expanded=False):
        st.markdown(r"""
### E02: Transformación de Mixto a Impropio (El ciclo)
**Situación:** Tienes $3 \frac{2}{5}$ de material. ¿Cuántos quintos son en total?
**La Carpintería:** Multiplicamos el entero por el denominador y sumamos el numerador. El denominador se mantiene.

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar entero por denominador ($3 \cdot 5$) | 15 |
| 2 | Sumar el numerador ($15 + 2$) | 17 |
| 3 | Mantener denominador | **17/5** |

---

### E03: Transformación de Impropio a Mixto (Buscando el entero)
**Situación:** Tienes $\frac{22}{4}$ de madera. ¿Cuántos tablones enteros tienes?
**La Carpintería:** Dividimos 22 por 4. El cociente es el entero y el resto es la nueva fracción.

| Dividendo | Divisor | Cociente (Enteros) | Resto (Sobras) | Resultado |
| :--- | :---: | :---: | :---: | :--- |
| 22 | 4 | 5 | 2 | $5 \frac{2}{4} = \mathbf{5 \frac{1}{2}}$ |

---

### E04: Simplificación de "Un solo golpe" (MCD)
**Situación:** Reducir $\frac{48}{72}$ a su forma irreductible.
**La Carpintería:** Buscamos el divisor más grande común (MCD). En este caso es 24.

| Acción | Operación | Resultado |
| :--- | :--- | :--- |
| Dividir por 24 | $(48 \div 24) / (72 \div 24)$ | **2/3** |

---

### E05: Suma con mcm (Distinto Denominador)
**Situación:** Resolver $\frac{3}{4} + \frac{5}{6}$.
**La Carpintería:** El mcm(4, 6) es 12. Amplificamos para igualar.

| Fracción | Amplificador | Resultado Parcial |
| :--- | :---: | :--- |
| 3/4 | $\cdot 3$ | 9/12 |
| 5/6 | $\cdot 2$ | 10/12 |
| **Suma** | $9+10$ | **19/12** |

---

### E06: Resta con Enteros Ocultos
**Situación:** Resolver $2 - \frac{3}{5}$.
**La Carpintería:** Ponemos un 1 "fantasma" debajo del 2 y operamos.

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Escribir como fracción | $2/1 - 3/5$ |
| 2 | mcm(1, 5) es 5 | $10/5 - 3/5$ |
| 3 | Resultado | **7/5** |

---

### E07: Simplificación Cruzada (Velocidad Pro)
**Situación:** Resolver $\frac{14}{15} \cdot \frac{5}{21}$.
**La Carpintería:** Antes de multiplicar números grandes, simplificamos el 14 con el 21 (por 7) y el 5 con el 15 (por 5).

| Antes | Simplificación | Después |
| :--- | :--- | :--- |
| 14/15 | 14 y 21 $\rightarrow$ 2 y 3 | 2/3 |
| 5/21 | 5 y 15 $\rightarrow$ 1 y 3 | 1/3 |
| **Final** | $2 \cdot 1$ / $3 \cdot 3$ | **2/9** |

---

### E08: División (Invertir y Multiplicar)
**Situación:** Resolver $\frac{4}{9} \div \frac{2}{3}$.
**La Carpintería:** Mantengo la primera, doy vuelta la segunda.

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir segunda | $4/9 \cdot 3/2$ |
| 2 | Simplificar | $2/3 \cdot 1/1$ |
| 3 | Final | **2/3** |

---

### E09: Comparación de Fracciones (El Baile Cruzado)
**Situación:** ¿Quién es mayor, $\frac{5}{8}$ o $\frac{7}{11}$?
**La Carpintería:** Multiplicamos cruzado y comparamos los resultados.

| Cruce | Operación | Resultado |
| :--- | :--- | :--- |
| Lado A | $5 \cdot 11$ | 55 |
| Lado B | $8 \cdot 7$ | 56 |
| **Conclusión** | $55 < 56$ | **7/11 es mayor** |

---

### E10: Fracción de una Cantidad
**Situación:** Calcular los $\frac{3}{5}$ de 200.
**La Carpintería:** La palabra "de" significa multiplicación.

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar | $(3 \cdot 200) / 5$ |
| 2 | Simplificar | $3 \cdot 40$ |
| 3 | Final | **120** |

---

### E11: Operatoria Combinada (PAPOMUDAS con Fracciones)
**Situación:** Resolver $\frac{1}{2} + \frac{1}{3} \cdot \frac{1}{4}$.
**La Carpintería:** Multiplicación antes que suma.

| Prioridad | Operación | Resultado Parcial |
| :--- | :--- | :--- |
| 1. Multiplicación | $1/3 \cdot 1/4$ | 1/12 |
| 2. Suma | $1/2 + 1/12$ | $6/12 + 1/12$ |
| 3. Final | | **7/12** |
""")

    with st.expander("🚀 Guía de Ejemplos: Identidad y Conversión", expanded=False):
        st.markdown(r"""
### E02: Del Dibujo a la Fracción
**Situación:** Una torta se corta en 8 trozos iguales y te comes 3.
**La Carpintería:** Identificamos quién corta y quién recolecta.

| Elemento | Significado | Valor |
| :--- | :--- | :---: |
| Denominador | Partes totales en que se cortó | 8 |
| Numerador | Partes que tomamos | 3 |
| **Fracción** | | **3/8** |

---

### E03: Fracción Propia (La que no llena el envase)
**Situación:** Identificar si $\frac{5}{6}$ es mayor o menor a 1 entero.
**La Carpintería:** Comparamos numerador vs denominador.

| Comparación | Lógica | Resultado |
| :--- | :--- | :--- |
| $5 < 6$ | El numerador es más pequeño | Es **Propia** |
| **Conclusión** | No alcanza a ser 1 entero | **< 1** |

---

### E04: Transformación de Mixto a Impropio (El "Reloj")
**Situación:** Tienes $2 \frac{3}{4}$ litros de bebida. ¿Cuántos cuartos son en total?
**La Carpintería:** Multiplicamos el entero por el de abajo y sumamos el de arriba.

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar entero por denominador ($2 \cdot 4$) | 8 |
| 2 | Sumar el numerador ($8 + 3$) | 11 |
| 3 | Resultado final (mantener denominador) | **11/4** |

---

### E05: Transformación de Impropio a Mixto (Repartición)
**Situación:** Tienes $\frac{13}{5}$ de chocolate. ¿Cuántas barras enteras hay?
**La Carpintería:** Dividimos el de arriba por el de abajo.

| División | Cociente (Enteros) | Resto (Sobras) | Resultado Mixto |
| :--- | :---: | :---: | :--- |
| $13 \div 5$ | 2 | 3 | **2 3/5** |

---

### E06: Amplificación (Cambio de Escala)
**Situación:** Necesitas que la fracción $\frac{2}{3}$ tenga denominador 15.
**La Carpintería:** Buscamos por cuánto multiplicar el 3 para que llegue a 15 ($15 \div 3 = 5$).

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar arriba y abajo por 5 | $(2 \cdot 5) / (3 \cdot 5)$ |
| 2 | Resultado | **10/15** |

---

### E07: Simplificación Básica (La Mitad)
**Situación:** Achicar la fracción $\frac{12}{16}$.
**La Carpintería:** Buscamos un divisor común. Probemos con el 2 (mitad).

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Dividir arriba y abajo por 2 | $6/8$ |
| 2 | Volver a dividir por 2 | **3/4** |

---

### E08: Simplificación Avanzada (Usando el MCD)
**Situación:** Llevar $\frac{30}{45}$ a su forma irreductible de un solo golpe.
**La Carpintería:** El divisor más grande común entre 30 y 45 es 15.

| Acción | Operación | Resultado |
| :--- | :--- | :--- |
| Dividir por 15 | $(30 \div 15) / (45 \div 15)$ | **2/3** |

---

### E09: Fracciones Equivalentes (La Igualdad)
**Situación:** Comprobar si $\frac{1}{2}$ es igual a $\frac{5}{10}$.
**La Carpintería:** Multiplicamos cruzado. Si da lo mismo, son hermanas.

| Cruce | Operación | Resultado |
| :--- | :--- | :--- |
| $1 \cdot 10$ | Numerador 1 por Denominador 2 | 10 |
| $2 \cdot 5$ | Denominador 1 por Numerador 2 | 10 |
| **Veredicto** | $10 = 10$ | **Son Equivalentes** |

---

### E10: Comparación de Magnitud (¿Quién es más grande?)
**Situación:** ¿Qué es más, $\frac{3}{4}$ o $\frac{2}{3}$ de una pizza?
**La Carpintería:** Aplicamos el baile cruzado.

| Cruce | Operación | Resultado |
| :--- | :--- | :--- |
| Lado Izquierdo | $3 \cdot 3$ | 9 |
| Lado Derecho | $4 \cdot 2$ | 8 |
| **Veredicto** | $9 > 8$ | **3/4 es mayor** |

---

### E11: El Entero Disfrazado
**Situación:** ¿A qué equivale la fracción $\frac{12}{4}$?
**La Carpintería:** Cuando el de abajo cabe justo en el de arriba.

| Operación | Lógica | Resultado |
| :--- | :--- | :--- |
| $12 \div 4$ | La división es exacta | 3 |
| **Conclusión** | Es una fracción entera | **3** |
""")

    with st.expander("❓ Cuestionario N11", expanded=False):
        from utils import render_multiple_choice_quiz
        import json as _json
        _quiz_data = [
            {
                        "question": "¿Cuál es la fracción equivalente a $\\frac{2}{3}$ con denominador 12?",
                        "options": {
                                    "A": "$\\frac{4}{12}$",
                                    "B": "$\\frac{6}{12}$",
                                    "C": "$\\frac{8}{12}$",
                                    "D": "$\\frac{9}{12}$"
                        },
                        "answer": "C",
                        "explanation": "Multiplica numerador y denominador por 4: $\\frac{2 \\times 4}{3 \\times 4} = \\frac{8}{12}$."
            },
            {
                        "question": "$\\frac{3}{4} + \\frac{1}{4}$ es igual a:",
                        "options": {
                                    "A": "$\\frac{4}{8}$",
                                    "B": "$\\frac{3}{16}$",
                                    "C": "1",
                                    "D": "$\\frac{4}{4}$"
                        },
                        "answer": "C",
                        "explanation": "Con denominador igual se suman los numeradores: $\\frac{3+1}{4} = \\frac{4}{4} = 1$."
            },
            {
                        "question": "¿Cuál es el resultado de $\\frac{2}{3} \\times \\frac{3}{4}$?",
                        "options": {
                                    "A": "$\\frac{5}{7}$",
                                    "B": "$\\frac{6}{7}$",
                                    "C": "$\\frac{1}{2}$",
                                    "D": "$\\frac{8}{9}$"
                        },
                        "answer": "C",
                        "explanation": "Se multiplica numerador con numerador y denominador con denominador: $\\frac{2 \\times 3}{3 \\times 4} = \\frac{6}{12} = \\frac{1}{2}$."
            },
            {
                        "question": "$\\frac{5}{6} - \\frac{1}{3}$ es igual a:",
                        "options": {
                                    "A": "$\\frac{4}{3}$",
                                    "B": "$\\frac{1}{2}$",
                                    "C": "$\\frac{4}{6}$",
                                    "D": "$\\frac{1}{3}$"
                        },
                        "answer": "B",
                        "explanation": "El mcm de 6 y 3 es 6. $\\frac{5}{6} - \\frac{2}{6} = \\frac{3}{6} = \\frac{1}{2}$."
            },
            {
                        "question": "¿Cómo se escribe el número mixto $2\\frac{1}{3}$ como fracción impropia?",
                        "options": {
                                    "A": "$\\frac{5}{3}$",
                                    "B": "$\\frac{7}{3}$",
                                    "C": "$\\frac{2}{3}$",
                                    "D": "$\\frac{6}{3}$"
                        },
                        "answer": "B",
                        "explanation": "$2 \\times 3 + 1 = 7$, por lo tanto $2\\frac{1}{3} = \\frac{7}{3}$."
            },
            {
                        "question": "¿Cuál es el resultado de $\\frac{3}{4} \\div \\frac{1}{2}$?",
                        "options": {
                                    "A": "$\\frac{3}{8}$",
                                    "B": "$\\frac{3}{2}$",
                                    "C": "$\\frac{4}{3}$",
                                    "D": "$\\frac{6}{4}$"
                        },
                        "answer": "B",
                        "explanation": "Dividir por una fracción es multiplicar por su inverso: $\\frac{3}{4} \\times \\frac{2}{1} = \\frac{6}{4} = \\frac{3}{2}$."
            },
            {
                        "question": "La fracción $\\frac{18}{24}$ simplificada es:",
                        "options": {
                                    "A": "$\\frac{9}{12}$",
                                    "B": "$\\frac{3}{4}$",
                                    "C": "$\\frac{6}{8}$",
                                    "D": "$\\frac{2}{3}$"
                        },
                        "answer": "B",
                        "explanation": "El MCD de 18 y 24 es 6. $\\frac{18 \\div 6}{24 \\div 6} = \\frac{3}{4}$."
            },
            {
                        "question": "¿Cuál de estos números es racional?",
                        "options": {
                                    "A": "$\\sqrt{2}$",
                                    "B": "$\\pi$",
                                    "C": "$\\frac{7}{3}$",
                                    "D": "$\\sqrt{5}$"
                        },
                        "answer": "C",
                        "explanation": "Un número racional puede expresarse como cociente de enteros. $\\frac{7}{3}$ cumple eso; $\\sqrt{2}$, $\\pi$, $\\sqrt{5}$ son irracionales."
            },
            {
                        "question": "$\\frac{1}{2} + \\frac{1}{3} + \\frac{1}{6}$ es igual a:",
                        "options": {
                                    "A": "$\\frac{3}{11}$",
                                    "B": "$\\frac{1}{2}$",
                                    "C": "1",
                                    "D": "$\\frac{2}{3}$"
                        },
                        "answer": "C",
                        "explanation": "El mcm de 2, 3 y 6 es 6. $\\frac{3}{6} + \\frac{2}{6} + \\frac{1}{6} = \\frac{6}{6} = 1$."
            },
            {
                        "question": "Si $\\frac{x}{5} = \\frac{4}{20}$, entonces $x$ vale:",
                        "options": {
                                    "A": "4",
                                    "B": "2",
                                    "C": "1",
                                    "D": "5"
                        },
                        "answer": "C",
                        "explanation": "$\\frac{4}{20} = \\frac{1}{5}$, por lo tanto $x = 1$."
            }
]
        render_multiple_choice_quiz(_quiz_data, key_prefix="n11_quiz")
