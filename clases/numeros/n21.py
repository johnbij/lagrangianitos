import streamlit as st


def render_N21():
    st.markdown("## N21: Racionalización Básica - El Arte de Limpiar el Denominador")
    st.markdown("---")

    st.markdown("### 🏛️ Contexto Histórico: La obsesión por la forma estándar")
    st.markdown("""
Durante siglos, el cálculo manual era un dolor de cabeza, y dividir por un número irracional (como $\\sqrt{2}$) era el equivalente a tratar de escribir con un lápiz sin punta. Los matemáticos de la época renacentista buscaban formas **\"canónicas\"** o estándar para los números. Descubrieron que si multiplicaban el numerador y el denominador por el mismo radical, el valor de la fracción no cambiaba, pero el denominador se convertía en un número entero agradable y fácil de usar para dividir. La racionalización nace no solo por estética, sino por una necesidad pura de velocidad y precisión en el cálculo.
    """)
    st.markdown("---")

    st.markdown("""
<div style="background-color: #E8F5E9; border-left: 8px solid #2E7D32; padding: 25px; border-radius: 10px;">
    <h2 style="color: #1B5E20; margin-top: 0;">¿Qué es Racionalizar?</h2>
    Racionalizar es un proceso algebraico que consiste en eliminar las raíces del denominador de una fracción. El objetivo es obtener una fracción equivalente cuyo denominador sea un número racional (entero o fracción entera).
</div>
""", unsafe_allow_html=True)

    st.markdown("### 🛡️ El Procedimiento Maestro")
    st.markdown("""
Para racionalizar una raíz simple del tipo $\\dfrac{A}{\\sqrt[n]{b^m}}$, multiplicamos tanto el numerador como el denominador por otra raíz que **\"complete\"** la potencia del denominador para que el índice se cancele.

$$\\frac{A}{\\sqrt[n]{b^m}} \\cdot \\frac{\\sqrt[n]{b^{n-m}}}{\\sqrt[n]{b^{n-m}}} = \\frac{A \\cdot \\sqrt[n]{b^{n-m}}}{b}$$
    """)

    st.markdown("### 🛡️ Casos Básicos")
    st.markdown("""
| Denominador | Factor Racionalizante | Resultado en Denominador |
| :--- | :--- | :--- |
| $\\sqrt{a}$ | $\\sqrt{a}$ | $a$ |
| $\\sqrt[3]{a}$ | $\\sqrt[3]{a^2}$ | $a$ |
| $\\sqrt[4]{a^3}$ | $\\sqrt[4]{a}$ | $a$ |

**Típ:** ¡No te olvides de multiplicar arriba también! Si solo multiplicas abajo, estás cambiando el valor de la fracción, no racionalizándola.
    """)
    st.markdown("---")

    with st.expander("📝 Guía de Ejemplos Paso a Paso - Racionalización Básica"):
        st.markdown("""
**E01. Racionalizar una raíz cuadrada simple.** Racionalizar $\\dfrac{1}{\\sqrt{2}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante | $\\sqrt{2}$ |
| 2 | Multiplicar arriba y abajo | $\\dfrac{1 \\cdot \\sqrt{2}}{\\sqrt{2} \\cdot \\sqrt{2}}$ |
| 3 | Resolver producto | $\\dfrac{\\sqrt{2}}{2}$ |

---

**E02. Racionalizar con coeficiente en el denominador.** Racionalizar $\\dfrac{3}{\\sqrt{3}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante | $\\sqrt{3}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{3 \\cdot \\sqrt{3}}{\\sqrt{3} \\cdot \\sqrt{3}}$ |
| 3 | Resolver y simplificar | $\\dfrac{3\\sqrt{3}}{3} = \\sqrt{3}$ |

---

**E03. Racionalizar con número entero en el numerador.** Racionalizar $\\dfrac{2}{3\\sqrt{5}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante (solo la raíz) | $\\sqrt{5}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{2 \\cdot \\sqrt{5}}{3\\sqrt{5} \\cdot \\sqrt{5}}$ |
| 3 | Resolver producto en denominador | $\\dfrac{2\\sqrt{5}}{3 \\cdot 5} = \\dfrac{2\\sqrt{5}}{15}$ |

---

**E04. Racionalizar raíz cúbica.** Racionalizar $\\dfrac{1}{\\sqrt[3]{2}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor para completar exponente 3 | $\\sqrt[3]{2^2}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{1 \\cdot \\sqrt[3]{2^2}}{\\sqrt[3]{2} \\cdot \\sqrt[3]{2^2}}$ |
| 3 | Resolver denominador | $\\dfrac{\\sqrt[3]{4}}{\\sqrt[3]{2^3}} = \\dfrac{\\sqrt[3]{4}}{2}$ |

---

**E05. Racionalizar raíz sobre raíz.** Racionalizar $\\dfrac{\\sqrt{2}}{\\sqrt{3}}$.

| Paso | Acción | Resultado |
| :--- | :--- | :--- |
| 1 | Identificar factor racionalizante | $\\sqrt{3}$ |
| 2 | Multiplicar numerador y denominador | $\\dfrac{\\sqrt{2} \\cdot \\sqrt{3}}{\\sqrt{3} \\cdot \\sqrt{3}}$ |
| 3 | Resolver productos | $\\dfrac{\\sqrt{6}}{3}$ |
        """)

    with st.expander("❓ Cuestionario N21: Racionalización Básica"):
        st.markdown("""
**1. ¿Cuál es el resultado de racionalizar $\\dfrac{1}{\\sqrt{5}}$?**  
A) $\\dfrac{\\sqrt{5}}{5}$ &nbsp;&nbsp; B) $\\sqrt{5}$ &nbsp;&nbsp; C) $\\dfrac{1}{5}$ &nbsp;&nbsp; D) $\\dfrac{5}{\\sqrt{5}}$

**2. ¿Cuál es el factor racionalizante para $\\dfrac{A}{\\sqrt{7}}$?**  
A) $7$ &nbsp;&nbsp; B) $\\sqrt{7}$ &nbsp;&nbsp; C) $\\sqrt{49}$ &nbsp;&nbsp; D) $\\dfrac{\\sqrt{7}}{7}$

**3. Racionaliza la expresión $\\dfrac{2}{\\sqrt{2}}$:**  
A) $2\\sqrt{2}$ &nbsp;&nbsp; B) $\\dfrac{\\sqrt{2}}{2}$ &nbsp;&nbsp; C) $\\sqrt{2}$ &nbsp;&nbsp; D) $2$

**4. Al racionalizar $\\dfrac{1}{\\sqrt[3]{3}}$, el denominador resultante es:**  
A) $3$ &nbsp;&nbsp; B) $9$ &nbsp;&nbsp; C) $\\sqrt[3]{3}$ &nbsp;&nbsp; D) $\\sqrt[3]{9}$

**5. El resultado de $\\dfrac{\\sqrt{2}}{\\sqrt{6}}$ tras racionalizar es:**  
A) $\\dfrac{\\sqrt{12}}{6}$ &nbsp;&nbsp; B) $\\dfrac{\\sqrt{3}}{3}$ &nbsp;&nbsp; C) $\\dfrac{1}{\\sqrt{3}}$ &nbsp;&nbsp; D) $\\dfrac{2}{6}$

**6. ¿Cuál es el resultado de racionalizar $\\dfrac{4}{3\\sqrt{2}}$?**  
A) $\\dfrac{4\\sqrt{2}}{3}$ &nbsp;&nbsp; B) $\\dfrac{2\\sqrt{2}}{3}$ &nbsp;&nbsp; C) $\\dfrac{2\\sqrt{2}}{6}$ &nbsp;&nbsp; D) $\\dfrac{\\sqrt{2}}{3}$

**7. Racionaliza $\\dfrac{1}{\\sqrt[4]{2^2}}$:**  
A) $\\dfrac{\\sqrt[4]{2}}{2}$ &nbsp;&nbsp; B) $\\dfrac{\\sqrt[4]{4}}{2}$ &nbsp;&nbsp; C) $\\sqrt[4]{2}$ &nbsp;&nbsp; D) $\\dfrac{1}{2}$

**8. ¿Qué expresión es equivalente a $\\dfrac{10}{2\\sqrt{5}}$?**  
A) $5\\sqrt{5}$ &nbsp;&nbsp; B) $2\\sqrt{5}$ &nbsp;&nbsp; C) $\\sqrt{5}$ &nbsp;&nbsp; D) $\\dfrac{\\sqrt{5}}{5}$

**9. Al racionalizar $\\dfrac{\\sqrt{3}}{\\sqrt{5}}$, ¿qué numerador obtienes?**  
A) $\\sqrt{3}$ &nbsp;&nbsp; B) $\\sqrt{5}$ &nbsp;&nbsp; C) $\\sqrt{15}$ &nbsp;&nbsp; D) $15$

**10. El factor racionalizante de $\\dfrac{1}{\\sqrt[5]{x^2}}$ es:**  
A) $\\sqrt[5]{x}$ &nbsp;&nbsp; B) $\\sqrt[5]{x^2}$ &nbsp;&nbsp; C) $\\sqrt[5]{x^3}$ &nbsp;&nbsp; D) $\\sqrt[5]{x^5}$
        """)

    with st.expander("✅ Pauta - Cuestionario N21"):
        st.markdown("""
| Pregunta | Respuesta | Carpintería Técnica (El porqué) |
| :--- | :---: | :--- |
| **1** | **A** | $\\dfrac{1}{\\sqrt{5}} \\cdot \\dfrac{\\sqrt{5}}{\\sqrt{5}} = \\dfrac{\\sqrt{5}}{5}$ |
| **2** | **B** | Se multiplica por la misma raíz cuadrada para eliminarla. |
| **3** | **C** | $\\dfrac{2}{\\sqrt{2}} \\cdot \\dfrac{\\sqrt{2}}{\\sqrt{2}} = \\dfrac{2\\sqrt{2}}{2} = \\sqrt{2}$ |
| **4** | **A** | $\\dfrac{1}{\\sqrt[3]{3}} \\cdot \\dfrac{\\sqrt[3]{3^2}}{\\sqrt[3]{3^2}} = \\dfrac{\\sqrt[3]{9}}{\\sqrt[3]{3^3}} = \\dfrac{\\sqrt[3]{9}}{3}$ |
| **5** | **B** | $\\dfrac{\\sqrt{2}}{\\sqrt{6}} \\cdot \\dfrac{\\sqrt{6}}{\\sqrt{6}} = \\dfrac{\\sqrt{12}}{6} = \\dfrac{2\\sqrt{3}}{6} = \\dfrac{\\sqrt{3}}{3}$ |
| **6** | **B** | $\\dfrac{4}{3\\sqrt{2}} \\cdot \\dfrac{\\sqrt{2}}{\\sqrt{2}} = \\dfrac{4\\sqrt{2}}{3 \\cdot 2} = \\dfrac{4\\sqrt{2}}{6} = \\dfrac{2\\sqrt{2}}{3}$ |
| **7** | **B** | $\\dfrac{1}{\\sqrt[4]{2^2}} \\cdot \\dfrac{\\sqrt[4]{2^2}}{\\sqrt[4]{2^2}} = \\dfrac{\\sqrt[4]{4}}{\\sqrt[4]{2^4}} = \\dfrac{\\sqrt[4]{4}}{2}$ |
| **8** | **C** | $\\dfrac{10}{2\\sqrt{5}} = \\dfrac{5}{\\sqrt{5}} \\cdot \\dfrac{\\sqrt{5}}{\\sqrt{5}} = \\dfrac{5\\sqrt{5}}{5} = \\sqrt{5}$ |
| **9** | **C** | $\\dfrac{\\sqrt{3}}{\\sqrt{5}} \\cdot \\dfrac{\\sqrt{5}}{\\sqrt{5}} = \\dfrac{\\sqrt{15}}{5}$ |
| **10** | **C** | Necesitamos exponente 5, faltan 3 ($5-2=3$). |
        """)

    st.markdown("---")
    st.markdown("> *\"La matemática es la reina de las ciencias.\"*")
