import streamlit as st


def render_P01():
    st.title("P01: Perímetro de Figuras Planas — El Contorno del Mundo")

    st.markdown(r"""
### 🛡️ 1. ¿Qué es el Perímetro?

El **perímetro** de una figura plana es la **longitud total de su contorno**. Imagina que caminas por el borde de una cancha de fútbol: la distancia total que recorres es el perímetro.

Se mide en **unidades de longitud**: metros (m), centímetros (cm), kilómetros (km), etc.

$$P = \text{suma de todos los lados}$$

> **Tip PAES:** El perímetro siempre se expresa en unidades lineales (m, cm), nunca en unidades cuadradas.

---

### 🛡️ 2. Perímetro de Triángulos

Para cualquier triángulo con lados $a$, $b$ y $c$:

$$P_{\triangle} = a + b + c$$

| Tipo de triángulo | Lados | Perímetro simplificado |
| :--- | :--- | :--- |
| **Equilátero** | $a = b = c = \ell$ | $P = 3\ell$ |
| **Isósceles** | $a = b \neq c$ | $P = 2a + c$ |
| **Escaleno** | Todos distintos | $P = a + b + c$ |

---

### 🛡️ 3. Perímetro de Cuadriláteros

| Figura | Lados | Fórmula del perímetro |
| :--- | :--- | :--- |
| **Cuadrado** | $\ell$ | $P = 4\ell$ |
| **Rectángulo** | $a$ (largo), $b$ (ancho) | $P = 2a + 2b = 2(a+b)$ |
| **Rombo** | $\ell$ | $P = 4\ell$ |
| **Paralelogramo** | $a$, $b$ | $P = 2(a + b)$ |
| **Trapecio** | $a, b, c, d$ | $P = a + b + c + d$ |

---

### 🛡️ 4. Perímetro de Polígonos Regulares

Un **polígono regular** tiene $n$ lados iguales de longitud $\ell$:

$$P = n \cdot \ell$$

| Polígono | $n$ | Perímetro |
| :--- | :---: | :--- |
| Pentágono regular | 5 | $P = 5\ell$ |
| Hexágono regular | 6 | $P = 6\ell$ |
| Octágono regular | 8 | $P = 8\ell$ |
| Decágono regular | 10 | $P = 10\ell$ |

---

### 🛡️ 5. Perímetro de la Circunferencia (Longitud)

La **circunferencia** no tiene lados, pero su contorno tiene una longitud bien definida:

$$L = 2\pi r = \pi d$$

donde $r$ es el radio y $d = 2r$ es el diámetro.

Para un **arco** de ángulo central $\theta$ (en grados):

$$L_{\text{arco}} = \frac{\theta}{360°} \cdot 2\pi r$$

---

### 🛡️ 6. Perímetro de Figuras Compuestas

Muchos problemas PAES combinan figuras. La clave es identificar qué **bordes** están expuestos (forman parte del contorno) y cuáles son **interiores** (no se cuentan).

**Estrategia:**
1. Descomponer la figura en formas simples.
2. Identificar los lados que forman el contorno exterior.
3. Sumar solo esos lados.

---

> *"La geometría es el conocimiento de lo eternamente existente."*
> — **Platón**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería P01", expanded=False):
        st.markdown(r"""
### E01: Perímetro de un terreno rectangular

**Situación:** Un terreno tiene $45 \text{ m}$ de largo y $30 \text{ m}$ de ancho. ¿Cuántos metros de cerco se necesitan para rodearlo?

**La Carpintería:**
1. **Identificar:** Rectángulo con $a = 45$ m, $b = 30$ m.
2. **Fórmula:** $P = 2(a + b) = 2(45 + 30) = 2 \cdot 75 = 150$ m.
3. Se necesitan **150 metros** de cerco.

| Dato | Valor |
| :--- | :---: |
| Largo | $45$ m |
| Ancho | $30$ m |
| **Perímetro** | **$150$ m** |

---

### E02: Perímetro de un hexágono regular

**Situación:** Un hexágono regular tiene lados de $8$ cm. ¿Cuál es su perímetro?

**La Carpintería:**
1. **Identificar:** Polígono regular con $n = 6$, $\ell = 8$ cm.
2. **Fórmula:** $P = n \cdot \ell = 6 \cdot 8 = 48$ cm.

---

### E03: Longitud de una pista circular

**Situación:** Una pista circular tiene un radio de $50$ m. ¿Cuánto recorre un atleta en una vuelta completa? Usa $\pi \approx 3{,}14$.

**La Carpintería:**
1. **Identificar:** Circunferencia con $r = 50$ m.
2. **Fórmula:** $L = 2\pi r = 2(3{,}14)(50) = 314$ m.
3. El atleta recorre aproximadamente **314 metros**.

---

### E04: Perímetro de una figura compuesta

**Situación:** Una ventana tiene forma de un rectángulo de $1{,}2$ m de ancho y $1{,}5$ m de alto, coronada por un semicírculo. ¿Cuál es el perímetro del marco?

**La Carpintería:**
1. El semicírculo tiene diámetro $d = 1{,}2$ m, así que $r = 0{,}6$ m.
2. El contorno incluye: 2 lados verticales ($1{,}5$ m cada uno) + 1 base ($1{,}2$ m) + semicircunferencia.
3. Semicircunferencia: $\frac{1}{2} \cdot 2\pi r = \pi(0{,}6) \approx 1{,}885$ m.
4. $P = 2(1{,}5) + 1{,}2 + 1{,}885 = 3 + 1{,}2 + 1{,}885 = 6{,}085$ m.

| Componente | Medida |
| :--- | :---: |
| Dos lados verticales | $3{,}0$ m |
| Base inferior | $1{,}2$ m |
| Semicircunferencia | $\approx 1{,}885$ m |
| **Perímetro total** | **$\approx 6{,}09$ m** |
""")

    with st.expander("❓ Cuestionario P01: Perímetro de Figuras Planas", expanded=False):
        st.markdown(r"""
**1. ¿Cuál es el perímetro de un cuadrado de lado $9$ cm?**

A) $18$ cm
B) $27$ cm
C) $36$ cm
D) $81$ cm

