import streamlit as st


def render_N16():
    st.title("N16: El Orden en los Racionales (ℚ) - La Recta Infinita")

    st.markdown(r"""
### 🏛️ Contexto Histórico: El Infinito entre dos Puntos
A diferencia de los números naturales, donde después del 1 viene el 2, los matemáticos de la **Antigua Grecia** y más tarde los pensadores de la **Edad Media** se dieron cuenta de una propiedad asombrosa de las fracciones: la **Densidad**.

Se descubrió que entre dos números racionales, por muy cerca que estén, siempre es posible encontrar otro número racional (y, de hecho, infinitos más). Esta idea cambió la forma de entender el espacio y el movimiento, permitiendo que la navegación y la astronomía fueran precisas. No se trata solo de contar cosas enteras, sino de entender que el universo se puede dividir infinitamente.

---

### 🧱 Teoría Fundamental: Comparación y Densidad

Para ordenar números racionales en la PAES, existen tres estrategias maestras que no fallan:

1. **Multiplicación Cruzada:** Para comparar $a/b$ y $c/d$, multiplicamos $a \cdot d$ y $b \cdot c$. El resultado mayor indica la fracción mayor.
2. **Igualación de Denominadores:** Convertir ambas fracciones a un común denominador (usando el MCM) y comparar solo los numeradores.
3. **Conversión a Decimal:** Dividir el numerador por el denominador. Es útil cuando las fracciones tienen números muy grandes o poco amigables.

**Propiedad de Densidad:** En $\mathbb{Q}$, siempre existe un número entre otros dos. El "truco" más simple para hallarlo es calcular el promedio entre ambos: $(n_1 + n_2) / 2$.

---

> **Típ:** En la recta numérica, los números negativos funcionan al revés que los positivos. Mientras "más grande" parece el número negativo (ej: $-3/4$ vs $-1/4$), más a la izquierda está y, por lo tanto, es **menor**. ¡No caigas en la trampa visual!
""")

    with st.expander("❓ Cuestionario N16: El Orden en los Racionales", expanded=False):
        st.markdown(r"""
**Responda las siguientes preguntas siguiendo el protocolo de análisis de orden.**

**1. ¿Cuál de las siguientes relaciones de orden es CORRECTA?**
\
A) $1/2 < 1/3$
\
B) $2/5 > 3/7$
\
C) $5/6 < 7/8$
\
D) $3/4 = 9/12$

**2. Si ordenamos de mayor a menor los números $a = 2/3$, $b = 3/4$ y $c = 5/6$, el orden es:**
\
A) $c, b, a$
\
B) $a, b, c$
\
C) $b, c, a$
\
D) $c, a, b$

**3. ¿Cuál de los siguientes números se encuentra entre $1/4$ y $1/3$?**
\
A) $2/12$
\
B) $5/12$
\
C) $7/24$
\
D) $1/5$

**4. En la recta numérica, el número racional $-7/2$ se ubica entre:**
\
A) $-3$ y $-4$
\
B) $-7$ y $-8$
\
C) $-2$ y $-3$
\
D) $3$ y $4$

**5. ¿Cuál es la fracción más pequeña de este grupo? $\{1/2, 2/5, 3/10, 1/4\}$**
\
A) $1/2$
\
B) $2/5$
\
C) $3/10$
\
D) $1/4$

**6. Al comparar $x = -0,5$ con $y = -2/3$, se puede afirmar que:**
\
A) $x < y$
\
B) $x > y$
\
C) $x = y$
\
D) No se pueden comparar.

**7. ¿Qué número es mayor que $-1/5$?**
\
A) $-1/4$
\
B) $-1/6$
\
C) $-1/2$
\
D) $-1$

**8. ¿Cuál es el promedio exacto entre $1/2$ y $3/4$?**
\
A) $1$
\
B) $5/8$
\
C) $4/6$
\
D) $2/3$

**9. Si $a < 0$ y $b > 0$, entonces en la recta numérica:**
\
A) $a$ está a la derecha de $b$.
\
B) $b$ está a la izquierda del origen.
\
C) $a$ está a la izquierda de $b$.
\
D) Ambos están al mismo lado del cero.

**10. Si sumamos un número racional con su inverso aditivo, el resultado en la recta numérica se ubica en:**
\
A) El origen (cero).
\
B) A la derecha del cero.
\
C) A la izquierda del cero.
\
D) Depende del valor del número.
""")
