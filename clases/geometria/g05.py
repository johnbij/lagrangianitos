import streamlit as st


def render_G05():
    st.title("G05: Transformaciones Isométricas — El Movimiento sin Deformación")

    st.markdown(r"""
### 🛡️ 1. El Portal: Mover sin Romper

Imagina que tomas una figura geométrica y la mueves, la giras o la reflejas en un espejo. Si al hacerlo la figura **no cambia de forma ni de tamaño**, has realizado una **transformación isométrica** (del griego *iso* = igual, *metría* = medida).

Las transformaciones isométricas conservan:
- Las **longitudes** de los lados.
- Las **medidas** de los ángulos.
- La **forma** y el **tamaño** de la figura.

Lo único que puede cambiar es la **posición** y, en el caso de la reflexión, la **orientación** (sentido de giro).

---

### 🛡️ 1.1 Traslación

Una **traslación** desplaza todos los puntos de una figura la misma distancia y en la misma dirección. Se define por un **vector de traslación** $\vec{v} = (a, b)$.

Si un punto $P(x, y)$ se traslada por el vector $\vec{v} = (a, b)$, su imagen es:

$$P'(x + a,\; y + b)$$

| Característica | Descripción |
| :--- | :--- |
| ¿Qué se conserva? | Forma, tamaño, orientación |
| ¿Qué cambia? | Solo la posición |
| Elemento que la define | Un vector $\vec{v} = (a, b)$ |

**Ejemplo:** Si $P(3, 2)$ se traslada por $\vec{v} = (-4, 5)$, entonces $P' = (3 + (-4),\; 2 + 5) = (-1, 7)$.

---

### 🏛️ 1.2 Rotación

Una **rotación** gira todos los puntos de una figura alrededor de un punto fijo llamado **centro de rotación**, un **ángulo** determinado y en un **sentido** (horario o antihorario).

Para una rotación de $90°$ antihorario con centro en el origen:

$$P(x, y) \rightarrow P'(-y, x)$$

Para una rotación de $180°$ con centro en el origen:

$$P(x, y) \rightarrow P'(-x, -y)$$

| Característica | Descripción |
| :--- | :--- |
| ¿Qué se conserva? | Forma, tamaño, orientación |
| ¿Qué cambia? | La posición |
| Elementos que la definen | Centro, ángulo, sentido de giro |

> **Convención PAES:** Salvo que se indique lo contrario, el sentido **positivo** es el **antihorario** (sentido contrario a las agujas del reloj).

---

### 🛡️ 1.3 Reflexión (Simetría Axial)

Una **reflexión** transforma cada punto en su imagen "espejo" respecto de una recta llamada **eje de simetría**. El eje es la **mediatriz** del segmento que une cada punto con su imagen.

| Eje de reflexión | Regla |
| :--- | :--- |
| Eje $x$ (horizontal) | $P(x, y) \rightarrow P'(x, -y)$ |
| Eje $y$ (vertical) | $P(x, y) \rightarrow P'(-x, y)$ |
| Recta $y = x$ | $P(x, y) \rightarrow P'(y, x)$ |

| Característica | Descripción |
| :--- | :--- |
| ¿Qué se conserva? | Forma, tamaño |
| ¿Qué cambia? | Posición y **orientación** (la figura queda "invertida") |
| Elemento que la define | Un eje de simetría (recta) |

> **Clave PAES:** La reflexión es la **única** transformación isométrica que cambia la orientación de la figura. Un triángulo con vértices en sentido horario queda con vértices en sentido antihorario.

---

### 🛡️ 1.4 Simetría Central

La **simetría central** es equivalente a una rotación de $180°$ respecto de un punto fijo (centro de simetría). Cada punto $P$ y su imagen $P'$ están a la misma distancia del centro $O$, y $O$ es el punto medio de $\overline{PP'}$.

$$P(x, y) \rightarrow P'(2a - x,\; 2b - y) \quad \text{si el centro es } O(a, b)$$

Si el centro es el origen: $P(x, y) \rightarrow P'(-x, -y)$.

---

### 🏛️ 1.5 Composición de Transformaciones y Teselaciones

**Composición:** Se pueden aplicar transformaciones sucesivas. Por ejemplo:
- Dos reflexiones respecto de ejes **paralelos** equivalen a una **traslación**.
- Dos reflexiones respecto de ejes que se **cortan** equivalen a una **rotación** (de ángulo igual al doble del ángulo entre los ejes).

**Teselaciones:** Un **teselado** (o mosaico) es un recubrimiento del plano sin huecos ni superposiciones, usando una o más figuras repetidas mediante transformaciones isométricas.

| Polígono regular | ¿Tesela el plano? | Razón |
| :--- | :--- | :--- |
| Triángulo equilátero | ✅ Sí | $60° \times 6 = 360°$ |
| Cuadrado | ✅ Sí | $90° \times 4 = 360°$ |
| Hexágono regular | ✅ Sí | $120° \times 3 = 360°$ |
| Pentágono regular | ❌ No | $108°$ no divide a $360°$ |

> **Solo tres polígonos regulares** teselan el plano por sí solos: el triángulo equilátero, el cuadrado y el hexágono regular.

---

> "La simetría es el concepto que unifica la física, la matemática y el arte."
> — **Hermann Weyl**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería G05", expanded=False):
        st.markdown(r"""
### E01: Traslación de un punto

**Situación:** Traslada el punto $A(2, -3)$ por el vector $\vec{v} = (5, 4)$.

**La Carpintería:**
1. Aplicar la regla: $A' = (x + a,\; y + b)$.
2. $A' = (2 + 5,\; -3 + 4) = (7, 1)$.

| Punto | Coordenada $x$ | Coordenada $y$ |
| :--- | :---: | :---: |
| Original $A$ | $2$ | $-3$ |
| Vector $\vec{v}$ | $+5$ | $+4$ |
| Imagen $A'$ | $7$ | $1$ |

---

### E02: Rotación de 90° antihorario

**Situación:** Rota el punto $B(4, 1)$ en $90°$ antihorario respecto del origen.

**La Carpintería:**
1. Regla para $90°$ antihorario: $P(x, y) \rightarrow P'(-y, x)$.
2. $B' = (-1, 4)$.
3. **Verificación:** La distancia al origen se conserva: $\sqrt{4^2 + 1^2} = \sqrt{17}$ y $\sqrt{(-1)^2 + 4^2} = \sqrt{17}$ ✅.

---

### E03: Reflexión respecto del eje $y$

**Situación:** Refleja el triángulo con vértices $P(1, 3)$, $Q(4, 3)$ y $R(2, 6)$ respecto del eje $y$.

**La Carpintería:**
1. Regla: $P(x, y) \rightarrow P'(-x, y)$.
2. $P' = (-1, 3)$, $Q' = (-4, 3)$, $R' = (-2, 6)$.
3. La figura queda "reflejada" como en un espejo vertical.

| Vértice original | Imagen |
| :--- | :--- |
| $P(1, 3)$ | $P'(-1, 3)$ |
| $Q(4, 3)$ | $Q'(-4, 3)$ |
| $R(2, 6)$ | $R'(-2, 6)$ |

---

### E04: Composición de transformaciones

**Situación:** El punto $C(3, 2)$ se traslada por $\vec{v} = (-1, 3)$ y luego se refleja respecto del eje $x$. ¿Cuál es la imagen final?

**La Carpintería:**
1. **Traslación:** $C_1 = (3 + (-1),\; 2 + 3) = (2, 5)$.
2. **Reflexión en eje $x$:** $C' = (2, -5)$.
3. La imagen final es $C'(2, -5)$.
""")

    with st.expander("❓ Cuestionario G05: Transformaciones Isométricas", expanded=False):
        st.markdown(r"""
**1. Si el punto $P(3, -2)$ se traslada por el vector $\vec{v} = (-5, 4)$, ¿cuáles son las coordenadas de su imagen?**

A) $(8, 2)$
B) $(-2, 2)$
C) $(-2, -6)$
D) $(2, -2)$

