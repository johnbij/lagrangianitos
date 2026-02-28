import streamlit as st
import matplotlib.pyplot as plt


def render_N06():
    st.title("N06: Los Números Irracionales (ℐ) — Lo Inconmensurable")

    # ── PORTAL ──────────────────────────────────────────────────────────────
    st.header("🛡️ 1. El Portal: El Secreto que Rompió una Secta")
    st.markdown(r"""
Para Pitágoras y sus seguidores, los números eran la esencia del universo y todo debía ser
una fracción perfecta. Sin embargo, al intentar medir la diagonal de un cuadrado de lado 1,
se encontraron con un monstruo: $\sqrt{2}$.

Este número no se podía escribir como fracción. Era "inconmensurable". Cuenta la leyenda que
**Hipaso de Metaponto** fue arrojado al mar por revelar este secreto. Hoy los llamamos
**Irracionales**, no porque estén locos, sino porque no pueden expresarse como una **Razón** (fracción).
""")

    # ── FIGURA 1: DIAGONAL DE PITÁGORAS ─────────────────────────────────────
    st.subheader("📊 El Origen de los Irracionales: La Diagonal de Pitágoras")
    fig, ax = plt.subplots(figsize=(5, 5))
    cuadrado_x = [0, 1, 1, 0, 0]
    cuadrado_y = [0, 0, 1, 1, 0]
    ax.plot(cuadrado_x, cuadrado_y, color='black', lw=2.5)
    ax.plot([0, 1], [0, 1], color='red', ls='--', lw=3, label='Diagonal = √2')
    ax.text(0.5, -0.12, "Lado = 1", ha='center', fontweight='bold', fontsize=12)
    ax.text(-0.18, 0.5, "Lado = 1", va='center', rotation='vertical', fontweight='bold', fontsize=12)
    ax.text(0.35, 0.62, "√2 ≈ 1,4142...", color='red', fontsize=12, fontweight='bold', rotation=45)
    ax.set_xlim(-0.3, 1.3)
    ax.set_ylim(-0.25, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title("El problema que destruyó una secta", pad=15, fontsize=12, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # ── DEFINICIÓN ──────────────────────────────────────────────────────────
    st.header("🛡️ 2. Definición y Características")
    st.markdown(r"""
Un número es **Irracional** si su expresión decimal es **infinita y no tiene periodo**
(no hay una secuencia que se repita jamás).

- **Indomables:** No importa cuántos decimales calcules, nunca aparecerá un patrón.
- **El Vacío de la Recta:** Los irracionales llenan los puntos que los racionales no pueden tocar.
  Sin ellos, la recta numérica sería como un colador lleno de agujeros.
""")

    # ── LOS TRES PILARES ────────────────────────────────────────────────────
    st.header("🛡️ 3. Los Tres Pilares (Reconocimiento PAES)")
    st.markdown(r"""
**1. Irracionales Algebraicos (Raíces No Exactas):**
- Ejemplos: $\sqrt{2},\; \sqrt{3},\; \sqrt{5},\; \sqrt{10}$
- ⚠️ **Ojo de Halcón:** $\sqrt{9} = 3$ (¡es Racional!). Solo si la raíz no es un cuadrado perfecto, el número es irracional.

**2. Números Trascendentes (Los Especiales):**
- $\pi$ ≈ 3,14159... — relación entre el perímetro de un círculo y su diámetro.
- $e$ ≈ 2,71828... — vital para crecimiento de poblaciones y finanzas.
- $\phi$ ≈ 1,61803... — la proporción áurea en el arte y la naturaleza.
""")

    # ── FIGURA 2: TRASCENDENTES ──────────────────────────────────────────────
    st.subheader("📊 Los Tres Grandes Trascendentes en la Recta Numérica")
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.axhline(0, color='black', lw=2.5)
    ax.set_xlim(1, 4)
    ax.set_ylim(-0.6, 1.2)

    for i in range(1, 5):
        ax.plot(i, 0, '|', color='black', markersize=15, lw=2)
        ax.text(i, -0.25, str(i), ha='center', fontweight='bold', fontsize=12)

    datos = [
        ('φ (Phi)', 1.61803, '#D4AF37'),
        ('e (Euler)', 2.71828, '#2E7D32'),
        ('π (Pi)', 3.14159, '#1565C0'),
    ]
    alturas = [0.5, 0.8, 0.5]
    for (nombre, val, col), alt in zip(datos, alturas):
        ax.plot(val, 0, 'o', color=col, markersize=12, zorder=3)
        ax.annotate(f"{nombre}\n≈ {val:.5f}...",
                    xy=(val, 0.06), xytext=(val, alt),
                    arrowprops=dict(arrowstyle='->', color=col, lw=2),
                    ha='center', color=col, fontweight='bold', fontsize=10)

    ax.axis('off')
    plt.title("Los Tres Grandes Trascendentes", fontsize=13, fontweight='bold', pad=15)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    # ── OPERATIVA ───────────────────────────────────────────────────────────
    st.header("🛡️ 4. Operativa: El \"Virus\" Irracional")
    st.markdown(r"""
| Operación | Resultado | Ejemplo |
|:---|:---:|:---|
| Racional $\pm$ Irracional | **Siempre Irracional** | $5 + \pi = 8{,}14159...$ |
| Irracional × Irracional | **Incierto** | $\sqrt{2} \cdot \sqrt{3} = \sqrt{6}$ (irracional) |
| Irracional × Irracional | **Incierto** | $\sqrt{2} \cdot \sqrt{2} = 2$ (¡racional!) |
""")
    st.info("💡 **Tip:** Un irracional es como un virus. Sumado a un racional, lo vuelve irracional inmediatamente. Pero dos irracionales 'compatibles' pueden 'curarse' al multiplicarse.")

    # ── CLAUSURA ────────────────────────────────────────────────────────────
    st.header("🛡️ 5. Clausura: El Caos Total")
    st.markdown(r"""
¿Se cumple la clausura en $\mathbb{I}$? **Rotundamente NO.**

$\pi + (-\pi) = 0$ → el 0 es racional → la suma de dos irracionales puede sacarte del conjunto.

En los irracionales, **ninguna operación básica es cerrada**.
""")

    # ── EL CERO ─────────────────────────────────────────────────────────────
    st.header("🛡️ 6. El Cero: El Gran Impostor")
    st.markdown(r"""
**Anótalo con fuego:** El número **0 NO es irracional**.

El cero se puede escribir como fracción ($0/1$, $0/5$, etc.), por lo tanto:
- El cero es **Entero**.
- El cero es **Racional**.
- El cero **NUNCA** será irracional.
""")
    st.warning("⚠️ **Trampa PAES:** Si aparece $\\sqrt{0}$, el resultado es $0$ → Racional. No te confundas.")

    st.markdown("""
---
> *"Dondequiera que haya un número, hay belleza."*
> — **Proclo**
""")

    # ── EJEMPLOS ────────────────────────────────────────────────────────────
    with st.expander("🚀 Carpintería de Ejemplos N06", expanded=False):
        st.markdown(r"""
### E02: El Filtro de Raíces
Clasificar: $\sqrt{49}$, $\sqrt{50}$, $\sqrt{0{,}25}$

| Número | Valor | Tipo |
|:---|:---:|:---:|
| $\sqrt{49}$ | 7 | **Racional** |
| $\sqrt{50}$ | $5\sqrt{2} \approx 7{,}07...$ | **Irracional** |
| $\sqrt{0{,}25}$ | 0,5 | **Racional** |

---
### E03: La Infección del Virus
$5 + \pi$ → 5 es racional + $\pi$ es irracional = **Irracional** ✅

---
### E04: La "Cura" en la Multiplicación
$\sqrt{2} \cdot \sqrt{18} = \sqrt{36} = 6$ → **¡Racional!** ✅

---
### E05: Operando con e
$3e - e = 2e \approx 5{,}436...$ → **Irracional** (racional × irracional)

---
### E06: El Cero y el Irracional (La Trampa)
$0 \cdot \sqrt{7} = 0$ → **Racional** (el cero "mata" al irracional)
""")

    # ── CUESTIONARIO ────────────────────────────────────────────────────────
    with st.expander("❓ Cuestionario N06", expanded=False):
        st.markdown(r"""
**1.** ¿Cuál pertenece a los Irracionales?
- A) $\sqrt{121}$ · B) $\sqrt{0{,}01}$ · C) **$\sqrt{8}$** · D) 0

**2.** $\pi$ es irracional porque:
- A) Su valor es exactamente 3,14 · B) Es raíz inexacta · C) **Decimal infinito sin periodo** · D) No se ubica en la recta

**3.** Si $q$ racional ≠ 0 e $i$ irracional, ¿qué es $q \cdot i$?
- A) Siempre entero · B) Siempre racional · C) **Siempre irracional** · D) Siempre cero

**4.** ¿Cuál representa un número racional?
- A) $\sqrt{2} + \sqrt{2}$ · B) **$\pi - \pi$** · C) $e + 1$ · D) $\sqrt{3} \cdot \sqrt{5}$

**5.** El Número de Oro ($\phi$) es:
- A) Irracional algebraico · B) **Irracional trascendente** · C) Racional periódico · D) Semiperiódico

**6.** Sobre el 0, ¿cuál es CORRECTA?
- A) Es irracional por ser especial · B) **Es racional porque se expresa como fracción** · C) No pertenece a ningún conjunto · D) Es el origen de los trascendentes

**7.** $\sqrt{2} \cdot \sqrt{32} =$
- A) $\sqrt{34}$ · B) **8** · C) $4\sqrt{2}$ · D) Irracional
""")

    with st.expander("🔑 Pauta N06", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | Carpintería |
|:---:|:---:|:---|
| 1 | **C** | $\sqrt{121}=11$, $\sqrt{0{,}01}=0{,}1$, $0$ son racionales. $\sqrt{8}$ no es exacta. |
| 2 | **C** | Definición fundamental: decimales infinitos sin periodo. |
| 3 | **C** | Propiedad "Infección": racional ≠ 0 no puede quitar el desorden a un irracional. |
| 4 | **B** | $\pi - \pi = 0$. El 0 es racional. |
| 5 | **B** | Números con nombre propio ($\pi$, $e$, $\phi$) son trascendentes. |
| 6 | **B** | $0 = 0/1$ → cumple definición de ℚ. |
| 7 | **B** | $\sqrt{2 \cdot 32} = \sqrt{64} = 8$. Dos irracionales que al multiplicarse dan racional. |
""")
