import streamlit as st


def render_V01():
    st.title("V01: Vectores en el Plano — La Flecha que Cambia Todo")

    st.markdown(r"""
### 🛡️ 1. ¿Qué es un Vector?

Un **vector** es un ente matemático que tiene **magnitud** (cuánto), **dirección** (hacia dónde) y **sentido** (en qué orientación). Se representa gráficamente como una **flecha**.

A diferencia de un número (escalar), un vector necesita más de un dato para ser descrito. En el plano, un vector se escribe como:

$$\vec{v} = (v_1,\; v_2)$$

donde $v_1$ es la **componente horizontal** y $v_2$ la **componente vertical**.

---

### 🛡️ 2. Componentes de un Vector

Si un vector va del punto $A(x_1, y_1)$ al punto $B(x_2, y_2)$, sus componentes son:

$$\vec{AB} = (x_2 - x_1,\; y_2 - y_1)$$

| Punto inicial | Punto final | Vector |
| :--- | :--- | :--- |
| $A(1, 3)$ | $B(4, 7)$ | $\vec{AB} = (3, 4)$ |
| $P(5, 2)$ | $Q(1, 6)$ | $\vec{PQ} = (-4, 4)$ |
| $M(0, 0)$ | $N(3, -2)$ | $\vec{MN} = (3, -2)$ |

---

### 🛡️ 3. Vector Posición

El **vector posición** de un punto $P(a, b)$ es el vector que va desde el **origen** $O(0, 0)$ hasta $P$:

$$\vec{OP} = (a, b)$$

Todo punto del plano tiene un único vector posición.

---

### 🛡️ 4. Módulo (Magnitud) de un Vector

El **módulo** o **norma** de un vector $\vec{v} = (v_1, v_2)$ es su "largo":

$$|\vec{v}| = \|\vec{v}\| = \sqrt{v_1^2 + v_2^2}$$

| Vector | Módulo |
| :--- | :--- |
| $\vec{v} = (3, 4)$ | $\|\vec{v}\| = \sqrt{9+16} = 5$ |
| $\vec{w} = (1, 1)$ | $\|\vec{w}\| = \sqrt{2}$ |
| $\vec{u} = (-5, 12)$ | $\|\vec{u}\| = \sqrt{25+144} = 13$ |

> **Tip PAES:** El módulo siempre es un número **no negativo**. Solo el vector nulo tiene módulo $0$.

---

### 🛡️ 5. Dirección y Sentido

- **Dirección:** La recta sobre la que yace el vector (dada por la pendiente o el ángulo con el eje $x$).
- **Sentido:** La orientación sobre esa recta (indica hacia qué lado apunta la flecha).

El ángulo $\theta$ que forma el vector con el eje $x$ positivo se calcula con:

$$\tan \theta = \frac{v_2}{v_1}$$

---

### 🛡️ 6. Vectores Iguales, Vector Nulo y Vector Unitario

| Concepto | Definición |
| :--- | :--- |
| **Vectores iguales** | Tienen las mismas componentes: $\vec{u} = \vec{v}$ si $u_1 = v_1$ y $u_2 = v_2$ |
| **Vector nulo** | $\vec{0} = (0, 0)$. Módulo cero, dirección indefinida |
| **Vector unitario** | Tiene módulo $1$: $\hat{v} = \frac{\vec{v}}{\|\vec{v}\|}$ |
| **Vectores opuestos** | $\vec{v}$ y $-\vec{v}$ tienen igual módulo y dirección, pero sentido contrario |

Los vectores unitarios canónicos son:

$$\hat{i} = (1, 0) \quad \text{y} \quad \hat{j} = (0, 1)$$

Cualquier vector se puede escribir como: $\vec{v} = v_1 \hat{i} + v_2 \hat{j}$.

---

> *"Los vectores son el idioma en que la naturaleza describe el movimiento."*
> — **Tradición matemática**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería V01", expanded=False):
        st.markdown(r"""
### E01: Componentes de un vector

**Situación:** Encuentra el vector $\vec{AB}$ si $A(2, -1)$ y $B(5, 3)$.

**La Carpintería:**
1. $\vec{AB} = (x_B - x_A,\; y_B - y_A) = (5 - 2,\; 3 - (-1)) = (3, 4)$.

| Componente | Cálculo | Resultado |
| :--- | :--- | :---: |
| Horizontal | $5 - 2$ | $3$ |
| Vertical | $3 - (-1)$ | $4$ |
| **Vector** | | **(3, 4)** |

---

### E02: Módulo de un vector

**Situación:** Calcula el módulo de $\vec{v} = (-6, 8)$.

**La Carpintería:**
1. $\|\vec{v}\| = \sqrt{(-6)^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$.

---

### E03: Vector unitario

**Situación:** Encuentra el vector unitario en la dirección de $\vec{u} = (3, 4)$.

**La Carpintería:**
1. $\|\vec{u}\| = \sqrt{9 + 16} = 5$.
2. $\hat{u} = \frac{\vec{u}}{\|\vec{u}\|} = \frac{(3, 4)}{5} = \left(\frac{3}{5},\; \frac{4}{5}\right)$.
3. **Verificación:** $\|\hat{u}\| = \sqrt{\left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2} = \sqrt{\frac{9+16}{25}} = 1$ ✅.

---

### E04: Vectores iguales

**Situación:** Si $\vec{PQ} = (2, -3)$ con $P(1, 5)$, ¿cuáles son las coordenadas de $Q$?

**La Carpintería:**
1. $\vec{PQ} = (x_Q - 1,\; y_Q - 5) = (2, -3)$.
2. $x_Q - 1 = 2 \Rightarrow x_Q = 3$.
3. $y_Q - 5 = -3 \Rightarrow y_Q = 2$.
4. $Q = (3, 2)$.
""")

    with st.expander("❓ Cuestionario V01: Vectores en el Plano", expanded=False):
        st.markdown(r"""
**1. Si $A(3, 1)$ y $B(7, 4)$, ¿cuál es el vector $\vec{AB}$?**

A) $(10, 5)$
B) $(4, 3)$
C) $(-4, -3)$
D) $(3, 4)$

