import streamlit as st


def render_V05():
    st.title("V05: Aplicaciones de Vectores en Geometría Analítica — Vectores en Acción")

    st.markdown(r"""
### 🛡️ 1. Punto Medio con Vectores

El **punto medio** $M$ del segmento $\overline{AB}$, con $A(x_1, y_1)$ y $B(x_2, y_2)$, se obtiene como:

$$M = \frac{1}{2}(\vec{OA} + \vec{OB}) = \left(\frac{x_1 + x_2}{2},\; \frac{y_1 + y_2}{2}\right)$$

Vectorialmente, $\vec{OM} = \frac{1}{2}(\vec{OA} + \vec{OB})$, es decir, el promedio de los vectores posición.

---

### 🛡️ 2. Distancia de un Punto a una Recta

La distancia desde un punto $P(x_0, y_0)$ a la recta $ax + by + c = 0$ se calcula con:

$$d(P, \ell) = \frac{|ax_0 + by_0 + c|}{\sqrt{a^2 + b^2}}$$

Esta fórmula utiliza el vector normal $\vec{n} = (a, b)$ de la recta: la distancia es la magnitud de la proyección del vector $\vec{P_0 P}$ sobre $\vec{n}$.

> **Tip PAES:** No olvides el **valor absoluto** en el numerador y la **raíz** en el denominador.

---

### 🛡️ 3. Baricentro (Centroide) de un Triángulo

El **baricentro** $G$ de un triángulo con vértices $A(x_1, y_1)$, $B(x_2, y_2)$ y $C(x_3, y_3)$ es el punto donde se cortan las tres medianas:

$$G = \left(\frac{x_1 + x_2 + x_3}{3},\; \frac{y_1 + y_2 + y_3}{3}\right)$$

Vectorialmente:

$$\vec{OG} = \frac{1}{3}(\vec{OA} + \vec{OB} + \vec{OC})$$

> **Propiedad:** El baricentro divide cada mediana en razón $2:1$ desde el vértice.

---

### 🛡️ 4. Traslaciones Vectoriales

Una **traslación** desplaza todos los puntos de una figura según un vector $\vec{t} = (a, b)$:

$$P'(x', y') = P(x, y) + \vec{t} = (x + a,\; y + b)$$

| Propiedad de la traslación | Descripción |
| :--- | :--- |
| Conserva distancias | $d(P', Q') = d(P, Q)$ |
| Conserva ángulos | Los ángulos no cambian |
| Conserva el paralelismo | Lados paralelos siguen paralelos |
| Es una isometría | No deforma la figura |

---

### 🛡️ 5. Aplicaciones en Navegación y Física

Los vectores se usan para modelar situaciones reales:

| Situación | Modelo vectorial |
| :--- | :--- |
| Velocidad del viento | Vector con magnitud (km/h) y dirección |
| Fuerza resultante | Suma de vectores de fuerza |
| Desplazamiento | Vector desde posición inicial a final |
| Corriente marina | Suma con el vector de velocidad del barco |

La **velocidad resultante** de un barco que navega con velocidad $\vec{v}_b$ en una corriente $\vec{v}_c$ es:

$$\vec{v}_R = \vec{v}_b + \vec{v}_c$$

---

### 🛡️ 6. Resumen de Fórmulas Clave

| Concepto | Fórmula |
| :--- | :--- |
| Punto medio | $M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$ |
| Distancia punto-recta | $d = \frac{\|ax_0 + by_0 + c\|}{\sqrt{a^2+b^2}}$ |
| Baricentro | $G = \left(\frac{x_1+x_2+x_3}{3}, \frac{y_1+y_2+y_3}{3}\right)$ |
| Traslación | $P' = P + \vec{t}$ |

---

> *"El universo no puede ser leído hasta que hayamos aprendido el lenguaje en el que está escrito. Está escrito en lenguaje matemático, y las letras son triángulos, círculos y otras figuras geométricas."*
> — **Galileo Galilei**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería V05", expanded=False):
        st.markdown(r"""
### E01: Punto medio de un segmento

**Situación:** Encuentra el punto medio de $A(2, 8)$ y $B(6, -4)$.

**La Carpintería:**
1. $M = \left(\frac{2+6}{2},\; \frac{8+(-4)}{2}\right) = \left(\frac{8}{2},\; \frac{4}{2}\right) = (4, 2)$.

| Coordenada | Cálculo | Resultado |
| :--- | :--- | :---: |
| $x_M$ | $\frac{2+6}{2}$ | $4$ |
| $y_M$ | $\frac{8+(-4)}{2}$ | $2$ |
| **Punto medio** | | **(4, 2)** |

---

### E02: Distancia de un punto a una recta

**Situación:** ¿Cuál es la distancia del punto $P(1, 3)$ a la recta $3x - 4y + 5 = 0$?

**La Carpintería:**
1. $a = 3$, $b = -4$, $c = 5$, $(x_0, y_0) = (1, 3)$.
2. Numerador: $|3(1) + (-4)(3) + 5| = |3 - 12 + 5| = |-4| = 4$.
3. Denominador: $\sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = 5$.
4. $d = \frac{4}{5} = 0{,}8$ unidades.

---

### E03: Baricentro de un triángulo

**Situación:** Encuentra el baricentro del triángulo con vértices $A(0, 0)$, $B(6, 0)$ y $C(3, 9)$.

**La Carpintería:**
1. $G = \left(\frac{0+6+3}{3},\; \frac{0+0+9}{3}\right) = \left(\frac{9}{3},\; \frac{9}{3}\right) = (3, 3)$.

---

### E04: Traslación de un triángulo

**Situación:** Un triángulo tiene vértices $A(1, 2)$, $B(4, 2)$ y $C(1, 5)$. Se aplica la traslación $\vec{t} = (3, -1)$. ¿Cuáles son los nuevos vértices?

**La Carpintería:**
1. $A' = (1+3,\; 2+(-1)) = (4, 1)$.
2. $B' = (4+3,\; 2+(-1)) = (7, 1)$.
3. $C' = (1+3,\; 5+(-1)) = (4, 4)$.

| Vértice original | $+ \vec{t} = (3, -1)$ | Vértice trasladado |
| :--- | :---: | :--- |
| $A(1, 2)$ | → | $A'(4, 1)$ |
| $B(4, 2)$ | → | $B'(7, 1)$ |
| $C(1, 5)$ | → | $C'(4, 4)$ |

---

### E05: Velocidad resultante (navegación)

**Situación:** Un barco navega hacia el este a $15$ km/h ($\vec{v}_b = (15, 0)$) y la corriente marina empuja hacia el norte a $8$ km/h ($\vec{v}_c = (0, 8)$). ¿Cuál es la velocidad resultante?

**La Carpintería:**
1. $\vec{v}_R = \vec{v}_b + \vec{v}_c = (15, 0) + (0, 8) = (15, 8)$.
2. Rapidez: $\|\vec{v}_R\| = \sqrt{225 + 64} = \sqrt{289} = 17$ km/h.
3. El barco se mueve a **17 km/h** en una dirección entre el este y el norte.
""")

    with st.expander("❓ Cuestionario V05: Aplicaciones de Vectores", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el punto medio de $A(-2, 6)$ y $B(4, 2)$?**

A) $(2, 8)$
B) $(1, 4)$
C) $(3, 4)$
D) $(6, 8)$

---

**2. La distancia del punto $P(0, 0)$ a la recta $3x + 4y - 10 = 0$ es:**

A) $1$
B) $2$
C) $5$
D) $10$

---

**3. El baricentro de un triángulo con vértices $(0, 0)$, $(6, 0)$ y $(0, 6)$ es:**

A) $(3, 3)$
B) $(2, 2)$
C) $(6, 6)$
D) $(1, 1)$

---

**4. Si se aplica la traslación $\vec{t} = (-2, 5)$ al punto $P(3, 1)$, ¿cuál es la imagen $P'$?**

A) $(5, -4)$
B) $(1, 6)$
C) $(-2, 5)$
D) $(5, 6)$

---

**5. Un avión vuela con velocidad $\vec{v}_a = (200, 0)$ km/h y un viento sopla con $\vec{v}_v = (0, -50)$ km/h. ¿Cuál es la rapidez resultante?**

A) $150$ km/h
B) $\sqrt{42\,500}$ km/h
C) $250$ km/h
D) $50\sqrt{17}$ km/h

---

**6. ¿Cuál propiedad NO conserva una traslación?**

A) Distancias
B) Ángulos
C) Posición
D) Paralelismo

---

**7. El baricentro divide cada mediana en razón:**

A) $1:1$ desde el vértice
B) $1:2$ desde el vértice
C) $2:1$ desde el vértice
D) $3:1$ desde el vértice
""")

    with st.expander("🔑 Pauta Técnica V05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $M = \left(\frac{-2+4}{2}, \frac{6+2}{2}\right) = (1, 4)$. |
| **2** | **B** | $d = \frac{|0+0-10|}{\sqrt{9+16}} = \frac{10}{5} = 2$. |
| **3** | **B** | $G = \left(\frac{0+6+0}{3}, \frac{0+0+6}{3}\right) = (2, 2)$. |
| **4** | **B** | $P' = (3+(-2), 1+5) = (1, 6)$. |
| **5** | **D** | $\|\vec{v}_R\| = \sqrt{200^2 + 50^2} = \sqrt{42\,500} = 50\sqrt{17} \approx 206{,}2$ km/h. B y D son equivalentes. |
| **6** | **C** | La traslación cambia la posición de los puntos, pero conserva distancias, ángulos y paralelismo. |
| **7** | **C** | El baricentro está a $\frac{2}{3}$ del vértice y a $\frac{1}{3}$ del punto medio del lado opuesto, razón $2:1$. |
""")
