import streamlit as st


def render_N32():
    st.markdown("""## N32: Proporcionalidad Inversa - El Efecto Balancín

---

### 🏛️  Contexto Histórico: La Optimización del Tiempo

Desde la construcción de las calzadas romanas hasta la logística de las grandes fábricas de la Revolución Industrial, la proporcionalidad inversa ha sido la clave de la eficiencia. Los ingenieros del siglo XIX entendieron que el tiempo no es una variable fija, sino que depende de la fuerza que le apliques. Si querían terminar un túnel ferroviario en la mitad del tiempo, sabían que la relación no era sumar un par de hombres, sino duplicar la potencia de trabajo. Esta "ley de compensación" es la que permite que hoy entendamos que para mantener un resultado constante, si un factor flaquea, el otro debe crecer obligatoriamente.

---

<div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1565C0; margin-top: 0;">🛡️ Definición: Los Rivales</h2>
    Dos variables $x$ e $y$ son <b>inversamente proporcionales</b> si funcionan como un balancín: para que el sistema esté en equilibrio, si una sube, la otra debe bajar en la misma escala.
    <br><br>
    <ul>
        <li>Si una variable se <b>multiplica por 2</b>, la otra se <b>divide por 2</b>.</li>
        <li>Si una se reduce a la <b>tercera parte</b>, la otra se <b>triplica</b>.</li>
    </ul>
    <b>Regla de Oro:</b> Se mueven en direcciones opuestas pero con la misma intensidad proporcional.
</div>

### 🛡️ La Constante de Proporcionalidad ($k$)
A diferencia de la directa, aquí lo que se mantiene siempre igual es el **PRODUCTO** (la multiplicación) entre las variables. Ese valor $k$ representa la "tarea total" o el "objetivo":

$$x \\cdot y = k \\quad \\implies \\quad y = \\frac{k}{x}$$

* **$k$** es la "llave" del ejercicio. Si multiplicas un par de datos $(x, y)$, obtienes $k$ y puedes despejar cualquier otra incógnita.
* **Típ:** Piensa en $k$ como el trabajo total que hay que hacer (ej: metros cuadrados por pintar, hoyos por cavar).

### 🛡️ Representación Gráfica: La Hipérbola
¡Mucho ojo aquí! El gráfico **NUNCA es una línea recta**.
* Es una curva decreciente llamada **hipérbola**.
* Se acerca a los ejes $X$ e $Y$ pero jamás los toca (asíntotas).
* **Típ PAES:** Si ves una recta hacia abajo, es una función afín/lineal, **NO** es proporción inversa.



### 🛡️ Identificación en Tablas
Para pillar la inversa, multiplica cada par. Si el resultado es siempre el mismo, es una "balanza" perfecta.

| $x$ (Obreros) | $y$ (Días) | $x \\cdot y = k$ |
| :--- | :--- | :--- |
| 2 | 30 | $2 \\cdot 30 = 60$ |
| 4 | 15 | $4 \\cdot 15 = 60$ |
| 10 | 6 | $10 \\cdot 6 = 60$ |

---

"El equilibrio es la clave de la perfección."  
— **Anónimo**""", unsafe_allow_html=True)
    st.markdown("---")
    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: El Balancín Matemático

**E01. Encontrar valores faltantes usando la constante $k$.**
Si $x$ e $y$ son inversamente proporcionales, y cuando $x = 6$, $y = 10$. ¿Cuánto vale $y$ si $x = 15$?
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Calcular la constante $k$ (Multiplicar) | $k = 6 \\cdot 10 = 60$ |
| 2 | Plantear la ecuación con el nuevo $x$ | $15 \\cdot y = 60$ |
| 3 | Resultado final (Dividir) | $y = 4$ |

**E02. Identificar si una tabla es Inversa.**
| x | 3 | 5 | 15 |
| :--- | :--- | :--- | :--- |
| y | 20 | 12 | 4 |
**Análisis:** $3 \\cdot 20 = 60$; $5 \\cdot 12 = 60$; $15 \\cdot 4 = 60$. Como el producto es constante ($k=60$), es **Inversa**.

**E03. Problema de aplicación PAES: Los Pintores.**
3 pintores tardan 12 días en pintar un edificio. ¿Cuántos pintores se necesitan para terminar en solo 4 días?
| Magnitud A (Pintores) | Magnitud B (Días) | Producto ($k$) |
| :--- | :--- | :--- |
| 3 | 12 | $3 \\cdot 12 = 36$ |
| $x$ | 4 | $x \\cdot 4 = 36$ |
**Resultado:** Se necesitan 9 pintores ($36/4$).

