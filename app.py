import streamlit as st
from datetime import datetime
import pytz
import time
from streamlit_autorefresh import st_autorefresh

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state:
    st.session_state.eje_actual = None
if 'sub_seccion_actual' not in st.session_state:
    st.session_state.sub_seccion_actual = None
if 'rama_datos' not in st.session_state:
    st.session_state.rama_datos = None
if 'clase_seleccionada' not in st.session_state:
    st.session_state.clase_seleccionada = None

# --- ESTADOS DEL CRONÓMETRO ---
if 'cronometro_activo' not in st.session_state:
    st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state:
    st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. DICCIONARIO DE CONTENIDOS :::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# Para agregar una clase nueva: añade una entrada al diccionario del eje
# correspondiente. La key es el código (ej: "N01"), el valor es un dict
# con "label" (texto del botón) y "contenido" (función que renderiza el contenido).

def render_N01():
    st.markdown("""
    # <span style="color:darkblue">N01: Teoría de Conjuntos</span>
    ## <span style="color:darkblue">El Lenguaje Maestro</span>
    
    Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer 
    fronteras y a entender que todo gran sistema se basa en quién pertenece 
    a qué y bajo qué reglas.
    """, unsafe_allow_html=True)

def render_proximamente(codigo):
    st.info(f"🚀 La clase {codigo} está en desarrollo.")

