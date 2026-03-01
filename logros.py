import json
import os
from datetime import datetime

import pytz
import streamlit as st

RANKING_FILE = os.path.join(os.path.dirname(__file__), "ranking.json")


def _cargar_ranking():
    """Carga el ranking desde el archivo JSON."""
    if not os.path.exists(RANKING_FILE):
        return {}
    try:
        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def _guardar_ranking(data):
    """Guarda el ranking en el archivo JSON."""
    with open(RANKING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def registrar_usuario(nick):
    """Registra un nuevo usuario o retorna False si ya existe."""
    nick = nick.strip()
    if not nick:
        return False
    data = _cargar_ranking()
    clave = nick.lower()
    if clave in data:
        return False
    zona_cl = pytz.timezone("America/Santiago")
    ahora = datetime.now(zona_cl).isoformat()
    data[clave] = {
        "nick": nick,
        "clases_vistas": [],
        "fecha_registro": ahora,
        "ultima_actividad": ahora,
    }
    _guardar_ranking(data)
    return True


def registrar_clase(nick, codigo_clase):
    """Registra que un usuario vio una clase."""
    if not nick:
        return
    data = _cargar_ranking()
    clave = nick.strip().lower()
    if clave not in data:
        return
    if codigo_clase not in data[clave]["clases_vistas"]:
        data[clave]["clases_vistas"].append(codigo_clase)
    zona_cl = pytz.timezone("America/Santiago")
    data[clave]["ultima_actividad"] = datetime.now(zona_cl).isoformat()
    _guardar_ranking(data)


def obtener_ranking():
    """Retorna la lista de usuarios ordenada por clases vistas (desc)."""
    data = _cargar_ranking()
    usuarios = sorted(
        data.values(), key=lambda u: len(u["clases_vistas"]), reverse=True
    )
    return usuarios


def render_ranking():
    """Renderiza la página de ranking."""

    st.markdown(
        """
    <div style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 50%,#0f3460 100%);
                border-radius:20px; padding:30px 20px; text-align:center;
                color:white; margin-bottom:24px;">
        <div style="font-size:60px;">🏆</div>
        <div style="font-size:24px; font-weight:900; letter-spacing:2px;">RANKING LAGRANGIANITOS</div>
        <div style="font-size:14px; opacity:0.8; margin-top:6px;">
            Registra tu nick y sube en el ranking estudiando clases
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- Registro de nick ---
    nick_actual = st.session_state.get("nick_usuario", "")

    if not nick_actual:
        st.markdown("### 📝 Regístrate")
        col_input, col_btn = st.columns([3, 1])
        with col_input:
            nick_input = st.text_input(
                "Tu nick:", max_chars=20, key="input_nick",
                placeholder="Ej: DragonMath99",
                label_visibility="collapsed",
            )
        with col_btn:
            if st.button("Unirse 🚀", key="btn_registrar", use_container_width=True):
                if nick_input and nick_input.strip():
                    ok = registrar_usuario(nick_input)
                    if ok:
                        st.session_state.nick_usuario = nick_input.strip()
                        st.rerun()
                    else:
                        data = _cargar_ranking()
                        clave = nick_input.strip().lower()
                        if clave in data:
                            st.session_state.nick_usuario = data[clave]["nick"]
                            st.rerun()
                else:
                    st.warning("Escribe un nick válido.")
    else:
        st.markdown(
            f'<div style="background:#e8f5e9; border-radius:12px; padding:12px 16px;'
            f' font-size:15px; margin-bottom:16px;">'
            f'👤 Conectado como: <b>{nick_actual}</b></div>',
            unsafe_allow_html=True,
        )
        if st.button("Cambiar nick", key="btn_cambiar_nick"):
            st.session_state.nick_usuario = ""
            st.rerun()

    # --- Tabla de ranking ---
    st.markdown("### 🏅 Tabla de Ranking")
    usuarios = obtener_ranking()

    if not usuarios:
        st.info("Aún no hay participantes. ¡Sé el primero en registrarte!")
        return

    medallas = {0: "🥇", 1: "🥈", 2: "🥉"}

    for i, u in enumerate(usuarios):
        medalla = medallas.get(i, f"#{i+1}")
        n_clases = len(u["clases_vistas"])
        es_yo = nick_actual and u["nick"].lower() == nick_actual.lower()
        bg = "#fff8e1" if es_yo else "#ffffff"
        borde = "2px solid #f0c040" if es_yo else "1px solid #e0e0e0"
        st.markdown(
            f'<div style="background:{bg}; border:{borde}; border-radius:12px;'
            f' padding:12px 16px; margin-bottom:8px; display:flex;'
            f' align-items:center; gap:12px;">'
            f'<span style="font-size:24px; min-width:36px; text-align:center;">{medalla}</span>'
            f'<div style="flex:1;">'
            f'<div style="font-size:16px; font-weight:bold; color:#1a1a2e;">{u["nick"]}</div>'
            f'<div style="font-size:12px; color:#888;">📚 {n_clases} clase{"s" if n_clases != 1 else ""} vista{"s" if n_clases != 1 else ""}</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
