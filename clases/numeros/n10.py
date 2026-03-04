import streamlit as st


def render_N10():
    with st.expander("📚 Teoría", expanded=False):
        st.title("N10: Mecánica de Operatoria - El Manual de Seguridad del Taller")

        st.markdown(r"""
    **Eje:** Números | **Nivel:** Control de Errores Críticos

    ---

    ### 🏛️ Contexto Histórico: De las Piedras a los Algoritmos
    Durante milenios, la humanidad solo sabía sumar y restar (poner y quitar ovejas). La **Multiplicación** nació como un "atajo" para no sumar lo mismo mil veces, pero la **División**... la división fue el verdadero dolor de cabeza.

    En la Edad Media, saber dividir era considerado una habilidad de nivel universitario; la gente viajaba cientos de kilómetros solo para aprender el algoritmo de la división larga. ¿Por qué? Porque sin el **Cero** (que nos trajeron los árabes de la India) y sin un orden claro, repartir 1.543 sacos de trigo entre 12 familias era una misión imposible. El **PAPOMUDAS** no es un capricho moderno; es el resultado de siglos de errores, barcos hundidos por cálculos mal hechos y puentes caídos. Es el protocolo para que la lógica no se rompa.

    ---

    ### 🛡️ El Protocolo Universal: PAPOMUDAS
    En un taller, no puedes pintar antes de lijar. En matemática, no puedes sumar antes de multiplicar. El orden es sagrado para que el resultado sea único.

    ### 🛠️ La Jerarquía de Mando:
    1. **PA (Paréntesis)**
    2. **PO (Potencias)**
    3. **MU - DA (Multiplicación y División)** de izquierda a derecha.
    4. **S (Suma y Resta)** de izquierda a derecha.

    **Ejemplo de Aplicación Paso a Paso:**
    Ejercicio: $20 + [ 5 \cdot (2^3 - 3) ]$

    * **Paso 1 (Potencia dentro del paréntesis):** $20 + [ 5 \cdot (8 - 3) ]$
    * **Paso 2 (Resolver paréntesis circular):** $20 + [ 5 \cdot 5 ]$
    * **Paso 3 (Resolver corchete/multiplicación):** $20 + 25$
    * **Paso 4 (Suma final):** $45$

    ---

    ### 🛡️  La Guerra de los Signos (Lógica de Sentido Común)
    Olvida la memoria mecánica. Entiende la lógica:

    * **Suma y Resta:** Piénsalo como dinero.
        * **Signos Iguales:** Si debes 5 ($-5$) y pides prestado 3 más ($-3$), ahora debes 8 ($-8$). Se suman las deudas o los haberes.
        * **Signos Distintos:** Si tienes 10 ($+10$) pero debes 15 ($-15$), pagas y quedas debiendo 5 ($-5$). Es una resta donde manda el que tiene más "fuerza".

    * **Multiplicación y División:** Aquí el signo es un "operador de dirección".
        * El amigo (+) de mi amigo (+) es mi **amigo (+)**.
        * El enemigo (-) de mi enemigo (-) es mi **amigo (+)**.
        * El enemigo (-) de mi amigo (+) es mi **enemigo (-)**.

    ---

    ### 🛡️ La División: Desmitificando el Monstruo
    Dividir no es más que **restar repetidamente**. Si digo $20 \div 5$, estoy preguntando: "¿Cuántas veces puedo quitarle 5 al 20 hasta que no quede nada?".

    **El truco de la coma (A prueba de errores):**
    El cerebro humano odia dividir por "pedazos" (decimales). Si tienes $12 \div 0,2$, la técnica es **amplificar**.
    * Multiplicas el dividendo y el divisor por 10: $120 \div 2 = 60$.
    * ¡Es el mismo resultado y no te arriesgaste con la coma!

    ---

    ### 🛡️  Multiplicación y División por potencias de 10
    Es como mover un mueble en el taller. La coma salta según la cantidad de ceros.

    **Ejemplos Paso a Paso:**

    * **Multiplicación ($45,67 \cdot 100$):**
        * Hay 2 ceros, la coma se mueve 2 lugares a la **derecha**.
        * $45,67 \rightarrow 456,7 \rightarrow 4567$
    * **División ($12,8 \div 1000$):**
        * Hay 3 ceros, la coma se mueve 3 lugares a la **izquierda**.
        * $12,8 \rightarrow 1,28 \rightarrow 0,128 \rightarrow 0,0128$

    > **Típ:** Si al mover la coma hacia la izquierda te quedas sin números, rellena con ceros. El cero es el guardián de la posición vacía.

    ---

    > "La aritmética es ser capaz de contar hasta veinte sin quitarse los zapatos".
    > — **Mickey Mouse**
    """)


    with st.expander("🚀 Guía de Ejemplos: El Taller de Operatoria", expanded=False):
        st.markdown(r"""
### 1: La Trampa de la Prioridad Horizontal
**Situación:** Resolver $40 \div 5 \cdot 2$.
**La Carpintería:** Muchos cometen el error de multiplicar $5 \cdot 2$ primero. Según el PAPOMUDAS, MU y DA tienen igual rango, se opera de izquierda a derecha.

| Paso | Operación | Resultado Parcial |
| :--- | :--- | :--- |
| 1 | $40 \div 5$ | 8 |
| 2 | $8 \cdot 2$ | **16** |

---

### 2: Paréntesis Anidados (Cebolla Matemática)
**Situación:** Resolver $100 - [ 20 + (5 \cdot 4) ]$.
**La Carpintería:** Se parte desde el "corazón" del ejercicio hacia afuera.

| Capa | Operación | Expresión Resultante |
| :--- | :--- | :--- |
| Original | $100 - [ 20 + (5 \cdot 4) ]$ | $100 - [ 20 + (20) ]$ |
| Corchete | $20 + 20$ | $100 - [ 40 ]$ |
| Final | $100 - 40$ | **60** |

---

### 3: Suma y Resta de Signos Distintos
**Situación:** Resolver $-15 + 8 - 12 + 20$.
**La Carpintería:** Una técnica segura es agrupar "deudas" y "haberes".

| Grupo | Operación | Total |
| :--- | :--- | :--- |
| Deudas (-) | $-15 - 12$ | -27 |
| Haberes (+) | $+8 + 20$ | +28 |
| **Balance** | **-27 + 28** | **1** |

---

### 4: División con Divisor Decimal (Amplificación)
**Situación:** Resolver $7,5 \div 0,25$.
**La Carpintería:** Limpiamos la coma del divisor multiplicando ambos por 100 (porque 0,25 tiene dos decimales).

| Paso | Acción | Nueva Operación |
| :--- | :--- | :--- |
| 1 | Amplificar por 100 | $(7,5 \cdot 100) \div (0,25 \cdot 100)$ |
| 2 | Ejecutar | $750 \div 25$ |
| 3 | Dividir | **30** |

---

### 5: Multiplicación por 0,1, 0,01, etc.
**Situación:** Resolver $458 \cdot 0,01$.
**La Carpintería:** Multiplicar por 0,01 es lo mismo que dividir por 100. La coma corre a la izquierda.

| Valor Inicial | Movimiento de Coma | Resultado |
| :--- | :--- | :--- |
| 458,0 | 2 espacios izquierda | **4,58** |

---

### 6: El Desafío del PAPOMUDAS Completo
**Situación:** Resolver $5 + 2 \cdot 3^2 - (10 \div 2)$.

| Prioridad | Operación | Estado de la Expresión |
| :--- | :--- | :--- |
| 1. Paréntesis | $(10 \div 2) = 5$ | $5 + 2 \cdot 3^2 - 5$ |
| 2. Potencia | $3^2 = 9$ | $5 + 2 \cdot 9 - 5$ |
| 3. Multiplicación | $2 \cdot 9 = 18$ | $5 + 18 - 5$ |
| 4. Suma/Resta | $23 - 5$ | **18** |

---

### 7: Ley de Signos en Multiplicación Múltiple
**Situación:** Resolver $(-2) \cdot (-3) \cdot (-4)$.
**La Carpintería:** Operamos par por par para no marearnos con los signos.

| Paso | Operación | Signo Resultante |
| :--- | :--- | :--- |
| 1 | $(-2) \cdot (-3)$ | $+6$ (Menos por menos es más) |
| 2 | $(+6) \cdot (-4)$ | **-24** (Más por menos es menos) |

---

### 8: División con "Cero al Cociente"
**Situación:** Resolver $1025 \div 5$.
**La Carpintería:** Cuidado cuando el divisor no cabe en una cifra intermedia.

| Paso | Acción | Cociente Parcial |
| :--- | :--- | :--- |
| 1 | 10 dividido en 5 | 2 |
| 2 | Bajar el 2. ¿Cabe el 5? | No (ponemos 0 al cociente) |
| 3 | Bajar el 5. ¿25 en 5? | 5 |
| **Final** | | **205** |

---

### 9: El "Fantasma" del Signo delante del Paréntesis
**Situación:** Resolver $15 - ( -3 + 8 )$.
**La Carpintería:** El signo menos afuera cambia el sentido de TODO lo que esté adentro, o resolvemos adentro primero.

| Camino | Operación | Resultado |
| :--- | :--- | :--- |
| Interior primero | $15 - ( 5 )$ | 10 |
| Distributiva | $15 + 3 - 8$ | **10** |

---

### 10: Potencias de 10 y Decimales Extremos
**Situación:** Resolver $0,004 \div 100$.
**La Carpintería:** Dividir por 100 es encoger. Movemos la coma 2 espacios más a la izquierda.

| Inicial | Movimiento (2 ceros) | Final |
| :--- | :--- | :--- |
| 0,004 | 0,0004 $\rightarrow$ 0,00004 | **0,00004** |
""")

    with st.expander("❓ Cuestionario N10", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿Cuál es el resultado de $12 - 4 \\cdot 2 + 5$?**\n\\', 'options': {'A': '21', 'B': '9', 'C': '13', 'D': '24'}, 'answer': 'B', 'explanation': 'Multiplicación primero: $12 - 8 + 5 = 4 + 5 = 9$.'},
            {'question': 'Al resolver $30 \\div 5 \\cdot 3$, el resultado correcto es:**\n\\', 'options': {'A': '2', 'B': '18', 'C': '10', 'D': '45'}, 'answer': 'B', 'explanation': 'De izquierda a derecha: $30 \\div 5 = 6$, luego $6 \\cdot 3 = 18$.'},
            {'question': 'El valor de la expresión $-10 - (-5) + (-8)$ es:**\n\\', 'options': {'A': '-23', 'B': '-13', 'C': '-7', 'D': '-3'}, 'answer': 'B', 'explanation': '$-10 + 5 - 8 \\rightarrow -5 - 8 = -13$.'},
            {'question': '¿Cuál es el resultado de $2 \\cdot [ 15 - (2^3 + 2) ]$?**\n\\', 'options': {'A': '10', 'B': '20', 'C': '5', 'D': '30'}, 'answer': 'A', 'explanation': 'Paréntesis: $(8+2)=10 \\rightarrow 2 \\cdot [15-10] \\rightarrow 2 \\cdot 5 = 10$.'},
            {'question': 'Si dividimos $1,2$ por $0,02$, obtenemos:**\n\\', 'options': {'A': '0,6', 'B': '6', 'C': '60', 'D': '600'}, 'answer': 'C', 'explanation': 'Amplificar por 100: $120 \\div 2 = 60$.'},
            {'question': '¿Qué resultado se obtiene de $100 \\div 10^2 + 5 \\cdot 0$?**\n\\', 'options': {'A': '1', 'B': '0', 'C': '6', 'D': '10'}, 'answer': 'A', 'explanation': 'Potencia: $100 \\div 100 + 0 \\rightarrow 1 + 0 = 1$.'},
            {'question': 'El resultado de $(-2) \\cdot (-1) \\cdot (-3) \\cdot (-2)$ es:**\n\\', 'options': {'A': '12', 'B': '-12', 'C': '6', 'D': '-6'}, 'answer': 'A', 'explanation': 'Cuatro signos negativos (par) resulta en positivo: $2 \\cdot 1 \\cdot 3 \\cdot 2 = 12$.'},
            {'question': 'Si a $-15$ le restamos $-20$, el resultado es:**\n\\', 'options': {'A': '-35', 'B': '35', 'C': '-5', 'D': '5'}, 'answer': 'D', 'explanation': '$-15 - (-20) = -15 + 20 = 5$.'},
            {'question': 'Al multiplicar $0,045$ por $1.000$, el resultado es:**\n\\', 'options': {'A': '4,5', 'B': '45', 'C': '450', 'D': '0,45'}, 'answer': 'B', 'explanation': 'Tres ceros, la coma corre 3 espacios a la derecha: $45$.'},
            {'question': '¿Cuál es el valor de $50 - 2 \\cdot (10 - 4 \\cdot 2)$?**\n\\', 'options': {'A': '96', 'B': '46', 'C': '42', 'D': '38'}, 'answer': 'B', 'explanation': 'Paréntesis interior: $10 - 8 = 2 \\rightarrow 50 - 2 \\cdot 2 \\rightarrow 50 - 4 = 46$.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n10_quiz")

    with st.expander("🔑 Pauta Técnica N10: Mecánica de Operatoria", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El Paso a Paso) |
| :--- | :---: | :--- |
| **1** | **B** | Multiplicación primero: $12 - 8 + 5 = 4 + 5 = 9$. |
| **2** | **B** | De izquierda a derecha: $30 \div 5 = 6$, luego $6 \cdot 3 = 18$. |
| **3** | **B** | $-10 + 5 - 8 \rightarrow -5 - 8 = -13$. |
| **4** | **A** | Paréntesis: $(8+2)=10 \rightarrow 2 \cdot [15-10] \rightarrow 2 \cdot 5 = 10$. |
| **5** | **C** | Amplificar por 100: $120 \div 2 = 60$. |
| **6** | **A** | Potencia: $100 \div 100 + 0 \rightarrow 1 + 0 = 1$. |
| **7** | **A** | Cuatro signos negativos (par) resulta en positivo: $2 \cdot 1 \cdot 3 \cdot 2 = 12$. |
| **8** | **D** | $-15 - (-20) = -15 + 20 = 5$. |
| **9** | **B** | Tres ceros, la coma corre 3 espacios a la derecha: $45$. |
| **10** | **B** | Paréntesis interior: $10 - 8 = 2 \rightarrow 50 - 2 \cdot 2 \rightarrow 50 - 4 = 46$. |

---

> **Típ:** El error más común en la PAES es el signo. Si ves un signo menos delante de un paréntesis, trátalo como una alarma de incendio: todo lo de adentro va a cambiar.
""")
