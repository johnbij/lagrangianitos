import streamlit as st
import matplotlib.pyplot as plt


def render_N05():
    st.title("N05: Los Números Racionales (ℚ) — La Densidad y el Cociente")

    # ── PORTAL ──────────────────────────────────────────────────────────────
    st.header("🛡️ 1. El Portal: El Arte de Partir el Todo")
    st.markdown(r"""
Hasta ahora, en nuestra carpintería matemática, solo trabajábamos con "piezas completas"
(vigas de 1 metro, de 2 metros). Pero la realidad es más compleja: a veces necesitas
media viga o un tercio de tabla.

El nombre **Racional** viene de "Razón" (un cociente entre dos cantidades). Los antiguos
egipcios ya usaban fracciones para repartir el grano y medir tierras tras las crecidas del Nilo.
Al crear $\mathbb{Q}$ (del italiano *Quoziente*), la humanidad logró por fin la
**Clausura de la División**: ahora cualquier reparto tiene un número que lo representa.
""")

    # ── DEFINICIÓN ──────────────────────────────────────────────────────────
    st.header("🛡️ 2. Definición Formal")
    st.markdown(r"""
Un número es **Racional** si puede expresarse como cociente entre dos enteros:

$$\mathbb{Q} = \left\{ \frac{a}{b} \mid a, b \in \mathbb{Z},\; b \neq 0 \right\}$$

- **Numerador ($a$):** Cuántas partes tomamos.
- **Denominador ($b$):** En cuántas partes iguales se dividió la unidad.
- **⚠️ La Restricción Suprema:** El denominador **jamás puede ser cero**.
""")

    # ── FIGURA ──────────────────────────────────────────────────────────────
    st.subheader("📊 La Densidad de los Racionales")
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axhline(0, color='black', lw=2.5)

    racionales = {0: "0", 1/4: "1/4", 1/3: "1/3", 1/2: "1/2", 2/3: "2/3", 3/4: "3/4", 1: "1"}
    colores_r = ['#1a237e', '#283593', '#1565C0', '#0288d1', '#0097a7', '#00796b', '#2e7d32']

    for (val, label), col in zip(racionales.items(), colores_r):
        ax.plot(val, 0, 'o', color=col, markersize=11, zorder=3)
        ax.text(val, 0.25, label, ha='center', fontsize=10, fontweight='bold', color=col)
        ax.vlines(val, -0.08, 0.08, color='black', lw=1)

    # Mostrar infinitos entre 0 y 1/4
    for x in [0.05, 0.10, 0.15, 0.20]:
        ax.plot(x, 0, '.', color='gray', markersize=5)
    ax.text(0.125, -0.3, "∞ números entre\ncualquier par", ha='center', fontsize=8, color='gray')

    ax.annotate('', xy=(1.2, 0), xytext=(1.05, 0), arrowprops=dict(arrowstyle='->', lw=2))
    ax.set_xlim(-0.2, 1.3)
    ax.set_ylim(-0.6, 0.7)
    ax.axis('off')
    plt.title("Densidad de ℚ: Entre dos racionales siempre hay infinitos más", fontsize=12, fontweight='bold', pad=10)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # ── DENSIDAD ────────────────────────────────────────────────────────────
    st.header("🛡️ 3. La Propiedad de Densidad")
    st.markdown(r"""
Este es el concepto clave para los 1000 puntos:

- En $\mathbb{N}, \mathbb{N}_0$ y $\mathbb{Z}$, los números son **discretos** (hay saltos entre ellos). Existe el "que viene después".
- **En $\mathbb{Q}$ NO existe el sucesor ni el antecesor.** Entre dos racionales, por muy pegados que estén, siempre hay **infinitos** números más.
""")

    # ── DECIMALES ───────────────────────────────────────────────────────────
    st.header("🛡️ 4. Representación Decimal y Clasificación")
    st.markdown(r"""
| Tipo | Descripción | Ejemplo |
|:---|:---|:---:|
| **Decimal Finito** | Cantidad limitada de cifras | $1/4 = 0{,}25$ |
| **Infinito Periódico** | Ciclo que se repite desde la coma | $1/3 = 0{,}\overline{3}$ |
| **Infinito Semiperiódico** | Hay anteperiodo antes del periodo | $0{,}1\overline{6}$ |
""")

    # ── CLAUSURA ────────────────────────────────────────────────────────────
    st.header("🛡️ 5. Clausura: El Club casi Perfecto")
    st.markdown(r"""
| Operación | Cerrada en ℚ | Carpintería |
|:---|:---:|:---|
| **Suma / Resta / Multiplicación** | ✅ SÍ | Siempre dan otro racional |
| **División** | ⚠️ CASI | Cerrada **siempre que el divisor ≠ 0** |
""")

    # ── FRACCIONES EQUIVALENTES ─────────────────────────────────────────────
    st.header("🛡️ 6. Amplificar y Simplificar")
    st.markdown(r"""
- **Amplificar:** Multiplicar numerador y denominador por el mismo número.
  - $\frac{2}{3} \xrightarrow{\times 4} \frac{8}{12}$

- **Simplificar:** Dividir numerador y denominador por un divisor común.
  - $\frac{15}{20} \xrightarrow{\div 5} \frac{3}{4}$
""")
    st.info("💡 **Tip PAES:** Nunca entregues una respuesta sin simplificar al máximo. Si calculas $20/40$, en las alternativas solo aparecerá $1/2$.")

    st.markdown("""
---
> *"Las matemáticas son el lenguaje con el que se describe el mundo, y las fracciones son las palabras que nos permiten ser precisos."*
> — **Henri Poincaré**
""")

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Carpintería de Ejemplos N05", expanded=False):
        st.markdown(r"""
### E01: Decimal Finito a Fracción
**Expresar $0{,}75$ como fracción irreducible.**

1. Numerador = 75 (número sin coma)
2. Denominador = 100 (2 decimales → potencia de 10)
3. $\frac{75}{100} \div 25 = \frac{3}{4}$ ✅

---
### E02: Verificar si es Racional
**¿Es $0{,}333...$ racional?** Sí: $0{,}\overline{3} = 1/3$ → tiene periodo → **Racional** ✅

---
### E03: Amplificación
**Amplificar $2/7$ por 4:**
$\frac{2 \times 4}{7 \times 4} = \frac{8}{28}$

---
### E04: Simplificación
**Simplificar al máximo $45/60$:**
$\text{MCD}(45, 60) = 15$ → $\frac{45 \div 15}{60 \div 15} = \frac{3}{4}$

---
### E05: Densidad
**Encontrar un racional entre $1/3$ y $1/2$:**
Promedio: $\frac{1/3 + 1/2}{2} = \frac{5/6}{2} = \frac{5}{12}$ ✅
""")

    # ── CUESTIONARIO ────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario N05", expanded=False):
        st.markdown(r"""
**1.** ¿Cuál NO puede escribirse como $a/b$ con $b \neq 0$?
- A) 0 · B) -10 · C) $1{,}\bar{3}$ · D) **Un decimal cuyas cifras no tienen patrón ni fin**

**2.** Al simplificar al máximo $45/60$:
- A) 9/12 · B) 15/20 · C) **3/4** · D) 0,75

**3.** ¿Qué resulta de amplificar $2/7$ por 4?
- A) 8/7 · B) 2/28 · C) **8/28** · D) 6/11

**4.** El número $0{,}4\overline{6}$ es:
- A) Irracional · B) Decimal finito · C) Periódico puro · D) **Semiperiódico**

**5.** ¿En ℚ existe el antecesor de un número?
- A) Sí, siempre · B) Solo para enteros · C) **No, por la propiedad de densidad** · D) Solo para positivos
""")

    with st.expander("🔑 Pauta N05", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería |
|:---:|:---:|:---|
| 1 | **D** | Los racionales requieren orden (periodo) o fin. Decimal infinito caótico → Irracional. |
| 2 | **C** | $45$ y $60$ son divisibles por $15$. $45:15=3$ y $60:15=4$. |
| 3 | **C** | Amplificar: multiplicar arriba y abajo por 4. $2 \times 4=8$, $7 \times 4=28$. |
| 4 | **D** | Tiene anteperiodo (4) antes del periodo (6). |
| 5 | **C** | En ℚ el conjunto es denso; entre cualquier par hay infinitos racionales. |
""")
