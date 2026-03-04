import streamlit as st
import matplotlib.pyplot as plt


def render_N06():
    with st.expander("📚 Teoría", expanded=False):
        st.title("N06: Los Números Irracionales (ℐ o ℚ*) — Lo Inconmensurable")

        st.markdown(r"""
    ### 🛡️  El Portal: El Secreto que Rompió una Secta

    Para Pitágoras y sus seguidores, los números eran la esencia del universo y todo debía ser una fracción perfecta. Sin embargo, al intentar medir la diagonal de un cuadrado de lado 1, se encontraron con un monstruo: $\sqrt{2}$.

    Este número no se podía escribir como fracción. Era "inconmensurable". Cuenta la leyenda que Hipaso de Metaponto fue arrojado al mar por revelar este secreto. Hoy los llamamos **Irracionales**, no porque estén locos, sino porque no pueden expresarse como una **Razón** (fracción).
    """)

        # Figura 1: Diagonal de Pitágoras
        fig, ax = plt.subplots(figsize=(6, 6))
        cuadrado_x = [0, 1, 1, 0, 0]
        cuadrado_y = [0, 0, 1, 1, 0]
        ax.plot(cuadrado_x, cuadrado_y, color='black', lw=2)
        ax.plot([0, 1], [0, 1], color='red', ls='--', lw=3, label='Diagonal = √2')
        ax.text(0.5, -0.1, "Lado = 1", ha='center', fontweight='bold')
        ax.text(-0.15, 0.5, "Lado = 1", va='center', rotation='vertical', fontweight='bold')
        ax.text(0.4, 0.6, "√2 ≈ 1,4142...", color='red', fontsize=12, fontweight='bold', rotation=45)
        ax.set_xlim(-0.2, 1.2)
        ax.set_ylim(-0.2, 1.2)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.title("El Origen de los Irracionales: La Diagonal Inconmensurable", pad=20)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        st.markdown(r"""
    ---

    ### 🛡️ Definición y Características

    Un número es **Irracional** si su expresión decimal es **infinita y no tiene periodo** (no hay una secuencia que se repita jamás).

    * **Indomables:** No importa cuántos decimales calcules, nunca aparecerá un patrón.
    * **El Vacío de la Recta:** Los irracionales vienen a llenar los puntos que los racionales no pueden tocar. Sin ellos, la recta numérica sería como un colador lleno de agujeros.

    ---

    ### 🛡️ Los Tres Pilares (Reconocimiento M1)

    Para la PAES, tu alumno debe identificar estos tres grupos a simple vista:

    1. **Irracionales Algebraicos (Raíces No Exactas):**
        * Ejemplos: $\sqrt{2}, \sqrt{3}, \sqrt{5}, \sqrt{10}$.
        * **⚠️ Ojo de Halcón:** No te dejes engañar. $\sqrt{9} = 3$ (es Racional). Solo si la raíz no es un "cuadrado perfecto", el número es irracional.

    2. **Números Trascendentes (Los Especiales):** Estos son números que tienen nombre propio y aparecen en toda la naturaleza:
        * **$\pi$ (Pi):** El más famoso. Es la relación entre el perímetro de un círculo y su diámetro. $\pi \approx 3,14159...$
        * **$e$ (Número de Euler):** Vital para entender el crecimiento de poblaciones y finanzas. $e \approx 2,71828...$
        * **$\phi$ (Número de Oro / Phi):** Representa la proporción divina en el arte y la naturaleza. $\phi \approx 1,618...$
    """)

        # Figura 2: Los tres trascendentes
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.axhline(0, color='black', lw=2)
        ax.set_xlim(1, 4)
        ax.set_ylim(-0.5, 1)
        for i in range(1, 5):
            ax.plot(i, 0, '|', color='black', markersize=15)
            ax.text(i, -0.2, str(i), ha='center', fontweight='bold')
        nombres = ['Número de Oro (φ)', 'Número de Euler (e)', 'Pi (π)']
        valores = [1.61803, 2.71828, 3.14159]
        colores = ['#D4AF37', '#2E7D32', '#1565C0']
        for i, (nombre, val, col) in enumerate(zip(nombres, valores, colores)):
            ax.plot(val, 0, 'o', color=col, markersize=10)
            ax.annotate(f"{nombre}\n≈ {val:.5f}...",
                        xy=(val, 0.05),
                        xytext=(val, 0.4 + (i * 0.2)),
                        arrowprops=dict(arrowstyle='->', color=col),
                        ha='center', color=col, fontweight='bold')
        ax.axis('off')
        plt.title("Los Tres Grandes Trascendentes en la Recta Numérica", fontsize=14, pad=30)
        plt.tight_layout()
        st.pyplot(fig)
        plt.close()

        st.markdown(r"""
    ---

    ### 🛡️  Operativa: El "Virus" Irracional

    La mezcla de conjuntos tiene reglas de carpintería muy claras:

    * **Racional $\pm$ Irracional = SIEMPRE Irracional.**
        * Ejemplo: $5 + \pi$ es irracional. El irracional "infecta" al número racional.
    * **Irracional $\cdot$ Irracional = INCIERTO.**
        * Caso A: $\sqrt{2} \cdot \sqrt{3} = \sqrt{6}$ (Sigue siendo Irracional).
        * Caso B: $\sqrt{2} \cdot \sqrt{2} = 2$ (¡Se volvió Racional!).

    > **Típ:** Dile a tu alumno que un irracional es como un virus. Si lo sumas a un número "sano" (racional), lo vuelve irracional inmediatamente. Pero si multiplicas dos irracionales "compatibles", pueden terminar curándose y volviendo al mundo de las fracciones.

    ---

    ### 🛡️ Clausura: El Caos Total

    ¿Se cumple la clausura en $\mathbb{I}$? **Rotundamente NO.**
    Si sumas $\pi$ con $-\pi$, el resultado es $0$. Como el $0$ es racional, la suma de dos irracionales puede sacarte del conjunto. En los irracionales, ninguna operación básica es cerrada.

    ---

    ### 🛡️ El Cero: El Gran Impostor

    **Anótalo con fuego:** El número **0 NO es irracional**.
    Aunque el cero es "especial", se puede escribir como una fracción (ejemplo: $0/1$, $0/5$, etc.). Por lo tanto:
    * El cero es **Entero**.
    * El cero es **Racional**.
    * El cero **NUNCA** será irracional.

    > **Típ:** Si en un ejercicio de raíces te aparece $\sqrt{0}$, el resultado es $0$. Por lo tanto, $\sqrt{0}$ es un número Racional. No dejes que el vacío del cero te confunda con el caos de los irracionales.

    ---

    > "Dondequiera que haya un número, hay belleza".
    > — **Proclo**
    """)


    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería N06", expanded=False):
        st.markdown(r"""
### 1: El Filtro de Raíces

**Situación:** Clasificar los siguientes números en Racionales o Irracionales: $\sqrt{49}$, $\sqrt{50}$, $\sqrt{0,25}$.

**La Carpintería:**
1. **Analizar $\sqrt{49}$:** Buscamos un número que al cuadrado dé 49. $7 \cdot 7 = 49$. Es exacta.
2. **Analizar $\sqrt{50}$:** $7^2 = 49$ y $8^2 = 64$. No hay un entero exacto. Es inexacta.
3. **Analizar $\sqrt{0,25}$:** $0,5 \cdot 0,5 = 0,25$. Es exacta.
4. **Resultado:** Solo $\sqrt{50}$ es irracional.

| Número | Valor | Tipo de Número | ¿Por qué? |
| :--- | :---: | :---: | :--- |
| $\sqrt{49}$ | 7 | **Racional** | Entero perfecto. |
| $\sqrt{50}$ | $5\sqrt{2} \approx 7,07...$ | **Irracional** | Decimal infinito sin periodo. |
| $\sqrt{0,25}$ | 0,5 | **Racional** | Decimal finito. |

---

### 2: La Infección del Virus (Suma)

**Situación:** Determinar la naturaleza del número resultante de la expresión: $5 + \pi$.

**La Carpintería:**
1. **Identificar:** 5 es Racional (un entero limpio).
2. **Identificar:** $\pi$ es Irracional Trascendente ($3,14159...$).
3. **Operar:** Al sumar, el desorden infinito de $\pi$ se traslada al resultado: $8,14159...$
4. **Conclusión:** El desorden no se puede "limpiar". El resultado es Irracional.

| Término 1 | Término 2 | Resultado | Clasificación |
| :--- | :--- | :---: | :---: |
| 5 (Racional) | $\pi$ (Irracional) | $5 + \pi$ | **Irracional** |

---

### 3: La "Cura" en la Multiplicación

**Situación:** Resolver $\sqrt{2} \cdot \sqrt{18}$ y clasificar el resultado.

**La Carpintería:**
1. **Unir bajo una raíz:** Por propiedad, multiplicamos los interiores: $\sqrt{2 \cdot 18}$.
2. **Calcular:** $\sqrt{36}$.
3. **Extraer raíz:** $\sqrt{36} = 6$.
4. **Conclusión:** Dos números que por separado eran irracionales, al multiplicarse, se "curaron" y dieron un Racional.

| Paso | Operación | Resultado Parcial | ¿Es Irracional? |
| :--- | :--- | :---: | :---: |
| 1 | Multiplicar interiores | $\sqrt{36}$ | - |
| 2 | Resolver raíz | 6 | **❌ NO (Racional)** |

---

### 4: Operando con el Número de Euler ($e$)

**Situación:** ¿Qué tipo de número es $3e - e$?

**La Carpintería:**
1. **Términos semejantes:** Tratamos a $e$ como una manzana. 3 manzanas menos 1 manzana = 2 manzanas.
2. **Reducir:** $2e$.
3. **Analizar:** $2$ es racional, pero $e$ es irracional ($2,718...$).
4. **Propiedad:** Racional $\cdot$ Irracional (distinto de cero) = Irracional.

| Expresión | Reducción | Valor Aprox. | Tipo |
| :--- | :---: | :---: | :--- |
| $3e - e$ | $2e$ | $5,436...$ | **Irracional** |

---

### 5: El Cero y el Irracional (La Trampa)

**Situación:** Determinar el conjunto del resultado de $0 \cdot \sqrt{7}$.

**La Carpintería:**
1. **Identificar:** $\sqrt{7}$ es irracional.
2. **Aplicar propiedad del cero:** Todo número multiplicado por cero es igual a cero.
3. **Evaluar el cero:** El $0$ es un entero, por lo tanto, es Racional.
4. **Conclusión:** El cero es el único que "mata" al irracional y lo vuelve racional.

| Operación | Lógica | Resultado | Clasificación |
| :--- | :--- | :---: | :---: |
| $0 \cdot \sqrt{7}$ | Elemento absorbente | 0 | **Racional** |
""")

    with st.expander("❓ Cuestionario N06", expanded=False):
        from utils import render_multiple_choice_quiz
        quiz = [
            {'question': '¿Cuál de los siguientes números pertenece al conjunto de los Irracionales ($\\mathbb{I}$)?', 'options': {'A': '$\\sqrt{121}$', 'B': '$\\sqrt{0,01}$', 'C': '$\\sqrt{8}$', 'D': '$0$'}, 'answer': 'C', 'explanation': '$\\sqrt{121} = 11$ (Racional). $\\sqrt{0,01} = 0,1$ (Racional). $0$ es Racional. $\\sqrt{8}$ no es exacta, por ende es Irracional.'},
            {'question': 'El número $\\pi$ (Pi) se define como un número irracional porque:', 'options': {'A': 'Su valor es exactamente $3,14$.', 'B': 'Es el resultado de una raíz inexacta.', 'C': 'Su parte decimal es infinita y no tiene un patrón repetitivo (periodo).', 'D': 'No se puede ubicar en la recta numérica.'}, 'answer': 'C', 'explanation': 'Es la definición fundamental: decimales infinitos sin periodo.'},
            {'question': 'Si $q$ es un número racional distinto de cero e $i$ es un número irracional, ¿qué se puede afirmar del producto $q \\cdot i$?', 'options': {'A': 'Es siempre un número entero.', 'B': 'Es siempre un número racional.', 'C': 'Es siempre un número irracional.', 'D': 'Es siempre igual a cero.'}, 'answer': 'C', 'explanation': 'Propiedad de la "Infección": Un racional (distinto de cero) no puede quitarle el desorden infinito a un irracional al multiplicarlos.'},
            {'question': '¿Cuál de las siguientes expresiones representa un número racional?', 'options': {'A': '$\\sqrt{2} + \\sqrt{2}$', 'B': '$\\pi - \\pi$', 'C': '$e + 1$', 'D': '$\\sqrt{3} \\cdot \\sqrt{5}$'}, 'answer': 'B', 'explanation': '$\\pi - \\pi = 0$. Como el $0$ es un número entero, es Racional.'},
            {'question': 'El número de Oro ($\\phi \\approx 1,618...$) es un ejemplo de:', 'options': {'A': 'Irracional algebraico.', 'B': 'Irracional trascendente.', 'C': 'Racional periódico.', 'D': 'Decimal infinito semiperiódico.'}, 'answer': 'B', 'explanation': 'Los números con nombre propio como $\\pi$, $e$ y $\\phi$ se clasifican como trascendentes.'},
            {'question': 'Respecto al número $0$, ¿cuál de las siguientes afirmaciones es CORRECTA?', 'options': {'A': 'Es un número irracional porque es "especial".', 'B': 'Es racional porque puede expresarse como fracción (ej: $0/1$).', 'C': 'Es un número que no pertenece a ningún conjunto.', 'D': 'Es el origen de los números trascendentes.'}, 'answer': 'B', 'explanation': 'El cero es un número racional. Al poder escribirse como $0/n$, cumple la definición de $\\mathbb{Q}$.'},
            {'question': '¿Cuál es el resultado de la operación $\\sqrt{2} \\cdot \\sqrt{32}$?', 'options': {'A': '$\\sqrt{34}$', 'B': '$8$', 'C': '$64$', 'D': '$4\\sqrt{2}$'}, 'answer': 'B', 'explanation': '$\\sqrt{2} \\cdot \\sqrt{32} = \\sqrt{64} = 8$. El producto de dos irracionales puede dar un racional.'},
            {'question': 'Si sumamos el número irracional $\\sqrt{3}$ con el número irracional $-\\sqrt{3}$, el resultado es:', 'options': {'A': '$2\\sqrt{3}$', 'B': '$\\sqrt{6}$', 'C': '$0$', 'D': 'Un número irracional.'}, 'answer': 'C', 'explanation': '$\\sqrt{3} + (-\\sqrt{3}) = 0$. Esto demuestra que la suma de dos irracionales no siempre da otro irracional.'},
            {'question': 'El número $2,718281828...$ (donde el bloque "1828" se repite infinitamente) es:', 'options': {'A': 'El número de Euler ($e$).', 'B': 'Un número irracional.', 'C': 'Un número racional periódico.', 'D': 'Un número entero.'}, 'answer': 'C', 'explanation': '**Ojo:** Si hay un bloque que se repite (1828), hay periodo. Si hay periodo, es Racional por definición.'},
            {'question': 'Si multiplicas $0 \\cdot \\pi$, el resultado es:', 'options': {'A': '$\\pi$', 'B': '$0$', 'C': 'Un número irracional.', 'D': 'No se puede calcular.'}, 'answer': 'B', 'explanation': 'El cero es el elemento absorbente. $0 \\cdot \\text{Cualquier cosa} = 0$. El resultado es un Racional.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="n06_quiz")

    with st.expander("🔑 Pauta Técnica N06: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **C** | $\sqrt{121} = 11$ (Racional). $\sqrt{0,01} = 0,1$ (Racional). $0$ es Racional. $\sqrt{8}$ no es exacta, por ende es Irracional. |
| **2** | **C** | Es la definición fundamental: decimales infinitos sin periodo. |
| **3** | **C** | Propiedad de la "Infección": Un racional (distinto de cero) no puede quitarle el desorden infinito a un irracional al multiplicarlos. |
| **4** | **B** | $\pi - \pi = 0$. Como el $0$ es un número entero, es Racional. |
| **5** | **B** | Los números con nombre propio como $\pi$, $e$ y $\phi$ se clasifican como trascendentes. |
| **6** | **B** | El cero es un número racional. Al poder escribirse como $0/n$, cumple la definición de $\mathbb{Q}$. |
| **7** | **B** | $\sqrt{2} \cdot \sqrt{32} = \sqrt{64} = 8$. El producto de dos irracionales puede dar un racional. |
| **8** | **C** | $\sqrt{3} + (-\sqrt{3}) = 0$. Esto demuestra que la suma de dos irracionales no siempre da otro irracional. |
| **9** | **C** | **Ojo:** Si hay un bloque que se repite (1828), hay periodo. Si hay periodo, es Racional por definición. |
| **10** | **B** | El cero es el elemento absorbente. $0 \cdot \text{Cualquier cosa} = 0$. El resultado es un Racional. |
""")
