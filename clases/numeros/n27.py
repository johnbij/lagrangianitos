import streamlit as st


def render_N27():
    st.markdown("""## N27: Reparto Proporcional Directo - ¿Cómo dividimos la torta?

---

### 🏛️ Contexto Histórico: El Código de Hammurabi y la Equidad

Desde las primeras civilizaciones en Mesopotamia, el reparto de bienes no era al azar. En el **Código de Hammurabi**, ya se establecían reglas de proporcionalidad para dividir cosechas o pagar deudas según el aporte de cada ciudadano. Si un agricultor ponía más bueyes para la labranza, su parte de la cosecha debía ser mayor en una razón exacta. Este concepto de "justicia aritmética" es lo que hoy usamos para que nadie reciba ni un peso más ni un peso menos de lo que le corresponde según su esfuerzo o inversión.

---

<div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1565C0; margin-top: 0;">¿Qué es el Reparto Proporcional Directo?</h2>
    Repartir una cantidad total <b>S</b> en partes directamente proporcionales a ciertos números <i>a, b, c...</i> significa que a mayor índice, mayor es la tajada.
    <br><br>
    <blockquote><b>Regla de Oro:</b> Si tu índice de participación es el doble, recibes el doble.</blockquote>
</div>



### 🛡️ El Algoritmo de Reparto (Método k)
Para no fallar y asegurar que el reparto sea exacto, sigue esta estructura:

1.  **Asignar la constante:** Si las partes son proporcionales a $n_1, n_2$ y $n_3$, las partes reales que buscaremos son $n_1k, n_2k$ y $n_3k$.
2.  **Plantear la Suma Total:** La suma de todas las partes debe ser igual al total a repartir ($S$). \\
    $(n_1 + n_2 + n_3) \\cdot k = S$
3.  **Calcular k:** $k = \\frac{S}{\\sum n_i}$ (Es el valor de "una parte" del total).
4.  **Repartir:** Multiplicas $k$ por cada índice original para obtener los valores reales.

### 🛡️ Reparto con índices fraccionarios
Si te dan índices como $1/2$ y $1/3$, trabajar con decimales es el camino al error.

--------------
**Típ:** Amplifica todos los índices por el **Mínimo Común Múltiplo (MCM)** de los denominadores. Así trabajarás con números enteros y el reparto será mucho más rápido y exacto. La proporción se mantiene idéntica.

---

"La justicia es una proporción constante entre el mérito y la recompensa."  
— **Montesquieu**""", unsafe_allow_html=True)
    st.markdown("---")
    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: Reparto Proporcional Directo

**E01. Reparto de bonos por antigüedad.** Se reparte un bono de \\$600.000 entre dos empleados de forma directamente proporcional a sus años de servicio: 2 y 4 años.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Definir partes con $k$ | $2k$ y $4k$ |
| 2 | Sumar e igualar al total | $2k + 4k = 600.000 \\implies 6k = 600.000$ |
| 3 | Hallar $k$ | $k = 100.000$ |
| 4 | Calcular partes reales | $E_1: \\$200.000$, $E_2: \\$400.000$ |

**E02. Reparto de tres partes (Dulces).** Se dividen 1.200 caramelos entre tres niños de forma proporcional a sus edades: 5, 7 y 8 años. ¿Cuántos recibe el mayor?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Definir índices | $5k, 7k, 8k$ |
| 2 | Sumar e igualar | $(5+7+8)k = 1.200 \\implies 20k = 1.200$ |
| 3 | Hallar $k$ | $k = 60$ |
| 4 | Calcular parte del mayor | $8 \\cdot 60 = 480$ caramelos |

**E03. Hallar el total a partir de una parte.** En un reparto proporcional a 3, 5 y 8, la parte menor recibió \\$15.000. ¿Cuál era el monto total repartido?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar la parte menor | $3k = 15.000$ |
| 2 | Hallar $k$ | $k = 5.000$ |
| 3 | Calcular suma de índices | $3+5+8 = 16$ |
| 4 | Calcular total ($16k$) | $16 \\cdot 5.000 = \\$80.000$ |

**E04. Reparto con fracciones (Uso del Típ).** Repartir 700 unidades proporcionalmente a $1/2$ y $2/3$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Hallar MCM de 2 y 3 | MCM = 6 |
| 2 | Amplificar índices | $1/2 \\cdot 6 = 3$ ; $2/3 \\cdot 6 = 4$ |
| 3 | Plantear con índices enteros | $3k + 4k = 700 \\implies 7k = 700$ |
| 4 | Hallar partes | $k = 100 \\implies$ Partes: 300 y 400 |

