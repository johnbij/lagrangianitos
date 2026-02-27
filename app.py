import streamlit as st
from datetime import datetime
import pytz
import time
from streamlit_autorefresh import st_autorefresh

from contenidos import CONTENIDOS
from styles import aplicar_estilos

# =============================================================================
# 1. CONFIGURACIÓN Y ESTADOS
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
if 'sub_seccion_actual' not in st.session_state: st.session_state.sub_seccion_actual = None
if 'rama_datos'         not in st.session_state: st.session_state.rama_datos         = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None
if 'ir_a_pdf'           not in st.session_state: st.session_state.ir_a_pdf           = False
if 'cronometro_activo'  not in st.session_state: st.session_state.cronometro_activo  = False
if 'tiempo_inicio'      not in st.session_state: st.session_state.tiempo_inicio       = None

# =============================================================================
# 2. ESTILOS
# =============================================================================

aplicar_estilos()

# =============================================================================
# 3. BARRA LATERAL
# =============================================================================

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# =============================================================================
# 4. DASHBOARD PRINCIPAL
# =============================================================================

if menu == "🏠 Dashboard PAES":

    if st.session_state.cronometro_activo:
        st_autorefresh(interval=1000, limit=None, key="crono_refresh")

    zona_cl = pytz.timezone('America/Santiago')
    ahora   = datetime.now(zona_cl)

    st.markdown(
        f'<div class="header-azul">'
        f'<div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div>'
        f'<div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    paes_date = datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl)
    delta = paes_date - ahora
    dias  = delta.days
    horas = delta.seconds // 3600
    st.markdown(
        f'<div class="header-rojo">'
        f'<div class="timer-item">⏳ Días: {dias}</div>'
        f'<div class="timer-item">Hrs: {horas}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    st.write("")

    # ── SECCIÓN PDF ──────────────────────────────────────────────────────────
    if st.session_state.get('ir_a_pdf'):
        st.session_state.ir_a_pdf = False
        st.header("📂 Biblioteca de Recursos en PDF")
        st.info("🚀 Aquí irán los materiales descargables. Próximamente.")
        if st.button("🔙 Volver al inicio", key="volver_pdf"):
            st.rerun()

    # ── PANTALLA INICIAL: selección de eje ──────────────────────────────────
    elif st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="eje-numeros">', unsafe_allow_html=True)
            if st.button("🔢 Números",   key="m_n", use_container_width=True): st.session_state.eje_actual = "🔢 Números"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="eje-algebra">', unsafe_allow_html=True)
            if st.button("📉 Álgebra",   key="m_a", use_container_width=True): st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<div class="eje-geometria">', unsafe_allow_html=True)
            if st.button("📐 Geometría", key="m_g", use_container_width=True): st.session_state.eje_actual = "📐 Geometría"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="eje-datos">', unsafe_allow_html=True)
            if st.button("📊 Datos y Azar", key="m_d", use_container_width=True): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.write("")
        col_iz, col_pdf, col_der = st.columns([1, 4, 1])
        with col_pdf:
            st.markdown('<div class="pdf-btn">', unsafe_allow_html=True)
            if st.button("📄 Materiales descargables en PDF", key="m_pdf", use_container_width=True):
                st.session_state.ir_a_pdf = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    # ── DENTRO DE UN EJE ────────────────────────────────────────────────────
    else:
        # Barra de navegación
        n_cols = st.columns(5)
        if n_cols[0].button("🏠", key="n_h"):
            st.session_state.eje_actual = st.session_state.sub_seccion_actual = st.session_state.clase_seleccionada = st.session_state.rama_datos = None
            st.rerun()
        if n_cols[1].button("N", key="n_n"): st.session_state.eje_actual = "🔢 Números";      st.session_state.sub_seccion_actual = st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[2].button("A", key="n_a"): st.session_state.eje_actual = "📉 Álgebra";      st.session_state.sub_seccion_actual = st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[3].button("G", key="n_g"): st.session_state.eje_actual = "📐 Geometría";    st.session_state.sub_seccion_actual = st.session_state.clase_seleccionada = None; st.rerun()
        if n_cols[4].button("D", key="n_d"): st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_seccion_actual = st.session_state.clase_seleccionada = st.session_state.rama_datos = None; st.rerun()

        st.write("---")

        # Cronómetro
        with st.container(border=True):
            col_btn, col_crono = st.columns([1, 2])
            with col_btn:
                if not st.session_state.cronometro_activo:
                    if st.button("▶️ Iniciar", key="btn_start_crono"):
                        st.session_state.tiempo_inicio    = time.time()
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

        # Navegación de contenido
        eje            = st.session_state.eje_actual
        clases_del_eje = CONTENIDOS.get(eje, {})

        if st.session_state.sub_seccion_actual is None:
            st.markdown(f"## {eje}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            if st.button("📘 Teoría y Conceptos",      key="bt_t"): st.session_state.sub_seccion_actual = "Teoria";       st.rerun()
            if st.button("📝 Ejercitación y Práctica", key="bt_e"): st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        elif st.session_state.clase_seleccionada is None:
            sub = st.session_state.sub_seccion_actual
            st.subheader(f"📚 Clases de {eje}")
            st.markdown('<div class="cat-container">', unsafe_allow_html=True)
            for codigo, datos in clases_del_eje.get(sub, {}).items():
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

            if clase:
                clase["render"]()
            else:
                st.warning(f"Clase {codigo} no encontrada.")

            if st.button("🔙 Volver al listado de clases", key="volver_lista"):
                st.session_state.clase_seleccionada = None
                st.rerun()

# =============================================================================
# 5. BIBLIOTECA DE PDFs
# =============================================================================

elif menu == "📂 Biblioteca de PDFs":
    st.header("📂 Biblioteca de Recursos")
