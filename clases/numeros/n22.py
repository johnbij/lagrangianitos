import streamlit as st


def render_N22():
    st.markdown("## N22: Racionalización Avanzada - El Binomio en el Denominador")
    st.markdown("---")

    st.markdown("### 🏛️ Contexto Histórico: El \"Horror Vacui\" de los Radicales")
    st.markdown("""
Durante el Renacimiento, los matemáticos italianos como **Cardano** y **Bombelli** empezaron a resolver ecuaciones de tercer grado que arrojaban resultados extrañísimos: fracciones con sumas de raíces en el denominador. Para ellos, un número así estaba \"sucio\" o incompleto. Desarrollaron la racionalización por el conjugado basándose en un producto notable que ya conocían desde los griegos: la **Diferencia de Cuadrados**. Entendieron que para eliminar la raíz no bastaba con multiplicar por ella misma, sino que había que crear una estructura simétrica que anulara los términos medios. Hoy no lo hacemos por estética, sino porque simplifica brutalmente el cálculo de límites y derivadas en la educación superior.
    """)
    st.markdown("---")

    st.markdown("""
<div style="background-color: #E8F5E9; border-left: 8px solid #2E7D32; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1B5E20; margin-top: 0;">Racionalización de Binomios</h2>
    Cuando el denominador es una suma o resta que involucra raíces cuadradas ($\\sqrt{a} \\pm \\sqrt{b}$), multiplicamos por su <b>conjugado</b>.
</div>
""", unsafe_allow_html=True)

    st.markdown("### 🛡️ El Conjugado: Tu mejor aliado")
    st.markdown("""
El conjugado de una expresión binomia es la misma expresión pero con el **signo central cambiado**.
- El conjugado de $(x + y)$ es $(x - y)$.
- El conjugado de $(\\sqrt{3} - \\sqrt{2})$ es $(\\sqrt{3} + \\sqrt{2})$.
    """)

    st.markdown("### 🛡️ La Propiedad Maestra")
    st.markdown("""
Al multiplicar un binomio por su conjugado, generamos una **Suma por su Diferencia**, lo que elimina las raíces al elevar ambos términos al cuadrado:
$$(a + b)(a - b) = a^2 - b^2$$
$$(\\sqrt{5} + \\sqrt{2})(\\sqrt{5} - \\sqrt{2}) = (\\sqrt{5})^2 - (\\sqrt{2})^2 = 5 - 2 = 3$$
    """)

    st.markdown("### 🛡️ Procedimiento General")
    st.markdown("""
1. Identificar el conjugado del denominador.
2. Multiplicar numerador y denominador por dicho conjugado.
3. Resolver el numerador (distributividad si es necesario).
4. Resolver el denominador usando la diferencia de cuadrados.
5. Simplificar la fracción si es posible.

**Típ:** Mucho cuidado con los paréntesis en el numerador. Un error común es olvidarse de multiplicar el número de arriba por **ambos** términos del conjugado.
    """)
    st.markdown("---")

    with st.expander("📝 Guía de Ejemplos: Racionalización por Conjugado"):
        st.markdown("""
**E01. Racionalización de binomio simple.** Racionalizar $\\dfrac{1}{\\sqrt{3} - 1}$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar el conjugado del denominador | $\\sqrt{3} + 1$ |
| 2 | Multiplicar arriba y abajo | $\\dfrac{1 \\cdot (\\sqrt{3} + 1)}{(\\sqrt{3} - 1)(\\sqrt{3} + 1)}$ |
| 3 | Aplicar diferencia de cuadrados abajo | $\\dfrac{\\sqrt{3} + 1}{(\\sqrt{3})^2 - 1^2}$ |
| 4 | Resolver y simplificar | $\\dfrac{\\sqrt{3} + 1}{3 - 1} = \\dfrac{\\sqrt{3} + 1}{2}$ |

**E02. Binomio con dos raíces.** Racionalizar $\\dfrac{2}{\\sqrt{5} + \\sqrt{3}}$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar por el conjugado ($\\sqrt{5} - \\sqrt{3}$) | $\\dfrac{2(\\sqrt{5} - \\sqrt{3})}{(\\sqrt{5})^2 - (\\sqrt{3})^2}$ |
| 2 | Resolver denominador | $\\dfrac{2(\\sqrt{5} - \\sqrt{3})}{5 - 3}$ |
| 3 | Simplificar el 2 de arriba con el 2 de abajo | $\\sqrt{5} - \\sqrt{3}$ |

**E03. Numerador compuesto.** Racionalizar $\\dfrac{\\sqrt{2}}{\\sqrt{2} + 1}$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar por conjugado ($\\sqrt{2} - 1$) | $\\dfrac{\\sqrt{2}(\\sqrt{2} - 1)}{(\\sqrt{2})^2 - 1^2}$ |
| 2 | Distribuir en el numerador | $\\dfrac{\\sqrt{2}\\cdot\\sqrt{2} - \\sqrt{2}}{2 - 1}$ |
| 3 | Resultado final | $2 - \\sqrt{2}$ |

**E04. Constante y raíz.** Racionalizar $\\dfrac{4}{3 - \\sqrt{5}}$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar por conjugado ($3 + \\sqrt{5}$) | $\\dfrac{4(3 + \\sqrt{5})}{3^2 - (\\sqrt{5})^2}$ |
| 2 | Resolver denominador | $\\dfrac{4(3 + \\sqrt{5})}{9 - 5} = \\dfrac{4(3 + \\sqrt{5})}{4}$ |
| 3 | Simplificar el 4 | $3 + \\sqrt{5}$ |

**E05. Conjugado con resta y simplificación.** Racionalizar $\\dfrac{1}{\\sqrt{7} - \\sqrt{5}}$.
| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Multiplicar por $(\\sqrt{7} + \\sqrt{5})$ | $\\dfrac{\\sqrt{7} + \\sqrt{5}}{(\\sqrt{7})^2 - (\\sqrt{5})^2}$ |
| 2 | Resolver denominador | $\\dfrac{\\sqrt{7} + \\sqrt{5}}{7 - 5}$ |
| 3 | Resultado final | $\\dfrac{\\sqrt{7} + \\sqrt{5}}{2}$ |
        """)

    with st.expander("❓ Cuestionario N22: Racionalización Avanzada"):
        st.markdown("""
**1. ¿Cuál es el conjugado de la expresión $2 - \\sqrt{3}$?**  
A) $-2 - \\sqrt{3}$ &nbsp;&nbsp; B) $2 + \\sqrt{3}$ &nbsp;&nbsp; C) $\\sqrt{2} - 3$ &nbsp;&nbsp; D) $-2 + \\sqrt{3}$

**2. Al racionalizar $\\dfrac{1}{\\sqrt{2} + 1}$, se obtiene:**  
A) $\\sqrt{2} + 1$ &nbsp;&nbsp; B) $\\sqrt{2} - 1$ &nbsp;&nbsp; C) $\\dfrac{\\sqrt{2} - 1}{3}$ &nbsp;&nbsp; D) $1 - \\sqrt{2}$

**3. El resultado de multiplicar $(\\sqrt{6} - \\sqrt{2})(\\sqrt{6} + \\sqrt{2})$ es:**  
A) $4$ &nbsp;&nbsp; B) $8$ &nbsp;&nbsp; C) $\\sqrt{4}$ &nbsp;&nbsp; D) $32$

**4. Al racionalizar $\\dfrac{3}{\\sqrt{5} - \\sqrt{2}}$, el denominador resultante después de aplicar diferencia de cuadrados es:**  
A) $7$ &nbsp;&nbsp; B) $3$ &nbsp;&nbsp; C) $\\sqrt{3}$ &nbsp;&nbsp; D) $21$

**5. La expresión $\\dfrac{1}{\\sqrt{3} + \\sqrt{2}}$ es equivalente a:**  
A) $\\sqrt{3} + \\sqrt{2}$ &nbsp;&nbsp; B) $\\sqrt{2} - \\sqrt{3}$ &nbsp;&nbsp; C) $\\sqrt{3} - \\sqrt{2}$ &nbsp;&nbsp; D) $\\dfrac{\\sqrt{3} - \\sqrt{2}}{5}$

**6. ¿Cuál es el valor de $\\dfrac{\\sqrt{5} + 1}{\\sqrt{5} - 1}$ después de racionalizar?**  
A) $\\dfrac{3 + \\sqrt{5}}{2}$ &nbsp;&nbsp; B) $3 + \\sqrt{5}$ &nbsp;&nbsp; C) $\\dfrac{6 + 2\\sqrt{5}}{4}$ &nbsp;&nbsp; D) $2 + \\sqrt{5}$

**7. Si racionalizamos $\\dfrac{2}{4 - \\sqrt{12}}$, ¿por qué expresión debemos multiplicar arriba y abajo?**  
A) $4 - \\sqrt{12}$ &nbsp;&nbsp; B) $4 + \\sqrt{12}$ &nbsp;&nbsp; C) $\\sqrt{12}$ &nbsp;&nbsp; D) $4 + 12$

**8. Al simplificar $\\dfrac{2}{\\sqrt{6} - 2}$ resulta:**  
A) $\\sqrt{6} + 2$ &nbsp;&nbsp; B) $\\sqrt{6} - 2$ &nbsp;&nbsp; C) $\\dfrac{\\sqrt{6} + 2}{2}$ &nbsp;&nbsp; D) $2\\sqrt{6} + 4$

**9. ¿Qué sucede con el valor de una fracción cuando se racionaliza su denominador?**  
A) El valor aumenta. &nbsp;&nbsp; B) El valor disminuye. &nbsp;&nbsp; C) El valor se mantiene igual. &nbsp;&nbsp; D) El valor se vuelve racional.

**10. El resultado de racionalizar $\\dfrac{\\sqrt{3}}{\\sqrt{3} + \\sqrt{2}}$ es:**  
A) $3 - \\sqrt{6}$ &nbsp;&nbsp; B) $3 + \\sqrt{6}$ &nbsp;&nbsp; C) $\\sqrt{3} - \\sqrt{2}$ &nbsp;&nbsp; D) $1 - \\sqrt{6}$
        """)

    with st.expander("✅ Pauta Explicativa - Cuestionario N22"):
        st.markdown("""
1. **B.** El conjugado solo cambia el signo de la operación central entre los dos términos.
2. **B.** Al multiplicar por $(\\sqrt{2}-1)$, el denominador queda $(\\sqrt{2})^2 - 1^2 = 2-1 = 1$.
3. **A.** Suma por su diferencia: $(\\sqrt{6})^2 - (\\sqrt{2})^2 = 6 - 2 = 4$.
4. **B.** El denominador queda $(\\sqrt{5})^2 - (\\sqrt{2})^2 = 5 - 2 = 3$.
5. **C.** Al multiplicar por el conjugado $(\\sqrt{3}-\\sqrt{2})$, el denominador resulta $3-2=1$.
6. **A.** Arriba queda $(\\sqrt{5}+1)^2 = 5 + 2\\sqrt{5} + 1 = 6 + 2\\sqrt{5}$. Abajo queda $5-1=4$. Al simplificar por 2, queda $\\dfrac{3+\\sqrt{5}}{2}$.
7. **B.** Siempre se multiplica por el conjugado del denominador original para eliminar la raíz.
8. **A.** Multiplicamos por $(\\sqrt{6}+2)$. Denominador: $6-4=2$. El 2 de arriba se cancela con el 2 de abajo.
9. **C.** Se mantiene igual porque multiplicamos por un \"1 conveniente\" (una fracción donde numerador y denominador son iguales).
10. **A.** Multiplicamos $\\sqrt{3}(\\sqrt{3}-\\sqrt{2})$. Distribuyendo: $\\sqrt{3}\\cdot\\sqrt{3} - \\sqrt{3}\\cdot\\sqrt{2} = 3 - \\sqrt{6}$. Abajo queda $3-2=1$.
        """)

    st.markdown("---")
    st.markdown("> *\"La unidad es la variedad, y la variedad en la unidad es la ley suprema del universo.\"*  \n> — **Isaac Newton**")
