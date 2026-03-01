import streamlit as st


def render_PB02():
    st.title("PB02: Probabilidad Clásica — La Regla de Laplace")

    st.markdown(r"""
### 🛡️ 1. El Portal: Medir la Incertidumbre con un Número

¿Qué tan probable es que llueva mañana? ¿Qué chance tienes de sacar un $6$ con un dado? La probabilidad asigna un **número entre $0$ y $1$** a cada evento, donde $0$ significa imposible y $1$ significa seguro. La **Regla de Laplace** es el método más directo para calcular probabilidades cuando todos los resultados son **igualmente probables**.

---

### 🛡️ 2. Definición Clásica de Probabilidad (Laplace)

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{casos favorables}}{\text{casos posibles}}$$

**Condición clave:** Todos los resultados del espacio muestral deben ser **equiprobables** (tener la misma probabilidad).

---

### 🛡️ 3. Propiedades Fundamentales

| Propiedad | Fórmula | Significado |
| :--- | :---: | :--- |
| Rango | $0 \leq P(A) \leq 1$ | Toda probabilidad está entre $0$ y $1$ |
| Evento seguro | $P(\Omega) = 1$ | Algún resultado siempre ocurre |
| Evento imposible | $P(\emptyset) = 0$ | Lo imposible tiene probabilidad $0$ |
| Complemento | $P(A^c) = 1 - P(A)$ | La probabilidad de que NO ocurra $A$ |
| Unión (excl.) | $P(A \cup B) = P(A) + P(B)$ | Si $A \cap B = \emptyset$ |
| Unión (general) | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | Para cualquier par de eventos |

> **Tip PAES:** Muchas veces es más fácil calcular $P(A^c)$ y luego $P(A) = 1 - P(A^c)$, especialmente cuando $A$ tiene muchos casos favorables.

---

### 🛡️ 4. Probabilidades Clásicas — Situaciones Frecuentes

#### 🎲 Dado justo (6 caras)
| Evento | Casos favorables | $P$ |
| :--- | :---: | :---: |
| Obtener un $4$ | $1$ | $\frac{1}{6}$ |
| Obtener un par | $\{2, 4, 6\}$ → $3$ | $\frac{3}{6} = \frac{1}{2}$ |
| Obtener un primo | $\{2, 3, 5\}$ → $3$ | $\frac{1}{2}$ |
| Obtener más de $4$ | $\{5, 6\}$ → $2$ | $\frac{1}{3}$ |

#### 🪙 Monedas
| Experimento | $|\Omega|$ | Evento | $P$ |
| :--- | :---: | :--- | :---: |
| $1$ moneda | $2$ | Cara | $\frac{1}{2}$ |
| $2$ monedas | $4$ | Exactamente $1$ cara | $\frac{2}{4} = \frac{1}{2}$ |
| $3$ monedas | $8$ | Las $3$ caras | $\frac{1}{8}$ |

#### 🃏 Baraja española (40 cartas, 4 palos)
| Evento | Casos favorables | $P$ |
| :--- | :---: | :---: |
| Sacar un as | $4$ | $\frac{4}{40} = \frac{1}{10}$ |
| Sacar una carta de oros | $10$ | $\frac{10}{40} = \frac{1}{4}$ |
| Sacar el $7$ de espadas | $1$ | $\frac{1}{40}$ |

---

### 🛡️ 5. Probabilidad del Complemento

Si calcular $P(A)$ directamente es difícil, usa el complemento:

$$P(A) = 1 - P(A^c)$$

**Ejemplo:** ¿Cuál es la probabilidad de obtener **al menos un $6$** al lanzar dos dados?
- Es más fácil calcular $P(\text{ningún } 6) = \frac{5}{6} \times \frac{5}{6} = \frac{25}{36}$.
- Entonces $P(\text{al menos un } 6) = 1 - \frac{25}{36} = \frac{11}{36}$.

---

> *"La probabilidad es el sentido común reducido a cálculo."*
> — **Pierre-Simon Laplace**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería PB02", expanded=False):
        st.markdown(r"""
### E01: Probabilidad con un dado

**Situación:** Se lanza un dado justo. ¿Cuál es la probabilidad de obtener un número mayor que $2$?

**La Carpintería:**
1. $\Omega = \{1, 2, 3, 4, 5, 6\}$, $|\Omega| = 6$.
2. Evento $A$: "mayor que $2$" → $A = \{3, 4, 5, 6\}$, $|A| = 4$.
3. $P(A) = \frac{4}{6} = \frac{2}{3}$.

---

### E02: Probabilidad con cartas

**Situación:** De un mazo de $52$ cartas (baraja inglesa), se saca una carta al azar. ¿Cuál es la probabilidad de que sea un rey o un corazón?

**La Carpintería:**
1. $A$: "ser rey" → $|A| = 4$ (un rey por palo).
2. $B$: "ser corazón" → $|B| = 13$.
3. $A \cap B$: "rey de corazones" → $|A \cap B| = 1$.
4. $P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}$.

