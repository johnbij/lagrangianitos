import streamlit as st


def render_P05():
    st.title("P05: Área de Superficies de Cuerpos Geométricos — Envolviendo el Espacio")

    st.markdown(r"""
### 🛡️ 1. ¿Qué es el Área de Superficie?

El **área de superficie** de un cuerpo geométrico es la medida total de la superficie que lo envuelve. Es la cantidad de material necesario para "forrar" el cuerpo, como el papel de regalo que cubre una caja.

Se distingue entre:
- **Área lateral** ($A_L$): superficie de las caras laterales.
- **Área total** ($A_T$): área lateral + área de las bases.

---

### 🛡️ 2. Desarrollo Plano (Red)

El **desarrollo plano** de un cuerpo es la figura plana que se obtiene al "desplegar" todas sus caras. Permite visualizar y calcular el área total como una suma de áreas planas conocidas.

| Cuerpo | Desarrollo plano |
| :--- | :--- |
| Cubo | 6 cuadrados iguales |
| Cilindro | 2 círculos + 1 rectángulo |
| Cono | 1 círculo + 1 sector circular |
| Pirámide cuadrada | 1 cuadrado + 4 triángulos |

---

### 🛡️ 3. Prismas

Para un **prisma recto** de perímetro de base $P_b$ y altura $h$:

$$A_L = P_b \cdot h$$
$$A_T = A_L + 2 \cdot A_{\text{base}}$$

| Prisma | $A_L$ | $A_T$ |
| :--- | :--- | :--- |
| Cubo (arista $\ell$) | $4\ell^2$ | $6\ell^2$ |
| Paralelepípedo ($a, b, c$) | $2c(a+b)$ | $2(ab + ac + bc)$ |

---

### 🛡️ 4. Cilindro

Al desplegar un cilindro, la cara lateral se convierte en un rectángulo de base $2\pi r$ y altura $h$:

$$A_L = 2\pi r h$$
$$A_T = 2\pi r h + 2\pi r^2 = 2\pi r(h + r)$$

---

### 🛡️ 5. Cono

El desarrollo lateral del cono es un **sector circular** de radio $g$ (generatriz) y arco $2\pi r$:

$$A_L = \pi r g$$
$$A_T = \pi r g + \pi r^2 = \pi r(g + r)$$

donde la **generatriz** se calcula con Pitágoras: $g = \sqrt{r^2 + h^2}$.

---

### 🛡️ 6. Pirámides

Para una **pirámide regular** de perímetro de base $P_b$ y apotema lateral $a_p$ (altura de las caras triangulares):

$$A_L = \frac{P_b \cdot a_p}{2}$$
$$A_T = A_L + A_{\text{base}}$$

---

### 🛡️ 7. Esfera

La esfera no tiene caras planas ni desarrollo plano. Su área superficial es:

$$A_{\text{esfera}} = 4\pi r^2$$

> **Dato notable:** El área de la esfera es exactamente **4 veces** el área de su círculo máximo ($\pi r^2$).

---

### 🛡️ 8. Resumen de Fórmulas

| Cuerpo | Área lateral | Área total |
| :--- | :--- | :--- |
| Cubo | $4\ell^2$ | $6\ell^2$ |
| Prisma recto | $P_b \cdot h$ | $P_b \cdot h + 2A_b$ |
| Cilindro | $2\pi r h$ | $2\pi r(h + r)$ |
| Cono | $\pi r g$ | $\pi r(g + r)$ |
| Pirámide regular | $\frac{P_b \cdot a_p}{2}$ | $\frac{P_b \cdot a_p}{2} + A_b$ |
| Esfera | — | $4\pi r^2$ |

---

> *"En la geometría no hay caminos exclusivos para los reyes."*
> — **Euclides**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería P05", expanded=False):
        st.markdown(r"""
### E01: Pintar un estanque cilíndrico

**Situación:** Se quiere pintar la superficie lateral de un estanque cilíndrico de radio $2$ m y altura $3$ m. ¿Cuántos m² de pintura se necesitan?

**La Carpintería:**
1. Solo la cara lateral (sin tapas): $A_L = 2\pi r h$.
2. $A_L = 2\pi(2)(3) = 12\pi \approx 37{,}7 \text{ m}^2$.

| Dato | Valor |
| :--- | :---: |
| Radio | $2$ m |
| Altura | $3$ m |
| **Área lateral** | **$12\pi \approx 37{,}7$ m²** |

---

### E02: Forrar una caja (paralelepípedo)

**Situación:** Una caja tiene dimensiones $30$ cm × $20$ cm × $15$ cm. ¿Cuánto cartón se necesita para fabricarla?

**La Carpintería:**
1. $A_T = 2(ab + ac + bc)$ con $a=30$, $b=20$, $c=15$.
2. $A_T = 2(600 + 450 + 300) = 2(1\,350) = 2\,700 \text{ cm}^2$.

---

### E03: Área total de un cono

**Situación:** Un cono tiene radio $5$ cm y altura $12$ cm. Calcula su área total.

**La Carpintería:**
1. **Generatriz:** $g = \sqrt{r^2 + h^2} = \sqrt{25 + 144} = \sqrt{169} = 13$ cm.
2. **Área lateral:** $A_L = \pi r g = \pi(5)(13) = 65\pi$ cm².
3. **Área de la base:** $A_b = \pi r^2 = 25\pi$ cm².
4. **Área total:** $A_T = 65\pi + 25\pi = 90\pi \approx 282{,}7$ cm².

| Componente | Valor |
| :--- | :---: |
| Generatriz | $13$ cm |
| Área lateral | $65\pi$ cm² |
| Área base | $25\pi$ cm² |
| **Área total** | **$90\pi \approx 282{,}7$ cm²** |

---

### E04: Área superficial de una pelota

**Situación:** Un balón de básquetbol tiene un diámetro de $24$ cm. ¿Cuál es su área superficial?

**La Carpintería:**
1. $r = \frac{24}{2} = 12$ cm.
2. $A = 4\pi r^2 = 4\pi(12)^2 = 4\pi(144) = 576\pi \approx 1\,809{,}6$ cm².
""")

    with st.expander("❓ Cuestionario P05: Área de Superficies", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el área total de un cubo de arista $4$ cm?**

A) $16$ cm²
B) $64$ cm²
C) $96$ cm²
D) $256$ cm²

---

**2. El área lateral de un cilindro de radio $3$ cm y altura $7$ cm es:**

A) $21\pi$ cm²
B) $42\pi$ cm²
C) $63\pi$ cm²
D) $84\pi$ cm²

---

**3. Un cono tiene radio $6$ cm y generatriz $10$ cm. ¿Cuál es su área lateral?**

A) $30\pi$ cm²
B) $36\pi$ cm²
C) $60\pi$ cm²
D) $96\pi$ cm²

---

**4. El área superficial de una esfera de radio $5$ cm es:**

A) $20\pi$ cm²
B) $25\pi$ cm²
C) $100\pi$ cm²
D) $500\pi$ cm²

---

**5. Se quiere forrar una caja de $10$ cm × $8$ cm × $6$ cm. ¿Cuánto material se necesita?**

A) $188$ cm²
B) $296$ cm²
C) $376$ cm²
D) $480$ cm²

---

**6. Si se duplica el radio de una esfera, su área superficial:**

A) Se duplica
B) Se triplica
C) Se cuadruplica
D) Se multiplica por $8$

---

**7. ¿Cuál es el área total de un cilindro de radio $5$ cm y altura $10$ cm?**

A) $100\pi$ cm²
B) $150\pi$ cm²
C) $250\pi$ cm²
D) $300\pi$ cm²
""")
