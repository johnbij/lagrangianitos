import streamlit as st
from datetime import datetime
import pytz

# =============================================================================
# 📖 CAPÍTULO 0: BIBLIOTECA DE CONTENIDOS (MARKDOWN)
# =============================================================================
# Aquí defines el texto de tus clases. Al estar al margen izquierdo, 
# evitamos el error de renderizado (fondo gris).

CLASE_N01_TEORIA = """
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás...

### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
A finales del siglo XIX, un hombre decidió desafiar a la teología...

### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
* **El Universo ($\mathcal{U}$)**
* **El Vacío ($\emptyset$)**

### 🛡️ 4. Operaciones de "1000 Puntos"
| Operación | Símbolo | Significado |
| :--- | :---: | :--- |
| **Unión** | $\cup$ | Agrupar todos. |

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**
"""

# Aquí insertarás luego: CLASE_N01_EJEMPLOS, CLASE_N01_CUESTIONARIO, etc.

# =============================================================================
# 🎨 CAPÍTULO I: CONFIGURACIÓN Y ESTILOS (FRONT-END)
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .clase-box { 
        background-color: white; padding: 40px; border-radius: 15px; border: 1px solid #e0e0e0; 
        color: #1a1a1a; line-height: 1.6; box-shadow: 0px 4px 10px rgba(0,0,0,0.03);
    }
    /* Estilos para botones de navegación superior */
    [data-testid="stHorizontalBlock"] button { width: 100% !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# ⚙️ CAPÍTULO II: SISTEMA DE NAVEGACIÓN Y ESTADOS
# =============================================================================

if 'eje' not in st.session_state: st.session_state.eje = None
if 'seccion' not in st.session_state: st.session_state.seccion = None
if 'clase' not in st.session_state: st.session_state.clase = None

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# =============================================================================
# 🖥️ CAPÍTULO III: RENDERIZADO DEL DASHBOARD
# =============================================================================

if menu == "🏠 Dashboard PAES":
    # --- Encabezado Dinámico ---
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul">🐉 Lagrangianitos Hub | 🕒 {ahora.strftime("%H:%M")}</div>', unsafe_allow_html=True)
    
    # --- Navegación Superior (Capítulos del Libro) ---
    nav = st.columns(5)
    if nav[0].button("🏠"): st.session_state.eje = None; st.rerun()
    if nav[1].button("N"): st.session_state.eje = "🔢 Números"; st.rerun()
    if nav[2].button("A"): st.session_state.eje = "📉 Álgebra"; st.rerun()
    if nav[3].button("G"): st.session_state.eje = "📐 Geometría"; st.rerun()
    if nav[4].button("D"): st.session_state.eje = "📊 Datos y Azar"; st.rerun()

    st.divider()

    # --- Lógica de Visualización de Folios ---
    if st.session_state.eje is None:
        st.info("Selecciona un eje temático arriba para comenzar.")
    
    elif st.session_state.clase is None:
        st.header(f"Secciones de {st.session_state.eje}")
        if st.button("📖 N01: Teoría de Conjuntos"):
            st.session_state.clase = "N01"
            st.rerun()
            
    else:
        # Aquí es donde el "Libro" imprime el contenido del Capítulo 0
        if st.session_state.clase == "N01":
            st.markdown('<div class="clase-box">', unsafe_allow_html=True)
            st.markdown(CLASE_N01_TEORIA)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🔙 Volver al Índice"):
            st.session_state.clase = None
            st.rerun()
    