---

### E03: Usando el complemento

**Situación:** Se lanzan $3$ monedas. ¿Cuál es la probabilidad de obtener **al menos una cara**?

**La Carpintería:**
1. $|\Omega| = 2^3 = 8$.
2. Complemento: "ninguna cara" = "todos sellos" → $\{SSS\}$ → $|A^c| = 1$.
3. $P(A^c) = \frac{1}{8}$.
4. $P(\text{al menos 1 cara}) = 1 - \frac{1}{8} = \frac{7}{8}$.

---

### E04: Probabilidad con dos dados

**Situación:** Se lanzan dos dados. ¿Cuál es la probabilidad de que la suma sea $7$?

**La Carpintería:**
1. $|\Omega| = 6 \times 6 = 36$.
2. Pares que suman $7$: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ → $|A| = 6$.
3. $P(A) = \frac{6}{36} = \frac{1}{6}$.

| Dado 1 | Dado 2 | Suma |
| :---: | :---: | :---: |
| $1$ | $6$ | $7$ |
| $2$ | $5$ | $7$ |
| $3$ | $4$ | $7$ |
| $4$ | $3$ | $7$ |
| $5$ | $2$ | $7$ |
| $6$ | $1$ | $7$ |
""")

    with st.expander("❓ Cuestionario PB02: Probabilidad Clásica", expanded=False):
        st.markdown(r"""
**1. Se lanza un dado justo. $P(\text{obtener un } 5) =$**

A) $\frac{1}{5}$
B) $\frac{5}{6}$
C) $\frac{1}{6}$
D) $\frac{1}{3}$

---

**2. Si $P(A) = 0{,}3$, entonces $P(A^c) =$**

A) $0{,}3$
B) $0{,}7$
C) $1{,}3$
D) $-0{,}3$

---

**3. De una urna con $5$ bolas rojas y $3$ azules, la probabilidad de sacar una bola azul es:**

A) $\frac{3}{5}$
B) $\frac{5}{8}$
C) $\frac{3}{8}$
D) $\frac{5}{3}$

---

**4. Al lanzar dos monedas, $P(\text{ambas caras}) =$**

A) $\frac{1}{2}$
B) $\frac{1}{3}$
C) $\frac{1}{4}$
D) $\frac{2}{4}$

---

**5. Si $P(A) = \frac{1}{4}$ y $P(B) = \frac{1}{3}$, y $A$ y $B$ son mutuamente excluyentes, $P(A \cup B) =$**

A) $\frac{1}{12}$
B) $\frac{7}{12}$
C) $\frac{1}{7}$
D) $\frac{2}{7}$

---

**6. De un mazo de $40$ cartas (baraja española), ¿cuál es la probabilidad de NO sacar un as?**

A) $\frac{4}{40}$
B) $\frac{1}{10}$
C) $\frac{36}{40}$
D) $\frac{39}{40}$

---

**7. Se lanzan dos dados. ¿Cuántos resultados posibles hay en el espacio muestral?**

A) $12$
B) $36$
C) $6$
D) $24$
""")

    with st.expander("🔑 Pauta Técnica PB02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $P(5) = \frac{1}{6}$. Hay $1$ caso favorable entre $6$ posibles. |
| **2** | **B** | $P(A^c) = 1 - P(A) = 1 - 0{,}3 = 0{,}7$. Propiedad del complemento. |
| **3** | **C** | $P(\text{azul}) = \frac{3}{5+3} = \frac{3}{8}$. Total de bolas = $8$. |
| **4** | **C** | $\Omega = \{CC, CS, SC, SS\}$, $|\Omega|=4$. Solo $CC$ → $P = \frac{1}{4}$. |
| **5** | **B** | Como $A \cap B = \emptyset$: $P(A \cup B) = \frac{1}{4} + \frac{1}{3} = \frac{3+4}{12} = \frac{7}{12}$. |
| **6** | **C** | $P(\text{no as}) = 1 - P(\text{as}) = 1 - \frac{4}{40} = \frac{36}{40} = \frac{9}{10}$. |
| **7** | **B** | $|\Omega| = 6 \times 6 = 36$. Cada dado tiene $6$ caras independientes. |
""")