---

**2. ¿Cuál es la imagen de $A(2, 5)$ al reflejarlo respecto del eje $x$?**

A) $(-2, 5)$
B) $(2, -5)$
C) $(-2, -5)$
D) $(5, 2)$

---

**3. Al rotar el punto $(0, 3)$ en $180°$ respecto del origen, se obtiene:**

A) $(3, 0)$
B) $(0, -3)$
C) $(-3, 0)$
D) $(0, 3)$

---

**4. ¿Cuál de las transformaciones isométricas cambia la orientación de la figura?**

A) Traslación
B) Rotación
C) Reflexión
D) Ninguna

---

**5. ¿Cuáles de los siguientes polígonos regulares pueden teselar el plano por sí solos?**

A) Pentágono y hexágono
B) Triángulo, cuadrado y hexágono
C) Cuadrado y pentágono
D) Solo el cuadrado

---

**6. ¿Cuál es la imagen de $M(-1, 4)$ al reflejarlo respecto de la recta $y = x$?**

A) $(4, -1)$
B) $(-4, 1)$
C) $(1, -4)$
D) $(-1, -4)$

---

**7. Dos reflexiones respecto de ejes paralelos equivalen a:**

A) Una rotación
B) Una traslación
C) Una reflexión
D) Una simetría central
""")

    with st.expander("🔑 Pauta Técnica G05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | $P' = (3 + (-5),\; -2 + 4) = (-2, 2)$. |
| **2** | **B** | Reflexión en eje $x$: $(x, y) \to (x, -y)$, así $A' = (2, -5)$. |
| **3** | **B** | Rotación $180°$: $(x, y) \to (-x, -y)$, así $(0, 3) \to (0, -3)$. |
| **4** | **C** | La reflexión invierte la orientación (sentido de recorrido de los vértices). Traslación y rotación la conservan. |
| **5** | **B** | Los tres polígonos regulares que teselan solos son el triángulo equilátero ($60°$), el cuadrado ($90°$) y el hexágono regular ($120°$). |
| **6** | **A** | Reflexión en $y = x$: $(x, y) \to (y, x)$, así $(-1, 4) \to (4, -1)$. |
| **7** | **B** | Dos reflexiones en ejes paralelos producen una traslación cuya magnitud es el doble de la distancia entre los ejes. |
""")
