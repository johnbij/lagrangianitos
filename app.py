import streamlit as st
from datetime import datetime
import pytz

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS (UI/UX) :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* Header Azul - Limpio y con espacio */
    .header-azul { 
        background-color: #3b71ca; 
        padding: 15px; 
        border-radius: 15px 15px 0 0; 
        color: white; 
        text-align: center; 
    }
    .titulo-header { 
        font-size: 20px; 
        font-weight: bold; 
        margin-bottom: 5px; 
    }
    .info-header { 
        font-size: 14px; 
        opacity: 0.9;
    }
    
    /* Countdown Rojo */
    .header-rojo {
        background-color: #cc0000; 
        padding: 10px; 
        color: white; 
        display: flex; 
        justify-content: space-around; 
        border-radius: 0 0 15px 15px;
    }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* Botones y Contenedores */
    div.stButton > button { 
        min-height: 60px !important; 
        border-radius: 12px !important; 
        border: 1px solid #e0e0e0 !important; 
        color: #31333F !important; 
    }
    .clase-box { max-width: 900px; margin: 0 auto; padding: 10px; line-height: 1.6; }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil")
    st.markdown("**Barton** \n*Estudiante de Ingeniería en FCFM*")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    # ::: Cabecera Azul (Sin segundos, con Ciudad y País) :::
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f"""
        <div class="header-azul">
            <div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div>
            <div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div>
        </div>
        """, unsafe_allow_html=True)

    # ::: Cabecera Roja :::
    dias = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    horas = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600
    st.markdown(f"""
        <div class="header-rojo">
            <div class="timer-item">⏳ Días: {dias}</div>
            <div class="timer-item">Hrs: {horas}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # ::: Lógica de Ejes :::
    if st.session_state.eje_actual is None:
        st.subheader("📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números\nConjuntos y operatoria", key="main_n", use_container_width=True):
            st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if c2.button("📉 Álgebra\nFunciones y más", key="main_a", use_container_width=True):
            st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
    
    # ::: SECCIÓN: NÚMEROS :::
    else:
        # Navegación superior compacta
        n_ejes = ["🏠 Inicio", "🔢 Números", "📉 Álgebra"]
        cols_nav = st.columns(3)
        for i, n in enumerate(n_ejes):
            if cols_nav[i].button(n, key=f"nav_top_{i}", use_container_width=True):
                st.session_state.eje_actual = None if n == "🏠 Inicio" else n
                st.session_state.sub_seccion_actual = None; st.rerun()

        if st.session_state.eje_actual == "🔢 Números":
            if st.session_state.sub_seccion_actual is None:
                st.subheader("📌 Categorías")
                cs1, cs2 = st.columns(2)
                if cs1.button("📦 Conjuntos Numéricos", use_container_width=True):
                    st.session_state.sub_seccion_actual = "N01"; st.rerun()
                if cs2.button("➕ Operatoria", use_container_width=True): pass
            
            # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            # ::: CLASE N01: TEORÍA DE CONJUNTOS ::::::::::::::::::::::::::::::
            # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            elif st.session_state.sub_seccion_actual == "N01":
                st.markdown('<div class="clase-box">', unsafe_allow_html=True)
                st.markdown("""
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

---
### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás...
...
---
> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla". — **Georg Cantor**
""", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca")
            
