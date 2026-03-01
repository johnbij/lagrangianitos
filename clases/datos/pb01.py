import streamlit as st


def render_PB01():
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
        st.markdown(r"""
**1. El espacio muestral de lanzar dos monedas es:**

A) $\{C, S\}$
B) $\{CC, CS, SS\}$
C) $\{CC, CS, SC, SS\}$
D) $\{C, S, CC, SS\}$

---

**2. Al lanzar un dado, el evento "obtener un número primo" es:**

A) $\{1, 3, 5\}$
B) $\{2, 3, 5\}$
C) $\{2, 4, 6\}$
D) $\{1, 2, 3\}$

---

**3. Dos eventos son mutuamente excluyentes cuando:**

A) Siempre ocurren juntos
B) Su unión es el espacio muestral
C) Su intersección es vacía
D) Son complementarios

---

**4. Si $\Omega = \{1, 2, 3, 4, 5, 6\}$ y $A = \{2, 4, 6\}$, entonces $A^c$ es:**

A) $\{1, 2, 3\}$
B) $\{1, 3, 5\}$
C) $\{4, 5, 6\}$
D) $\{2, 4, 6\}$

---

**5. ¿Cuántos elementos tiene el espacio muestral al lanzar $3$ monedas?**

A) $3$
B) $6$
C) $8$
D) $9$

---

**6. El evento imposible se denota como:**

A) $\Omega$
B) $\{0\}$
C) $\emptyset$
D) $\{1\}$

---

**7. Al lanzar un dado, los eventos $A = \{1, 3, 5\}$ y $B = \{5, 6\}$ tienen $A \cap B$ igual a:**

A) $\{1, 3, 5, 6\}$
B) $\{5\}$
C) $\emptyset$
D) $\{6\}$
""")

    with st.expander("🔑 Pauta Técnica PB01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | Cada moneda tiene $2$ resultados → $2 \times 2 = 4$ pares: $CC, CS, SC, SS$. $CS \neq SC$. |
| **2** | **B** | Los primos entre $1$ y $6$ son $2, 3, 5$. El $1$ no es primo. |
| **3** | **C** | Mutuamente excluyentes $\Leftrightarrow$ $A \cap B = \emptyset$. No pueden ocurrir a la vez. |
| **4** | **B** | $A^c = \Omega \setminus A = \{1, 3, 5\}$. Son los elementos de $\Omega$ que no están en $A$. |
| **5** | **C** | $|\Omega| = 2^3 = 8$. Cada moneda aporta $2$ resultados. |
| **6** | **C** | El evento imposible es el conjunto vacío $\emptyset$. No tiene elementos. |
| **7** | **B** | $A \cap B = \{5\}$. Es el único elemento que pertenece a ambos conjuntos. |
""")