**E04. Reconocimiento gráfico y puntos.**
Un gráfico de proporción inversa pasa por el punto $(4, 9)$. ¿Pasa también por el punto $(12, 3)$?
**Análisis:** Calculamos $k = 4 \\cdot 9 = 36$.
* Verificamos el segundo punto: $12 \\cdot 3 = 36$.
**Resultado:** Sí, ambos pertenecen a la misma proporción inversa.

**E05. Velocidad y Tiempo.**
Un bus viaja a 80 km/h y tarda 3 horas en llegar. Si aumenta su velocidad a 120 km/h, ¿cuánto tardará?
**Análisis:** $k = 80 \\cdot 3 = 240$ (esta es la distancia total).
$120 \\cdot \\text{tiempo} = 240 \\implies \\text{tiempo} = 2$ horas.""")
    with st.expander("❓ Cuestionario N32", expanded=False):
        st.markdown("""# ❓ Cuestionario N32: Proporcionalidad Inversa

**1. Dos variables son inversamente proporcionales cuando:** \\
A) Si una aumenta al doble, la otra aumenta al doble. \\
B) Si una aumenta al triple, la otra disminuye a la tercera parte. \\
C) Su cociente (división) es siempre constante. \\
D) Su gráfico es una línea recta descendente.

**2. Si $x$ e $y$ son inversamente proporcionales y $k = 120$, ¿cuánto vale $y$ si $x = 30$?** \\
A) 4 \\
B) 3.600 \\
C) 90 \\
D) 0,25

**3. El gráfico de una proporcionalidad inversa se denomina:** \\
A) Parábola \\
B) Línea Recta \\
C) Hipérbola \\
D) Elipse

**4. Si 4 máquinas envasan un pedido en 6 horas, ¿cuántas máquinas se necesitan para hacerlo en 3 horas?** \\
A) 2 máquinas \\
B) 8 máquinas \\
C) 12 máquinas \\
D) 6 máquinas

**5. En la proporcionalidad inversa, la constante $k$ se obtiene mediante:** \\
A) La suma de las variables. \\
B) El producto de las variables. \\
C) El cociente de las variables. \\
D) La raíz cuadrada de las variables.

**6. Si un grifo con un caudal de 10 litros/min tarda 12 minutos en llenar un balde, ¿cuánto tardará un grifo de 15 litros/min?** \\
A) 18 minutos \\
B) 10 minutos \\
C) 8 minutos \\
D) 6 minutos

**7. ¿Cuál de los siguientes puntos pertenece a la misma proporción inversa que el punto (2, 50)?** \\
A) (4, 100) \\
B) (10, 10) \\
C) (5, 20) \\
D) (25, 2)

**8. Si $y$ es inversamente proporcional a $x$, y cuando $x = 8$, $y = 3$. ¿Cuánto vale $x$ si $y = 12$?** \\
A) 2 \\
B) 32 \\
C) 4 \\
D) 1

**9. Al observar un gráfico de una curva que baja y se acerca a los ejes sin tocarlos, podemos decir que:** \\
A) Es una proporción directa. \\
B) No hay relación entre las variables. \\
C) Es una proporción inversa. \\
D) Es una función constante.

**10. Si 10 obreros tardan 20 días en cavar una zanja, ¿cuántos días tardarán 20 obreros?** \\
A) 40 días \\
B) 10 días \\
C) 5 días \\
D) 15 días""")
    with st.expander("✅ Pauta - N32", expanded=False):
        st.markdown("""# ✅ Pauta Explicativa - Cuestionario N32

1. **B.** Definición de inversa: cambio opuesto en la misma proporción.
2. **A.** Usamos $x \\cdot y = k \\implies 30 \\cdot y = 120 \\implies y = 120/30 = 4$.
3. **C.** La hipérbola es la forma geométrica que representa la función $y = k/x$.
4. **B.** $k = 4 \\cdot 6 = 24$. Si queremos tiempo 3: $x \\cdot 3 = 24 \\implies x = 8$.
5. **B.** El producto constante es la firma de la proporción inversa.
6. **C.** $k = 10 \\cdot 12 = 120$. Con nuevo caudal: $15 \\cdot t = 120 \\implies t = 120/15 = 8$.
7. **B.** Calculamos $k = 2 \\cdot 50 = 100$. Verificamos puntos: $10 \\cdot 10 = 100$. El resto no cumple.
8. **A.** $k = 8 \\cdot 3 = 24$. Si $y = 12$, entonces $x \\cdot 12 = 24 \\implies x = 2$.
9. **C.** Es la descripción visual de la hipérbola en el primer cuadrante.
10. **B.** Al doble de obreros, la mitad de tiempo. $20/2 = 10$.""")