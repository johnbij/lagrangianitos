import streamlit as st


def render_F05():
    st.title("F05: Composición de Funciones y Transformaciones — Combinando y Moviendo Funciones")

    st.markdown(r"""
### 🛡️ 1. El Portal: Funciones que Trabajan en Equipo

Hasta ahora hemos estudiado funciones por separado, pero la verdadera potencia aparece cuando las **combinamos**. Piensa en una cadena de producción: una máquina corta la madera y otra la pinta. El resultado final depende de aplicar la segunda máquina **al resultado de la primera**. Eso es exactamente la **composición de funciones**.

La **composición** de $f$ con $g$ se escribe $(f \circ g)(x)$ y significa:

$$\boxed{(f \circ g)(x) = f\!\big(g(x)\big)}$$

Primero aplicas $g$ a $x$, y luego aplicas $f$ al resultado. El orden importa: en general, $f \circ g \neq g \circ f$.

---

### 🛡️ 1.1 Cómo Calcular una Composición

La receta es sencilla: **sustituye** la función interior donde aparece la variable de la función exterior.

Sea $f(x) = 2x + 3$ y $g(x) = x^2$:

| Composición | Cálculo | Resultado |
| :--- | :--- | :--- |
| $(f \circ g)(x) = f(g(x))$ | $f(x^2) = 2(x^2) + 3$ | $2x^2 + 3$ |
| $(g \circ f)(x) = g(f(x))$ | $g(2x + 3) = (2x + 3)^2$ | $4x^2 + 12x + 9$ |

Observa que $(f \circ g)(x) \neq (g \circ f)(x)$. **El orden cambia el resultado.**

> **Tip PAES:** Lee $(f \circ g)(x)$ como "primero $g$, luego $f$". La función que está *más cerca* de la $x$ se aplica primero.

---

### 🛡️ 1.2 Evaluación de Composiciones en un Punto

Para calcular $(f \circ g)(a)$, sigue dos pasos:

1. **Paso 1:** Calcula $g(a)$.
2. **Paso 2:** Usa ese resultado como entrada de $f$.

**Ejemplo:** Si $f(x) = x - 1$ y $g(x) = 3x + 2$, calcula $(f \circ g)(4)$.

1. $g(4) = 3(4) + 2 = 14$.
2. $f(14) = 14 - 1 = 13$.
3. $(f \circ g)(4) = 13$.

---

### 🏛️ 1.3 Traslaciones (Desplazamientos)

Las **traslaciones** mueven el gráfico de una función sin cambiar su forma. Son la transformación más común en la PAES:

| Transformación | Ecuación | Efecto en el gráfico |
| :--- | :--- | :--- |
| Traslación **vertical hacia arriba** | $y = f(x) + k$ con $k > 0$ | Sube $k$ unidades |
| Traslación **vertical hacia abajo** | $y = f(x) - k$ con $k > 0$ | Baja $k$ unidades |
| Traslación **horizontal a la derecha** | $y = f(x - h)$ con $h > 0$ | Se mueve $h$ unidades a la **derecha** |
| Traslación **horizontal a la izquierda** | $y = f(x + h)$ con $h > 0$ | Se mueve $h$ unidades a la **izquierda** |

> **Cuidado con el signo horizontal:** Es contraintuitivo. $f(x - 3)$ mueve la gráfica **a la derecha**, no a la izquierda. Piénsalo así: para que $f$ "vea" el mismo valor que antes veía en $x = 0$, ahora necesitas $x = 3$.

---

### 🛡️ 1.4 Reflexiones

Las **reflexiones** son como poner un espejo sobre un eje:

| Transformación | Ecuación | Efecto |
| :--- | :--- | :--- |
| Reflexión respecto al **eje $x$** | $y = -f(x)$ | Voltea el gráfico "arriba-abajo" |
| Reflexión respecto al **eje $y$** | $y = f(-x)$ | Voltea el gráfico "izquierda-derecha" |

**Ejemplo:** Si $f(x) = x^2$, entonces:
- $-f(x) = -x^2$ es la parábola invertida (abierta hacia abajo).
- $f(-x) = (-x)^2 = x^2$ se ve igual (porque $x^2$ es simétrica respecto al eje $y$).

---

### 🏛️ 1.5 Dilataciones y Compresiones

Las **dilataciones** cambian el "tamaño" del gráfico:

| Transformación | Ecuación | Efecto |
| :--- | :--- | :--- |
| Dilatación **vertical** | $y = k \cdot f(x)$ con $k > 1$ | Estira verticalmente (más alto) |
| Compresión **vertical** | $y = k \cdot f(x)$ con $0 < k < 1$ | Aplasta verticalmente (más bajo) |
| Dilatación **horizontal** | $y = f(kx)$ con $0 < k < 1$ | Estira horizontalmente (más ancho) |
| Compresión **horizontal** | $y = f(kx)$ con $k > 1$ | Comprime horizontalmente (más angosto) |

---

### 🛡️ 1.6 Modelación con Funciones: Combinando Todo

En la PAES, los problemas de modelación combinan funciones con contextos reales. La estrategia es:

1. **Identificar** las variables y la relación entre ellas.
2. **Elegir** el tipo de función adecuado (lineal, cuadrática, exponencial).
3. **Aplicar** transformaciones si el problema lo requiere (desplazar, escalar).
4. **Evaluar** para responder la pregunta.

| Contexto | Función base | Transformación típica |
| :--- | :--- | :--- |
| Objeto lanzado hacia arriba | $f(t) = -at^2 + bt + c$ | Traslación vertical (altura inicial) |
| Crecimiento poblacional | $P(t) = P_0 \cdot a^t$ | Dilatación vertical (población inicial) |
| Costo con descuento | $C(x) = mx + n$ | Traslación vertical (descuento fijo) |

---

> "La matemática es el arte de dar el mismo nombre a cosas diferentes."
> — **Henri Poincaré**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería F05", expanded=False):
        st.markdown(r"""
### E01: Calcular composiciones

**Situación:** Si $f(x) = x + 5$ y $g(x) = 2x - 1$, encuentra $(f \circ g)(x)$ y $(g \circ f)(x)$.

**La Carpintería:**

| Composición | Sustitución | Resultado |
| :--- | :--- | :--- |
| $(f \circ g)(x) = f(g(x))$ | $f(2x - 1) = (2x - 1) + 5$ | $2x + 4$ |
| $(g \circ f)(x) = g(f(x))$ | $g(x + 5) = 2(x + 5) - 1$ | $2x + 9$ |

Verificación: $(f \circ g)(3) = 2(3) + 4 = 10$ y $(g \circ f)(3) = 2(3) + 9 = 15$. Son distintos ✅.

---

### E02: Identificar transformaciones

**Situación:** El gráfico de $y = (x - 2)^2 + 3$ se obtiene a partir de $y = x^2$ mediante:

**La Carpintería:**
1. **$x - 2$ dentro del cuadrado:** Traslación horizontal $2$ unidades **a la derecha**.
2. **$+ 3$ fuera del cuadrado:** Traslación vertical $3$ unidades **hacia arriba**.
3. **Resultado:** El vértice de $y = x^2$ pasa de $(0, 0)$ a $(2, 3)$.

| Función | Vértice | Transformación aplicada |
| :--- | :---: | :--- |
| $y = x^2$ | $(0, 0)$ | Función original |
| $y = (x - 2)^2$ | $(2, 0)$ | Traslación derecha $2$ |
| $y = (x - 2)^2 + 3$ | $(2, 3)$ | Traslación arriba $3$ |

---

### E03: Reflexiones

**Situación:** A partir de $f(x) = \sqrt{x}$, describe el gráfico de $g(x) = -\sqrt{x}$ y $h(x) = \sqrt{-x}$.

**La Carpintería:**
1. **$g(x) = -\sqrt{x}$:** Reflexión respecto al eje $x$. El gráfico se voltea hacia abajo. Dominio: $x \geq 0$.
2. **$h(x) = \sqrt{-x}$:** Reflexión respecto al eje $y$. El gráfico se voltea hacia la izquierda. Dominio: $x \leq 0$.

---

### E04: Composición con evaluación numérica

**Situación:** Si $f(x) = x^2 - 1$ y $g(x) = x + 3$, calcula $(f \circ g)(-2)$ y $(g \circ f)(-2)$.

**La Carpintería:**

| Cálculo | Paso 1 | Paso 2 | Resultado |
| :--- | :--- | :--- | :---: |
| $(f \circ g)(-2)$ | $g(-2) = -2 + 3 = 1$ | $f(1) = 1^2 - 1 = 0$ | $0$ |
| $(g \circ f)(-2)$ | $f(-2) = (-2)^2 - 1 = 3$ | $g(3) = 3 + 3 = 6$ | $6$ |
""")

    with st.expander("❓ Cuestionario F05: Composición y Transformaciones", expanded=False):
        st.markdown(r"""
**1. Si $f(x) = 3x$ y $g(x) = x + 2$, entonces $(f \circ g)(1)$ es:**

A) $5$
B) $9$
C) $6$
D) $7$

