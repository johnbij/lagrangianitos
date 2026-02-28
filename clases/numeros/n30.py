import streamlit as st


def render_N30():
    st.markdown("""## N30: El Mapa de las Proporciones - ¿Cómo se relacionan las cosas?

---

### 🏛️ Contexto Histórico: La Lógica de la Anticipación

Imagina que tienes que organizar un asado para tu curso. Si no entiendes las proporciones, estás frito. Tienes que tomar tres decisiones rápidas:

1. **Si llegan más amigos**, ¿necesitas más carne? Obvio. Eso es **Proporcionalidad Directa** (Crecen juntas).
2. **Si llegan más amigos a ayudar**, ¿se demoran menos en prender el fuego? Sí. Eso es **Proporcionalidad Inversa** (Uno sube, el otro baja).
3. **Si tienes más amigos, que traen más parrillas y cocinan más horas...** ¿cuánta carne puedes tirar? Eso es **Proporcionalidad Compuesta** (Varios factores a la vez).

Dominar esto permitió que los antiguos repartieran raciones de comida en ejércitos gigantes sin que nadie muriera de hambre y que los ingenieros modernos calculen cuánta bencina necesita un cohete para llegar a Marte. La proporción es la herramienta que te permite predecir el resultado de cualquier cambio.

---

<div style="background-color: #E3F2FD; border-left: 8px solid #1E88E5; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1565C0; margin-top: 0;"> 🛡️ Los Tres Caminos: ¿Amigos u Enemigos?</h2>
    Para resolver cualquier ejercicio, primero debes clasificar la relación. No uses fórmulas antes de saber en qué camino estás:
    <br><br>
    <b>1. Proporcionalidad Directa (Partners):</b>
    Hacen lo mismo. Si una variable se duplica, la otra se duplica. Si una baja a la mitad, la otra también.
    <ul>
        <li><b>Lógica:</b> Se mantienen unidas porque su división siempre da el mismo número ($\\frac{y}{x} = k$).</li>
        <li><b>Ejemplo:</b> Más kilómetros recorridos $\\rightarrow$ Más gasto de bencina.</li>
    </ul>
    <br>
    <b>2. Proporcionalidad Inversa (Rivales):</b>
    Hacen lo contrario. Si una variable se duplica, la otra se reduce a la mitad. Son como un balancín.
    <ul>
        <li><b>Lógica:</b> Se mantienen unidas porque su multiplicación siempre da el mismo número ($x \\cdot y = k$).</li>
        <li><b>Ejemplo:</b> Más velocidad $\\rightarrow$ Menos tiempo de viaje.</li>
    </ul>
    <br>
    <b>3. Proporcionalidad Compuesta (Multiverso):</b>
    Es un sistema con 3 o más variables. Es como la vida real: depende de cuánta gente haya, cuánto tiempo trabajen y qué tan rápido sean.
</div>



### 🛡️ El Test de la Verdad
**Típ:** Antes de anotar números, haz la prueba del "Doble":
* "¿Si pongo el <b>doble</b> de obreros, el muro será el <b>doble</b> de largo?" $\\rightarrow$ Sí, entonces es <b>Directa</b>.
* "¿Si pongo el <b>doble</b> de obreros, el tiempo será el <b>doble</b>?" $\\rightarrow$ No, será la mitad, entonces es <b>Inversa</b>.

---

"La simplicidad es la forma final de la sofisticación."  
— **Leonardo da Vinci**""", unsafe_allow_html=True)
    st.markdown("---")
    with st.expander("📝 Guía de Ejemplos", expanded=False):
        st.markdown("""## 📝 Guía de Ejemplos: El Radar de Proporciones

**E01. Clasificar según la "Lógica del Asado" (Directa, Inversa o Compuesta).**
| Situación Real | Análisis: ¿Qué pasa si duplico la primera? | Tipo de Proporción |
| :--- | :--- | :--- |
| Cantidad de invitados y cantidad de choripanes. | Al doble de amigos, necesito el doble de choripanes. | **Directa** |
| Cantidad de parrilleros y tiempo en tener la carne lista. | Al doble de parrilleros, demoramos la mitad del tiempo. | **Inversa** |
| Dinero recolectado y cantidad de carne que se puede comprar. | Al doble de plata, compro el doble de carne. | **Directa** |
| Amigos, presupuesto y días que dura el paseo. | Hay **3 factores** (Gente, Lucas, Tiempo). | **Compuesta** |
| Velocidad del viento y tiempo de secado de la ropa. | A más viento, menos tiempo de secado. | **Inversa** |

**E02. Identificación por "Firma Matemática" (Tablas).**
¿Cómo saber qué proporción es solo mirando los números?
* **Si la División ($y/x$) es constante:** Es **Directa**. (Ej: $10/2=5$, $20/4=5$).
* **Si la Multiplicación ($x \\cdot y$) es constante:** Es **Inversa**. (Ej: $2 \\cdot 20=40$, $4 \\cdot 10=40$).

**E03. Ejemplo de Identificación Gráfica.**

* La **Directa** siempre será una línea recta que nace desde el cero $(0,0)$.
* La **Inversa** siempre será una curva que baja (hipérbola) buscando los ejes pero sin tocarlos.

**E04. El caso de la Compuesta.**
"5 obreros construyen 2 casas en 30 días".
**Típ:** Si ves más de dos magnitudes (Obreros, Casas, Días), no le des más vueltas: es **Compuesta**.""")
    with st.expander("❓ Cuestionario N30", expanded=False):
        st.markdown("""# ❓ Cuestionario N30: El Mapa de las Proporciones

**1. Si al doble de "A" le corresponde el doble de "B", ¿qué camino estamos siguiendo?** \\
A) Proporción Inversa \\
B) Proporción Directa \\
C) Proporción Compuesta \\
D) No hay proporción

**2. ¿Cuál de estas situaciones representa una Proporción Inversa?** \\
A) Kilos de pan y el precio total a pagar. \\
B) Velocidad de un auto y el tiempo que tarda en llegar. \\
C) Cantidad de bencina y distancia recorrida. \\
D) Número de páginas de un libro y su peso.

**3. En una fiesta, si llegan más invitados y la comida se acaba más rápido (menos tiempo), la relación es:** \\
A) Directa \\
B) Inversa \\
C) Compuesta \\
D) Constante

**4. Si el gráfico de una relación es una línea recta que sale del origen (0,0), es una:** \\
A) Proporción Directa \\
B) Proporción Inversa \\
C) Proporción Compuesta \\
D) Proporción Nula

**5. ¿Qué operación define a la Proporción Inversa entre dos variables?** \\
A) Su suma es constante. \\
B) Su resta es constante. \\
C) Su producto (multiplicación) es constante. \\
D) Su cociente (división) es constante.

**6. Si 3 máquinas imprimen 500 libros en 2 horas, la relación entre máquinas, libros y horas es:** \\
A) Simple Directa \\
B) Simple Inversa \\
C) Compuesta \\
D) Lineal

**7. En la Proporción Directa, si una variable disminuye a la cuarta parte, la otra:** \\
A) Se cuadruplica \\
B) Disminuye a la cuarta parte \\
C) Se mantiene igual \\
D) Aumenta el doble

**8. Si en una tabla $x \\cdot y = 100$ para todos los valores, el gráfico será:** \\
A) Una línea recta ascendente. \\
B) Una línea recta descendente. \\
C) Una curva (hipérbola). \\
D) Un círculo.

**9. ¿Cuál de las siguientes constantes ($k$) pertenece a una Proporción Directa?** \\
A) $k = x \\cdot y$ \\
B) $k = y / x$ \\
C) $k = x + y$ \\
D) $k = x - y$

**10. "Si contrato al doble de maestros, la casa estará lista en la mitad del tiempo". Esta frase describe una:** \\
A) Proporción Directa \\
B) Proporción Inversa \\
C) Proporción Compuesta \\
D) Relación Aditiva""")
    with st.expander("✅ Pauta - N30", expanded=False):
        st.markdown("""# ✅ Pauta - Cuestionario N30

1. **B.** Relación de "compañerismo": lo que le pasa a una, le pasa a la otra. Eso es Directa.
2. **B.** A más velocidad, menos tiempo. Una sube y la otra baja. Es Inversa.
3. **B.** Sigue la lógica del asado: más gente, menos dura la comida (Inversa).
4. **A.** Visualmente, la directa siempre es una recta que arranca desde el origen.
5. **C.** La firma matemática de la inversa es que $x \\cdot y$ siempre da el mismo resultado ($k$).
6. **C.** Al haber 3 variables (Máquinas, Libros, Horas), el sistema es Compuesto.
7. **B.** En la directa son "partners": si una baja a la cuarta parte, la otra le copia.
8. **C.** El gráfico de la inversa ($x \\cdot y = k$) siempre es una curva llamada hipérbola.
9. **B.** La constante de la directa se encuentra dividiendo la variable dependiente por la independiente.
10. **B.** Al doble de esfuerzo, la mitad de tiempo. Es el ejemplo clásico de Proporción Inversa.""")