---

**2. Un rectángulo tiene un perímetro de $40$ cm y un largo de $12$ cm. ¿Cuánto mide el ancho?**

A) $6$ cm
B) $8$ cm
C) $16$ cm
D) $28$ cm

---

**3. ¿Cuál es la longitud de una circunferencia de diámetro $10$ cm?**

A) $10\pi$ cm
B) $20\pi$ cm
C) $5\pi$ cm
D) $25\pi$ cm

---

**4. Un triángulo equilátero tiene un perímetro de $27$ cm. ¿Cuánto mide cada lado?**

A) $6$ cm
B) $9$ cm
C) $13{,}5$ cm
D) $27$ cm

---

**5. Un arco de circunferencia tiene un ángulo central de $90°$ y un radio de $4$ cm. ¿Cuál es la longitud del arco?**

A) $\pi$ cm
B) $2\pi$ cm
C) $4\pi$ cm
D) $8\pi$ cm

---

**6. Un pentágono regular tiene un perímetro de $35$ cm. ¿Cuánto mide cada lado?**

A) $5$ cm
B) $7$ cm
C) $8$ cm
D) $10$ cm

---

**7. Se desea cercar un jardín rectangular de $20$ m × $15$ m, dejando una puerta de $3$ m. ¿Cuántos metros de cerco se necesitan?**

A) $67$ m
B) $70$ m
C) $73$ m
D) $300$ m
""")

    with st.expander("🔑 Pauta Técnica P01: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $P = 4\ell = 4 \cdot 9 = 36$ cm. |
| **2** | **B** | $P = 2(a+b) \Rightarrow 40 = 2(12 + b) \Rightarrow 20 = 12 + b \Rightarrow b = 8$ cm. |
| **3** | **A** | $L = \pi d = \pi \cdot 10 = 10\pi$ cm. |
| **4** | **B** | Equilátero: $P = 3\ell \Rightarrow 27 = 3\ell \Rightarrow \ell = 9$ cm. |
| **5** | **B** | $L_{\text{arco}} = \frac{90°}{360°} \cdot 2\pi(4) = \frac{1}{4} \cdot 8\pi = 2\pi$ cm. |
| **6** | **B** | $P = 5\ell \Rightarrow 35 = 5\ell \Rightarrow \ell = 7$ cm. |
| **7** | **A** | $P = 2(20+15) = 70$ m, pero se descuenta la puerta: $70 - 3 = 67$ m. |
""")