CONTENIDOS = {
    "🔢 Números": {
        "Teoria": {
            "N01": {"label": "📖 N01: Teoría de Conjuntos",   "render": render_N01},
            "N02": {"label": "📖 N02: Próximamente",           "render": lambda: render_proximamente("N02")},
            "N03": {"label": "📖 N03: Próximamente",           "render": lambda: render_proximamente("N03")},
        },
        "Ejercitacion": {
            "NE01": {"label": "📝 NE01: Ejercicios Conjuntos", "render": lambda: render_proximamente("NE01")},
        },
    },
    "📉 Álgebra": {
        "Teoria": {
            "A01": {"label": "📖 A01: Expresiones Algebraicas", "render": lambda: render_proximamente("A01")},
            "A02": {"label": "📖 A02: Ecuaciones",              "render": lambda: render_proximamente("A02")},
        },
        "Ejercitacion": {
            "AE01": {"label": "📝 AE01: Ejercicios Álgebra",   "render": lambda: render_proximamente("AE01")},
        },
    },
    "📐 Geometría": {
        "Teoria": {
            "G01": {"label": "📖 G01: Geometría Plana",        "render": lambda: render_proximamente("G01")},
            "G02": {"label": "📖 G02: Geometría del Espacio",  "render": lambda: render_proximamente("G02")},
        },
        "Ejercitacion": {
            "GE01": {"label": "📝 GE01: Ejercicios Geometría", "render": lambda: render_proximamente("GE01")},
        },
    },
    "📊 Datos y Azar": {
        "Teoria": {
            "D01": {"label": "📖 D01: Estadística Descriptiva","render": lambda: render_proximamente("D01")},
            "D02": {"label": "📖 D02: Probabilidades",         "render": lambda: render_proximamente("D02")},
        },
        "Ejercitacion": {
            "DE01": {"label": "📝 DE01: Ejercicios Datos",     "render": lambda: render_proximamente("DE01")},
        },
    },
}

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. ESTILOS CSS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    [data-testid="stHorizontalBlock"] { display: flex !important; flex-direction: row !important; flex-wrap: nowrap !important; gap: 4px !important; }
    [data-testid="stHorizontalBlock"] > div { flex: 1 1 0% !important; min-width: 0 !important; }
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; }

    .cat-container div.stButton > button { 
        min-height: 85px !important; border-radius: 15px !important; margin-bottom: 15px !important;
        width: 100% !important; font-size: 18px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important; box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
    
    .crono-digital {
        font-family: 'Courier New', monospace;
        font-size: 35px;
        font-weight: bold;
        color: #3b71ca;
        text-align: center;
        width: 100%;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 5. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":

    # --- AUTO REFRESH solo cuando el cronómetro está activo ---
    if st.session_state.cronometro_activo:
        st_autorefresh(interval=1000, limit=None, key="crono_refresh")

    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    
    paes_date = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    delta = paes_date - ahora
    dias = delta.days
    horas = delta.seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días: {dias}</div><div class="timer-item">Hrs: {horas}</div></div>', unsafe_allow_html=True)

    st.write("")

    # --- BOTONES DE EJES ---
    if st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        if c1.button("🔢 Números",     key="m_n", use_container_width=True): st.session_state.eje_actual = "🔢 Números";      st.rerun()
        if c2.button("📉 Álgebra",     key="m_a", use_container_width=True): st.session_state.eje_actual = "📉 Álgebra";      st.rerun()
        c3, c4 = st.columns(2)
        if c3.button("📐 Geometría",   key="m_g", use_container_width=True): st.session_state.eje_actual = "📐 Geometría";    st.rerun()
        if c4.button("📊 Datos y Azar",key="m_d", use_container_width=True): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

    else:
        # --- BARRA DE NAVEGACIÓN SUPERIOR ---
        n_cols = st.columns(5)
        if n_cols[0].button("🏠", key="n_h"):
            st.session_state.eje_actual = None
            st.session_state.sub_seccion_actual = None
            st.session_state.clase_seleccionada = None
            st.session_state.rama_datos = None
            st.rerun()
        if n_cols[1].button("N", key="n_n"):
            st.session_state.eje_actual = "🔢 Números";      st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[2].button("A", key="n_a"):
            st.session_state.eje_actual = "📉 Álgebra";      st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[3].button("G", key="n_g"):
            st.session_state.eje_actual = "📐 Geometría";    st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[4].button("D", key="n_d"):
            st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.session_state.rama_datos = None; st.rerun()

        st.write("---")

        # --- CRONÓMETRO ---
        with st.container(border=True):
            col_btn, col_crono = st.columns([1, 2])
            with col_btn:
                if not st.session_state.cronometro_activo:
                    if st.button("▶️ Iniciar", key="btn_start_crono"):
                        st.session_state.tiempo_inicio = time.time()
                        st.session_state.cronometro_activo = True
                        st.rerun()
                else:
                    if st.button("⏹️ Detener", key="btn_stop_crono"):
                        st.session_state.cronometro_activo = False
                        st.rerun()
            with col_crono:
                if st.session_state.cronometro_activo and st.session_state.tiempo_inicio:
                    secs = int(time.time() - st.session_state.tiempo_inicio)
                    st.markdown(f'<span class="crono-digital">{secs//60:02d}:{secs%60:02d}</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

        # --- NAVEGACIÓN DE CONTENIDO BASADA EN DICCIONARIO ---
        eje = st.session_state.eje_actual
        clases_del_eje = CONTENIDOS.get(eje, {})

        if st.session_state.sub_seccion_actual is None:
            st.markdown(f"## {eje}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📘 Teoría y Conceptos",      key="bt_t"): st.session_state.sub_seccion_actual = "Teoria";      st.rerun()
            if st.button("📝 Ejercitación y Práctica", key="bt_e"): st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.clase_seleccionada is None:
            sub = st.session_state.sub_seccion_actual
            st.subheader(f"📚 Clases de {eje}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            clases = clases_del_eje.get(sub, {})
            for codigo, datos in clases.items():
                if st.button(datos["label"], key=f"cls_{codigo}"):
                    st.session_state.clase_seleccionada = codigo
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            if st.button("🔙 Volver", key="volver_sub"):
                st.session_state.sub_seccion_actual = None
                st.rerun()

        else:
            sub    = st.session_state.sub_seccion_actual
            codigo = st.session_state.clase_seleccionada
            clase  = clases_del_eje.get(sub, {}).get(codigo)

            st.markdown('<div class="clase-box">', unsafe_allow_html=True)
            if clase:
                clase["render"]()
            else:
                st.warning(f"Clase {codigo} no encontrada.")
            st.markdown('</div>', unsafe_allow_html=True)

            if st.button("🔙 Volver al listado de clases", key="volver_lista"):
                st.session_state.clase_seleccionada = None
                st.rerun()

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos")