**E05. Diferencia entre beneficiarios.** Se reparte una ganancia proporcional a 4 y 9. Si el que más recibió obtuvo \\$100.000 más que el otro, ¿cuánto recibió el menor?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Plantear la diferencia | $9k - 4k = 100.000$ |
| 2 | Hallar $k$ | $5k = 100.000 \\implies k = 20.000$ |
| 3 | Calcular parte menor | $4 \\cdot 20.000 = \\$80.000$ |
| 4 | Calcular parte mayor | $9 \\cdot 20.000 = \\$180.000$ |""")
    with st.expander("❓ Cuestionario N27", expanded=False):
        st.markdown("""# ❓ Cuestionario N27: Reparto Proporcional Directo

**1. Si se reparten \\$800.000 en razón $3 : 5$, ¿cuánto recibe la parte menor?** \\
A) 300.000 \\
B) 500.000 \\
C) 400.000 \\
D) 150.000

**2. Se dividen 240 puntos proporcionalmente a 1, 2 y 5. ¿Cuántos puntos corresponden a la parte más grande?** \\
A) 150\\
B) 120\\
C) 180\\
D) 30

**3. En un reparto proporcional a 2, 4 y 6, la parte intermedia recibió 40 objetos. ¿Cuál es el valor de k?** \\
A) 10\\
B) 20\\
C) 5\\
D) 12

**4. Tres socios invierten \\$1, \\$4 y \\$5 millones. Si la ganancia total es \\$2.000.000, ¿cuánto recibe el que menos invirtió?** \\
A) 200.000\\
B) 100.000\\
C) 400.000\\
D) 500.000

**5. Si se reparten 900 metros de cable proporcionalmente a los números 2, 3 y 4, ¿cuánto mide el trozo más largo?** \\
A) 400 m\\
B) 300 m\\
C) 450 m\\
D) 200 m

**6. Un premio de \\$150.000 se reparte entre dos ganadores en razón $2 : 3$. ¿Cuál es la diferencia de dinero entre ambos?** \\
A) 30.000\\
B) 60.000\\
C) 90.000\\
D) 50.000

**7. En un reparto proporcional a 5 y 8, la parte mayor es \\$64.000. ¿Cuál es el total repartido?** \\
A) 104.000\\
B) 40.000\\
C) 120.000\\
D) 80.000

**8. Al repartir una herencia proporcionalmente a las edades 10, 15 y 25 años, el total de índices es:** \\
A) 50\\
B) 40\\
C) 25\\
D) 60

**9. Se reparte una cantidad en razón $1/3 : 1/5$. Si el total es 320, ¿cuánto recibe el índice $1/3$ (índice mayor)?** \\
A) 200\\
B) 120\\
C) 160\\
D) 100

**10. Tres camiones transportan 600 toneladas. El primero hace 3 viajes, el segundo 5 viajes y el tercero 7 viajes. ¿Cuántas toneladas transportó el segundo?** \\
A) 200 ton\\
B) 120 ton\\
C) 280 ton\\
D) 150 ton""")
    with st.expander("✅ Pauta - N27", expanded=False):
        st.markdown("""# ✅ Pauta - Cuestionario N27

1. **A.** $3k + 5k = 800.000 \\implies 8k = 800.000 \\implies k = 100.000$. Menor: $3k = 300.000$.
2. **A.** $1k+2k+5k = 240 \\implies 8k = 240 \\implies k = 30$. Mayor: $5k = 150$.
3. **A.** La intermedia es $4k$. Si $4k = 40 \\implies k = 10$.
4. **A.** Suma de índices: $1+4+5 = 10$. $10k = 2.000.000 \\implies k = 200.000$. Menor ($1k$): $200.000$.
5. **A.** $2k+3k+4k = 900 \\implies 9k = 900 \\implies k = 100$. Largo: $4 \\cdot 100 = 400$.
6. **A.** $2k+3k=150.000 \\implies 5k=150.000 \\implies k=30.000$. Partes: 60k y 90k. Diferencia: 30k.
7. **A.** $8k = 64.000 \\implies k = 8.000$. Total ($13k$): $13 \\cdot 8.000 = 104.000$.
8. **A.** Suma de los índices: $10 + 15 + 25 = 50$.
9. **A.** MCM(15). Índices: $5$ y $3$. $8k = 320 \\implies k = 40$. Parte $1/3$ (índice 5): $5 \\cdot 40 = 200$.
10. **A.** $3k+5k+7k = 600 \\implies 15k = 600 \\implies k = 40$. Segundo ($5k$): $200$ toneladas.""")