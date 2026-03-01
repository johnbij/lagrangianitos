import streamlit as st


def render_D03():
    st.title("D03: Medidas de Dispersión y Posición — ¿Qué Tan Esparcidos Están los Datos?")

    st.markdown(r"""
### 🛡️ 1. El Portal: Más Allá del Centro

Saber que el promedio de notas de un curso es $5{,}5$ no dice todo: ¿todos sacaron cerca de $5{,}5$ o algunos tuvieron $2$ y otros $7$? Las **medidas de dispersión** cuantifican cuán esparcidos están los datos alrededor del centro, y las **medidas de posición** dividen los datos en partes iguales.

---

### 🛡️ 2. Rango

Es la medida de dispersión más sencilla:

$$R = x_{\max} - x_{\min}$$

**Ejemplo:** Datos $3, 5, 7, 9, 15$ → $R = 15 - 3 = 12$.

> **Limitación:** Solo usa dos datos (el mayor y el menor), por lo que un solo outlier puede inflarlo enormemente.

---

### 🛡️ 3. Desviación Estándar ($\sigma$ o $s$) y Varianza ($\sigma^2$)

La varianza mide el promedio de las desviaciones al cuadrado respecto a la media:

$$\sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}$$

La desviación estándar es su raíz cuadrada:

$$\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$$

> **Nota:** En algunos contextos (muestral), se divide por $n - 1$ en lugar de $n$. En la PAES generalmente se usa $n$.

**Interpretación:**
- $\sigma$ pequeño → datos muy concentrados alrededor de la media.
- $\sigma$ grande → datos muy dispersos.

**Pasos para calcular $\sigma$:**
1. Calcular $\bar{x}$.
2. Restar la media a cada dato: $(x_i - \bar{x})$.
3. Elevar al cuadrado: $(x_i - \bar{x})^2$.
4. Promediar las desviaciones al cuadrado → varianza.
5. Sacar raíz cuadrada → desviación estándar.

---

### 🛡️ 4. Coeficiente de Variación ($CV$)

Permite comparar la dispersión de dos conjuntos con distintas unidades o escalas:

$$CV = \frac{\sigma}{\bar{x}} \times 100\%$$

**Ejemplo:** Si un grupo tiene $\bar{x} = 50$ y $\sigma = 10$, entonces $CV = \frac{10}{50} \times 100\% = 20\%$.

> **Regla:** A mayor $CV$, mayor variabilidad relativa. Se usa para comparar dispersiones entre conjuntos con medias distintas.

---

### 🛡️ 5. Cuartiles ($Q_1, Q_2, Q_3$)

Los cuartiles dividen los datos **ordenados** en **4 partes iguales** (cada una con el $25\%$ de los datos).

| Cuartil | Posición | Significado |
| :---: | :--- | :--- |
| $Q_1$ | $25\%$ de los datos están por debajo | Primer cuartil |
| $Q_2$ | $50\%$ de los datos están por debajo | Segundo cuartil = **Mediana** |
| $Q_3$ | $75\%$ de los datos están por debajo | Tercer cuartil |

**Método práctico para encontrar cuartiles:**
1. Ordenar datos de menor a mayor.
2. Encontrar la mediana ($Q_2$).
3. $Q_1$ = mediana de la mitad inferior.
4. $Q_3$ = mediana de la mitad superior.

---

### 🛡️ 6. Rango Intercuartílico ($RIC$ o $IQR$)

$$RIC = Q_3 - Q_1$$

El $RIC$ mide la dispersión del $50\%$ central de los datos. Es más robusto que el rango porque **no depende de valores extremos**.

**Detección de outliers (regla del $1{,}5 \cdot RIC$):**
- Límite inferior: $Q_1 - 1{,}5 \cdot RIC$
- Límite superior: $Q_3 + 1{,}5 \cdot RIC$
- Cualquier dato fuera de estos límites se considera **atípico** (outlier).

---

### 🛡️ 7. Percentiles

Los percentiles dividen los datos en **100 partes iguales**.

- El percentil $P_{k}$ indica que el $k\%$ de los datos está por debajo de ese valor.
- $P_{25} = Q_1$, $P_{50} = Q_2 = Me$, $P_{75} = Q_3$.

**Ejemplo:** Si un estudiante está en el percentil $85$, significa que supera al $85\%$ de los estudiantes.

---

> *"La variación es la voz de los procesos. Escucharla es el primer paso para mejorar."*
> — **Walter A. Shewhart**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería D03", expanded=False):
        st.markdown(r"""
### E01: Calcular varianza y desviación estándar

**Situación:** Datos: $4, 6, 8, 10, 12$.

**La Carpintería:**
1. **Media:** $\bar{x} = \frac{4+6+8+10+12}{5} = \frac{40}{5} = 8$.
2. **Desviaciones y cuadrados:**

| $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
| :---: | :---: | :---: |
| $4$ | $-4$ | $16$ |
| $6$ | $-2$ | $4$ |
| $8$ | $0$ | $0$ |
| $10$ | $2$ | $4$ |
| $12$ | $4$ | $16$ |
| **Suma** | $0$ | $40$ |

3. **Varianza:** $\sigma^2 = \frac{40}{5} = 8$.
4. **Desviación estándar:** $\sigma = \sqrt{8} \approx 2{,}83$.

---

### E02: Cuartiles y RIC

**Situación:** Datos ordenados: $2, 3, 5, 7, 8, 10, 12, 14, 15$ ($n = 9$).

**La Carpintería:**
1. **$Q_2$ (mediana):** posición $\frac{9+1}{2} = 5$ → $Q_2 = 8$.
2. **Mitad inferior:** $2, 3, 5, 7$ → $Q_1 = \frac{3+5}{2} = 4$.
3. **Mitad superior:** $10, 12, 14, 15$ → $Q_3 = \frac{12+14}{2} = 13$.
4. **$RIC = Q_3 - Q_1 = 13 - 4 = 9$**.
5. **Detección de outliers:**
   - Límite inferior: $4 - 1{,}5 \times 9 = 4 - 13{,}5 = -9{,}5$.
   - Límite superior: $13 + 1{,}5 \times 9 = 13 + 13{,}5 = 26{,}5$.
   - Todos los datos están entre $-9{,}5$ y $26{,}5$ → **no hay outliers**.

| Medida | Valor |
| :--- | :---: |
| $Q_1$ | $4$ |
| $Q_2$ | $8$ |
| $Q_3$ | $13$ |
| $RIC$ | $9$ |

---

### E03: Comparar dispersión con coeficiente de variación

**Situación:** Grupo A (edades): $\bar{x}_A = 40$, $\sigma_A = 8$. Grupo B (puntajes): $\bar{x}_B = 200$, $\sigma_B = 30$. ¿Cuál tiene mayor variabilidad relativa?

**La Carpintería:**
1. $CV_A = \frac{8}{40} \times 100\% = 20\%$.
2. $CV_B = \frac{30}{200} \times 100\% = 15\%$.
3. **Conclusión:** El Grupo A tiene mayor variabilidad relativa ($20\% > 15\%$), aunque su $\sigma$ absoluta sea menor.

| Grupo | $\bar{x}$ | $\sigma$ | $CV$ |
| :--- | :---: | :---: | :---: |
| A | $40$ | $8$ | $20\%$ |
| B | $200$ | $30$ | $15\%$ |
""")

    with st.expander("❓ Cuestionario D03: Medidas de Dispersión y Posición", expanded=False):
        st.markdown(r"""
**1. El rango del conjunto $\{3, 7, 2, 9, 5\}$ es:**

A) $5$
B) $7$
C) $9$
D) $2$

