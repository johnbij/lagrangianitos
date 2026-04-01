import streamlit as st


def render_N01():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(r"""
# N01: Teoría de Conjuntos - El Lenguaje Maestro

---

### 🛡️ 1. El Portal
Antes de entrar al universo de los números, necesitamos el lenguaje que los une a todos. La **Teoría de Conjuntos** es la **Gramática del Universo matemático**: el marco fundamental que define qué es un objeto, cómo se agrupan y cómo se relacionan entre sí.

Este es el punto de partida de todo viaje matemático serio. Sin él, el álgebra, los números y la probabilidad no tendrían cimientos.

---

### 🛡️ 2. Crónica del Infinito
A finales del siglo XIX, el matemático alemán **Georg Cantor** se atrevió a lo impensable: trató el infinito como si fuera un objeto matemático concreto. Su idea revolucionaria fue que una colección de objetos bien definidos podía ser tratada como un ente matemático único: el **conjunto**.

Su trabajo fue rechazado por muchos contemporáneos, pero hoy es la piedra angular de toda la matemática moderna.

---

### 🛡️ 3. El Marco de Referencia

| Concepto | Símbolo | Definición |
| :--- | :---: | :--- |
| **Universo** | $\mathcal{U}$ | El conjunto que contiene a todos los elementos posibles en un contexto dado. |
| **Vacío** | $\emptyset$ | El conjunto sin ningún elemento. Es subconjunto de cualquier conjunto. |
| **Pertenencia** | $\in$ | $x \in A$ significa que el elemento $x$ está dentro del conjunto $A$. |
| **Subconjunto** | $\subset$ | $A \subset B$ significa que todo elemento de $A$ también está en $B$. |

> **Típ:** Si $A \subset B$, entonces $A \cap B = A$ y $A \cup B = B$. Esto es un atajo poderoso en la PAES.

---

### 🛡️ 4. Operaciones de "1000 Puntos"

| Operación | Símbolo | Definición | Ejemplo ($A=\{1,2,3\}$, $B=\{3,4,5\}$) |
| :--- | :---: | :--- | :--- |
| **Unión** | $A \cup B$ | Todos los elementos que están en $A$ **o** en $B$ (o en ambos). | $\{1,2,3,4,5\}$ |
| **Intersección** | $A \cap B$ | Solo los elementos que están en $A$ **y** en $B$ al mismo tiempo. | $\{3\}$ |
| **Diferencia** | $A - B$ | Los elementos de $A$ que **no** están en $B$. | $\{1,2\}$ |
| **Complemento** | $A^c$ | Todo lo que está en el Universo $\mathcal{U}$ pero **fuera** de $A$. | Depende de $\mathcal{U}$ |

---

### 🛡️ 5. Cardinalidad y Conjunto Potencia

* **Cardinalidad** ($\#A = n$): Es el número de elementos que tiene un conjunto.
* **Regla de Oro** (Principio de Inclusión-Exclusión):
$$\#(A \cup B) = \#A + \#B - \#(A \cap B)$$
* **Conjunto Potencia** ($\mathcal{P}(A)$): Es el conjunto formado por **todos los subconjuntos posibles** de $A$, incluidos el conjunto vacío $\emptyset$ y el propio $A$.
* **Fórmula:** Si $\#A = n$, entonces $\#\mathcal{P}(A) = 2^n$.

> **Típ:** El conjunto potencia **siempre** incluye al vacío $\emptyset$ y al conjunto completo $A$. ¡No los olvides en la cuenta!

---

### 🛡️ 6. Cartografía Visual (Diagramas de Venn-Euler)
Los **Diagramas de Venn-Euler** son la herramienta visual definitiva para representar conjuntos y sus operaciones. Se usan rectángulos para el Universo y círculos (u óvalos) para los conjuntos. Las zonas de superposición representan la intersección, mientras que las zonas exclusivas representan las diferencias.

Son especialmente útiles para resolver problemas de conteo con múltiples grupos superpuestos.

---

> *"En matemáticas, el arte de hacer preguntas es más valioso que el de resolver problemas."*
>
> — **Georg Cantor**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería N01", expanded=False):
        st.markdown(r"""
### E01: Identificación de Pertenencia

Dado el conjunto $V = \{m, n, \{p, q\}\}$, verifica las siguientes afirmaciones:

| Afirmación | ¿Es verdadera? | Razón |
| :--- | :---: | :--- |
| $p \in V$ | ❌ NO | $p$ no es un elemento directo de $V$; está dentro del subconjunto $\{p,q\}$. |
| $\{p, q\} \in V$ | ✅ SÍ | El objeto $\{p,q\}$ es un elemento directo de $V$. |
| $q \in V$ | ❌ NO | $q$ no es un elemento directo de $V$; está dentro del subconjunto $\{p,q\}$. |
| $\{m, n\} \in V$ | ❌ NO | $\{m,n\}$ no es un elemento de $V$; $m$ y $n$ son elementos separados. |

---

### E02: Operaciones Básicas

Dados $A = \{1,2,3,4,5\}$ y $B = \{3,4,5,6,7\}$:

| Operación | Resultado |
| :--- | :--- |
| $A \cup B$ | $\{1,2,3,4,5,6,7\}$ |
| $A \cap B$ | $\{3,4,5\}$ |
| $A - B$ | $\{1,2\}$ |
| $B - A$ | $\{6,7\}$ |

---

### E03: Cardinalidad y Conjunto Potencia

Sea $C = \{a, b, c\}$. Entonces $\#C = 3$ y $\#\mathcal{P}(C) = 2^3 = 8$.

Los 8 subconjuntos de $C$ son:

$$\emptyset,\ \{a\},\ \{b\},\ \{c\},\ \{a,b\},\ \{a,c\},\ \{b,c\},\ \{a,b,c\}$$

---

### E04: Problema de Aplicación (Regla de Oro)

En un curso de **40 alumnos**, 20 practican fútbol ($F$), 15 practican básquetbol ($B$) y 5 practican ambos deportes.

**¿Cuántos no practican ninguno?**

Paso 1 — Aplicar la Regla de Oro:
$$\#(F \cup B) = \#F + \#B - \#(F \cap B) = 20 + 15 - 5 = 30$$

Paso 2 — Calcular los que no practican ninguno:
$$\text{Ninguno} = \text{Total} - \#(F \cup B) = 40 - 30 = \boxed{10}$$

---

### E05: Verificación de Subconjuntos

Sea $M = \{2, 4, 6, 8\}$. ¿Cuál de las siguientes opciones es un subconjunto de $M$?

| Conjunto | ¿Es subconjunto de $M$? | Razón |
| :--- | :---: | :--- |
| $\{2, 4, 10\}$ | ❌ NO | El 10 no pertenece a $M$. |
| $\{6, 8, 0\}$ | ❌ NO | El 0 no pertenece a $M$. |
| $\{2, 8\}$ | ✅ SÍ | Tanto el 2 como el 8 están en $M$. |
| $\{4, 5, 6\}$ | ❌ NO | El 5 no pertenece a $M$. |
""")

    with st.expander("❓ Cuestionario N01: Teoría de Conjuntos", expanded=False):
        from utils import render_multiple_choice_quiz
        _quiz_data = [
            {
                "question": "Si el conjunto $A$ tiene una cardinalidad $n = 5$, ¿cuántos subconjuntos tiene en total su conjunto potencia?",
                "options": {"A": "$5$", "B": "$10$", "C": "$25$", "D": "$32$"},
                "answer": "D",
                "explanation": "Si $n = 5$, el total de subconjuntos es $2^5 = 32$."
            },
            {
                "question": "Dado el conjunto $V = \\{m, n, \\{p, q\\}\\}$, ¿cuál de las siguientes afirmaciones es CORRECTA?",
                "options": {"A": "$p \\in V$", "B": "$\\{p, q\\} \\in V$", "C": "$q \\in V$", "D": "$\\{m, n\\} \\in V$"},
                "answer": "B",
                "explanation": "$\\{p, q\\}$ es un elemento dentro del conjunto $V$."
            },
            {
                "question": "La operación que representa a los elementos que pertenecen al conjunto $A$ pero que NO pertenecen al conjunto $B$ es:",
                "options": {"A": "$A \\cup B$", "B": "$A \\cap B$", "C": "$A - B$", "D": "$A^c$"},
                "answer": "C",
                "explanation": "La diferencia $A - B$ elimina los elementos comunes con $B$."
            },
            {
                "question": "Si $A \\subset B$, entonces es SIEMPRE cierto que:",
                "options": {"A": "$A \\cap B = B$", "B": "$A \\cup B = A$", "C": "$A \\cap B = A$", "D": "$A - B = B$"},
                "answer": "C",
                "explanation": "Si $A$ está contenido en $B$, su intersección es $A$ mismo."
            },
            {
                "question": "En un curso de 40 alumnos, 20 practican fútbol, 15 practican básquetbol y 5 practican ambos deportes. ¿Cuántos alumnos NO practican ninguno de estos dos deportes?",
                "options": {"A": "$0$", "B": "$5$", "C": "$10$", "D": "$30$"},
                "answer": "C",
                "explanation": "Total practican algún deporte: $20 + 15 - 5 = 30$. No practican: $40 - 30 = 10$."
            },
            {
                "question": "El conjunto que no posee elementos y es subconjunto de cualquier otro conjunto se denomina:",
                "options": {"A": "Conjunto Universo", "B": "Conjunto Unitario", "C": "Conjunto Vacío", "D": "Conjunto Potencia"},
                "answer": "C",
                "explanation": "El conjunto vacío $\\emptyset$ no tiene elementos y es subconjunto de cualquier conjunto."
            },
            {
                "question": "Si $\\#A = 8$, $\\#B = 12$ y $\\#(A \\cap B) = 0$, ¿cuál es la cardinalidad de $A \\cup B$?",
                "options": {"A": "$0$", "B": "$4$", "C": "$12$", "D": "$20$"},
                "answer": "D",
                "explanation": "Si no hay intersección: $\\#(A \\cup B) = 8 + 12 = 20$."
            },
            {
                "question": "Si un conjunto aumenta su cardinalidad de $n=2$ a $n=3$, ¿en cuánto aumenta su cantidad de subconjuntos?",
                "options": {"A": "En $1$", "B": "En $2$", "C": "En $4$", "D": "En $8$"},
                "answer": "C",
                "explanation": "De $n=2$ a $n=3$: $2^3 - 2^2 = 8 - 4 = 4$ subconjuntos más."
            },
            {
                "question": "¿Qué operación define a todos los elementos que están en el Universo ($\\mathcal{U}$) pero que están fuera del conjunto $A$?",
                "options": {"A": "$A \\cap \\mathcal{U}$", "B": "$A^c$", "C": "$A - \\mathcal{U}$", "D": "$\\emptyset$"},
                "answer": "B",
                "explanation": "El complemento $A^c$ es todo lo que está fuera de $A$ pero en $\\mathcal{U}$."
            },
            {
                "question": "Si el conjunto $M = \\{2, 4, 6, 8\\}$, ¿cuál de los siguientes es un subconjunto de $M$?",
                "options": {"A": "$\\{2, 4, 10\\}$", "B": "$\\{6, 8, 0\\}$", "C": "$\\{2, 8\\}$", "D": "$\\{4, 5, 6\\}$"},
                "answer": "C",
                "explanation": "$\\{2, 8\\}$ está completamente contenido en $M$."
            }
        ]
        render_multiple_choice_quiz(_quiz_data, key_prefix="n01_quiz")

        if st.button("🚀 ENVIAR RESPUESTAS Y COMPLETAR CLASE"):
            exito = st.session_state.registrar_progreso("N01")
            if exito:
                st.success("¡Progreso guardado! Revisa tu radar en el inicio.")
                st.balloons()
