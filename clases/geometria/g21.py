v s timport streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G21():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G21: Cuerpos 3D II — Pirámides, Conos y Esfera")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    # G21: Cuerpos 3D II - Pirámides, Conos y Esfera
    

    ---

    ### 🛡️ 1. Cuerpos que terminan en punta (Pirámide y Cono)
    A diferencia de los prismas, estos cuerpos ocupan menos espacio. De hecho, ¡caben exactamente tres veces en un prisma de su misma base y altura!
    * **Volumen ($V$):** Es un tercio del área de la base por la altura.
      $$V = \frac{A_{base} \cdot h}{3}$$

    ### ⚖️ 2. La Esfera: El cuerpo perfecto
    No tiene caras, ni bases, ni aristas. Solo depende de su **radio ($r$)**.
    * **Área Superficial:** $4 \cdot \pi \cdot r^2$ (equivale al área de 4 círculos grandes).
    * **Volumen:** $\frac{4}{3} \cdot \pi \cdot r^3$

    ### 📐 3. Elementos del Cono
    * **Generatriz ($g$):** Es la hipotenusa del triángulo rectángulo que gira para formar el cono.
    * **Relación Pitagórica:** $r^2 + h^2 = g^2$.

    >
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G21 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ EjercitacióTcnica G21 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Volumen de una pirámide: base de 30 cm² y altura de 10 cm. | 1. Multiplicar base por altura: $30 \cdot 10 = 300$.<br>2. Dividir por 3: $300 / 3$. | **100 cm³** |
| **E02** | Volumen de un cono de radio 3 y altura 4. | 1. Área base: $\pi \cdot 3^2 = 9\pi$.<br>2. Volumen: $(9\pi \cdot 4) / 3 = 36\pi / 3$. | **$12\pi$ u³** |
| **E03** | Hallar la generatriz ($g$) de un cono si $r=3$ y $h=4$. | 1. Aplicar Pitágoras: $3^2 + 4^2 = g^2$.<br>2. $9 + 16 = 25 \implies \sqrt{25}$. | **5** |
| **E04** | Área de una esfera de radio 2. | 1. Aplicar fórmula: $4 \cdot \pi \cdot 2^2$.<br>2. $4 \cdot \pi \cdot 4$. | **$16\pi$ u²** |
| **E05** | Si el radio de una esfera se dobla, ¿qué pasa con el volumen? | 1. El volumen depende de $r^3$.<br>2. $2^3 = 8$. | **Aumenta 8 veces** |
""")

    with st.expander("❓ Cuestionario G21", expanded=False):
        quiz = [
            {'question': 'El volumen de un cono es exactamente la _____ parte del de un cilindro de igual base y altura:', 'options': {'A': 'Mitad', 'B': 'Tercera', 'C': 'Cuarta', 'D': 'Quinta'}, 'answer': 'B', 'explanation': 'Es la relación mágica de los cuerpos que terminan en punta. Siempre es un tercio.'},
            {'question': '¿Cuál es el volumen de una esfera de radio 3?', 'options': {'A': '$12\\pi$', 'B': '$36\\pi$', 'C': '$108\\pi$', 'D': '$9\\pi$'}, 'answer': 'B', 'explanation': '$\\frac{4}{3} \\cdot \\pi \\cdot 3^3 = \\frac{4}{3} \\cdot \\pi \\cdot 27$. Dividimos 27 en 3 ($=9$) y $9 \\cdot 4 = 36$.'},
            {'question': 'En un cono recto, la altura, el radio y la generatriz forman un triángulo:', 'options': {'A': 'Equilátero', 'B': 'Obtusángulo', 'C': 'Rectángulo', 'D': 'Isósceles'}, 'answer': 'C', 'explanation': 'Ese triángulo es el que permite usar el Teorema de Pitágoras para hallar cualquier medida faltante.'},
            {'question': 'Si una pirámide tiene base cuadrada de lado 6 y altura 5, su volumen es:', 'options': {'A': '180', 'B': '90', 'C': '60', 'D': '30'}, 'answer': 'C', 'explanation': 'Área base $= 6 \\cdot 6 = 36$. Luego $(36 \\cdot 5) / 3 = 12 \\cdot 5 = 60$.'},
            {'question': 'El área de una esfera de diámetro 10 es:', 'options': {'A': '$100\\pi$', 'B': '$400\\pi$', 'C': '$25\\pi$', 'D': '$50\\pi$'}, 'answer': 'A', 'explanation': 'Típ: Diámetro 10 significa Radio 5. Área $= 4 \\cdot \\pi \\cdot 5^2 = 4 \\cdot 25 \\cdot \\pi = 100\\pi$.'},
            {'question': '¿Qué cuerpo se genera al rotar un semicírculo sobre su diámetro?', 'options': {'A': 'Cono', 'B': 'Cilindro', 'C': 'Esfera', 'D': 'Pirámide'}, 'answer': 'C', 'explanation': 'Es la definición clásica de la esfera como cuerpo de revolución.'},
            {'question': 'Si una pirámide y un prisma tienen la misma base y volumen, la pirámide debe ser:', 'options': {'A': 'Más baja', 'B': 'Igual de alta', 'C': 'Tres veces más alta', 'D': 'La mitad de alta'}, 'answer': 'C', 'explanation': 'Como la pirámide pierde volumen por terminar en punta, necesita compensar siendo 3 veces más alta para igualar al prisma.'},
            {'question': 'El volumen de un cono de radio $r$ y altura $h$ es:', 'options': {'A': '$\\pi r^2 h$', 'B': '$2\\pi r h$', 'C': '$(\\pi r^2 h) / 3$', 'D': '$\\frac{4}{3} \\pi r^3$'}, 'answer': 'C', 'explanation': 'Es la fórmula estándar. No olvides el cuadrado en el radio y el 3 en el denominador.'},
            {'question': 'Si la generatriz de un cono es 13 y el radio es 5, la altura es:', 'options': {'A': '8', 'B': '12', 'C': '10', 'D': '18'}, 'answer': 'B', 'explanation': 'Trío pitagórico (5, 12, 13). Si el radio es 5 y la hipotenusa (generatriz) es 13, la altura es 12.'},
            {'question': 'La esfera es un cuerpo que tiene:', 'options': {'A': 'Una base circular', 'B': 'Infinitos vértices', 'C': 'Cero caras planas', 'D': 'Una cara lateral rectangular'}, 'answer': 'C', 'explanation': 'Típ: La esfera es pura curva. Es el único cuerpo que no tiene ninguna superficie plana.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g21_quiz")
