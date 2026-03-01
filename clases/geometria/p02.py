import streamlit as st


def render_P02():
    st.title("P02: Área de Figuras Planas — Midiendo la Superficie")

    st.markdown(r"""
### 🛡️ 1. ¿Qué es el Área?

El **área** de una figura plana es la **medida de la superficie** que encierra su contorno. Mientras el perímetro mide el borde, el área mide el espacio interior.

Se expresa en **unidades cuadradas**: $\text{cm}^2$, $\text{m}^2$, $\text{km}^2$, hectáreas (ha), etc.

| Equivalencia | Valor |
| :--- | :--- |
| $1 \text{ m}^2$ | $10\,000 \text{ cm}^2$ |
| $1 \text{ km}^2$ | $1\,000\,000 \text{ m}^2$ |
| $1 \text{ ha}$ | $10\,000 \text{ m}^2$ |

---

### 🛡️ 2. Área del Rectángulo y del Cuadrado

$$A_{\text{rectángulo}} = b \cdot h$$

donde $b$ es la base y $h$ la altura.

Para el **cuadrado** ($b = h = \ell$):

$$A_{\text{cuadrado}} = \ell^2$$

---

### 🛡️ 3. Área del Triángulo

$$A_{\triangle} = \frac{b \cdot h}{2}$$

donde $b$ es cualquier lado tomado como base y $h$ es la **altura** perpendicular trazada desde el vértice opuesto a esa base.

> **Tip PAES:** La altura no siempre está dentro del triángulo (en triángulos obtusángulos se prolonga la base).

---

### 🛡️ 4. Área del Paralelogramo, Trapecio y Rombo

| Figura | Fórmula | Variables |
| :--- | :--- | :--- |
| **Paralelogramo** | $A = b \cdot h$ | $b$ = base, $h$ = altura perpendicular |
| **Trapecio** | $A = \dfrac{(B + b) \cdot h}{2}$ | $B$ = base mayor, $b$ = base menor, $h$ = altura |
| **Rombo** | $A = \dfrac{D \cdot d}{2}$ | $D$ = diagonal mayor, $d$ = diagonal menor |

---

### 🛡️ 5. Área del Círculo y Sector Circular

$$A_{\text{círculo}} = \pi r^2$$

Para un **sector circular** de ángulo central $\theta$ (en grados):

$$A_{\text{sector}} = \frac{\theta}{360°} \cdot \pi r^2$$

---

### 🛡️ 6. Área de Figuras Compuestas

Muchos problemas PAES presentan figuras irregulares que se pueden descomponer en figuras simples.

**Estrategia:**
1. **Descomponer** la figura en rectángulos, triángulos, semicírculos, etc.
2. **Calcular** el área de cada parte.
3. **Sumar** (si se agregan partes) o **restar** (si se quitan partes, como un agujero).

---

### 🛡️ 7. Resumen de Fórmulas de Área

| Figura | Fórmula |
| :--- | :--- |
| Rectángulo | $A = b \cdot h$ |
| Cuadrado | $A = \ell^2$ |
| Triángulo | $A = \frac{b \cdot h}{2}$ |
| Paralelogramo | $A = b \cdot h$ |
| Trapecio | $A = \frac{(B+b) \cdot h}{2}$ |
| Rombo | $A = \frac{D \cdot d}{2}$ |
| Círculo | $A = \pi r^2$ |
| Sector circular | $A = \frac{\theta}{360°} \cdot \pi r^2$ |

---

> *"La naturaleza es un libro escrito en lenguaje matemático, y los caracteres son triángulos, círculos y otras figuras geométricas."*
> — **Galileo Galilei**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería P02", expanded=False):
        st.markdown(r"""
### E01: Área de un terreno triangular

**Situación:** Un terreno triangular tiene una base de $80$ m y una altura de $35$ m. ¿Cuál es su área?

**La Carpintería:**
1. **Identificar:** Triángulo con $b = 80$ m, $h = 35$ m.
2. **Fórmula:** $A = \frac{b \cdot h}{2} = \frac{80 \cdot 35}{2} = \frac{2\,800}{2} = 1\,400 \text{ m}^2$.

| Dato | Valor |
| :--- | :---: |
| Base | $80$ m |
| Altura | $35$ m |
| **Área** | **$1\,400 \text{ m}^2$** |

---

### E02: Área de un trapecio

**Situación:** Un trapecio tiene bases de $12$ cm y $8$ cm, y una altura de $5$ cm.

**La Carpintería:**
1. $A = \frac{(B + b) \cdot h}{2} = \frac{(12 + 8) \cdot 5}{2} = \frac{20 \cdot 5}{2} = \frac{100}{2} = 50 \text{ cm}^2$.

---

### E03: Área de una corona circular

**Situación:** Un anillo tiene un radio exterior de $10$ cm y un radio interior de $6$ cm. Calcula el área de la corona circular.

**La Carpintería:**
1. Área del círculo grande: $A_1 = \pi (10)^2 = 100\pi$.
2. Área del círculo pequeño: $A_2 = \pi (6)^2 = 36\pi$.
3. Área de la corona: $A = A_1 - A_2 = 100\pi - 36\pi = 64\pi \approx 201{,}06 \text{ cm}^2$.

| Componente | Área |
| :--- | :---: |
| Círculo mayor | $100\pi$ cm² |
| Círculo menor | $36\pi$ cm² |
| **Corona** | **$64\pi \approx 201{,}06$ cm²** |

---

### E04: Área de una figura compuesta

**Situación:** Una piscina tiene forma rectangular de $10$ m × $5$ m con un semicírculo en uno de sus lados menores. ¿Cuál es el área total?

**La Carpintería:**
1. Área del rectángulo: $A_1 = 10 \cdot 5 = 50 \text{ m}^2$.
2. El semicírculo tiene diámetro $5$ m, así que $r = 2{,}5$ m.
3. Área del semicírculo: $A_2 = \frac{\pi r^2}{2} = \frac{\pi (2{,}5)^2}{2} = \frac{6{,}25\pi}{2} \approx 9{,}82 \text{ m}^2$.
4. Área total: $A = 50 + 9{,}82 = 59{,}82 \text{ m}^2$.
""")

    with st.expander("❓ Cuestionario P02: Área de Figuras Planas", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el área de un rectángulo de $15$ cm de largo y $8$ cm de ancho?**

A) $46$ cm²
B) $60$ cm²
C) $120$ cm²
D) $240$ cm²

---

**2. Un triángulo tiene base $10$ cm y altura $7$ cm. ¿Cuál es su área?**

A) $17$ cm²
B) $35$ cm²
C) $70$ cm²
D) $140$ cm²

---

**3. ¿Cuál es el área de un círculo de radio $6$ cm?**

A) $6\pi$ cm²
B) $12\pi$ cm²
C) $36\pi$ cm²
D) $72\pi$ cm²

---

**4. Un rombo tiene diagonales de $10$ cm y $14$ cm. ¿Cuál es su área?**

A) $24$ cm²
B) $35$ cm²
C) $70$ cm²
D) $140$ cm²

---

**5. Un trapecio tiene bases de $6$ cm y $10$ cm, y una altura de $4$ cm. ¿Cuál es su área?**

A) $20$ cm²
B) $32$ cm²
C) $40$ cm²
D) $60$ cm²

---

**6. ¿Cuántos metros cuadrados tiene un terreno de $0{,}5$ hectáreas?**

A) $50$ m²
B) $500$ m²
C) $5\,000$ m²
D) $50\,000$ m²

---

**7. Un sector circular tiene radio $8$ cm y ángulo central de $45°$. ¿Cuál es su área?**

A) $4\pi$ cm²
B) $8\pi$ cm²
C) $16\pi$ cm²
D) $32\pi$ cm²
""")

    with st.expander("🔑 Pauta Técnica P02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $A = 15 \cdot 8 = 120$ cm². |
| **2** | **B** | $A = \frac{10 \cdot 7}{2} = 35$ cm². |
| **3** | **C** | $A = \pi r^2 = \pi (6)^2 = 36\pi$ cm². |
| **4** | **C** | $A = \frac{D \cdot d}{2} = \frac{10 \cdot 14}{2} = 70$ cm². |
| **5** | **B** | $A = \frac{(6+10) \cdot 4}{2} = \frac{16 \cdot 4}{2} = 32$ cm². |
| **6** | **C** | $1 \text{ ha} = 10\,000 \text{ m}^2$, así que $0{,}5 \text{ ha} = 5\,000 \text{ m}^2$. |
| **7** | **B** | $A = \frac{45}{360} \cdot \pi (8)^2 = \frac{1}{8} \cdot 64\pi = 8\pi$ cm². |
""")
