import streamlit as st


def render_N34():
    st.markdown("""## N34: De las Proporciones a las Igualdades (El Puente)

---

### 🏛️ Contexto Histórico: El Arte de la Balanza

Mucho antes de que existieran los libros de matemáticas, los comerciantes en los mercados de Egipto y Babilonia usaban balanzas de platos. Si ponían una pesa de 1 kilo en un lado, debían poner exactamente 1 kilo de grano en el otro para que la barra se mantuviera horizontal. El término "Álgebra" viene del árabe *Al-Jabr*, que significa "restauración" o "completar". Los antiguos entendieron que una **igualdad** es como una balanza: si haces un cambio en un lado, debes hacer el mismo cambio en el otro para no romper el equilibrio. Lo que hemos estado haciendo con las razones es buscar ese equilibrio.

---

### ⚖️ ¿Qué es una Igualdad Matemática?
Hasta ahora, hemos usado razones como $\\frac{x}{10} = 5$. Sin saberlo, ya estabas trabajando con modelos algebraicos. Una igualdad es simplemente una oración matemática que afirma que dos expresiones valen lo mismo.

**Típ:** Imagina que el signo **"="** es el centro de una balanza.
* Si en el lado izquierdo sumas 5, la balanza se inclina.
* Para enderezarla, **debes sumar 5 en el lado derecho**.



---

### 🛡️ Las Reglas del Movimiento (Despeje)
Para encontrar el valor de nuestra incógnita (esa $k$ o esa $x$ que tanto hemos buscado), debemos dejarla sola. Para mover los números de un lado a otro del "=" sin romper la balanza, usamos la **operación inversa**:

1. **Si un número está sumando:** Pasa al otro lado restando.
2. **Si un número está restando:** Pasa al otro lado sumando.
3. **Si un número está multiplicando:** Pasa al otro lado dividiendo.
4. **Si un número está dividiendo:** Pasa al otro lado multiplicando (como hacíamos al resolver $\\frac{x}{4} = 10 \\implies x = 10 \\cdot 4$).

---

### 🛡️ Relación con las Proporciones
¿Te acuerdas de la Proporcionalidad Directa? Teníamos la relación:
$$\\frac{y}{x} = k$$
Si queremos saber cuánto vale $y$, el $x$ que está dividiendo pasa al otro lado multiplicando:
$$y = k \\cdot x$$
¡Eso es! Acabas de transformar una **razón** en un **modelo predictivo**. Todo lo que hemos despejado en los problemas de edades, mezclas y móviles seguía esta misma lógica de equilibrio.

---

### 🛡️ Lenguaje Cotidiano a Lenguaje Matemático
El gran truco para lo que viene es saber traducir las palabras en símbolos:
* **"Un número aumentado en 5"** $\\rightarrow x + 5$
* **"El doble de un número"** $\\rightarrow 2x$
* **"La tercera parte de algo"** $\\rightarrow \\frac{x}{3}$
* **"Es igual a" / "Resulta en"** $\\rightarrow =$

---

"La esencia de las matemáticas no es hacer las cosas simples complicadas, sino hacer las cosas complicadas simples."  
— **S. Gudder**""", unsafe_allow_html=True)
    st.markdown("---")