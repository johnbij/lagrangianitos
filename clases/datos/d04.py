import streamlit as st


def render_D04():
    st.title("D04: Gráficos Estadísticos — Leer e Interpretar Datos Visualmente")

    st.markdown(r"""
### 🛡️ 1. El Portal: Los Datos Tienen Forma

Un gráfico bien elegido puede revelar patrones que una tabla de números esconde. En la PAES, los gráficos aparecen constantemente: te pedirán **leer valores**, **comparar categorías**, **identificar tendencias** y **detectar errores** en su interpretación. Conocer cada tipo de gráfico y cuándo usarlo es esencial.

---

### 🛡️ 2. Gráfico de Barras

- **Uso:** Variables **cualitativas** o cuantitativas **discretas** con pocos valores.
- **Estructura:** Barras separadas (no se tocan), donde la altura representa la frecuencia.
- **Lectura:** Compara directamente las alturas de las barras.

| Característica | Detalle |
| :--- | :--- |
| Eje horizontal | Categorías o valores |
| Eje vertical | Frecuencia absoluta o relativa |
| Barras | Separadas entre sí |

> **Variante:** Gráfico de barras **horizontal** (útil cuando los nombres de categorías son largos) y **barras agrupadas** o **apiladas** para comparar subgrupos.

---

### 🛡️ 3. Histograma

- **Uso:** Variables **cuantitativas continuas** agrupadas en intervalos.
- **Estructura:** Barras **juntas** (sin separación), ya que los intervalos son consecutivos.
- **Lectura:** El área de cada barra es proporcional a la frecuencia de ese intervalo.

| Histograma vs Barras | Diferencia clave |
| :--- | :--- |
| Barras separadas | Gráfico de barras (categorías) |
| Barras juntas | Histograma (intervalos continuos) |

> **Tip PAES:** Si ves barras pegadas, es un **histograma**. Si ves barras separadas, es un gráfico **de barras**.

---

### 🛡️ 4. Polígono de Frecuencias

- **Uso:** Datos agrupados en intervalos.
- **Construcción:** Se marcan puntos en las **marcas de clase** a la altura de la frecuencia correspondiente y se unen con segmentos de recta.
- **Ventaja:** Permite superponer varios polígonos para comparar distribuciones.

---

### 🛡️ 5. Gráfico Circular (Torta)

- **Uso:** Mostrar la **proporción** de cada categoría respecto al total.
- **Estructura:** Un círculo dividido en sectores cuyo ángulo central es proporcional a la frecuencia relativa.
- **Fórmula del ángulo:** $\alpha_i = h_i \times 360°$.

| Categoría | $f_i$ | $h_i$ | Ángulo |
| :--- | :---: | :---: | :---: |
| A | $15$ | $0{,}30$ | $108°$ |
| B | $25$ | $0{,}50$ | $180°$ |
| C | $10$ | $0{,}20$ | $72°$ |
| **Total** | $50$ | $1{,}00$ | $360°$ |

> **Tip PAES:** Si el ángulo de un sector es $90°$, ese sector representa $\frac{90}{360} = 25\%$ del total.

---

### 🛡️ 6. Diagrama de Caja (Boxplot)

- **Uso:** Resumir la distribución mostrando posición, dispersión y simetría.
- **Los 5 números del boxplot:**

$$x_{\min}, \quad Q_1, \quad Q_2 \text{ (mediana)}, \quad Q_3, \quad x_{\max}$$

- **La caja** va de $Q_1$ a $Q_3$ (contiene el $50\%$ central de los datos).
- **Los bigotes** se extienden hasta $x_{\min}$ y $x_{\max}$ (o hasta $1{,}5 \cdot RIC$).
- **Puntos aislados** más allá de los bigotes → **outliers**.

| Elemento | Información |
| :--- | :--- |
| Línea central de la caja | Mediana ($Q_2$) |
| Ancho de la caja | $RIC = Q_3 - Q_1$ |
| Bigotes | Extensión de los datos |
| Puntos sueltos | Valores atípicos |

---

### 🛡️ 7. Gráfico de Dispersión (Nube de Puntos)

- **Uso:** Visualizar la relación entre **dos variables cuantitativas**.
- **Lectura:** Cada punto $(x_i, y_i)$ representa un par de datos.
- **Patrones:** Si los puntos sugieren una línea, hay **correlación lineal** (tema de D05).

---

### 🛡️ 8. Errores Comunes en la Lectura de Gráficos (PAES)

| Error | Descripción |
| :--- | :--- |
| Eje cortado | El eje $y$ no parte de $0$, exagerando diferencias |
| Escala irregular | Los intervalos del eje no son uniformes |
| Gráfico inadecuado | Usar un gráfico circular para datos continuos |
| Confundir frecuencia con porcentaje | Leer la altura como porcentaje cuando es frecuencia absoluta |

---

> *"Un buen gráfico vale más que mil números."*
> — **Edward Tufte**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería D04", expanded=False):
        st.markdown(r"""
### E01: Interpretar un gráfico de barras

**Situación:** Un gráfico de barras muestra las preferencias de deporte de 100 estudiantes:
- Fútbol: altura $35$
- Básquetbol: altura $20$
- Tenis: altura $15$
- Natación: altura $30$

**La Carpintería:**
1. **¿Cuál es el deporte más popular?** Fútbol ($35$ estudiantes).
2. **¿Qué porcentaje prefiere natación?** $\frac{30}{100} \times 100\% = 30\%$.
3. **¿Cuántos prefieren fútbol o tenis?** $35 + 15 = 50$ estudiantes.
4. **Verificación:** $35 + 20 + 15 + 30 = 100$ ✅.

---

### E02: Calcular ángulos de un gráfico circular

**Situación:** Encuesta sobre medio de transporte a $n = 200$ personas: Bus $= 80$, Metro $= 60$, Auto $= 40$, Bicicleta $= 20$.

**La Carpintería:**
1. Frecuencias relativas: $h_1 = \frac{80}{200} = 0{,}40$; $h_2 = 0{,}30$; $h_3 = 0{,}20$; $h_4 = 0{,}10$.
2. Ángulos: $\alpha_1 = 0{,}40 \times 360° = 144°$; $\alpha_2 = 108°$; $\alpha_3 = 72°$; $\alpha_4 = 36°$.
3. Verificación: $144 + 108 + 72 + 36 = 360°$ ✅.

| Transporte | $f_i$ | $h_i$ | Ángulo |
| :--- | :---: | :---: | :---: |
| Bus | $80$ | $0{,}40$ | $144°$ |
| Metro | $60$ | $0{,}30$ | $108°$ |
| Auto | $40$ | $0{,}20$ | $72°$ |
| Bicicleta | $20$ | $0{,}10$ | $36°$ |

---

### E03: Leer un diagrama de caja

**Situación:** Un boxplot muestra: $x_{\min} = 10$, $Q_1 = 25$, $Q_2 = 35$, $Q_3 = 50$, $x_{\max} = 70$, con un punto aislado en $95$.

**La Carpintería:**
1. **Mediana:** $35$ (línea central de la caja).
2. **$RIC = Q_3 - Q_1 = 50 - 25 = 25$**.
3. **Límite superior para outliers:** $Q_3 + 1{,}5 \times RIC = 50 + 37{,}5 = 87{,}5$.
4. **El punto en $95$** supera $87{,}5$ → es un **outlier**.
5. **Simetría:** La mediana ($35$) está más cerca de $Q_1$ ($25$) que de $Q_3$ ($50$), por lo que la distribución es **asimétrica a la derecha** (cola derecha más larga).

---

### E04: Elegir el gráfico adecuado

| Datos | Gráfico recomendado | Razón |
| :--- | :--- | :--- |
| Notas de una prueba (datos continuos) | Histograma | Datos cuantitativos continuos agrupados |
| Color favorito | Barras o circular | Variable cualitativa |
| Peso vs. estatura | Dispersión | Relación entre dos variables cuantitativas |
| Distribución de sueldos | Boxplot | Detecta outliers y muestra dispersión |
""")

    with st.expander("❓ Cuestionario D04: Gráficos Estadísticos", expanded=False):
        st.markdown(r"""
**1. La diferencia principal entre un histograma y un gráfico de barras es:**

A) El histograma usa colores y el gráfico de barras no
B) En el histograma las barras están juntas; en el de barras, separadas
C) El histograma es circular
D) No hay diferencia

