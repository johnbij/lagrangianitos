from utils import render_multiple_choice_quiz
import streamlit as st


def render_PB04():
    with st.expander("📚 Teoría", expanded=False):
        st.title("PB04: Técnicas de Conteo y Combinatoria — Contar sin Enumerar")

        st.markdown(r"""
    ### 🛡️ 1. El Portal: ¿Cuántas Formas Hay?

    Antes de calcular una probabilidad con Laplace ($P = \frac{\text{favorables}}{\text{posibles}}$), necesitas **contar** esos casos. Cuando el espacio muestral es grande, enumerar uno por uno es impracticable. Las técnicas de conteo te dan atajos poderosos para determinar $|A|$ y $|\Omega|$ de forma eficiente.

    ---

    ### 🛡️ 2. Principio Multiplicativo

    Si una tarea se realiza en **etapas sucesivas**, donde la etapa $1$ tiene $n_1$ opciones, la etapa $2$ tiene $n_2$ opciones, etc., el total de formas es:

    $$\text{Total} = n_1 \times n_2 \times \cdots \times n_k$$

    **Ejemplo:** Un menú ofrece $3$ entradas, $4$ platos de fondo y $2$ postres → total de menús = $3 \times 4 \times 2 = 24$.

    ---

    ### 🛡️ 3. Principio Aditivo

    Si una tarea se puede hacer de **una forma O de otra** (formas mutuamente excluyentes), el total es:

    $$\text{Total} = n_1 + n_2 + \cdots + n_k$$

    **Ejemplo:** Puedo ir al trabajo en bus ($5$ líneas) o en metro ($3$ líneas) → total de opciones = $5 + 3 = 8$.

    > **Clave:** Multiplicativo = "Y" (etapas). Aditivo = "O" (alternativas).

    ---

    ### 🛡️ 4. Factorial ($n!$)

    $$n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1$$

    | $n$ | $n!$ |
    | :---: | :---: |
    | $0$ | $1$ (por definición) |
    | $1$ | $1$ |
    | $3$ | $6$ |
    | $5$ | $120$ |
    | $6$ | $720$ |
    | $10$ | $3.628.800$ |

    > **Uso:** $n!$ cuenta el número de formas de **ordenar** $n$ objetos distintos en fila.

    ---

    ### 🛡️ 5. Permutaciones

    Una **permutación** es una disposición ordenada de elementos. El **orden importa**.

    **Permutaciones de $n$ objetos tomados de $r$ en $r$:**

    $$P(n, r) = \frac{n!}{(n-r)!}$$

    **Ejemplo:** ¿De cuántas formas se pueden elegir presidente, vicepresidente y secretario de un grupo de $10$ personas?

    $$P(10, 3) = \frac{10!}{7!} = 10 \times 9 \times 8 = 720$$

    ---

    ### 🛡️ 6. Combinaciones

    Una **combinación** es una selección donde el **orden NO importa**.

    $$\binom{n}{k} = C(n, k) = \frac{n!}{k!(n-k)!}$$

    **Ejemplo:** ¿De cuántas formas se pueden elegir $3$ delegados de un grupo de $10$ personas (sin importar el cargo)?

    $$\binom{10}{3} = \frac{10!}{3! \cdot 7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

    ---

    ### 🛡️ 7. ¿Permutación o Combinación?

    | Pregunta clave | Si sí → | Si no → |
    | :--- | :--- | :--- |
    | ¿Importa el orden? | **Permutación** | **Combinación** |

    | Situación | ¿Importa el orden? | Tipo |
    | :--- | :---: | :--- |
    | Elegir presidente y secretario | Sí | Permutación |
    | Elegir un comité de $3$ personas | No | Combinación |
    | Formar una clave de $4$ dígitos | Sí | Permutación |
    | Elegir $5$ cartas de un mazo | No | Combinación |

    ---

    ### 🛡️ 8. Variaciones con Repetición

    Cuando los elementos se pueden **repetir** y el orden importa:

    $$VR(n, r) = n^r$$

    **Ejemplo:** Claves de $4$ dígitos (cada dígito de $0$ a $9$): $10^4 = 10.000$.

    ---

    > *"Contar es la primera habilidad matemática; saber contar bien, la última."*
    > — **Anónimo**
    """)


    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería PB04", expanded=False):
        st.markdown(r"""
### E01: Principio multiplicativo

**Situación:** Un código de acceso tiene $2$ letras (de $26$ posibles) seguidas de $3$ dígitos (de $0$ a $9$). ¿Cuántos códigos distintos hay? (Se pueden repetir.)

**La Carpintería:**
1. Letras: $26$ opciones cada una → $26 \times 26$.
2. Dígitos: $10$ opciones cada uno → $10 \times 10 \times 10$.
3. Total: $26^2 \times 10^3 = 676 \times 1000 = 676.000$.

---

### E02: Permutaciones

**Situación:** ¿De cuántas maneras se pueden sentar $5$ personas en $5$ sillas en fila?

**La Carpintería:**
1. La primera silla: $5$ opciones.
2. La segunda: $4$ opciones.
3. La tercera: $3$, cuarta: $2$, quinta: $1$.
4. Total: $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$.

---

### E03: Combinaciones

**Situación:** De $8$ estudiantes, se quiere formar un grupo de $3$ para un proyecto. ¿Cuántos grupos distintos se pueden formar?

**La Carpintería:**
1. No importa el orden (grupo $\{A, B, C\}$ = grupo $\{C, A, B\}$) → **combinación**.
2. $\binom{8}{3} = \frac{8!}{3! \cdot 5!} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = \frac{336}{6} = 56$.

---

### E04: Problema PAES contextualizado

**Situación:** Una heladería ofrece $6$ sabores. ¿De cuántas formas puedes pedir un helado de $2$ sabores distintos (sin importar el orden)?

**La Carpintería:**
1. No importa el orden (chocolate-vainilla = vainilla-chocolate) → **combinación**.
2. $\binom{6}{2} = \frac{6!}{2! \cdot 4!} = \frac{6 \times 5}{2 \times 1} = 15$.

---

### E05: Principio aditivo + multiplicativo combinados

**Situación:** Una contraseña tiene exactamente $3$ caracteres. Puede ser $3$ letras mayúsculas O $3$ dígitos. ¿Cuántas contraseñas hay?

**La Carpintería:**
1. Caso 1 ($3$ letras): $26^3 = 17.576$.
2. Caso 2 ($3$ dígitos): $10^3 = 1.000$.
3. Como son alternativas excluyentes → **principio aditivo**.
4. Total: $17.576 + 1.000 = 18.576$.
""")

    with st.expander("❓ Cuestionario PB04: Técnicas de Conteo", expanded=False):
        quiz_questions = [
            {"question": "$5!$ es igual a:", "options": {"A": "$25$", "B": "$120$", "C": "$60$", "D": "$720$"}, "answer": "B", "explanation": "$5!=5\\times4\\times3\\times2\\times1=120$."},
            {"question": "¿Cuántas formas hay de ordenar las letras de 'SOL'?", "options": {"A": "$3$", "B": "$6$", "C": "$9$", "D": "$27$"}, "answer": "B", "explanation": "$3!=6$."},
            {"question": "Se eligen $2$ delegados de $10$ alumnos (sin importar cargo). ¿Cuántas formas?", "options": {"A": "$90$", "B": "$45$", "C": "$20$", "D": "$100$"}, "answer": "B", "explanation": "$\\binom{10}{2}=45$."},
            {"question": "Una placa tiene $4$ letras y $2$ dígitos (con repetición). ¿Cuántas placas hay?", "options": {"A": "$26^4\\times10^2$", "B": "$26\\times10$", "C": "$\\binom{26}{4}\\times\\binom{10}{2}$", "D": "$26+10$"}, "answer": "A", "explanation": "Con repetición: $26^4\\cdot10^2$."},
            {"question": "$\\binom{5}{2}$ es igual a:", "options": {"A": "$25$", "B": "$20$", "C": "$10$", "D": "$\\dfrac{5}{2}$"}, "answer": "C", "explanation": "$\\binom{5}{2}=\\frac{5\\times4}{2}=10$."},
            {"question": "¿Cuál es la diferencia entre permutación y combinación?", "options": {"A": "En la permutación no importa el orden", "B": "En la combinación importa el orden", "C": "En la permutación importa el orden; en la combinación, no", "D": "Son lo mismo"}, "answer": "C", "explanation": "Permutación: orden importa. Combinación: orden no importa."},
            {"question": "Claves de $3$ dígitos del $1$ al $5$ SIN repetir. ¿Cuántas hay?", "options": {"A": "$125$", "B": "$60$", "C": "$10$", "D": "$15$"}, "answer": "B", "explanation": "$P(5,3)=5\\times4\\times3=60$."},
        ]
        render_multiple_choice_quiz(quiz_questions, key_prefix="pb04_quiz")