---

**2. El gráfico de $y = f(x) + 4$ se obtiene del gráfico de $y = f(x)$ mediante:**

A) Traslación $4$ unidades a la derecha
B) Traslación $4$ unidades a la izquierda
C) Traslación $4$ unidades hacia arriba
D) Traslación $4$ unidades hacia abajo

---

**3. Si $y = f(x - 5)$, el gráfico de $f$ se desplaza:**

A) $5$ unidades a la izquierda
B) $5$ unidades a la derecha
C) $5$ unidades hacia arriba
D) $5$ unidades hacia abajo

---

**4. La reflexión de $f(x) = 2x + 1$ respecto al eje $x$ es:**

A) $y = -2x + 1$
B) $y = -2x - 1$
C) $y = 2x - 1$
D) $y = 2(-x) + 1$

---

**5. Si $f(x) = x^2$ y $g(x) = x - 1$, entonces $(g \circ f)(3)$ es:**

A) $4$
B) $8$
C) $9$
D) $3$

---

**6. ¿Cuál transformación convierte $y = x^2$ en $y = 3x^2$?**

A) Traslación vertical $3$ unidades
B) Dilatación vertical por factor $3$
C) Traslación horizontal $3$ unidades
D) Compresión horizontal por factor $3$

---

**7. Si $f(x) = |x|$, el gráfico de $y = |x + 2| - 1$ tiene su vértice en:**

A) $(2, -1)$
B) $(-2, -1)$
C) $(-2, 1)$
D) $(2, 1)$
""")

    with st.expander("🔑 Pauta Técnica F05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | $(f \circ g)(1) = f(g(1)) = f(1 + 2) = f(3) = 3 \cdot 3 = 9$. |
| **2** | **C** | Sumar una constante positiva fuera de $f$ desplaza el gráfico hacia arriba. |
| **3** | **B** | $f(x - 5)$ desplaza el gráfico $5$ unidades a la **derecha** (el signo es contraintuitivo). |
| **4** | **B** | Reflexión respecto al eje $x$: $y = -f(x) = -(2x + 1) = -2x - 1$. |
| **5** | **B** | $(g \circ f)(3) = g(f(3)) = g(9) = 9 - 1 = 8$. |
| **6** | **B** | Multiplicar $f(x)$ por $3$ estira el gráfico verticalmente: es una dilatación vertical por factor $3$. |
| **7** | **B** | $|x + 2|$ desplaza $|x|$ dos unidades a la izquierda, y el $-1$ baja una unidad. Vértice: $(-2, -1)$. |
""")
