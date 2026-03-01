import streamlit as st


def render_D05():
    st.title("D05: Análisis de Datos y Correlación — Interpretar con Sentido Crítico")

    st.markdown(r"""
### 🛡️ 1. El Portal: De los Números a las Conclusiones

Recopilar y resumir datos es solo el inicio. El paso definitivo es **interpretar** lo que dicen (y lo que **no** dicen). En la PAES, te enfrentarás a afirmaciones basadas en datos y deberás decidir si son válidas, si hay sesgo o si se están sacando conclusiones apresuradas.

---

### 🛡️ 2. Correlación Lineal

La correlación mide la **fuerza y dirección** de la relación lineal entre dos variables cuantitativas.

| Tipo | Descripción | Gráfico de dispersión |
| :--- | :--- | :--- |
| **Positiva** | Al aumentar $x$, aumenta $y$ | Puntos suben de izq. a der. |
| **Negativa** | Al aumentar $x$, disminuye $y$ | Puntos bajan de izq. a der. |
| **Nula** | No hay relación lineal clara | Puntos dispersos sin patrón |

El **coeficiente de correlación** $r$ cuantifica esta relación:

$$-1 \leq r \leq 1$$

| Valor de $r$ | Interpretación |
| :---: | :--- |
| $r = 1$ | Correlación positiva perfecta |
| $0{,}7 \leq r < 1$ | Correlación positiva fuerte |
| $0{,}3 \leq r < 0{,}7$ | Correlación positiva moderada |
| $0 < r < 0{,}3$ | Correlación positiva débil |
| $r = 0$ | Sin correlación lineal |
| $r < 0$ | Correlación negativa (análogo) |
| $r = -1$ | Correlación negativa perfecta |

> **¡Cuidado!** Correlación **no** implica causalidad. Que dos variables se muevan juntas no significa que una cause a la otra.

---

### 🛡️ 3. Recta de Regresión (Intuición)

Si los datos muestran correlación lineal, se puede trazar una **recta de regresión** $y = a + bx$ que mejor se ajuste a la nube de puntos.

- **$b > 0$:** la recta sube → correlación positiva.
- **$b < 0$:** la recta baja → correlación negativa.
- **Uso:** Permite hacer **predicciones** estimando $y$ para un valor dado de $x$.

> **Tip PAES:** No te pedirán calcular $a$ y $b$, pero sí interpretar la recta, su pendiente y hacer predicciones con ella.

---

### 🛡️ 4. Sesgo en los Datos

El sesgo ocurre cuando los datos **no representan** fielmente a la población.

| Tipo de sesgo | Ejemplo |
| :--- | :--- |
| **De selección** | Encuestar solo a personas de una ciudad sobre preferencias nacionales |
| **De no respuesta** | Muchas personas no responden y sus opiniones difieren |
| **De pregunta** | Formular la pregunta de forma que induzca una respuesta |
| **Del sobreviviente** | Estudiar solo a empresas exitosas e ignorar las que quebraron |

---

### 🛡️ 5. Tipos de Muestreo

| Método | Descripción |
| :--- | :--- |
| **Aleatorio simple** | Cada individuo tiene la misma probabilidad de ser elegido |
| **Estratificado** | Se divide la población en grupos (estratos) y se selecciona de cada uno |
| **Sistemático** | Se elige un individuo cada $k$ posiciones en una lista |
| **Por conveniencia** | Se elige a los más accesibles (⚠️ mayor riesgo de sesgo) |

> **Tip PAES:** El muestreo **aleatorio** y **estratificado** son los más confiables. El muestreo por conveniencia es el más sesgado.

---

### 🛡️ 6. Interpretación Crítica de Información Estadística

**Preguntas clave que debes hacerte ante una afirmación estadística:**
1. ¿La muestra es representativa de la población?
2. ¿Se usó la medida de tendencia central adecuada?
3. ¿Se ocultan datos o se manipulan las escalas del gráfico?
4. ¿Se confunde correlación con causalidad?
5. ¿El tamaño de la muestra es suficiente?

---

> *"Tortura los datos lo suficiente y confesarán lo que quieras."*
> — **Ronald Coase**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería D05", expanded=False):
        st.markdown(r"""
### E01: Identificar tipo de correlación

**Situación:** Se registran las horas de estudio y el puntaje en una prueba de 6 estudiantes:

| Horas ($x$) | Puntaje ($y$) |
| :---: | :---: |
| $2$ | $45$ |
| $4$ | $60$ |
| $5$ | $65$ |
| $7$ | $80$ |
| $8$ | $85$ |
| $10$ | $95$ |

**La Carpintería:**
1. Al aumentar las horas de estudio, **aumenta** el puntaje.
2. Los puntos van de abajo-izquierda a arriba-derecha.
3. **Correlación: positiva** y aparentemente fuerte.
4. **Conclusión:** Mayor tiempo de estudio se **asocia** a mejores puntajes (pero no podemos afirmar que sea la única causa).

---

### E02: Detectar sesgo en una encuesta

**Situación:** Una empresa de comida rápida encuestó a 500 clientes **dentro de sus locales** y concluyó que "el $85\%$ de los chilenos prefiere comida rápida".

**La Carpintería:**
1. **Sesgo de selección:** Solo se encuestó a personas que ya están en el local → naturalmente prefieren comida rápida.
2. **No es representativa:** Falta la opinión de quienes no frecuentan esos locales.
3. **Conclusión válida:** "El $85\%$ de los clientes encuestados en los locales prefiere comida rápida" (no se puede extrapolar a todos los chilenos).

---

### E03: Interpretar una recta de regresión

**Situación:** La recta de regresión entre temperatura ($x$, en °C) y ventas de helado ($y$, en unidades) es $y = 10 + 5x$.

**La Carpintería:**
1. **Pendiente $b = 5$:** Por cada grado que sube la temperatura, se venden $5$ helados más.
2. **Intercepto $a = 10$:** Si la temperatura fuera $0°$C, se venderían $10$ helados (valor teórico).
3. **Predicción:** Si $x = 30°$C → $y = 10 + 5(30) = 160$ helados.
4. **Cuidado con extrapolar:** Si $x = 50°$C, la fórmula da $y = 260$, pero la predicción puede no ser válida fuera del rango de datos observados.

---

### E04: Elegir el muestreo adecuado

**Situación:** Se quiere conocer la opinión de los alumnos de un colegio con cursos de 7.° a IV medio (8 niveles) sobre el uniforme escolar.

**La Carpintería:**
1. **Muestreo aleatorio simple:** Elegir al azar alumnos de todo el colegio. Riesgo: podría quedar todo de un solo curso.
2. **Muestreo estratificado (mejor opción):** Definir cada nivel como un estrato y elegir alumnos al azar de cada uno. Así se garantiza representación de todos los cursos.
3. **Muestreo por conveniencia (peor opción):** Preguntar solo a los del patio en recreo. Sesgo: no todos están ahí.
""")

    with st.expander("❓ Cuestionario D05: Análisis de Datos y Correlación", expanded=False):
        st.markdown(r"""
**1. Si el coeficiente de correlación entre dos variables es $r = -0{,}85$, la correlación es:**

A) Positiva fuerte
B) Negativa fuerte
C) Nula
D) Positiva débil

