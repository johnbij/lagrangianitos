import streamlit as st
from datetime import datetime
import pytz
import time
from streamlit_autorefresh import st_autorefresh

from contenidos import CONTENIDOS
from styles import aplicar_estilos
from logros import registrar_clase, render_ranking

# =============================================================================
# 1. CONFIGURACIÓN Y ESTADOS
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual      = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None
if 'ir_a_pdf'           not in st.session_state: st.session_state.ir_a_pdf           = False
if 'cronometro_activo'  not in st.session_state: st.session_state.cronometro_activo  = False
if 'tiempo_inicio'      not in st.session_state: st.session_state.tiempo_inicio      = None
if 'bienvenida_vista'   not in st.session_state: st.session_state.bienvenida_vista   = False
if 'menu_actual'        not in st.session_state: st.session_state.menu_actual        = "🐉 Bienvenida"
if 'ultimo_visto'       not in st.session_state: st.session_state.ultimo_visto       = None
if 'nick_usuario'      not in st.session_state: st.session_state.nick_usuario      = ""

COLORES = {
    "rojo":    "#c0392b",
    "verde":   "#1b5e20",
    "morado":  "#7b1fa2",
    "naranja": "#e65100",
}

# =============================================================================
# 2. ESTILOS
# =============================================================================

aplicar_estilos()

# =============================================================================
# 3. BARRA LATERAL
# =============================================================================

