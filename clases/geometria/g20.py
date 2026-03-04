import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G20():
    st.markdown(_CSS, unsafe_allow_html=True)
    st.title("G20: Cuerpos 3D I — Prismas y Cilindros")
    st.markdown('<div class="clase-body">', unsafe_allow_html=True)

    st.markdown(r"""
# 🎬 Clase G20: Cuerpos 3D I - Prismas y Cilindros
**Eje:** Geometría | **Nivel:** Alcance del Objetivo

---

### 🛡️ 1. Definiciones Básicas
* **Cuerpos Poliedros (Prismas):** Tienen caras planas. Un prisma tiene dos bases paralelas iguales y caras laterales que son paralelogramos.
* **Cuerpos Redondos (Cilindro):** Se generan al girar una figura plana alrededor de un eje. El cilindro nace de girar un rectángulo.

### ⚖️ 2. Fórmulas Universales
Para la mayoría de los prismas y el cilindro, la lógica es la misma:
* **Área Total ($A_t$):** Es la suma del área de las dos bases ($2 \cdot A_b$) más el área lateral ($A_l$).
* **Volumen ($V$):** Es el producto del área de la base por la altura ($h$).
  $$V = A_base \cdot h$$

### 📐 3. El Cilindro de Cerca
Como su base es un círculo ($A = \pi r^2$) y su "contorno" desplegado es un rectángulo:
* **Área Lateral:** $2 \cdot \pi \cdot r \cdot h$
* **Volumen:** $\pi \cdot r^2 \cdot h$

> **Newton Tip:** "Seba, dile a tu alumno: el volumen es como llenar una piscina. Primero cubres el fondo (Área de la base) y luego vas subiendo capa por capa (Altura). ¡Es la misma fórmula para casi todo lo que sea 'recto'!"
""")

    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🛠️ Ejercitación Técnica G20 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G20 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Volumen de un cubo de arista 3 cm. | 1. Área base: $3 \cdot 3 = 9$.<br>2. Volumen: $9 \cdot 3$. | **27 cm³** |
