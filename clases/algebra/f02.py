import streamlit as st


def render_F02():
    st.title("F02: Función Lineal y Afín — La Recta que Cuenta Historias")

    st.markdown(r"""
### 🛡️ 1. El Portal: La Función más Importante

Si las funciones son el idioma de las matemáticas, la **función lineal** es la primera palabra que aprendes a pronunciar. Está en todas partes: en el cobro del taxi (tarifa fija + precio por kilómetro), en el sueldo de un trabajador (sueldo base + comisión por venta), en la conversión de temperaturas.

La **función afín** tiene la forma:

$$f(x) = mx + n$$

donde:
- $m$ es la **pendiente** (cuánto sube o baja la recta por cada unidad que avanzas en $x$).
- $n$ es el **intercepto con el eje $y$** (el valor de $f(x)$ cuando $x = 0$).

Cuando $n = 0$, la función se llama **función lineal** propiamente tal: $f(x) = mx$, y su gráfico pasa por el origen.

---

### 🛡️ 1.1 La Pendiente: El Corazón de la Recta

La pendiente $m$ mide la **razón de cambio** de la función. Se calcula con dos puntos $(x_1, y_1)$ y $(x_2, y_2)$:

$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}$$

| Valor de $m$ | Comportamiento de la recta |
| :---: | :--- |
| $m > 0$ | La recta **sube** (crece de izquierda a derecha) |
| $m < 0$ | La recta **baja** (decrece de izquierda a derecha) |
| $m = 0$ | La recta es **horizontal** ($f(x) = n$, función constante) |
| $m$ no definida | Recta **vertical** ($x = k$, no es función) |

> **Tip PAES:** La pendiente es el "ritmo" al que cambia la función. Una pendiente de $3$ significa que por cada unidad que avanzas en $x$, la función sube $3$ unidades en $y$.

---

### 🛡️ 1.2 El Intercepto y la Tabla de Valores

El **intercepto $y$** es el punto $(0, n)$ donde la recta cruza el eje vertical. El **intercepto $x$** (o **cero de la función**) es el punto donde la recta cruza el eje horizontal:

$$f(x) = 0 \quad \Rightarrow \quad mx + n = 0 \quad \Rightarrow \quad x = -\frac{n}{m}$$

Para graficar rápidamente, basta con dos puntos. Una tabla de valores útil:

| $x$ | $f(x) = 2x - 3$ |
| :---: | :---: |
| $0$ | $-3$ |
| $1$ | $-1$ |
| $\frac{3}{2}$ | $0$ ← cero de la función |
| $2$ | $1$ |

---

### 🏛️ 1.3 Ecuación Punto-Pendiente

Si conoces un punto $(x_0, y_0)$ que pertenece a la recta y la pendiente $m$, puedes escribir la ecuación de la recta directamente:

$$y - y_0 = m(x - x_0)$$

Esta forma es muy útil en la PAES porque te dan un punto y una condición de pendiente. Por ejemplo:

> "Encuentra la ecuación de la recta que pasa por $(2, 5)$ con pendiente $-3$."

$$y - 5 = -3(x - 2) \quad \Rightarrow \quad y = -3x + 6 + 5 \quad \Rightarrow \quad y = -3x + 11$$

---

### 🛡️ 1.4 Rectas Paralelas y Perpendiculares

Dos relaciones clave que la PAES adora preguntar:

| Relación | Condición | Ejemplo |
| :--- | :--- | :--- |
| **Paralelas** | Tienen la **misma pendiente**: $m_1 = m_2$ | $y = 3x + 1$ y $y = 3x - 7$ |
| **Perpendiculares** | Sus pendientes son **recíprocas negativas**: $m_1 \cdot m_2 = -1$ | $y = 2x + 1$ y $y = -\frac{1}{2}x + 4$ |

> **Regla de oro:** Si una recta tiene pendiente $\frac{a}{b}$, la perpendicular tiene pendiente $-\frac{b}{a}$.

---

### 🏛️ 1.5 Modelación con Funciones Lineales

La gran potencia de la función lineal es describir situaciones reales con crecimiento o decrecimiento **constante**:

| Situación | Función | Significado de $m$ | Significado de $n$ |
| :--- | :--- | :--- | :--- |
| Taxi cobra $\$800$ de bajada de bandera + $\$300$ por km | $f(x) = 300x + 800$ | Costo por km | Tarifa fija |
| Un estanque pierde $5$ litros por hora y partió con $200$ L | $f(t) = -5t + 200$ | Tasa de pérdida | Volumen inicial |
| Temperatura que sube $2°$ cada hora desde $15°$ | $T(t) = 2t + 15$ | Razón de cambio | Temperatura inicial |

---

> "La línea recta es la distancia más corta entre dos puntos, y también la función más elegante entre dos ideas."
> — **Leonhard Euler**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería F02", expanded=False):
        st.markdown(r"""
### E01: Calcular la pendiente entre dos puntos

**Situación:** Encuentra la pendiente de la recta que pasa por $A(1, 3)$ y $B(4, 9)$.

**La Carpintería:**
1. **Fórmula:** $m = \dfrac{y_2 - y_1}{x_2 - x_1}$.
2. **Sustituir:** $m = \dfrac{9 - 3}{4 - 1} = \dfrac{6}{3} = 2$.
3. **Interpretación:** Por cada unidad que $x$ avanza, $y$ sube $2$ unidades.

---

### E02: Encontrar la ecuación de una recta

**Situación:** Escribe la ecuación de la recta que pasa por $(3, -1)$ con pendiente $m = 4$.

**La Carpintería:**
1. **Punto-pendiente:** $y - (-1) = 4(x - 3)$.
2. **Desarrollar:** $y + 1 = 4x - 12$.
3. **Despejar:** $y = 4x - 13$.

| Verificación | $x = 3$ | $f(3) = 4(3) - 13 = -1$ ✅ |
| :--- | :--- | :--- |

---

### E03: Determinar si dos rectas son perpendiculares

**Situación:** ¿Son perpendiculares $y = \frac{2}{3}x + 1$ y $y = -\frac{3}{2}x + 5$?

**La Carpintería:**
1. **Pendientes:** $m_1 = \frac{2}{3}$ y $m_2 = -\frac{3}{2}$.
2. **Producto:** $m_1 \cdot m_2 = \frac{2}{3} \cdot \left(-\frac{3}{2}\right) = -1$.
3. **Conclusión:** Sí, son perpendiculares porque $m_1 \cdot m_2 = -1$.

---

### E04: Modelar con función lineal

**Situación:** Un plan de celular cobra $\$5\,000$ fijos mensuales más $\$50$ por cada minuto de llamada. Escribe la función de costo y calcula cuánto se paga por $120$ minutos.

**La Carpintería:**
1. **Variable:** $x$ = minutos de llamada.
2. **Función:** $C(x) = 50x + 5\,000$.
3. **Evaluar:** $C(120) = 50(120) + 5\,000 = 6\,000 + 5\,000 = \$11\,000$.

| Componente | Valor | Rol |
| :--- | :--- | :--- |
| Pendiente $m$ | $50$ | Costo por minuto |
| Intercepto $n$ | $5\,000$ | Cargo fijo mensual |
""")

    with st.expander("❓ Cuestionario F02: Función Lineal y Afín", expanded=False):
        st.markdown(r"""
**1. La pendiente de la recta que pasa por $(2, 1)$ y $(5, 7)$ es:**

A) $\dfrac{1}{2}$
B) $2$
C) $3$
D) $\dfrac{8}{7}$