---

**2. Si la varianza de un conjunto es $25$, la desviación estándar es:**

A) $625$
B) $12{,}5$
C) $5$
D) $50$

---

**3. ¿Qué medida permite comparar la dispersión de dos conjuntos con distintas unidades?**

A) Rango
B) Varianza
C) Coeficiente de variación
D) Desviación estándar

---

**4. Los datos $1, 3, 5, 7, 9, 11, 13$ tienen $Q_2$ igual a:**

A) $5$
B) $7$
C) $9$
D) $6$

---

**5. Si $Q_1 = 20$ y $Q_3 = 50$, el rango intercuartílico es:**

A) $70$
B) $35$
C) $30$
D) $15$

---

**6. Un estudiante está en el percentil $P_{90}$. Esto significa que:**

A) Obtuvo un $90\%$ de respuestas correctas
B) El $90\%$ de los estudiantes obtuvo un puntaje menor o igual al suyo
C) Solo el $10\%$ obtuvo menos que él
D) Su nota es $9{,}0$

---

**7. Si a todos los datos de un conjunto se les suma una constante $k$, la desviación estándar:**

A) Aumenta en $k$
B) Se multiplica por $k$
C) No cambia
D) Disminuye en $k$
""")

    with st.expander("🔑 Pauta Técnica D03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $R = 9 - 2 = 7$. Asegúrate de restar el mínimo del máximo. |
| **2** | **C** | $\sigma = \sqrt{25} = 5$. Desviación estándar = raíz cuadrada de la varianza. |
| **3** | **C** | El $CV$ expresa la dispersión como porcentaje de la media, eliminando las unidades. |
| **4** | **B** | $n = 7$, posición central = $4$. El dato en posición $4$ es $7$. |
| **5** | **C** | $RIC = Q_3 - Q_1 = 50 - 20 = 30$. |
| **6** | **B** | $P_{90}$ indica que el $90\%$ de los datos queda por debajo de su valor. |
| **7** | **C** | Sumar una constante desplaza todos los datos igual, sin cambiar su dispersión respecto a la media. |
""")
