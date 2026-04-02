from utils import render_multiple_choice_quiz
import streamlit as st


def render_PB01():
    with st.expander("📚 Teoría", expanded=False):
        st.title("PB01: Espacio Muestral y Eventos — El Universo de lo Posible")

        st.markdown(r"""
    ### 🛡️ 1. El Portal: Lo Aleatorio y lo Determinista

    En la vida diaria conviven dos mundos: el de los fenómenos **deterministas** (siempre dan el mismo resultado bajo las mismas condiciones, como calcular $2 + 3$) y el de los fenómenos **aleatorios** (su resultado no se puede predecir con certeza, como lanzar un dado). La probabilidad es la herramienta matemática que nos permite medir y razonar sobre lo incierto.

    ---

    ### 🛡️ 2. Experimento Aleatorio

    Un **experimento aleatorio** es una acción cuyo resultado no se puede predecir con seguridad, aunque sí se pueden enumerar todos los posibles resultados.

    | Concepto | Ejemplo |
    | :--- | :--- |
    | **Experimento determinista** | Soltar un objeto: siempre cae (gravedad) |
    | **Experimento aleatorio** | Lanzar una moneda: puede salir cara o sello |

    ---

    ### 🛡️ 3. Espacio Muestral ($\Omega$)

    El **espacio muestral** es el conjunto de **todos los resultados posibles** de un experimento aleatorio.

    | Experimento | Espacio muestral $\Omega$ | $|\Omega|$ |
    | :--- | :--- | :---: |
    | Lanzar una moneda | $\{C, S\}$ | $2$ |
    | Lanzar un dado | $\{1, 2, 3, 4, 5, 6\}$ | $6$ |
    | Lanzar dos monedas | $\{CC, CS, SC, SS\}$ | $4$ |
    | Lanzar dos dados | Pares $(i, j)$ con $i, j \in \{1,\ldots,6\}$ | $36$ |

    > **Tip PAES:** Siempre identifica primero el espacio muestral antes de calcular probabilidades. Es tu punto de partida.

    ---

    ### 🛡️ 4. Evento o Suceso

    Un **evento** es cualquier subconjunto del espacio muestral. Es "lo que nos interesa que ocurra".

    | Tipo de evento | Descripción | Ejemplo (dado) |
    | :--- | :--- | :--- |
    | **Simple** | Contiene un solo resultado | $A = \{3\}$ |
    | **Compuesto** | Contiene más de un resultado | $B = \{2, 4, 6\}$ (números pares) |
    | **Seguro** ($\Omega$) | Siempre ocurre | Obtener un número entre $1$ y $6$ |
    | **Imposible** ($\emptyset$) | Nunca ocurre | Obtener un $7$ |

    ---

    ### 🛡️ 5. Eventos Mutuamente Excluyentes

    Dos eventos $A$ y $B$ son **mutuamente excluyentes** si no pueden ocurrir al mismo tiempo:

    $$A \cap B = \emptyset$$

    | Eventos | ¿Mutuamente excluyentes? |
    | :--- | :---: |
    | Sacar par / sacar impar (un dado) | ✅ Sí |
    | Sacar par / sacar mayor que $4$ | ❌ No ($6$ cumple ambos) |
    | Sacar cara / sacar sello (una moneda) | ✅ Sí |

    ---

    ### 🛡️ 6. Operaciones con Eventos

    | Operación | Notación | Significado |
    | :--- | :---: | :--- |
    | **Unión** | $A \cup B$ | Ocurre $A$ **o** $B$ (o ambos) |
    | **Intersección** | $A \cap B$ | Ocurren $A$ **y** $B$ simultáneamente |
    | **Complemento** | $A^c$ o $\bar{A}$ | **No** ocurre $A$ |

    **Ejemplo (dado):** $A = \{1, 3, 5\}$ (impares), $B = \{4, 5, 6\}$ (mayores que $3$).
    - $A \cup B = \{1, 3, 4, 5, 6\}$
    - $A \cap B = \{5\}$
    - $A^c = \{2, 4, 6\}$

    ---

    > *"El azar no es más que la medida de nuestra ignorancia."*
    > — **Henri Poincaré**
    """)


    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería PB01", expanded=False):
        st.markdown(r"""
### E01: Determinar el espacio muestral

**Situación:** Se lanza una moneda y un dado simultáneamente. ¿Cuál es el espacio muestral?

**La Carpintería:**
1. La moneda tiene $2$ resultados: $\{C, S\}$.
2. El dado tiene $6$ resultados: $\{1, 2, 3, 4, 5, 6\}$.
3. **Principio multiplicativo:** $|\Omega| = 2 \times 6 = 12$.
4. $\Omega = \{(C,1), (C,2), (C,3), (C,4), (C,5), (C,6), (S,1), (S,2), (S,3), (S,4), (S,5), (S,6)\}$.

---

### E02: Identificar eventos

**Situación:** Con el espacio muestral del E01, define:
- $A$: "Sale cara y número par"
- $B$: "Sale sello"

**La Carpintería:**
1. $A = \{(C,2), (C,4), (C,6)\}$ → $|A| = 3$.
2. $B = \{(S,1), (S,2), (S,3), (S,4), (S,5), (S,6)\}$ → $|B| = 6$.
3. $A \cap B = \emptyset$ (no se puede tener cara y sello a la vez) → son **mutuamente excluyentes**.
4. $A \cup B = \{(C,2), (C,4), (C,6), (S,1), (S,2), (S,3), (S,4), (S,5), (S,6)\}$ → $|A \cup B| = 9$.

---

### E03: Complemento de un evento

**Situación:** Se lanza un dado. Sea $A = \{1, 2, 3\}$ (obtener un número menor o igual a $3$). Halla $A^c$.

**La Carpintería:**
1. $\Omega = \{1, 2, 3, 4, 5, 6\}$.
2. $A^c = \Omega \setminus A = \{4, 5, 6\}$.
3. $|A^c| = 3$.
4. **Verificación:** $|A| + |A^c| = 3 + 3 = 6 = |\Omega|$ ✅.

---

### E04: Clasificar experimentos

**Situación:** Clasifica como determinista o aleatorio:
- (a) Calentar agua a $100°$C al nivel del mar → hierve.
- (b) Elegir una carta de un mazo de $52$.
- (c) Calcular $\sqrt{9}$.

**La Carpintería:**

| Experimento | Clasificación | Razón |
| :--- | :--- | :--- |
| (a) Calentar agua | Determinista | Siempre hierve a $100°$C (al nivel del mar) |
| (b) Elegir una carta | Aleatorio | Hay $52$ resultados posibles, no se sabe cuál saldrá |
| (c) Calcular $\sqrt{9}$ | Determinista | Siempre da $3$ |
""")

    with st.expander("❓ Cuestionario PB01: Espacio Muestral y Eventos", expanded=False):
        quiz_questions = [
            {"question": "El espacio muestral de lanzar dos monedas es:", "options": {"A": "$\\{C,S\\}$", "B": "$\\{CC,CS,SS\\}$", "C": "$\\{CC,CS,SC,SS\\}$", "D": "$\\{C,S,CC,SS\\}$"}, "answer": "C", "explanation": "$2\\times2=4$ pares: $CC,CS,SC,SS$. $CS\\neq SC$."},
            {"question": "Al lanzar un dado, el evento 'número primo' es:", "options": {"A": "$\\{1,3,5\\}$", "B": "$\\{2,3,5\\}$", "C": "$\\{2,4,6\\}$", "D": "$\\{1,2,3\\}$"}, "answer": "B", "explanation": "Los primos entre $1$ y $6$ son $2,3,5$. El $1$ no es primo."},
            {"question": "Dos eventos son mutuamente excluyentes cuando:", "options": {"A": "Siempre ocurren juntos", "B": "Su unión es el espacio muestral", "C": "Su intersección es vacía", "D": "Son complementarios"}, "answer": "C", "explanation": "Mutuamente excluyentes $\\Leftrightarrow A\\cap B=\\emptyset$."},
            {"question": "Si $\\Omega=\\{1,2,3,4,5,6\\}$ y $A=\\{2,4,6\\}$, entonces $A^c$ es:", "options": {"A": "$\\{1,2,3\\}$", "B": "$\\{1,3,5\\}$", "C": "$\\{4,5,6\\}$", "D": "$\\{2,4,6\\}$"}, "answer": "B", "explanation": "$A^c=\\Omega\\setminus A=\\{1,3,5\\}$."},
            {"question": "¿Cuántos elementos tiene el espacio muestral al lanzar $3$ monedas?", "options": {"A": "$3$", "B": "$6$", "C": "$8$", "D": "$9$"}, "answer": "C", "explanation": "$|\\Omega|=2^3=8$."},
            {"question": "El evento imposible se denota como:", "options": {"A": "$\\Omega$", "B": "$\\{0\\}$", "C": "$\\emptyset$", "D": "$\\{1\\}$"}, "answer": "C", "explanation": "El evento imposible es $\\emptyset$. No tiene elementos."},
            {"question": "Con $A=\\{1,3,5\\}$ y $B=\\{5,6\\}$, $A\\cap B$ es:", "options": {"A": "$\\{1,3,5,6\\}$", "B": "$\\{5\\}$", "C": "$\\emptyset$", "D": "$\\{6\\}$"}, "answer": "B", "explanation": "$A\\cap B=\\{5\\}$."},
        ]
        render_multiple_choice_quiz(quiz_questions, key_prefix="pb01_quiz")