---

**2. ¿Cuál es el intercepto con el eje $y$ de la recta $y = -4x + 9$?**

A) $-4$
B) $9$
C) $\dfrac{9}{4}$
D) $0$

---

**3. La ecuación de la recta que pasa por $(0, 3)$ con pendiente $-2$ es:**

A) $y = 3x - 2$
B) $y = -2x + 3$
C) $y = -2x - 3$
D) $y = 2x + 3$

---

**4. Dos rectas paralelas tienen pendientes $m_1 = 5$ y $m_2$. Entonces $m_2$ es:**

A) $-5$
B) $\dfrac{1}{5}$
C) $5$
D) $-\dfrac{1}{5}$

---

**5. Si $y = \frac{1}{3}x - 2$, ¿para qué valor de $x$ se tiene $y = 0$?**

A) $x = 6$
B) $x = -6$
C) $x = 2$
D) $x = 3$

---

**6. Una recta perpendicular a $y = -\frac{2}{5}x + 1$ tiene pendiente:**

A) $\dfrac{2}{5}$
B) $-\dfrac{5}{2}$
C) $\dfrac{5}{2}$
D) $-\dfrac{2}{5}$

---

**7. Un estanque tiene $100$ litros y pierde $8$ litros por hora. ¿Después de cuántas horas queda vacío?**

A) $8$ horas
B) $10$ horas
C) $12$ horas
D) $12.5$ horas
""")

    with st.expander("🔑 Pauta Técnica F02: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **B** | $m = \frac{7-1}{5-2} = \frac{6}{3} = 2$. |
| **2** | **B** | El intercepto $y$ es el valor de $n$ en $y = mx + n$. Aquí $n = 9$, así que la recta cruza el eje $y$ en $(0, 9)$. |
| **3** | **B** | Con $m = -2$ y el punto $(0, 3)$: $y = -2x + 3$. El punto $(0, 3)$ es directamente el intercepto. |
| **4** | **C** | Rectas paralelas tienen la misma pendiente: $m_2 = m_1 = 5$. |
| **5** | **A** | $0 = \frac{1}{3}x - 2 \Rightarrow \frac{1}{3}x = 2 \Rightarrow x = 6$. |
| **6** | **C** | Si $m_1 = -\frac{2}{5}$, entonces $m_2 = -\frac{1}{m_1} = -\frac{1}{-2/5} = \frac{5}{2}$. |
| **7** | **D** | $f(t) = -8t + 100 = 0 \Rightarrow t = \frac{100}{8} = 12.5$ horas. |
""")
