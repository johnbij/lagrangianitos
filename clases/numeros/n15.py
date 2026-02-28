import streamlit as st


def render_N15():
    st.title("N15: Herramientas de Inspección - El ADN de los Números")

    st.markdown(r"""
### 🏛️ 1. Contexto Histórico: El Tamiz de Eratóstenes y los Ladrillos del Universo
Hace más de 2.200 años, Eratóstenes (el mismo que midió la Tierra con una sombra) se dio cuenta de que había números que eran "especiales". Algunos números se podían desarmar en otros más chicos, pero otros eran como átomos: imposibles de dividir. A estos los llamó **Números Primos**.

En el taller de la matemática, los números primos son los **ladrillos fundamentales**. Todo número que no es primo (compuesto) es simplemente una construcción hecha de primos. Entender esto es tener "visión de rayos X": cuando ves un 60, un maestro no ve un 60, ve $2 \cdot 2 \cdot 3 \cdot 5$. Esta técnica permitió a los antiguos simplificar cálculos astronómicos que hoy nos parecerían imposibles.

---

### 🛡️ 9.D.1 El Teorema Fundamental: Factorización Prima
Cualquier número entero mayor que 1 puede expresarse como un producto único de números primos. Es su **huella digital**.

### 🛠️ Cómo desarmar el motor (Árbol de Factores):
Para encontrar los factores primos de un número (como el 40), lo dividimos sucesivamente por los primos más chicos (2, 3, 5, 7...):
* 40 es $2 \cdot 20$
* 20 es $2 \cdot 10$
* 10 es $2 \cdot 5$
* **Resultado:** $40 = 2^3 \cdot 5$

**¿Para qué sirve esto?** Para simplificar fracciones. Si tienes $\frac{40}{60}$, y sabes que $60 = 2^2 \cdot 3 \cdot 5$, solo "tallas" los factores que se repiten arriba y abajo y llegas a $\frac{2}{3}$ sin dudar.

---

### 🛡️ 9.D.2 Las Reglas de Inspección (Divisibilidad)
No pierdas tiempo dividiendo. Usa estos atajos de "maestro pillo" para saber si el resto será cero:

1. **Por 2:** Si termina en cifra par (0, 2, 4, 6, 8).
2. **Por 3:** Si al **sumar sus dígitos**, el resultado está en la tabla del 3.
    * *Ejemplo:* 123 $\rightarrow 1+2+3 = 6$. ¡Es divisible por 3!
3. **Por 4:** Si sus últimas dos cifras son 00 o un múltiplo de 4.
4. **Por 5:** Si termina en 0 o 5.
5. **Por 6:** Si es divisible por 2 y por 3 al mismo tiempo.
6. **Por 9:** Si al sumar sus dígitos, el resultado es múltiplo de 9.
7. **Por 10:** Si termina en 0.

---

### 🛡️ 9.D.3 El MCD y el mcm: La Gestión de Repuestos
* **MCD (Máximo Común Divisor):** Es el molde más grande que cabe exactamente en varios números. Se obtiene multiplicando los factores primos comunes con su **menor** exponente.
* **mcm (mínimo común múltiplo):** Es el primer número donde se encuentran varios múltiplos. Se obtiene multiplicando todos los factores (comunes y no comunes) con su **mayor** exponente.

---

### 🛡️ 9.D.4 La Densidad Racional: El espacio infinito
A diferencia de los números naturales, donde entre el 5 y el 6 no hay nada, en los racionales **siempre hay espacio**.
Si tienes $\frac{1}{2}$ y $\frac{3}{4}$, siempre puedes encontrar un número justo al medio (el promedio).
**Técnica:** Sumas las fracciones y divides por 2. Esto demuestra que los números racionales son "densos": no importa cuánto te acerques, siempre hay más números en medio.

> **Típ:** Si en la PAES te piden simplificar una fracción gigante, no empieces a dividir a lo loco. Suma los dígitos para ver si es divisible por 3 o 9, o mira la última cifra. Usa las reglas de inspección primero; ahorran tiempo y errores de cálculo.

---

> "Los números primos son los átomos de la aritmética, las piezas indivisibles con las que se construye toda la realidad numérica".
> — **Marcus du Sautoy**
""")