with st.sidebar:
    st.markdown("### 🐉 Lagrangianitos")
    if st.session_state.ultimo_visto:
        st.markdown(
            f'<div style="background:#f0f0f0; border-radius:8px; padding:8px; font-size:12px; color:#555; margin-top:4px;">'
            f'🕐 Último visto:<br><b>{st.session_state.ultimo_visto}</b></div>',
            unsafe_allow_html=True
        )
    st.divider()
    menu = st.radio("Ir a:", ["🐉 Bienvenida", "🏠 Dashboard PAES", "🏆 Ranking", "📂 Biblioteca de PDFs"],
                    index=["🐉 Bienvenida", "🏠 Dashboard PAES", "🏆 Ranking", "📂 Biblioteca de PDFs"].index(st.session_state.menu_actual))
    st.session_state.menu_actual = menu
    st.divider()
    st.caption("💬 _\"Sólo existen dos días en el año en los que no se puede hacer nada.\"_ — Dalai Lama")

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
        f'<div class="titulo-header">🐉 Lagrangianitos — PAES M1</div>'
        f'<div class="info-header">📍 Santiago · 🕒 {ahora.strftime("%H:%M")}</div>'
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

    # ── PANTALLA INICIAL ─────────────────────────────────────────────────────
    if st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")

        st.markdown("""
        <style>
        .eje-grid div.stButton > button {
            min-height: 70px !important;
            font-size: 16px !important;
            font-weight: bold !important;
            color: white !important;
            border: none !important;
            border-radius: 14px !important;
            margin-bottom: 6px !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="eje-grid">', unsafe_allow_html=True)

        # Fila 1
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<style>div[data-testid="column"]:nth-child(1) button{background:linear-gradient(135deg,#e74c3c,#c0392b)!important;}</style>', unsafe_allow_html=True)
            if st.button("🔢 Números", key="m_n", use_container_width=True):
                st.session_state.eje_actual = "🔢 Números"; st.rerun()
        with c2:
            st.markdown('<style>div[data-testid="column"]:nth-child(2) button{background:linear-gradient(135deg,#27ae60,#1b5e20)!important;}</style>', unsafe_allow_html=True)
            if st.button("📉 Álgebra", key="m_a", use_container_width=True):
                st.session_state.eje_actual = "📉 Álgebra"; st.rerun()

        # Fila 2
        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<style>div[data-testid="column"]:nth-child(1) button{background:linear-gradient(135deg,#9b59b6,#7b1fa2)!important;}</style>', unsafe_allow_html=True)
            if st.button("📐 Geometría", key="m_g", use_container_width=True):
                st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        with c4:
            st.markdown('<style>div[data-testid="column"]:nth-child(2) button{background:linear-gradient(135deg,#f39c12,#e65100)!important;}</style>', unsafe_allow_html=True)
            if st.button("📊 Datos y Azar", key="m_d", use_container_width=True):
                st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

        st.write("")
        st.markdown('<div class="pdf-btn">', unsafe_allow_html=True)
        if st.button("📄 Materiales descargables en PDF", key="m_pdf", use_container_width=True):
            st.session_state.menu_actual = "📂 Biblioteca de PDFs"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # ── DENTRO DE UN EJE ────────────────────────────────────────────────────
    else:
        # CSS nth-child para colorear cada botón de la barra por posición
        st.markdown("""
        <style>
        div.stButton > button[data-testid="baseButton-secondary"] {
            background-color: inherit;
        }
        /* Barra nav: 5 columnas */
        [data-testid="stHorizontalBlock"]:first-of-type > div:nth-child(1) button { background: linear-gradient(135deg,#6C63FF,#1a1a2e) !important; color: white !important; border: none !important; }
        [data-testid="stHorizontalBlock"]:first-of-type > div:nth-child(2) button { background: linear-gradient(135deg,#e74c3c,#c0392b) !important; color: white !important; border: none !important; }
        [data-testid="stHorizontalBlock"]:first-of-type > div:nth-child(3) button { background: linear-gradient(135deg,#27ae60,#1b5e20) !important; color: white !important; border: none !important; }
        [data-testid="stHorizontalBlock"]:first-of-type > div:nth-child(4) button { background: linear-gradient(135deg,#9b59b6,#7b1fa2) !important; color: white !important; border: none !important; }
        [data-testid="stHorizontalBlock"]:first-of-type > div:nth-child(5) button { background: linear-gradient(135deg,#f39c12,#e65100) !important; color: white !important; border: none !important; }
        </style>
        """, unsafe_allow_html=True)

        n_cols = st.columns(5)
        with n_cols[0]:
            if st.button("🏠", key="n_h", use_container_width=True):
                st.session_state.eje_actual = None; st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        with n_cols[1]:
            if st.button("N", key="n_n", use_container_width=True): st.session_state.eje_actual = "🔢 Números";      st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        with n_cols[2]:
            if st.button("A", key="n_a", use_container_width=True): st.session_state.eje_actual = "📉 Álgebra";      st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        with n_cols[3]:
            if st.button("G", key="n_g", use_container_width=True): st.session_state.eje_actual = "📐 Geometría";    st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
        with n_cols[4]:
            if st.button("D", key="n_d", use_container_width=True): st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()

        st.write("---")

        # Cronómetro
        with st.container(border=True):
            col_btn, col_crono = st.columns([1, 2])
            with col_btn:
                if not st.session_state.cronometro_activo:
                    if st.button("▶️ Iniciar", key="btn_start_crono"):
                        st.session_state.tiempo_inicio = time.time(); st.session_state.cronometro_activo = True; st.rerun()
                else:
                    if st.button("⏹️ Detener", key="btn_stop_crono"):
                        st.session_state.cronometro_activo = False; st.rerun()
            with col_crono:
                if st.session_state.cronometro_activo and st.session_state.tiempo_inicio:
                    secs = int(time.time() - st.session_state.tiempo_inicio)
                    st.markdown(f'<span class="crono-digital">{secs//60:02d}:{secs%60:02d}</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="crono-digital" style="opacity:0.2;">00:00</span>', unsafe_allow_html=True)

        # ── NAVEGACIÓN ───────────────────────────────────────────────────────
        eje      = st.session_state.eje_actual
        eje_data = CONTENIDOS.get(eje, {})
        subcats  = eje_data.get("subcategorias", {})
        color    = COLORES.get(eje_data.get("color_subcats", "rojo"), "#c0392b")

        # NIVEL 1: subcategorías
        if st.session_state.subcat_actual is None:
            st.markdown(f"## {eje}")

            for nombre_subcat, clases_subcat in subcats.items():
                total = len(clases_subcat)
                disponibles = sum(
                    1 for c in clases_subcat.values()
                    if c["render"].__name__ != "<lambda>"
                )
                if disponibles == total:
                    badge = f"✅ {disponibles}/{total}"
                elif disponibles > 0:
                    badge = f"🟡 {disponibles}/{total}"
                else:
                    badge = f"🔒 0/{total}"

                col_btn, col_badge = st.columns([4, 1])
                with col_btn:
                    st.markdown(f"""
                    <style>
                    div[data-testid="stHorizontalBlock"]:has(+ *) div[data-testid="column"]:first-child button {{
                        background: linear-gradient(135deg, {color}, {color}cc) !important;
                        color: white !important;
                        border: none !important;
                        border-radius: 14px !important;
                        min-height: 65px !important;
                        font-size: 16px !important;
                        font-weight: bold !important;
                    }}
                    </style>
                    """, unsafe_allow_html=True)
                    if st.button(nombre_subcat, key=f"sc_{nombre_subcat}", use_container_width=True):
                        st.session_state.subcat_actual = nombre_subcat
                        st.rerun()
                with col_badge:
                    st.markdown(
                        f'<div style="text-align:center; font-size:15px; '
                        f'font-weight:bold; padding-top:18px;">{badge}</div>',
                        unsafe_allow_html=True
                    )

        # NIVEL 2: lista de clases
        elif st.session_state.clase_seleccionada is None:
            subcat = st.session_state.subcat_actual
            clases = subcats.get(subcat, {})
            st.subheader(f"{eje} › {subcat}")
            # CSS para botones de lista
            st.markdown("""
            <style>
            div.stButton > button p {
                font-size: 16px !important;
                font-weight: 600 !important;
            }
            </style>
            """, unsafe_allow_html=True)
            for codigo, datos in clases.items():
                es_real = datos["render"].__name__ != "<lambda>"
                if es_real:
                    if st.button(datos["label"], key=f"cls_{codigo}", use_container_width=True):
                        st.session_state.clase_seleccionada = codigo
                        st.rerun()
                else:
                    # Botón deshabilitado con candado
                    st.button(f"🔒 {datos['label'].split(': ',1)[-1] if ': ' in datos['label'] else datos['label']}",
                              key=f"cls_{codigo}", use_container_width=True, disabled=True)
            if st.button("🔙 Volver", key="volver_subcat"):
                st.session_state.subcat_actual = None; st.rerun()

        # NIVEL 3: contenido
        else:
            subcat  = st.session_state.subcat_actual
            codigo  = st.session_state.clase_seleccionada
            clase   = subcats.get(subcat, {}).get(codigo)

            # Calcular anterior / siguiente (solo entre clases reales)
            codigos   = list(subcats.get(subcat, {}).keys())
            codigos_reales = [c for c in codigos if subcats[subcat][c]["render"].__name__ != "<lambda>"]
            idx       = codigos.index(codigo)
            idx_real  = codigos_reales.index(codigo) if codigo in codigos_reales else -1
            anterior  = codigos[idx - 1] if idx > 0 else None
            siguiente = codigos[idx + 1] if idx < len(codigos) - 1 else None

            # Scroll automático al inicio
            st.markdown("""
            <script>
                window.scrollTo(0, 0);
            </script>
            """, unsafe_allow_html=True)
            # Truco más confiable para scroll en Streamlit
            st.markdown('<div id="top-anchor"></div>', unsafe_allow_html=True)
            st.markdown("""
            <style>
            #top-anchor { position: absolute; top: 0; }
            </style>
            <script>
            document.getElementById('top-anchor')?.scrollIntoView();
            </script>
            """, unsafe_allow_html=True)

            # CSS para los botones de navegación con color del eje
            st.markdown(f"""
            <style>
            .nav-clase div.stButton > button {{
                background: linear-gradient(135deg, {color}, {color}cc) !important;
                color: white !important;
                border: none !important;
                border-radius: 10px !important;
                min-height: 50px !important;
                font-size: 13px !important;
                font-weight: bold !important;
                width: 100% !important;
            }}
            </style>
            """, unsafe_allow_html=True)

            def barra_navegacion(sufijo):
                st.markdown('<div class="nav-clase">', unsafe_allow_html=True)
                col_ant, col_volver, col_sig = st.columns([2, 1, 2])
                with col_ant:
                    if anterior:
                        label_ant = subcats[subcat][anterior]["label"]
                        if st.button(f"← {label_ant}", key=f"btn_anterior_{sufijo}", use_container_width=True):
                            st.session_state.clase_seleccionada = anterior
                            st.rerun()
                with col_volver:
                    if st.button("📋", key=f"volver_lista_{sufijo}", use_container_width=True, help="Volver al listado"):
                        st.session_state.clase_seleccionada = None
                        st.rerun()
                with col_sig:
                    if siguiente:
                        label_sig = subcats[subcat][siguiente]["label"]
                        if st.button(f"{label_sig} →", key=f"btn_siguiente_{sufijo}", use_container_width=True):
                            st.session_state.clase_seleccionada = siguiente
                            st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

            # Guardar último visto
            label_actual = subcats.get(subcat, {}).get(codigo, {}).get("label", codigo)
            st.session_state.ultimo_visto = f"{subcat} · {label_actual}"

            # Registrar clase vista para el ranking
            if st.session_state.nick_usuario:
                registrar_clase(st.session_state.nick_usuario, codigo)

            # Indicador de posición + barra de progreso
            total        = len(codigos)
            reales_count = len(codigos_reales)
            pos_texto    = f"Clase {idx + 1} de {total}"
            progreso_pct = int((reales_count / total) * 100)
            bloques_llenos = int(progreso_pct / 10)
            barra = "█" * bloques_llenos + "░" * (10 - bloques_llenos)

            st.markdown(
                f'<div style="text-align:right; color:#888; font-size:14px; font-weight:600; margin-bottom:2px;">'
                f'📍 {subcat} · {pos_texto}</div>'
                f'<div style="text-align:right; color:{color}; font-size:12px; margin-bottom:6px;">'
                f'{barra} {reales_count}/{total} disponibles</div>',
                unsafe_allow_html=True
            )

            # Barra ARRIBA
            barra_navegacion("top")
            st.write("---")

            # Tiempo estimado de lectura (aprox 200 palabras/min)
            import inspect
            try:
                src = inspect.getsource(clase["render"])
                palabras = len(src.split())
                mins = max(1, round(palabras / 200))
                st.markdown(
                    f'<div style="color:#aaa; font-size:13px; margin-bottom:10px;">⏱ Tiempo estimado: ~{mins} min de lectura</div>',
                    unsafe_allow_html=True
                )
            except Exception:
                pass

            # Contenido de la clase
            if clase:
                clase["render"]()
            else:
                st.warning(f"Clase {codigo} no encontrada.")

            # Mensaje motivacional si es la última clase real de la subcategoría
            es_ultima_real = (codigo == codigos_reales[-1]) if codigos_reales else False
            no_hay_siguiente_real = siguiente is None or subcats[subcat][siguiente]["render"].__name__ == "<lambda>"
            if es_ultima_real and no_hay_siguiente_real:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,{color},{color}88);
                            border-radius:16px; padding:20px; text-align:center;
                            color:white; margin:20px 0;">
                    <div style="font-size:36px;">🏆</div>
                    <div style="font-size:16px; font-weight:bold; margin:8px 0;">
                        ¡Completaste {subcat}!
                    </div>
                    <div style="font-size:13px; opacity:0.9;">
                        Has terminado las clases disponibles de esta sección. ¡Sigue así! 💪
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Barra ABAJO
            st.write("---")
            barra_navegacion("bot")

            # Botón volver arriba
            st.markdown("""
            <div style="text-align:center; margin-top:10px;">
                <a href="#top-anchor" style="color:#888; font-size:13px; text-decoration:none;">
                    ↑ Volver al inicio de la clase
                </a>
            </div>
            """, unsafe_allow_html=True)

elif menu == "🏆 Ranking":
    render_ranking()

elif menu == "📂 Biblioteca de PDFs":
    if st.button("← Volver", key="back_pdf"):
        st.session_state.menu_actual = "🏠 Dashboard PAES"
        st.rerun()
    st.markdown("""
    <style>
    .pdf-card {
        background: white;
        border-radius: 14px;
        padding: 16px;
        margin-bottom: 12px;
        border-left: 5px solid #6C63FF;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .pdf-icon { font-size: 30px; }
    .pdf-nombre { font-size: 15px; font-weight: bold; color: #1a1a2e; margin-bottom: 3px; }
    .pdf-desc { font-size: 12px; color: #666; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="background:linear-gradient(135deg,#6C63FF,#1a1a2e);
                border-radius:16px; padding:20px; color:white;
                text-align:center; margin-bottom:20px;">
        <div style="font-size:36px;">📂</div>
        <div style="font-size:20px; font-weight:900; letter-spacing:2px;">BIBLIOTECA DE RECURSOS</div>
        <div style="font-size:13px; opacity:0.8; margin-top:4px;">Material oficial PAES M1 para descargar</div>
    </div>
    """, unsafe_allow_html=True)

    PDFS = [
        {
            "archivo": "pdfs/2026V-PaesM1.pdf",
            "nombre":  "PAES M1 — Verano 2026",
            "desc":    "Prueba oficial PAES Matemática 1 · Versión Verano 2026",
            "icono":   "📝"
        },
        {
            "archivo": "pdfs/2026V-ClavijeroPaesM1.pdf",
            "nombre":  "Clavijero PAES M1 — Verano 2026",
            "desc":    "Clavijero oficial con respuestas · Versión Verano 2026",
            "icono":   "🔑"
        },
        {
            "archivo": "pdfs/2027I-TemarioPaesM1.pdf",
            "nombre":  "Temario PAES M1 — Invierno 2027",
            "desc":    "Temario oficial PAES Matemática 1 · Versión Invierno 2027",
            "icono":   "📋"
        },
    ]

    for pdf in PDFS:
        st.markdown(f"""
        <div class="pdf-card">
            <div class="pdf-icon">{pdf["icono"]}</div>
            <div>
                <div class="pdf-nombre">{pdf["nombre"]}</div>
                <div class="pdf-desc">{pdf["desc"]}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        with open(pdf["archivo"], "rb") as f:
            st.download_button(
                label=f"⬇️ Descargar {pdf['nombre']}",
                data=f,
                file_name=pdf["archivo"].split("/")[-1],
                mime="application/pdf",
                key=f"dl_{pdf['archivo']}",
                use_container_width=True
            )

elif menu == "🐉 Bienvenida":
    st.markdown("""
    <style>
    .bienvenida-hero {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        color: white;
        margin-bottom: 24px;
    }
    .bienvenida-dragon { font-size: 80px; margin-bottom: 10px; }
    .bienvenida-titulo { font-size: 28px; font-weight: 900; letter-spacing: 2px; margin-bottom: 8px; }
    .bienvenida-lema {
        font-size: 17px;
        color: #f0c040;
        font-style: italic;
        font-weight: bold;
        margin-bottom: 16px;
    }
    .bienvenida-sub {
        font-size: 15px; font-weight: 600; opacity: 0.95;
        max-width: 500px; margin: 0 auto; line-height: 1.6;
    }

    .card-eje {
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 15px;
        margin-bottom: 8px;
    }

    .seccion-titulo {
        font-size: 20px;
        font-weight: bold;
        color: #1a1a2e;
        border-left: 5px solid #6C63FF;
        padding-left: 12px;
        margin: 24px 0 12px 0;
    }

    .pill {
        display: inline-block;
        background: #f0f0f0;
        border-radius: 20px;
        padding: 6px 14px;
        margin: 4px;
        font-size: 13px;
        color: #333;
    }
    </style>

    <div class="bienvenida-hero">
        <div class="bienvenida-dragon">🐉</div>
        <div class="bienvenida-titulo">LAGRANGIANITOS</div>
        <div class="bienvenida-lema">"Enseñamos conceptos, no solo tricks"</div>
        <div class="bienvenida-sub">
            Tu plataforma de preparación PAES M1.<br>
            Matemática con profundidad, desde los fundamentos hasta la prueba. 🚀
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Ejes disponibles
    st.markdown('<div class="seccion-titulo">📚 Contenidos del curso</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card-eje" style="background:linear-gradient(135deg,#e74c3c,#c0392b);">🔢 Números<br><small>Conjuntos · Operatoria · Razones</small></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-eje" style="background:linear-gradient(135deg,#9b59b6,#7b1fa2);">📐 Geometría<br><small>Figuras · Área y Volumen · Vectores</small></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card-eje" style="background:linear-gradient(135deg,#27ae60,#1b5e20);">📉 Álgebra<br><small>Álgebra · Funciones</small></div>', unsafe_allow_html=True)
        st.markdown('<div class="card-eje" style="background:linear-gradient(135deg,#f39c12,#e65100);">📊 Datos y Azar<br><small>Estadística · Probabilidad</small></div>', unsafe_allow_html=True)

    # CTA
    st.write("")
    if st.button("🚀 Ir al Dashboard", key="cta_dashboard", use_container_width=True):
        st.session_state.menu_actual = "🏠 Dashboard PAES"
        st.rerun()

    # Metodología
    st.markdown('<div class="seccion-titulo">🛡️ Nuestra metodología</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#f9f9f9; border-radius:14px; padding:16px; line-height:2;">
    <span class="pill">📖 Clases con historia y contexto</span>
    <span class="pill">📊 Visualizaciones interactivas</span>
    <span class="pill">🧠 Profundidad conceptual</span>
    <span class="pill">📝 Ejercitación dirigida</span>
    <span class="pill">⏱️ Cronómetro de estudio</span>
    <span class="pill">📄 Material descargable</span>
    </div>
    """, unsafe_allow_html=True)
