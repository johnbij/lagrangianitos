import streamlit as st
from datetime import datetime
import pytz
import time

# =============================================================================
# 📖 CAPÍTULO 0: BIBLIOTECA DE CONTENIDOS (MARKDOWN AL BORDE IZQUIERDO)
# =============================================================================
# NO TOCAR LA INDENTACIÓN DE ESTAS VARIABLES. Deben estar pegadas a la izquierda.

CLASE_N01_TEORIA = """
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás...

### 🛡️ 4. Operaciones de "1000 Puntos"
| Operación | Símbolo | Significado Lógico | Carpintería Técnica |
| :--- | :---: | :--- | :--- |
| **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ | Agrupar todos los elementos. |
| **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ | Solo los que se repiten. |

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**
"""

# =============================================================================
# 🎨 CAPÍTULO I: FRONT-END Y ESTILOS
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; align-items: center; }
    .timer-item { font-size: 16px; font-weight: bold; font-family: 'Courier New', Courier, monospace; }

    /* Fix para botones de navegación */
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 45px !important; font-weight: bold !important; border-radius: 8px !important; }

    .clase-box { 
        background-color: white; padding: 40px; border-radius: 15px; border: 1px solid #e0e0e0; 
        color: #1a1a1a; line-height: 1.6; box-shadow: 0px 4px 10px rgba(0,0,0,0.03);
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# ⚙️ CAPÍTULO II: SISTEMA DE NAVEGACIÓN
# =============================================================================

if 'eje' not in st.session_state: st.session_state.eje = None
if 'sub_seccion' not in st.session_state: st.session_state.sub_seccion = None
if 'clase' not in st.session_state: st.session_state.clase = None

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# =============================================================================
# 🖥️ CAPÍTULO III: RENDERIZADO CON CRONÓMETRO ACTIVO
# =============================================================================

if menu == "🏠 Dashboard PAES":
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    meta_paes = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    countdown = meta_paes - ahora

    # BARRA AZUL (Intacta)
    st.markdown(f'''
        <div class="header-azul">
            <div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div>
            <div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div>
        </div>
    ''', unsafe_allow_html=True)
    
    # BARRA ROJA CON CRONÓMETRO
    segundos_restantes = countdown.seconds % 60
    st.markdown(f'''
        <div class="header-rojo">
            <div class="timer-item">⏳ Días: {countdown.days}</div>
            <div class="timer-item">Horas: {countdown.seconds // 3600}</div>
            <div class="timer-item">Min: {(countdown.seconds // 60) % 60}</div>
            <div class="timer-item" style="color: #ffcccc;">Seg: {segundos_restantes}</div>
        </div>
    ''', unsafe_allow_html=True)

    st.write("") 

    # BOTONES DE NAVEGACIÓN
    n_cols = st.columns(5)
    iconos = ["🏠", "N", "A", "G", "D"]
    if n_cols[0].button(iconos[0]): st.session_state.eje = None; st.session_state.sub_seccion = None; st.session_state.clase = None; st.rerun()
    if n_cols[1].button(iconos[1]): st.session_state.eje = "🔢 Números"; st.session_state.sub_seccion = None; st.rerun()
    if n_cols[2].button(iconos[2]): st.session_state.eje = "📉 Álgebra"; st.session_state.sub_seccion = None; st.rerun()
    if n_cols[3].button(iconos[3]): st.session_state.eje = "📐 Geometría"; st.session_state.sub_seccion = None; st.rerun()
    if n_cols[4].button(iconos[4]): st.session_state.eje = "📊 Datos y Azar"; st.session_state.sub_seccion = None; st.rerun()

    st.divider()

    if st.session_state.eje is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números"): st.session_state.eje = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra"): st.session_state.eje = "📉 Álgebra"; st.rerun()
    
    elif st.session_state.sub_seccion is None:
        st.markdown(f"## {st.session_state.eje}")
        if st.button("📘 Teoría y Conceptos"): st.session_state.sub_seccion = "Teoria"; st.rerun()
        if st.button("📝 Ejercitación y Práctica"): st.session_state.sub_seccion = "Ejercitacion"; st.rerun()

    elif st.session_state.clase is None:
        st.subheader(f"📚 Material de {st.session_state.eje}")
        if st.button("📖 N01: Teoría de Conjuntos"): st.session_state.clase = "N01"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.sub_seccion = None; st.rerun()

    else:
        # PANTALLA DE CLASE FINAL (Sin errores de fondo gris)
        if st.session_state.clase == "N01":
            st.markdown('<div class="clase-box">', unsafe_allow_html=True)
            st.markdown(CLASE_N01_TEORIA)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("🔙 Volver al listado"): st.session_state.clase = None; st.rerun()

    # Pequeño delay para que el cronómetro se sienta vivo si se refresca
    # Nota: Streamlit refresca al interactuar, para cronómetro real 1s se usa st_autorefresh
    