| **E02** | Volumen de un cilindro de radio 2 y altura 5. | 1. Área base: $\pi \cdot 2^2 = 4\pi$.<br>2. Volumen: $4\pi \cdot 5$. | **$20\pi$ u³** |
| **E03** | Área total de un cubo de arista 2. | 1. Un cubo tiene 6 caras iguales.<br>2. Área una cara: $2^2 = 4$.<br>3. Total: $4 \cdot 6$. | **24 u²** |
| **E04** | Prisma base cuadrada (lado 4) y altura 10. | 1. Área base: $4^2 = 16$.<br>2. Volumen: $16 \cdot 10$. | **160 u³** |
| **E05** | ¿Qué pasa con el volumen del cilindro si doblo el radio? | 1. Radio al cuadrado: $2^2 = 4$.<br>2. El volumen se multiplica por 4. | **Se cuadruplica** |
""")

    with st.expander("❓ Cuestionario G20", expanded=False):
        quiz = [
            {'question': 'Un prisma cuya base es un hexágono tiene un total de:', 'options': {'A': '6 caras', 'B': '7 caras', 'C': '8 caras', 'D': '12 caras'}, 'answer': 'C', 'explanation': 'Tienes las 6 caras laterales de los lados del hexágono + las 2 bases (tapa y suelo). Total: 8.'},
            {'question': 'La fórmula del volumen para cualquier prisma recto es:', 'options': {'A': 'Base + Altura', 'B': '(Base $\\cdot$ Altura) / 2', 'C': 'Área de la base $\\cdot$ Altura', 'D': 'Perímetro $\\cdot$ Altura'}, 'answer': 'C', 'explanation': 'Es la regla de oro para prismas y cilindros. Superficie del fondo por lo alto que llegas.'},
            {'question': 'Si un cubo tiene un volumen de 64 cm³, su arista mide:', 'options': {'A': '4 cm', 'B': '8 cm', 'C': '16 cm', 'D': '32 cm'}, 'answer': 'A', 'explanation': 'Buscamos un número que multiplicado tres veces por sí mismo dé 64. $4 \\cdot 4 \\cdot 4 = 64$.'},
            {'question': 'El cuerpo generado al rotar un rectángulo sobre uno de sus lados es un:', 'options': {'A': 'Cono', 'B': 'Esfera', 'C': 'Cilindro', 'D': 'Prisma'}, 'answer': 'C', 'explanation': 'Imagina una puerta giratoria; el camino que recorre el borde es la curva del cilindro.'},
            {'question': 'El área lateral de un cilindro desplegado tiene forma de:', 'options': {'A': 'Círculo', 'B': 'Triángulo', 'C': 'Rectángulo', 'D': 'Trapecio'}, 'answer': 'C', 'explanation': 'Típ: Si cortas la etiqueta de una lata y la estiras, verás un rectángulo perfecto.'},
            {'question': 'Si el radio de un cilindro es 3 y su altura es 10, su volumen es:', 'options': {'A': '$30\\pi$', 'B': '$60\\pi$', 'C': '$90\\pi$', 'D': '$300\\pi$'}, 'answer': 'C', 'explanation': 'Radio al cuadrado ($3^2=9$), por altura ($10$), por $\\pi$. $9 \\cdot 10 \\cdot \\pi = 90\\pi$.'},
            {'question': 'Un "Paralelepípedo" es el nombre técnico para:', 'options': {'A': 'Un cilindro inclinado', 'B': 'Un prisma de caras rectangulares (como una caja)', 'C': 'Una esfera cortada', 'D': 'Una pirámide sin punta'}, 'answer': 'B', 'explanation': "Viene del griego 'planos paralelos'. Es la forma de los ladrillos o cajas de zapatos."},
            {'question': 'Si una caja mide 2x3x4, su volumen es:**\n| A) 9\n| B) 12\n| C) 24\n| D) 48\n\n**9. La cantidad de líquido que cabe en un recipiente se relaciona con su:', 'options': {'A': 'Área lateral', 'B': 'Perímetro', 'C': 'Volumen', 'D': 'Diagonal'}, 'answer': 'C', 'explanation': 'Simplemente multiplica las tres dimensiones: $2 \\cdot 3 \\cdot 4 = 24$.'},
            {'question': 'Si un cilindro y un prisma tienen la misma área de base y misma altura:', 'options': {'A': 'El cilindro tiene más volumen', 'B': 'El prisma tiene más volumen', 'C': 'Tienen el mismo volumen', 'D': 'Depende del valor de $\\pi$'}, 'answer': 'C', 'explanation': "Típ: Si el 'fondo' y la 'altura' son iguales, no importa la forma de la base, la capacidad es la misma."}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g20_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G20)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **C** | **Galileo Tip:** "Tienes las 6 caras laterales de los lados del hexágono + las 2 bases (tapa y suelo). Total: 8." |
| **2** | **C** | **Newton Tip:** "Es la regla de oro para prismas y cilindros. Superficie del fondo por lo alto que llegas." |
| **3** | **A** | **Hawking Tip:** "Buscamos un número que multiplicado tres veces por sí mismo dé 64. $4 \cdot 4 \cdot 4 = 64$." |
| **4** | **C** | **Curie Tip:** "Imagina una puerta giratoria; el camino que recorre el borde es la curva del cilindro." |
| **5** | **C** | **Statham Tip:** "Típ: Si cortas la etiqueta de una lata y la estiras, verás un rectángulo perfecto." |
| **6** | **C** | **Newton Tip:** "Radio al cuadrado ($3^2=9$), por altura ($10$), por $\pi$. $9 \cdot 10 \cdot \pi = 90\pi$." |
| **7** | **B** | **Galileo Tip:** "Viene del griego 'planos paralelos'. Es la forma de los ladrillos o cajas de zapatos." |
| **8** | **C** | **Hawking Tip:** "Simplemente multiplica las tres dimensiones: $2 \cdot 3 \cdot 4 = 24$." |
| **9** | **C** | **Curie Tip:** "El volumen es la medida del espacio tridimensional que ocupa un cuerpo." |
| **10** | **C** | **Statham Tip:** "Típ: Si el 'fondo' y la 'altura' son iguales, no importa la forma de la base, la capacidad es la misma." |
""")
