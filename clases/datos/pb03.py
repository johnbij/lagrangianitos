import streamlit as st


def render_PB03():
    st.title("PB03: Probabilidad Compuesta — Eventos Dependientes e Independientes")

    st.markdown(r"""
### 🛡️ 1. El Portal: Cuando los Eventos se Combinan

En muchas situaciones reales no ocurre un solo evento, sino una **secuencia** de eventos. ¿Qué probabilidad hay de sacar dos ases seguidos de una baraja? La respuesta depende de si el primer evento **afecta** o no al segundo. Este concepto es central en la PAES y se trabaja con diagramas de árbol y las reglas de multiplicación.

---

### 🛡️ 2. Eventos Independientes

Dos eventos $A$ y $B$ son **independientes** si la ocurrencia de uno **no afecta** la probabilidad del otro.

$$P(A \cap B) = P(A) \cdot P(B)$$

**Ejemplo:** Lanzar un dado y luego una moneda:
- $P(\text{dado } = 3) = \frac{1}{6}$, $P(\text{cara}) = \frac{1}{2}$.
- $P(3 \text{ y cara}) = \frac{1}{6} \cdot \frac{1}{2} = \frac{1}{12}$.

> El resultado del dado no cambia la probabilidad de la moneda.

---

### 🛡️ 3. Eventos Dependientes

Dos eventos son **dependientes** si la ocurrencia de uno **sí modifica** la probabilidad del otro. Se usa la probabilidad condicional.

$$P(A \cap B) = P(A) \cdot P(B|A)$$

---

### 🛡️ 4. Probabilidad Condicional

La probabilidad de $A$ **dado que** ya ocurrió $B$ es:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

**Interpretación:** Restringimos el espacio muestral a los casos donde $B$ ya ocurrió, y dentro de esos, contamos los que también cumplen $A$.

---

### 🛡️ 5. Con Reposición vs Sin Reposición

| Situación | Tipo | ¿Qué cambia? |
| :--- | :--- | :--- |
| **Con reposición** | Independiente | El elemento se devuelve → las probabilidades no cambian |
| **Sin reposición** | Dependiente | El elemento no se devuelve → el total disminuye y la composición puede cambiar |

**Ejemplo:** Urna con $3$ rojas y $2$ azules.

| Extracción | Con reposición | Sin reposición |
| :--- | :--- | :--- |
| $P(\text{1.ª roja})$ | $\frac{3}{5}$ | $\frac{3}{5}$ |
| $P(\text{2.ª roja})$ | $\frac{3}{5}$ | $\frac{2}{4} = \frac{1}{2}$ |
| $P(\text{ambas rojas})$ | $\frac{3}{5} \cdot \frac{3}{5} = \frac{9}{25}$ | $\frac{3}{5} \cdot \frac{2}{4} = \frac{6}{20} = \frac{3}{10}$ |

---

### 🛡️ 6. Diagrama de Árbol

El **diagrama de árbol** es una herramienta visual para organizar todos los resultados posibles de un experimento compuesto:

1. Cada **rama** representa un resultado posible.
2. Cada rama se etiqueta con su probabilidad.
3. La probabilidad de un **camino completo** se obtiene multiplicando las probabilidades de sus ramas.
4. La probabilidad total de un evento se obtiene **sumando** las probabilidades de todos los caminos que lo incluyen.

**Ejemplo simplificado (2 extracciones sin reposición, $3R$ y $2A$):**

```
              ┌── R (2/4) → RR: 3/5 · 2/4 = 6/20
         R (3/5)
              └── A (2/4) → RA: 3/5 · 2/4 = 6/20
         
              ┌── R (3/4) → AR: 2/5 · 3/4 = 6/20
         A (2/5)
              └── A (1/4) → AA: 2/5 · 1/4 = 2/20
```

**Verificación:** $\frac{6+6+6+2}{20} = \frac{20}{20} = 1$ ✅.

---

> *"La suerte no existe; lo que llamas suerte es el cuidado en los detalles."*
> — **Voltaire**
""")

    with st.expander("🚀 Guía de Ejemplos Paso a Paso: Carpintería PB03", expanded=False):
        st.markdown(r"""
### E01: Eventos independientes — dado y moneda

**Situación:** Se lanza un dado y una moneda. ¿Cuál es la probabilidad de obtener un número par **y** cara?

**La Carpintería:**
1. $P(\text{par}) = \frac{3}{6} = \frac{1}{2}$.
2. $P(\text{cara}) = \frac{1}{2}$.
3. Son **independientes** (un experimento no afecta al otro).
4. $P(\text{par y cara}) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.

---

### E02: Sin reposición — bolas en una urna

**Situación:** Una urna tiene $4$ bolas verdes y $6$ rojas. Se extraen $2$ bolas **sin reposición**. ¿Probabilidad de que ambas sean verdes?

**La Carpintería:**
1. $P(\text{1.ª verde}) = \frac{4}{10} = \frac{2}{5}$.
2. Después de sacar una verde, quedan $3$ verdes de $9$ bolas.
3. $P(\text{2.ª verde} | \text{1.ª verde}) = \frac{3}{9} = \frac{1}{3}$.
4. $P(\text{ambas verdes}) = \frac{2}{5} \cdot \frac{1}{3} = \frac{2}{15}$.

---

### E03: Probabilidad condicional

**Situación:** En un curso de $30$ alumnos, $18$ aprobaron matemáticas, $12$ aprobaron ciencias y $8$ aprobaron ambas. Si un alumno aprobó matemáticas, ¿cuál es la probabilidad de que también haya aprobado ciencias?

**La Carpintería:**
1. $P(M) = \frac{18}{30}$, $P(C) = \frac{12}{30}$, $P(M \cap C) = \frac{8}{30}$.
2. $P(C|M) = \frac{P(M \cap C)}{P(M)} = \frac{8/30}{18/30} = \frac{8}{18} = \frac{4}{9}$.
3. **Interpretación:** De los $18$ que aprobaron mate, $8$ también aprobaron ciencias → $\frac{8}{18} = \frac{4}{9}$.

---

### E04: Diagrama de árbol completo

**Situación:** Una bolsa tiene $2$ caramelos de menta y $3$ de limón. Se sacan $2$ **sin reposición**. ¿Probabilidad de sacar exactamente $1$ de menta?

**La Carpintería:**
1. Caminos con exactamente $1$ menta: ML y LM.
2. $P(ML) = \frac{2}{5} \cdot \frac{3}{4} = \frac{6}{20}$.
3. $P(LM) = \frac{3}{5} \cdot \frac{2}{4} = \frac{6}{20}$.
4. $P(\text{exactamente 1 menta}) = \frac{6}{20} + \frac{6}{20} = \frac{12}{20} = \frac{3}{5}$.
""")

    with st.expander("❓ Cuestionario PB03: Probabilidad Compuesta", expanded=False):
        st.markdown(r"""
**1. Se lanza una moneda $3$ veces. $P(\text{3 caras}) =$**

A) $\frac{1}{3}$
B) $\frac{3}{8}$
C) $\frac{1}{8}$
D) $\frac{1}{2}$

---

**2. Una urna tiene $5$ bolas rojas y $5$ azules. Se sacan $2$ CON reposición. $P(\text{ambas rojas}) =$**

A) $\frac{1}{4}$
B) $\frac{2}{9}$
C) $\frac{1}{2}$
D) $\frac{5}{10}$

---

**3. Misma urna del problema 2, pero SIN reposición. $P(\text{ambas rojas}) =$**

A) $\frac{1}{4}$
B) $\frac{2}{9}$
C) $\frac{5}{10}$
D) $\frac{4}{9}$

---

**4. Si $P(A) = \frac{1}{3}$ y $P(B|A) = \frac{1}{2}$, entonces $P(A \cap B) =$**

A) $\frac{5}{6}$
B) $\frac{1}{6}$
C) $\frac{2}{3}$
D) $\frac{1}{3}$

---

**5. Dos dados se lanzan. Los resultados son:**

A) Dependientes
B) Independientes
C) Mutuamente excluyentes
D) Complementarios

---

**6. En un diagrama de árbol, la probabilidad de un camino completo se obtiene:**

A) Sumando las probabilidades de las ramas
B) Multiplicando las probabilidades de las ramas
C) Restando las probabilidades
D) Dividiendo las probabilidades

---

**7. De un mazo de $52$ cartas, se sacan $2$ cartas sin reposición. $P(\text{ambas ases}) =$**

A) $\frac{4}{52} \cdot \frac{4}{52}$
B) $\frac{4}{52} \cdot \frac{3}{51}$
C) $\frac{4}{52} \cdot \frac{4}{51}$
D) $\frac{2}{52}$
""")

    with st.expander("🔑 Pauta Técnica PB03: Carpintería de Soluciones", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería Técnica |
| :--- | :---: | :--- |
| **1** | **C** | $P = \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{8}$. Tres lanzamientos independientes. |
| **2** | **A** | Con reposición: $P = \frac{5}{10} \cdot \frac{5}{10} = \frac{1}{4}$. La composición no cambia. |
| **3** | **B** | Sin reposición: $P = \frac{5}{10} \cdot \frac{4}{9} = \frac{20}{90} = \frac{2}{9}$. |
| **4** | **B** | $P(A \cap B) = P(A) \cdot P(B|A) = \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{6}$. |
| **5** | **B** | El resultado de un dado no afecta al otro → independientes. |
| **6** | **B** | Se multiplican las probabilidades a lo largo de las ramas del camino. |
| **7** | **B** | Sin reposición: $\frac{4}{52} \cdot \frac{3}{51}$. Después de sacar un as, quedan $3$ ases entre $51$ cartas. |
""")