---

**2. En un gráfico circular, un sector con ángulo de $72°$ representa:**

A) $72\%$ del total
B) $20\%$ del total
C) $25\%$ del total
D) $36\%$ del total

---

**3. En un diagrama de caja (boxplot), ¿qué representa el ancho de la caja?**

A) El rango
B) La media
C) El rango intercuartílico ($RIC$)
D) La desviación estándar

---

**4. ¿Qué gráfico es más adecuado para comparar la distribución de edades entre dos escuelas?**

A) Gráfico circular
B) Diagrama de caja (boxplot)
C) Gráfico de líneas
D) Pictograma

---

**5. Si en un histograma la barra del intervalo $[20, 30)$ tiene altura $15$ y el total de datos es $60$, la frecuencia relativa de ese intervalo es:**

A) $15\%$
B) $0{,}15$
C) $0{,}25$
D) $4$

---

**6. Un gráfico de dispersión muestra puntos que van de abajo-izquierda a arriba-derecha. Esto sugiere:**

A) Correlación negativa
B) Correlación nula
C) Correlación positiva
D) No hay relación

---

**7. Si un eje vertical no comienza en $0$, el gráfico puede:**

A) Ser más preciso
B) Exagerar las diferencias entre las barras
C) Disminuir las diferencias
D) No tiene ningún efecto
""")

    with st.expander("🔑 Pauta Técnica D04: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | El histograma tiene barras juntas (intervalos continuos); el de barras, separadas (categorías). |
| **2** | **B** | $\frac{72°}{360°} = 0{,}20 = 20\%$. Cada grado del círculo representa $\frac{1}{360}$ del total. |
| **3** | **C** | La caja va de $Q_1$ a $Q_3$, su ancho es $Q_3 - Q_1 = RIC$. |
| **4** | **B** | El boxplot permite comparar medianas, dispersiones y outliers de dos grupos lado a lado. |
| **5** | **C** | $h_i = \frac{15}{60} = 0{,}25$. Frecuencia relativa = frecuencia absoluta / total. |
| **6** | **C** | Puntos que suben de izquierda a derecha indican que al aumentar $x$, aumenta $y$ → correlación positiva. |
| **7** | **B** | Un eje que no parte de $0$ puede hacer que pequeñas diferencias parezcan enormes → sesgo visual. |
""")
