import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from pathlib import Path
import pytz
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

# Importaciones de tus módulos locales
from contenidos import CONTENIDOS
from styles import aplicar_estilos
from logros import registrar_clase
from visitas import registrar_visita, obtener_visitas

# =============================================================================
# 0. CONFIGURACIÓN DE PÁGINA Y AUTENTICACIÓN
# =============================================================================

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

# Cargar configuración desde tu config.yaml
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# [span_1](start_span)Inicializar el autenticador con tus credenciales y cookies[span_1](end_span)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Renderizar el formulario de Login en la pantalla principal
name, authentication_status, username = authenticator.login('Login', 'main')

# =============================================================================
# 1. LÓGICA SEGÚN ESTADO DE AUTENTICACIÓN
# =============================================================================

if authentication_status:
    # --- TODO EL CONTENIDO PROTEGIDO EMPIEZA AQUÍ ---

    # Inicialización de estados de sesión
    if 'eje_actual'         not in st.session_state: st.session_state.eje_actual         = None
    if 'subcat_actual'      not in st.session_state: st.session_state.subcat_actual      = None
    if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None
    if 'ir_a_pdf'           not in st.session_state: st.session_state.ir_a_pdf           = False
    if 'bienvenida_vista'   not in st.session_state: st.session_state.bienvenida_vista   = False
    if 'menu_actual'        not in st.session_state: st.session_state.menu_actual        = "🐉 Bienvenida"
    if 'ultimo_visto'       not in st.session_state: st.session_state.ultimo_visto       = None
    if 'nick_usuario'      not in st.session_state: st.session_state.nick_usuario       = username
    if 'crono_running'     not in st.session_state: st.session_state.crono_running      = False
    if 'crono_inicio'      not in st.session_state: st.session_state.crono_inicio       = None

    # Registrar visita una vez por sesión
    if 'visita_registrada' not in st.session_state:
        st.session_state.visita_registrada = True
        registrar_visita()

    COLORES = {
        "rojo":      "#c0392b",
        "verde":     "#1b5e20",
        "morado":    "#7b1fa2",
        "naranja":   "#e65100",
        "cian":      "#006064",
        "verde_bio": "#33691e",
        "ambar":     "#ff8f00",
    }

    # Aplicar tus estilos personalizados
    aplicar_estilos()

    # Sincronización de navegación en barra lateral
    if "nav_radio" not in st.session_state:
        st.session_state.nav_radio = st.session_state.menu_actual
    elif (st.session_state.get("prev_nav_radio") == st.session_state.nav_radio and
          st.session_state.nav_radio != st.session_state.menu_actual):
        st.session_state.nav_radio = st.session_state.menu_actual

    with st.sidebar:
        st.markdown(f"### 🐉 Bienvenido, {name}")
        # Botón de Logout integrado
        authenticator.logout('Cerrar Sesión', 'sidebar')
        st.divider()
        
        visitas_total = obtener_visitas()
        st.markdown(
            f'<div style="background:#eef2ff; border-radius:8px; padding:8px; font-size:12px; color:#3730a3; margin-top:4px; text-align:center;">'
            f'👁️ <b>{visitas_total:,}</b> visitas</div>',
            unsafe_allow_html=True
        )
        if st.session_state.ultimo_visto:
            st.markdown(
                f'<div style="background:#f0f0f0; border-radius:8px; padding:8px; font-size:12px; color:#555; margin-top:4px;">'
                f'🕐 Último visto:<br><b>{st.session_state.ultimo_visto}</b></div>',
                unsafe_allow_html=True
            )
        st.divider()
        menu = st.radio("Ir a:", ["🐉 Bienvenida", "🏠 Dashboard PAES", "📂 Biblioteca de PDFs"],
                        key="nav_radio")
        st.session_state.menu_actual = menu
        st.divider()
        st.caption("💬 _\"Sólo existen dos días en el año en los que no se puede hacer nada.\"_ — Dalai Lama")

    st.session_state.prev_nav_radio = st.session_state.nav_radio

    # --- LÓGICA DE MENÚS (DASHBOARD, BIBLIOTECA, BIENVENIDA) ---

    if menu == "🏠 Dashboard PAES":
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

        if st.session_state.eje_actual is None:
            st.markdown("""
            <style>
            .eje-select div.stButton > button {
                min-height: 80px !important;
                font-size: 17px !important;
                font-weight: bold !important;
                color: white !important;
                border: none !important;
                border-radius: 14px !important;
            }
            </style>
            """, unsafe_allow_html=True)
            st.markdown('<div class="eje-select">', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<style>.eje-select div[data-testid="column"]:nth-child(1) button{background:linear-gradient(135deg,#e74c3c,#c0392b)!important;}</style>', unsafe_allow_html=True)
                if st.button("🔢 Números", key="m_n", use_container_width=True):
                    st.session_state.eje_actual = "🔢 Números"; st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
            with c2:
                st.markdown('<style>.eje-select div[data-testid="column"]:nth-child(2) button{background:linear-gradient(135deg,#27ae60,#1b5e20)!important;}</style>', unsafe_allow_html=True)
                if st.button("📉 Álgebra", key="m_a", use_container_width=True):
                    st.session_state.eje_actual = "📉 Álgebra"; st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
            c3, c4 = st.columns(2)
            with c3:
                st.markdown('<style>.eje-select div[data-testid="column"]:nth-child(1) button{background:linear-gradient(135deg,#9b59b6,#7b1fa2)!important;}</style>', unsafe_allow_html=True)
                if st.button("📐 Geometría", key="m_g", use_container_width=True):
                    st.session_state.eje_actual = "📐 Geometría"; st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
            with c4:
                st.markdown('<style>.eje-select div[data-testid="column"]:nth-child(2) button{background:linear-gradient(135deg,#f39c12,#e65100)!important;}</style>', unsafe_allow_html=True)
                if st.button("📊 Datos y Azar", key="m_d", use_container_width=True):
                    st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        else:
            # Navegación superior dentro de los ejes
            st.markdown("""
            <style>
            div.stButton > button[data-testid="baseButton-secondary"] { background-color: inherit; }
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
                    st.session_state.menu_actual = "🐉 Bienvenida"; st.session_state.eje_actual = None; st.session_state.subcat_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
            with n_cols[1]:
                if st.button("N", key="n_n", use_container_width=True): st.session_state.eje_actual = "🔢 Números"; st.rerun()
            with n_cols[2]:
                if st.button("A", key="n_a", use_container_width=True): st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
            with n_cols[3]:
                if st.button("G", key="n_g", use_container_width=True): st.session_state.eje_actual = "📐 Geometría"; st.rerun()
            with n_cols[4]:
                if st.button("D", key="n_d", use_container_width=True): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()

            st.write("---")

            eje = st.session_state.eje_actual
            eje_data = CONTENIDOS.get(eje, {})
            subcats = eje_data.get("subcategorias", {})
            color = COLORES.get(eje_data.get("color_subcats", "rojo"), "#c0392b")

            if st.session_state.subcat_actual is None:
                st.markdown(f"## {eje}")
                # (Aquí iría tu lógica de cronómetro y listado de subcategorías...)
                for nombre_subcat, clases_subcat in subcats.items():
                    if st.button(nombre_subcat, key=f"sc_{nombre_subcat}", use_container_width=True):
                        st.session_state.subcat_actual = nombre_subcat
                        st.rerun()

            elif st.session_state.clase_seleccionada is None:
                subcat = st.session_state.subcat_actual
                clases = subcats.get(subcat, {})
                st.subheader(f"{eje} › {subcat}")
                for codigo, datos in clases.items():
                    if st.button(datos["label"], key=f"cls_{codigo}", use_container_width=True):
                        st.session_state.clase_seleccionada = codigo
                        st.rerun()
                if st.button("🔙 Volver", key="volver_subcat"):
                    st.session_state.subcat_actual = None; st.rerun()

            else:
                # Renderizado de la clase seleccionada
                subcat  = st.session_state.subcat_actual
                codigo  = st.session_state.clase_seleccionada
                clase   = subcats.get(subcat, {}).get(codigo)
                if clase:
                    clase["render"]()
                if st.button("📋 Volver al listado", key="volver_lista"):
                    st.session_state.clase_seleccionada = None; st.rerun()

    elif menu == "📂 Biblioteca de PDFs":
        st.subheader("Biblioteca de Recursos")
        # Tu lógica de PDFs...
        if st.button("🏠 Volver al Dashboard", key="back_pdf"):
            st.session_state.menu_actual = "🏠 Dashboard PAES"; st.rerun()

    elif menu == "🐉 Bienvenida":
        # Tu lógica de Bienvenida...
        st.title("Bienvenido a Lagrangianitos")
        if st.button("🚀 Empezar ahora", type="primary"):
            st.session_state.menu_actual = "🏠 Dashboard PAES"; st.rerun()

elif authentication_status == False:
    st.error('Usuario o contraseña incorrectos.')
    
elif authentication_status == None:
    st.warning('Por favor, ingresa tu usuario y contraseña para acceder.')

