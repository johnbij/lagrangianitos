import streamlit as st


def render_P04():
    st.title("P04: Cuerpos Geométricos y Volumen — La Tercera Dimensión")

    st.markdown(r"""
### 🛡️ 1. ¿Qué es el Volumen?

El **volumen** de un cuerpo geométrico es la **cantidad de espacio tridimensional** que ocupa. Se mide en **unidades cúbicas**: $\text{cm}^3$, $\text{m}^3$, litros (L), etc.

| Equivalencia | Valor |
| :--- | :--- |
| $1 \text{ L}$ | $1\,000 \text{ cm}^3 = 1 \text{ dm}^3$ |
| $1 \text{ m}^3$ | $1\,000 \text{ L}$ |
| $1 \text{ mL}$ | $1 \text{ cm}^3$ |

---

### 🛡️ 2. Prismas

Un **prisma** es un cuerpo con dos bases paralelas e iguales (polígonos) unidas por caras laterales rectangulares.

$$V_{\text{prisma}} = A_{\text{base}} \cdot h$$

| Prisma | Base | Fórmula del volumen |
| :--- | :--- | :--- |
| Cubo | Cuadrado ($\ell^2$) | $V = \ell^3$ |
| Paralelepípedo | Rectángulo ($a \cdot b$) | $V = a \cdot b \cdot c$ |
| Prisma triangular | Triángulo ($\frac{b \cdot h_b}{2}$) | $V = \frac{b \cdot h_b}{2} \cdot H$ |
| Prisma hexagonal | Hexágono regular | $V = \frac{3\sqrt{3}}{2}\ell^2 \cdot H$ |

---

### 🛡️ 3. Pirámides

Una **pirámide** tiene una base poligonal y caras laterales triangulares que convergen en un vértice (ápice).

$$V_{\text{pirámide}} = \frac{1}{3} \cdot A_{\text{base}} \cdot h$$

> **Tip PAES:** El volumen de una pirámide es exactamente **un tercio** del prisma con la misma base y altura.

---

### 🛡️ 4. Cilindro

Un **cilindro** tiene dos bases circulares paralelas de radio $r$ y una altura $h$:

$$V_{\text{cilindro}} = \pi r^2 \cdot h$$

---

### 🛡️ 5. Cono

Un **cono** tiene una base circular de radio $r$ y un vértice a una altura $h$:

$$V_{\text{cono}} = \frac{1}{3} \pi r^2 \cdot h$$

> **Tip PAES:** El cono es a la pirámide lo que el cilindro es al prisma. El cono es **un tercio** del cilindro con la misma base y altura.

---

### 🛡️ 6. Esfera

La **esfera** es el conjunto de todos los puntos del espacio que equidistan de un centro:

$$V_{\text{esfera}} = \frac{4}{3} \pi r^3$$

---

### 🛡️ 7. Relación entre Cuerpos

| Relación | Proporción |
| :--- | :--- |
| Pirámide vs. Prisma (misma base y altura) | $V_{\text{pirámide}} = \frac{1}{3} V_{\text{prisma}}$ |
| Cono vs. Cilindro (misma base y altura) | $V_{\text{cono}} = \frac{1}{3} V_{\text{cilindro}}$ |
| Semiesfera vs. Cilindro ($r = h$) | $V_{\text{semiesfera}} = \frac{2}{3} V_{\text{cilindro}}$ |

---

### 🛡️ 8. Resumen de Fórmulas de Volumen

| Cuerpo | Fórmula |
| :--- | :--- |
| Cubo | $V = \ell^3$ |
| Paralelepípedo | $V = a \cdot b \cdot c$ |
| Prisma general | $V = A_{\text{base}} \cdot h$ |
| Pirámide | $V = \frac{1}{3} A_{\text{base}} \cdot h$ |
| Cilindro | $V = \pi r^2 h$ |
| Cono | $V = \frac{1}{3} \pi r^2 h$ |
| Esfera | $V = \frac{4}{3} \pi r^3$ |

---

> *"Dadme un punto de apoyo y moveré el mundo."*
> — **Arquímedes**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería P04", expanded=False):
        st.markdown(r"""
### E01: Volumen de un cilindro (estanque de agua)

**Situación:** Un estanque cilíndrico tiene radio $1{,}5$ m y altura $2$ m. ¿Cuántos litros de agua puede almacenar?

**La Carpintería:**
1. $V = \pi r^2 h = \pi (1{,}5)^2 (2) = \pi (2{,}25)(2) = 4{,}5\pi \approx 14{,}14 \text{ m}^3$.
2. Como $1 \text{ m}^3 = 1\,000$ L: $V \approx 14\,140$ L.

| Dato | Valor |
| :--- | :---: |
| Radio | $1{,}5$ m |
| Altura | $2$ m |
| Volumen | $4{,}5\pi \approx 14{,}14$ m³ |
| **Capacidad** | **$\approx 14\,140$ L** |

---

### E02: Volumen de una pirámide cuadrada

**Situación:** Una pirámide tiene base cuadrada de lado $6$ cm y altura $10$ cm.

**La Carpintería:**
1. $A_{\text{base}} = 6^2 = 36 \text{ cm}^2$.
2. $V = \frac{1}{3} \cdot 36 \cdot 10 = \frac{360}{3} = 120 \text{ cm}^3$.

---

### E03: Volumen de una esfera (balón)

**Situación:** Un balón de fútbol tiene un diámetro de $22$ cm. ¿Cuál es su volumen?

**La Carpintería:**
1. $r = \frac{22}{2} = 11$ cm.
2. $V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi (11)^3 = \frac{4}{3}\pi (1\,331) = \frac{5\,324}{3}\pi \approx 5\,575{,}3 \text{ cm}^3$.

---

### E04: Problema de capacidad

**Situación:** Un cono tiene radio $3$ cm y altura $12$ cm. ¿Cuántos conos de agua se necesitan para llenar un cilindro de radio $3$ cm y altura $12$ cm?

**La Carpintería:**
1. $V_{\text{cilindro}} = \pi(3)^2(12) = 108\pi$ cm³.
2. $V_{\text{cono}} = \frac{1}{3}\pi(3)^2(12) = 36\pi$ cm³.
3. Razón: $\frac{108\pi}{36\pi} = 3$.
4. Se necesitan exactamente **3 conos** para llenar el cilindro.
""")

    with st.expander("❓ Cuestionario P04: Cuerpos Geométricos y Volumen", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el volumen de un cubo de arista $5$ cm?**

A) $15$ cm³
B) $25$ cm³
C) $125$ cm³
D) $150$ cm³

---

**2. Un cilindro tiene radio $4$ cm y altura $10$ cm. ¿Cuál es su volumen?**

A) $40\pi$ cm³
B) $80\pi$ cm³
C) $160\pi$ cm³
D) $640\pi$ cm³

---

**3. ¿Cuántos litros caben en un recipiente de $2\,000$ cm³?**

A) $0{,}2$ L
B) $2$ L
C) $20$ L
D) $200$ L

---

**4. Una pirámide de base cuadrada tiene arista base $10$ cm y altura $9$ cm. ¿Cuál es su volumen?**

A) $90$ cm³
B) $300$ cm³
C) $450$ cm³
D) $900$ cm³

---

**5. El volumen de una esfera de radio $3$ cm es:**

A) $12\pi$ cm³
B) $36\pi$ cm³
C) $\frac{108\pi}{3}$ cm³
D) B y C son equivalentes

---

**6. Si se duplica el radio de un cilindro manteniendo la altura, el volumen:**

A) Se duplica
B) Se triplica
C) Se cuadruplica
D) Se multiplica por $8$

---

**7. Un cono y un cilindro tienen la misma base y la misma altura. ¿Cuál es la razón $\frac{V_{\text{cono}}}{V_{\text{cilindro}}}$?**

A) $\frac{1}{4}$
B) $\frac{1}{3}$
C) $\frac{1}{2}$
D) $\frac{2}{3}$
""")