---

**2. "Los países que consumen más chocolate tienen más premios Nobel." Esta afirmación ilustra:**

A) Causalidad comprobada
B) Correlación sin necesariamente causalidad
C) Ausencia de relación
D) Muestreo estratificado

---

**3. Un periódico publicó: "El $90\%$ de los encuestados apoya la nueva ley." La encuesta se realizó por internet a quienes voluntariamente participaron. El principal problema es:**

A) El porcentaje es muy alto
B) Se usó media en vez de mediana
C) Sesgo de selección (autoselección)
D) La muestra es demasiado grande

---

**4. Si la recta de regresión es $y = 20 - 3x$, la pendiente indica que:**

A) Por cada unidad que aumenta $x$, $y$ aumenta en $3$
B) Por cada unidad que aumenta $x$, $y$ disminuye en $3$
C) $y$ siempre es $20$
D) No hay relación

---

**5. ¿Qué tipo de muestreo divide la población en grupos y selecciona de cada uno?**

A) Aleatorio simple
B) Sistemático
C) Estratificado
D) Por conveniencia

---

**6. Si $r = 0$ entre dos variables, se puede concluir que:**

A) No existe ninguna relación entre ellas
B) No hay relación lineal, pero podría haber otro tipo de relación
C) Las variables son independientes
D) Los datos tienen errores

---

**7. Un estudio muestra correlación positiva entre el tamaño de zapato y la habilidad lectora en niños. La explicación más probable es:**

A) Los zapatos grandes mejoran la lectura
B) Existe una variable de confusión: la edad
C) Es un error de medición
D) No hay relación
""")

    with st.expander("🔑 Pauta Técnica D05: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **B** | $r = -0{,}85$ está cerca de $-1$ → correlación negativa fuerte. |
| **2** | **B** | Es el ejemplo clásico de correlación sin causalidad. La riqueza del país podría ser la variable de confusión. |
| **3** | **C** | Quienes participan voluntariamente pueden tener opiniones más extremas → sesgo de autoselección. |
| **4** | **B** | Pendiente $b = -3$: por cada unidad que sube $x$, $y$ baja en $3$. |
| **5** | **C** | El muestreo estratificado garantiza representación de cada subgrupo de la población. |
| **6** | **B** | $r = 0$ solo descarta relación lineal. Podría haber relación cuadrática, por ejemplo. |
| **7** | **B** | La edad es la variable de confusión: niños mayores tienen pies más grandes **y** leen mejor, pero una cosa no causa la otra. |
""")