---

**2. ¿Cuál es el módulo del vector $\vec{v} = (5, -12)$?**

A) $7$
B) $13$
C) $17$
D) $\sqrt{119}$

---

**3. El vector nulo se define como:**

A) Un vector de módulo $1$
B) Un vector que solo tiene componente horizontal
C) $(0, 0)$, con módulo $0$ y dirección indefinida
D) Cualquier vector con una componente negativa

---

**4. ¿Cuál es el vector unitario en la dirección de $\vec{w} = (0, 5)$?**

A) $(0, 5)$
B) $(1, 0)$
C) $(0, 1)$
D) $(5, 0)$

---

**5. Dos vectores son iguales si y solo si:**

A) Tienen el mismo módulo
B) Tienen la misma dirección
C) Tienen las mismas componentes
D) Parten del mismo punto

---

**6. Si $\vec{v} = (a, -2)$ y $\|\vec{v}\| = \sqrt{13}$, ¿cuánto vale $a$ si $a > 0$?**

A) $1$
B) $3$
C) $9$
D) $\sqrt{9}$

---

**7. El vector opuesto de $\vec{u} = (-3, 7)$ es:**

A) $(3, 7)$
B) $(-3, -7)$
C) $(3, -7)$
D) $(7, -3)$
""")

    with st.expander("🔑 Pauta Técnica V01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $\vec{AB} = (7-3,\; 4-1) = (4, 3)$. |
| **2** | **B** | $\|\vec{v}\| = \sqrt{25 + 144} = \sqrt{169} = 13$. |
| **3** | **C** | El vector nulo es $(0,0)$ con módulo cero y sin dirección definida. |
| **4** | **C** | $\hat{w} = \frac{(0,5)}{5} = (0, 1)$. |
| **5** | **C** | Vectores iguales $\Leftrightarrow$ mismas componentes. El módulo igual no basta. |
| **6** | **B** | $\sqrt{a^2 + 4} = \sqrt{13} \Rightarrow a^2 = 9 \Rightarrow a = 3$ (pues $a > 0$). |
| **7** | **C** | $-\vec{u} = -(- 3, 7) = (3, -7)$. Se cambia el signo de cada componente. |
""")
