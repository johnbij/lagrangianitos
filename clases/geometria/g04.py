import streamlit as st


def render_G04():
    st.title("G04: La Circunferencia y el Círculo — La Geometría del Movimiento")

    st.markdown(r"""
### 🛡️ 1. El Portal: La Curva Perfecta

La circunferencia es la curva más perfecta de la naturaleza: todos sus puntos están a la **misma distancia** de un punto central. Desde la rueda hasta las órbitas planetarias, esta figura describe todo lo que gira.

- **Circunferencia:** Es el conjunto de puntos del plano que equidistan de un punto fijo llamado **centro**. Es una **línea curva cerrada**.
- **Círculo:** Es la **región interior** delimitada por la circunferencia. Es una **superficie**.

---

### 🛡️ 1.1 Elementos de la Circunferencia

| Elemento | Definición |
| :--- | :--- |
| **Centro** ($O$) | Punto interior equidistante de todos los puntos de la circunferencia |
| **Radio** ($r$) | Segmento desde el centro a cualquier punto de la circunferencia |
| **Diámetro** ($d$) | Segmento que une dos puntos de la circunferencia pasando por el centro; $d = 2r$ |
| **Cuerda** | Segmento que une dos puntos de la circunferencia (el diámetro es la cuerda mayor) |
| **Arco** | Porción de la circunferencia comprendida entre dos puntos |
| **Sector circular** | Región del círculo limitada por dos radios y el arco que los une (como una "rebanada de pizza") |
| **Segmento circular** | Región del círculo limitada por una cuerda y el arco correspondiente |

---

### 🏛️ 1.2 Ángulo Central y Ángulo Inscrito

El **ángulo central** tiene su vértice en el centro de la circunferencia y sus lados son radios. Su medida es igual a la del arco que abarca.

El **ángulo inscrito** tiene su vértice **sobre** la circunferencia y sus lados son cuerdas.

**Teorema del ángulo inscrito:**

$$\text{Ángulo inscrito} = \frac{\text{Ángulo central}}{2}$$

Equivalentemente, si ambos subtienden el mismo arco:

$$\alpha_{inscrito} = \frac{\alpha_{central}}{2}$$

> **Consecuencia fundamental:** Todo ángulo inscrito en una semicircunferencia (que subtiende un diámetro) es un **ángulo recto** ($90°$). Este es el **Teorema de Tales**.

---

### 🛡️ 1.3 Rectas y Circunferencia: Posiciones Relativas

| Posición | Descripción | Puntos en común | Relación con $r$ |
| :--- | :--- | :---: | :--- |
| **Secante** | La recta corta la circunferencia | $2$ | $d(O, \ell) < r$ |
| **Tangente** | La recta toca la circunferencia en un solo punto | $1$ | $d(O, \ell) = r$ |
| **Exterior** | La recta no toca la circunferencia | $0$ | $d(O, \ell) > r$ |

**Propiedad de la tangente:** La recta tangente es siempre **perpendicular** al radio en el punto de tangencia.

---

### 🛡️ 1.4 Longitud de la Circunferencia y Área del Círculo

Las fórmulas más importantes de este tema:

| Fórmula | Expresión |
| :--- | :--- |
| **Longitud de la circunferencia** | $L = 2\pi r = \pi d$ |
| **Área del círculo** | $A = \pi r^2$ |
| **Longitud de un arco** (ángulo central $\theta$ en grados) | $\ell = \dfrac{\theta}{360°} \cdot 2\pi r$ |
| **Área de un sector circular** (ángulo central $\theta$ en grados) | $A_s = \dfrac{\theta}{360°} \cdot \pi r^2$ |

> **Tip PAES:** Memoriza que $\pi \approx 3{,}14$. En muchas preguntas, la respuesta queda expresada "en términos de $\pi$" (por ejemplo, $12\pi$ cm²).

---

### 🛡️ 1.5 Posiciones Relativas entre Dos Circunferencias

| Posición | Condición (si $d$ es distancia entre centros) |
| :--- | :--- |
| **Exteriores** | $d > r_1 + r_2$ |
| **Tangentes exteriormente** | $d = r_1 + r_2$ |
| **Secantes** | $|r_1 - r_2| < d < r_1 + r_2$ |
| **Tangentes interiormente** | $d = |r_1 - r_2|$ |
| **Interiores** | $d < |r_1 - r_2|$ |
| **Concéntricas** | $d = 0$ (mismo centro) |

---

> "La geometría tiene dos grandes tesoros: uno es el Teorema de Pitágoras; el otro, la razón entre el diámetro y la circunferencia."
> — **Johannes Kepler**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G04", expanded=False):
        st.markdown(r"""
### E01: Longitud de circunferencia y área

**Situación:** Una circunferencia tiene radio $r = 5$ cm. Calcula su longitud y el área del círculo.

**La Carpintería:**
1. **Longitud:** $L = 2\pi r = 2\pi(5) = 10\pi \approx 31{,}42$ cm.
2. **Área:** $A = \pi r^2 = \pi(5)^2 = 25\pi \approx 78{,}54$ cm².

| Medida | Fórmula | Resultado |
| :--- | :--- | :---: |
| Longitud | $2\pi(5)$ | $10\pi$ cm |
| Área | $\pi(5)^2$ | $25\pi$ cm² |

---

### E02: Ángulo inscrito y ángulo central

**Situación:** Un ángulo central mide $140°$. ¿Cuánto mide el ángulo inscrito que subtiende el mismo arco?

**La Carpintería:**
1. **Teorema:** $\alpha_{inscrito} = \dfrac{\alpha_{central}}{2}$.
2. $\alpha_{inscrito} = \dfrac{140°}{2} = 70°$.

---

### E03: Longitud de un arco

**Situación:** En una circunferencia de radio $12$ cm, un ángulo central mide $90°$. ¿Cuál es la longitud del arco correspondiente?

**La Carpintería:**
1. Fórmula: $\ell = \dfrac{\theta}{360°} \cdot 2\pi r$.
2. $\ell = \dfrac{90°}{360°} \cdot 2\pi(12) = \dfrac{1}{4} \cdot 24\pi = 6\pi \approx 18{,}85$ cm.

---

### E04: Área de un sector circular

**Situación:** ¿Cuál es el área de un sector circular de radio $8$ cm y ángulo central $60°$?

**La Carpintería:**
1. Fórmula: $A_s = \dfrac{\theta}{360°} \cdot \pi r^2$.
2. $A_s = \dfrac{60°}{360°} \cdot \pi(8)^2 = \dfrac{1}{6} \cdot 64\pi = \dfrac{64\pi}{6} = \dfrac{32\pi}{3} \approx 33{,}51$ cm².

| Paso | Cálculo | Resultado |
| :--- | :--- | :---: |
| Fracción del círculo | $\frac{60}{360} = \frac{1}{6}$ | — |
| Área total | $\pi(8)^2 = 64\pi$ | — |
| Área del sector | $\frac{1}{6} \cdot 64\pi$ | $\frac{32\pi}{3}$ cm² |
""")

    with st.expander("❓ Cuestionario G04: Circunferencia y Círculo", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es la longitud de una circunferencia de diámetro $10$ cm?**

A) $5\pi$ cm
B) $10\pi$ cm
C) $20\pi$ cm
D) $100\pi$ cm

---

**2. Un ángulo inscrito subtiende el mismo arco que un ángulo central de $80°$. ¿Cuánto mide el ángulo inscrito?**

A) $40°$
B) $80°$
C) $160°$
D) $20°$

---

**3. ¿Cuál es el área de un círculo cuyo radio mide $7$ cm?**

A) $14\pi$ cm²
B) $7\pi$ cm²
C) $49\pi$ cm²
D) $21\pi$ cm²

---

**4. Una recta tangente a una circunferencia forma con el radio en el punto de tangencia un ángulo de:**

A) $45°$
B) $60°$
C) $90°$
D) $180°$

---

**5. ¿Cuál es la longitud del arco correspondiente a un ángulo central de $120°$ en una circunferencia de radio $9$ cm?**

A) $3\pi$ cm
B) $6\pi$ cm
C) $9\pi$ cm
D) $12\pi$ cm

---

**6. Un ángulo inscrito en una semicircunferencia mide:**

A) $45°$
B) $60°$
C) $90°$
D) $180°$

---

**7. Dos circunferencias tienen radios $3$ cm y $5$ cm, y la distancia entre sus centros es $8$ cm. ¿Cuál es su posición relativa?**

A) Secantes
B) Tangentes exteriormente
C) Exteriores
D) Tangentes interiormente
""")

    with st.expander("🔑 Pauta Técnica G04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | $L = \pi d = \pi \cdot 10 = 10\pi$ cm. |
| **2** | **A** | Ángulo inscrito $= \frac{80°}{2} = 40°$. |
| **3** | **C** | $A = \pi r^2 = \pi(7)^2 = 49\pi$ cm². |
| **4** | **C** | La tangente es perpendicular al radio en el punto de tangencia: $90°$. |
| **5** | **B** | $\ell = \frac{120}{360} \cdot 2\pi(9) = \frac{1}{3} \cdot 18\pi = 6\pi$ cm. |
| **6** | **C** | Teorema de Tales: todo ángulo inscrito en una semicircunferencia es recto ($90°$). |
| **7** | **B** | $d = 8 = 3 + 5 = r_1 + r_2$ → tangentes exteriormente. |
""")
