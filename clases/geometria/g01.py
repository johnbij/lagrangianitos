import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from utils import render_multiple_choice_quiz

_CSS = """
<style>
.clase-body p, .clase-body li, .clase-body td, .clase-body th { font-size: 1.07rem !important; line-height: 1.8; }
</style>
"""

def render_G01():
    with st.expander("📚 Teoría", expanded=False):
        st.markdown(_CSS, unsafe_allow_html=True)
        st.title("G01: Topografía Inicial — El Plano Cartesiano")
        st.markdown('<div class="clase-body">', unsafe_allow_html=True)

        st.markdown(r"""
    

    ---

    ### 🏛️ La Intuición de Descartes
    Cuenta la leyenda que **René Descartes** estaba en cama mirando una mosca caminar por el techo. Se preguntó: *¿Cómo puedo describir la posición exacta de esa mosca?* Así nacieron los ejes X e Y. Un sistema para que nadie se sintiera perdido en una superficie plana.

    ### ⚖️ 1. Las Reglas del Tablero
    * **Eje X (Abscisas):** El horizonte. Lo que avanzas o retrocedes.
    * **Eje Y (Ordenadas):** El vertical. Lo que subes o bajas.
    * **El Origen $(0,0)$:** El centro del mapa.

    ### ⚖️ 2. Coordenadas $P(x, y)$
    El primer número manda en horizontal, el segundo en vertical.
    * **Cuadrante I:** $(+,+)$ | **Cuadrante II:** $(-,+)$
    * **Cuadrante III:** $(-,-)$ | **Cuadrante IV:** $(+,-)$

    > **Galileo Tip:** "Escucha, el orden es sagrado: $(x, y)$. Primero caminas por el pasillo (X) y luego buscas el piso en el ascensor (Y). Si los cruzas, terminarás en la habitación equivocada."
    """)

        st.markdown('</div>', unsafe_allow_html=True)


    with st.expander("🛠️ Ejercitación Técnica G01 (Paso a Paso)", expanded=False):
        st.markdown(r"""
## 🛠️ Ejercitación Técnica G01 (Paso a Paso)

| ID | Desafío | Paso a Paso | Resultado |
| :--- | :--- | :--- | :--- |
| **E01** | Ubicar el punto $P(-3, 4)$ | 1. Parto en el origen $(0,0)$.<br>2. Me muevo 3 unidades a la izquierda (X es -3).<br>3. Subo 4 unidades (Y es 4). | **Punto en el II Cuadrante** |
| **E02** | ¿Cuál es la distancia entre $(0,0)$ y $(3,4)$? | 1. Dibujar el triángulo rectángulo con base 3 y altura 4.<br>2. Aplicar Pitágoras: $c^2 = 3^2 + 4^2 = 9 + 16 = 25$.<br>3. Calcular $\sqrt{25}$. | **5 unidades** |
| **E03** | Calcular el punto medio entre $A(2, 4)$ y $B(6, 10)$ | 1. Promedio de las X: $(2+6)/2 = 4$.<br>2. Promedio de las Y: $(4+10)/2 = 7$.<br>3. Armar el par ordenado $(X_m, Y_m)$. | **$M(4, 7)$** |
| **E04** | Reflejar el punto $(5, 2)$ respecto al eje X. | 1. El valor de X se mantiene intacto (5).<br>2. El valor de Y cambia de signo (espejo horizontal). | **$(5, -2)$** |
| **E05** | ¿Dónde se ubica un punto cuya coordenada es $(0, -6)$? | 1. Al ser $x=0$, no hay movimiento lateral.<br>2. Al ser $y=-6$, el punto bajó por el eje vertical. | **Eje Y negativo** |
""")

    with st.expander("❓ Cuestionario G01", expanded=False):
        quiz = [
            {'question': 'Un punto cuya abscisa es negativa y cuya ordenada es positiva se encuentra en el:', 'options': {'A': 'I Cuadrante', 'B': 'II Cuadrante', 'C': 'III Cuadrante', 'D': 'IV Cuadrante'}, 'answer': 'B', 'explanation': '¡No te pierdas! Si la abscisa ($x$) es negativa y la ordenada ($y$) es positiva, significa que te moviste a la izquierda y subiste. Eso define al **Segundo Cuadrante**. ¡Visualízalo!'},
            {'question': '¿Cuál es la distancia entre los puntos $A(1, 5)$ y $B(1, -2)$?', 'options': {'A': '3 unidades', 'B': '4 unidades', 'C': '7 unidades', 'D': '10 unidades'}, 'answer': 'C', 'explanation': 'Mira los puntos: $A(1, 5)$ y $B(1, -2)$. ¿Ves que el 1 no cambió? Solo te moviste verticalmente. Desde el 5 positivo hasta el 2 negativo hay 7 pasos de distancia. $'},
            {'question': 'El punto medio del segmento con extremos $( -4, 8)$ y $(2, 2)$ es:', 'options': {'A': '$(-1, 5)$', 'B': '$(-2, 10)$', 'C': '$(3, 3)$', 'D': '$(1, 5)$'}, 'answer': 'A', 'explanation': 'El punto medio es simplemente el promedio. Suma las X: $-4 + 2 = -2$, y la mitad es $-1$. Suma las Y: $8 + 2 = 10$, y la mitad es $5$. El centro de ese universo es $(-1, 5)$. ¡Es lógica pura!'},
            {'question': 'Si reflejamos el punto $P(3, 4)$ respecto al eje X, ¿cuáles son sus nuevas coordenadas?', 'options': {'A': '$(-3, 4)$', 'B': '$(3, -4)$', 'C': '$(-3, -4)$', 'D': '$(4, 3)$'}, 'answer': 'B', 'explanation': 'La simetría respecto al eje X es como un reflejo en el agua: lo que está arriba pasa abajo, pero la posición horizontal no cambia. El punto $(3,4)$ se convierte en $(3,-4)$.'},
            {'question': '¿En qué cuadrante se ubica un punto donde tanto la abscisa como la ordenada son negativas?', 'options': {'A': 'I Cuadrante', 'B': 'II Cuadrante', 'C': 'III Cuadrante', 'D': 'IV Cuadrante'}, 'answer': 'C', 'explanation': '¡Cuidado aquí! En el tercer cuadrante te mueves a la izquierda (X negativo) y bajas (Y negativo). La combinación $(-,-)$ es la trampa final del plano.'},
            {'question': 'Si un punto está sobre el eje Y, ¿qué valor es garantizado que sea 0?', 'options': {'A': 'La ordenada ($y$)', 'B': 'La abscisa ($x$)', 'C': 'Ambos son 0', 'D': 'Ninguno es 0'}, 'answer': 'B', 'explanation': 'Si no te mueves hacia los lados, estás clavado en la línea vertical. La línea vertical es donde la abscisa ($x$) es siempre cero.'},
            {'question': '¿Cuál es la distancia entre el origen $(0,0)$ y el punto $P(3, -4)$?', 'options': {'A': '1 unidad', 'B': '5 unidades', 'C': '7 unidades', 'D': '25 unidades'}, 'answer': 'B', 'explanation': 'Es un clásico triángulo 3-4-5. La distancia del origen a $(x, y)$ es $\\sqrt{x^2+y^2}$. $\\sqrt{3^2+(-4)^2} = \\sqrt{9+16} = 5$.'},
            {'question': 'Si $M(2, 3)$ es el punto medio entre $A(1, 1)$ y $B(x, y)$, ¿cuáles son los valores de $x$ e $y$?', 'options': {'A': '$(3, 5)$', 'B': '$(4, 6)$', 'C': '$(3, 2)$', 'D': '$(1, 2)$'}, 'answer': 'A', 'explanation': 'El punto medio es el promedio, así que deshaz el promedio: $2 = (1+x)/2 \\implies 4 = 1+x \\implies x=3$. $3 = (1+y)/2 \\implies 6 = 1+y \\implies y=5$.'},
            {'question': '¿Qué operación transforma el punto $(2, 3)$ en $(-2, 3)$?', 'options': {'A': 'Reflexión respecto al eje X', 'B': 'Reflexión respecto al eje Y', 'C': 'Rotación 180°', 'D': 'Traslación'}, 'answer': 'B', 'explanation': 'Si cambias el signo de X, estás reflejando al otro lado del eje vertical. Es como un espejo que cambia izquierda por derecha.'},
            {'question': 'El punto $A(-5, 0)$ se encuentra en:', 'options': {'A': 'El III Cuadrante', 'B': 'El II Cuadrante', 'C': 'El eje X', 'D': 'El eje Y'}, 'answer': 'C', 'explanation': 'Si la ordenada ($y$) es cero, no subiste ni bajaste. Estás sobre el eje X, específicamente 5 unidades a la izquierda del origen.'}
        ]
        render_multiple_choice_quiz(quiz, key_prefix="g01_quiz")

    with st.expander("🔑 Pauta Explicativa: Liga de los Genios (G01)", expanded=False):
        st.markdown(r"""
| Pregunta | Respuesta | La Voz del Maestro |
| :--- | :---: | :--- |
| **1** | **B** | **Galileo Tip:** "¡No te pierdas! Si la abscisa ($x$) es negativa y la ordenada ($y$) es positiva, significa que te moviste a la izquierda y subiste. Eso define al **Segundo Cuadrante**. ¡Visualízalo!" |
| **2** | **C** | **Newton Tip:** "Mira los puntos: $A(1, 5)$ y $B(1, -2)$. ¿Ves que el 1 no cambió? Solo te moviste verticalmente. Desde el 5 positivo hasta el 2 negativo hay 7 pasos de distancia. $|5 - (-2)| = 7$. No gastes energía en Pitágoras si la línea es recta." |
| **3** | **A** | **Hawking Tip:** "El punto medio es simplemente el promedio. Suma las X: $-4 + 2 = -2$, y la mitad es $-1$. Suma las Y: $8 + 2 = 10$, y la mitad es $5$. El centro de ese universo es $(-1, 5)$. ¡Es lógica pura!" |
| **4** | **B** | **Curie Tip:** "La simetría respecto al eje X es como un reflejo en el agua: lo que está arriba pasa abajo, pero la posición horizontal no cambia. El punto $(3,4)$ se convierte en $(3,-4)$." |
| **5** | **C** | **Galileo Tip:** "¡Cuidado aquí! En el tercer cuadrante te mueves a la izquierda (X negativo) y bajas (Y negativo). La combinación $(-,-)$ es la trampa final del plano." |
| **6** | **B** | **Newton Tip:** "Si no te mueves hacia los lados, estás clavado en la línea vertical. La línea vertical es donde la abscisa ($x$) es siempre cero." |
| **7** | **B** | **Hawking Tip:** "Es un clásico triángulo 3-4-5. La distancia del origen a $(x, y)$ es $\sqrt{x^2+y^2}$. $\sqrt{3^2+(-4)^2} = \sqrt{9+16} = 5$." |
| **8** | **A** | **Curie Tip:** "El punto medio es el promedio, así que deshaz el promedio: $2 = (1+x)/2 \implies 4 = 1+x \implies x=3$. $3 = (1+y)/2 \implies 6 = 1+y \implies y=5$." |
| **9** | **B** | **Galileo Tip:** "Si cambias el signo de X, estás reflejando al otro lado del eje vertical. Es como un espejo que cambia izquierda por derecha." |
| **10** | **C** | **Newton Tip:** "Si la ordenada ($y$) es cero, no subiste ni bajaste. Estás sobre el eje X, específicamente 5 unidades a la izquierda del origen." |
""")
