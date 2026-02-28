import streamlit as st


def render_N12():
    st.title("N12: Operatoria en ℚ - El Protocolo de Precisión")

    st.markdown(r"""
### 🏛️ 1. Contexto Histórico: El Caos de los Mares y el Orden de la Razón
Imagina estar en el siglo XVII, en medio del océano, tratando de calcular la posición de tu barco con un sextante. Un error de apenas $\frac{1}{64}$ en tus cálculos de navegación no significa un pequeño desvío; significa estrellarse contra un arrecife a kilómetros de tu destino.

Durante el Renacimiento, la matemática de fracciones pasó de ser un truco de comerciantes a ser una cuestión de vida o muerte. Los grandes navegantes y astrónomos se dieron cuenta de que el mundo no se mide en números redondos, sino en las grietas que hay entre ellos. Para dominar esas grietas, tuvieron que estandarizar un **orden de batalla**. El PAPOMUDAS que usas hoy es el mismo código de honor que permitió a la humanidad mapear los continentes y las estrellas. No es solo aritmética; es la herramienta que domesticó el caos de lo infinitamente pequeño.

---

### 🛡️ 9.B.1 El Protocolo Universal: PAPOMUDAS
Las reglas no cambian, pero el riesgo de error aumenta. El orden sigue siendo:

1. **PA (Paréntesis):** Resuelve lo de adentro primero.
2. **PO (Potencias):** (Próxima clase).
3. **MU - DA (Multiplicación y División):** De izquierda a derecha.
4. **S - R (Suma y Resta):** Al final, siempre con el **mcm**.

---

### 🛡️ 9.B.2 El "Atajo del Pillo" (Fracciones Complejas)
A veces verás un "castillo" de fracciones: $\frac{\frac{a}{b}}{\frac{c}{d}}$.
No te marees con tantos pisos. Usa el **Atajo del Pillo**: multiplica los extremos (el de más arriba con el de más abajo) para el numerador, y los medios para el denominador.
$$\frac{a \cdot d}{b \cdot c}$$

---

### 🛡️ 9.B.3 El Método del Cruce Directo
Cuando solo tienes **dos** fracciones y quieres velocidad, olvida la tabla del mcm. Haz el cruce:
$$\frac{a}{b} + \frac{c}{d} = \frac{(a \cdot d) + (b \cdot c)}{b \cdot d}$$

---

### 🛡️ 9.B.4 El "Efecto Espejo" del Signo Negativo
El signo menos en una fracción es como un camaleón; puede estar en tres posiciones y seguir significando lo mismo:
$$\left( -\frac{a}{b} \right) = \frac{-a}{b} = \frac{a}{-b}$$
**Regla Táctica:** Nunca dejes el signo negativo en el denominador para operar. Súbelo siempre al numerador o déjalo frente a la fracción para que no se te olvide en el "baile" de la suma.

---

### 🛡️ 9.B.5 La Identidad del Entero y el Factor $-1$
Todo número entero tiene una armadura invisible que lo convierte en fracción: el denominador $1$ ($n = \frac{n}{1}$).
Además, recuerda que una fracción negativa como $-\frac{3}{4}$ es equivalente a multiplicar por un **factor de inversión**:
$$(-1) \cdot \frac{3}{4} = \frac{-3}{4}$$
Este $-1$ es el que "da vuelta" el sentido de tus sumas y restas en la recta numérica.

---

### 🛡️ 9.B.6 El Desafío del Maestro: La Expresión del Terror
Vamos a desarmar esta pieza de ingeniería usando **PAPOMUDAS**:
$$\frac{1}{2} + \left( \frac{3}{4} - \frac{1}{2} \right) \div \frac{5}{2}$$

**Paso 1: Paréntesis (Resta con cruce directo)**
$\frac{3}{4} - \frac{1}{2} = \frac{6 - 4}{8} = \frac{2}{8} = \frac{1}{4}$

**Paso 2: División (Invertir y multiplicar)**
$\frac{1}{4} \div \frac{5}{2} = \frac{1}{4} \cdot \frac{2}{5} = \frac{2}{20} = \frac{1}{10}$

**Paso 3: Suma Final (mcm)**
$\frac{1}{2} + \frac{1}{10} = \frac{5}{10} + \frac{1}{10} = \frac{6}{10} = \frac{3}{5}$

---

> **Típ:** Si el ejercicio se ve muy grande, no intentes resolverlo de un viaje. Desarma los paréntesis primero como si fueran cajas pequeñas y luego junta todo.

---

> "Las fracciones son el lenguaje que usa la naturaleza para decirnos que nada es perfecto, pero todo es proporcional".
> — **Euclides (atribuido)**
""")

    with st.expander("🚀 Guía de Ejemplos: Maestría en Operatoria Racional", expanded=False):
        st.markdown(r"""
### E02: Suma de tres fracciones (El mcm en acción)
**Situación:** Resolver $\frac{1}{2} + \frac{2}{3} + \frac{3}{4}$.
**La Carpintería:** Buscamos el mcm entre 2, 3 y 4, que es 12. Amplificamos cada una para que todas tengan denominador 12.

| Fracción | Amplificador | Resultado Parcial |
| :--- | :---: | :--- |
| 1/2 | $\cdot 6$ | 6/12 |
| 2/3 | $\cdot 4$ | 8/12 |
| 3/4 | $\cdot 3$ | 9/12 |
| **Total** | $(6+8+9)/12$ | **23/12** |

---

### E03: Resta con número mixto
**Situación:** Resolver $3 \frac{1}{4} - \frac{5}{2}$.
**La Carpintería:** Primero pasamos el mixto a fracción impropia y luego igualamos denominadores.

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Pasar mixto a impropia | $13/4$ |
| 2 | Igualar denominadores (mcm=4) | $13/4 - 10/4$ |
| 3 | Restar | **3/4** |

---

### E04: El Atajo del Pillo (Fracción Compleja)
**Situación:** Resolver $\frac{\frac{3}{5}}{\frac{9}{10}}$.
**La Carpintería:** Extremos arriba, medios abajo.

| Piso | Operación | Resultado Parcial |
| :--- | :--- | :--- |
| Extremos | $3 \cdot 10$ | 30 |
| Medios | $5 \cdot 9$ | 45 |
| **Final** | $30/45$ (simplificar por 15) | **2/3** |

---

### E05: Multiplicación con "Limpieza" (Simplificación Cruzada)
**Situación:** Resolver $\frac{25}{18} \cdot \frac{12}{35}$.
**La Carpintería:** No multipliques $25 \cdot 12$. Simplifica el 25 con el 35 (por 5) y el 12 con el 18 (por 6).

| Antes | Simplificación | Después |
| :--- | :--- | :--- |
| 25/35 | Dividir por 5 | 5 y 7 |
| 12/18 | Dividir por 6 | 2 y 3 |
| **Final** | $(5 \cdot 2) / (3 \cdot 7)$ | **10/21** |

---

### E06: División con Entero y Fracción
**Situación:** Resolver $10 \div \frac{5}{4}$.
**La Carpintería:** El 10 tiene un 1 abajo. Invertimos la segunda fracción.

| Paso | Operación | Resultado |
| :--- | :--- | :--- |
| 1 | Invertir y multiplicar | $10/1 \cdot 4/5$ |
| 2 | Simplificar (10 y 5) | $2/1 \cdot 4/1$ |
| 3 | Final | **8** |

---

### E07: El Factor -1 en la Operatoria
**Situación:** Resolver $\frac{3}{4} + \left( - \frac{1}{2} \right) \cdot \frac{2}{3}$.
**La Carpintería:** Multiplicación antes que suma. El signo menos se mantiene.

| Prioridad | Operación | Estado |
| :--- | :--- | :--- |
| 1. Multiplicación | $(-1/2) \cdot (2/3) = -2/6$ | $3/4 - 1/3$ |
| 2. Resta (Cruce) | $(9 - 4) / 12$ | **5/12** |

---

### E08: Paréntesis con Resta y Multiplicación
**Situación:** Resolver $\frac{4}{5} \cdot \left( 1 - \frac{1}{4} \right)$.
**La Carpintería:** Resolvemos el "1 entero" como $4/4$ dentro del paréntesis.

| Capa | Operación | Resultado |
| :--- | :--- | :--- |
| Paréntesis | $4/4 - 1/4 = 3/4$ | $4/5 \cdot 3/4$ |
| Multiplicación | Simplificamos el 4 | **3/5** |

---

### E09: Doble División (Izquierda a Derecha)
**Situación:** Resolver $\frac{1}{2} \div \frac{1}{3} \div \frac{1}{4}$.
**La Carpintería:** No hagas la segunda división primero. Sigue el orden de lectura.

| Paso | Operación | Resultado Parcial |
| :--- | :--- | :--- |
| 1 | $(1/2 \cdot 3/1)$ | 3/2 |
| 2 | $3/2 \div 1/4 \rightarrow 3/2 \cdot 4/1$ | $12/2$ |
| 3 | Final | **6** |

---

### E10: El Castillo de Fracciones Combinado
**Situación:** Resolver $\frac{1 + \frac{1}{2}}{1 - \frac{1}{2}}$.
**La Carpintería:** Resolvemos el numerador y el denominador por separado y luego aplicamos el Atajo del Pillo.

| Parte | Operación | Resultado |
| :--- | :--- | :--- |
| Numerador | $2/2 + 1/2$ | 3/2 |
| Denominador | $2/2 - 1/2$ | 1/2 |
| **Pillo** | $(3 \cdot 2) / (2 \cdot 1)$ | **3** |

---

### E11: La Expresión del Terror II
**Situación:** Resolver $\left[ \frac{2}{3} \div \left( \frac{1}{2} + \frac{1}{6} \right) \right] - 1$.

| Prioridad | Operación | Resultado Parcial |
| :--- | :--- | :--- |
| 1. Paréntesis | $1/2 + 1/6 = 3/6 + 1/6 = 4/6$ | $2/3 \div 2/3$ |
| 2. Corchete | $2/3 \div 2/3 = 1$ | $1 - 1$ |
| 3. Final | | **0** |
""")

    with st.expander("❓ Cuestionario N12: Operatoria de Élite", expanded=False):
        st.markdown(r"""
> **Protocolo de Navegación:** Resuelve con calma. Cada signo y cada paréntesis tiene una razón de ser. No te saltes pasos si no quieres chocar con el arrecife.

**1. ¿Cuál es el resultado de $\frac{1}{2} + \frac{1}{3} \cdot \frac{3}{4}$?**
\
A) $\frac{5}{8}$
\
B) $\frac{3}{4}$
\
C) $\frac{5}{12}$
\
D) $\frac{1}{4}$

**2. Al resolver $\frac{2}{3} \div \frac{4}{3} \cdot \frac{1}{2}$, se obtiene:**
\
A) 1
\
B) $\frac{1}{4}$
\
C) $\frac{4}{9}$
\
D) $\frac{1}{2}$

**3. ¿Qué valor resulta de la expresión $\frac{\frac{2}{5}}{\frac{4}{15}}$?**
\
A) $\frac{8}{75}$
\
B) $\frac{3}{2}$
\
C) $\frac{2}{3}$
\
D) 6

**4. El resultado de $1 - \left( \frac{1}{2} - \frac{1}{4} \right)$ es:**
\
A) $\frac{3}{4}$
\
B) $\frac{1}{4}$
\
C) $\frac{1}{2}$
\
D) $\frac{5}{4}$

**5. Si calculamos $\left( -\frac{2}{3} \right) \cdot \left( -\frac{3}{4} \right)$, el resultado es:**
\
A) $-\frac{1}{2}$
\
B) $\frac{6}{12}$
\
C) $\frac{1}{2}$
\
D) $-\frac{5}{12}$

**6. ¿Cuál es el valor de $\frac{1}{2} \div 2$?**
\
A) 1
\
B) $\frac{1}{4}$
\
C) 4
\
D) $\frac{1}{2}$

**7. Al resolver $\frac{3}{4} - \frac{1}{2} + \frac{5}{4}$, el resultado simplificado es:**
\
A) $\frac{3}{2}$
\
B) $\frac{7}{4}$
\
C) 1
\
D) $\frac{9}{4}$

**8. El valor de la expresión $\frac{1 + \frac{1}{3}}{2}$ es:**
\
A) $\frac{4}{3}$
\
B) $\frac{8}{3}$
\
C) $\frac{2}{3}$
\
D) $\frac{1}{3}$

**9. ¿Cuál es el resultado de $\frac{2}{5} \cdot \frac{10}{3} \div \frac{4}{3}$?**
\
A) 1
\
B) $\frac{16}{25}$
\
C) $\frac{4}{3}$
\
D) $\frac{8}{15}$

**10. La expresión del terror: $\left( \frac{1}{2} + \frac{1}{2} \right) \cdot \frac{3}{4} - \frac{1}{4}$ resulta en:**
\
A) $\frac{1}{2}$
\
B) 1
\
C) $\frac{3}{4}$
\
D) 0
""")

    with st.expander("🔑 Pauta Técnica N12: Control de Navegación", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica (Análisis) |
| :--- | :---: | :--- |
| **1** | **B** | Mult. primero: $\frac{1}{3} \cdot \frac{3}{4} = \frac{1}{4}$. Luego $\frac{1}{2} + \frac{1}{4} = \frac{2}{4} + \frac{1}{4} = \frac{3}{4}$. |
| **2** | **B** | Izquierda a derecha: $\frac{2}{3} \cdot \frac{3}{4} = \frac{1}{2}$. Luego $\frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$. |
| **3** | **B** | **Atajo del Pillo:** $(2 \cdot 15) / (5 \cdot 4) = 30/20 = 3/2$. |
| **4** | **A** | Paréntesis: $1/2 - 1/4 = 1/4$. Luego $1 - 1/4 = 3/4$. |
| **5** | **C** | Menos por menos es más. Simplificando el 3: $2/4 = 1/2$. |
| **6** | **B** | Es $\frac{1}{2} \cdot \frac{1}{2} = 1/4$. El entero 2 tiene un 1 abajo. |
| **7** | **A** | mcm es 4: $3/4 - 2/4 + 5/4 = 6/4 = 3/2$. |
| **8** | **C** | Numerador: $4/3$. Luego $\frac{4/3}{2/1}$ (Atajo del Pillo) $= 4/6 = 2/3$. |
| **9** | **A** | Mult: $20/15 = 4/3$. Luego $4/3 \div 4/3 = 1$. |
| **10** | **A** | Paréntesis: $1 \cdot 3/4 = 3/4$. Luego $3/4 - 1/4 = 2/4 = 1/2$. |

---

> **Típ:** Si en la pregunta 2 multiplicaste primero, caíste en la trampa de la jerarquía. Multiplicación y División son "hermanos", se resuelven por orden de llegada (izquierda a derecha).
""")
