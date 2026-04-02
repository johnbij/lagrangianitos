import streamlit as st
from streamlit_gsheets import GSheetsConnection
from contenidos import CONTENIDOS
import textwrap # <--- NUEVO: Para limpiar sangrías del Markdown
import pandas as pd
from datetime import datetime
import pytz

_TZ = pytz.timezone("America/Santiago")

# ==========================================
# 1. CONFIGURACIÓN INICIAL
# ==========================================
st.set_page_config(page_title="Lagrangianitos - M1", page_icon="🐉", layout="wide")

# Inicialización de estados
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'page' not in st.session_state: st.session_state.page = "Inicio"
if 'clase_target' not in st.session_state: st.session_state.clase_target = None
if 'materia_sel' not in st.session_state: st.session_state.materia_sel = None
if 'eje_sel' not in st.session_state: st.session_state.eje_sel = None

conn = st.connection("gsheets", type=GSheetsConnection)

# ==========================================
# 2. FUNCIONES DE DATOS
# ==========================================

def cargar_usuario(u, p):
    try:
        df = conn.read(worksheet="Usuarios", ttl=0)
        res = df[(df['User'].astype(str) == str(u)) & (df['Pass'].astype(str) == str(p))]
        return res.iloc[0].to_dict() if not res.empty else None
    except Exception:
        return None

def _ahora():
    return datetime.now(_TZ)

def registrar_acceso(user):
    """Agrega una fila a Logs_Acceso al iniciar sesión."""
    try:
        now = _ahora()
        try:
            df = conn.read(worksheet="Logs_Acceso", ttl=0)
            if df is None or df.empty:
                df = pd.DataFrame(columns=["User", "Fecha", "Hora", "IP_Info"])
        except Exception:
            df = pd.DataFrame(columns=["User", "Fecha", "Hora", "IP_Info"])
        nueva = pd.DataFrame([{
            "User": user,
            "Fecha": now.strftime("%Y-%m-%d"),
            "Hora": now.strftime("%H:%M:%S"),
            "IP_Info": "Acceso Web",
        }])
        conn.update(worksheet="Logs_Acceso", data=pd.concat([df, nueva], ignore_index=True))
    except Exception:
        pass

def registrar_clase(user, materia, eje, clase_id, clase_label):
    """Agrega una fila a Clases cuando el usuario navega a una clase."""
    try:
        now = _ahora()
        try:
            df = conn.read(worksheet="Clases", ttl=0)
            if df is None or df.empty:
                df = pd.DataFrame(columns=["User", "Fecha", "Hora", "Materia", "Eje", "Clase_ID", "Clase"])
        except Exception:
            df = pd.DataFrame(columns=["User", "Fecha", "Hora", "Materia", "Eje", "Clase_ID", "Clase"])
        nueva = pd.DataFrame([{
            "User": user,
            "Fecha": now.strftime("%Y-%m-%d"),
            "Hora": now.strftime("%H:%M:%S"),
            "Materia": materia,
            "Eje": eje,
            "Clase_ID": clase_id,
            "Clase": clase_label,
        }])
        conn.update(worksheet="Clases", data=pd.concat([df, nueva], ignore_index=True))
    except Exception:
        pass

# ==========================================
# 4. LÓGICA DE NAVEGACIÓN (VISOR)
# ==========================================

def main():
    if not st.session_state.logged_in:
        st.title("LAGRANGIANITOS")
        with st.form("login"):
            u = st.text_input("Usuario")
            p = st.text_input("Pass", type="password")
            if st.form_submit_button("🚀 Entrar"):
                ud = cargar_usuario(u, p)
                if ud: 
                    st.session_state.logged_in = True
                    st.session_state.user_data = ud
                    st.session_state.acceso_registrado = False
                    st.rerun()
                else: st.error("Error")
    else:
        # Registrar acceso una sola vez por sesión al ingresar
        if not st.session_state.get("acceso_registrado", False):
            registrar_acceso(st.session_state.user_data['User'])
            st.session_state.acceso_registrado = True

        if st.session_state.page == "Inicio":
            st.title(f"Bienvenido, {st.session_state.user_data['User']}")
            st.divider()
            for mat in CONTENIDOS.keys():
                if st.button(f"📘 {mat}", use_container_width=True):
                    st.session_state.materia_sel = mat
                    st.session_state.page = "Visor"
                    st.session_state.clase_target = None
                    st.rerun()
            if st.button("🚪 Salir"): 
                st.session_state.logged_in = False
                st.rerun()

        elif st.session_state.page == "Visor":
            if st.button("⬅️ Hub"): 
                st.session_state.page = "Inicio"
                st.rerun()
            
            m_data = CONTENIDOS[st.session_state.materia_sel]
            ejes_disponibles = list(m_data["subcategorias"].keys())
            
            col_e, col_c = st.columns(2)
            
            with col_e:
                nuevo_eje = st.selectbox("🎯 Eje:", ejes_disponibles)
                if nuevo_eje != st.session_state.eje_sel:
                    st.session_state.eje_sel = nuevo_eje
                    st.session_state.clase_target = None
            
            clases_dict = m_data["subcategorias"][st.session_state.eje_sel]
            lista_ids = list(clases_dict.keys())

            if st.session_state.clase_target not in lista_ids:
                st.session_state.clase_target = lista_ids[0]

            with col_c:
                clase_actual = st.selectbox(
                    "📖 Clase:", 
                    lista_ids,
                    index=lista_ids.index(st.session_state.clase_target),
                    format_func=lambda x: clases_dict[x]["label"],
                    key=f"sel_{st.session_state.clase_target}_{st.session_state.eje_sel}"
                )
                st.session_state.clase_target = clase_actual

            # Registrar visita a clase cuando cambia
            clave_clase = f"{st.session_state.materia_sel}|{st.session_state.eje_sel}|{clase_actual}"
            if st.session_state.get("ultima_clase_registrada") != clave_clase:
                registrar_clase(
                    st.session_state.user_data['User'],
                    st.session_state.materia_sel,
                    st.session_state.eje_sel,
                    clase_actual,
                    clases_dict[clase_actual]["label"],
                )
                st.session_state.ultima_clase_registrada = clave_clase

            st.divider()

            # --- RENDERIZADO CORREGIDO ---
            if "render" in clases_dict[clase_actual]:
                # Ejecutamos la función de la clase. 
                # IMPORTANTE: Dentro de tus funciones render en contenidos.py, 
                # asegúrate de usar st.markdown()
                clases_dict[clase_actual]["render"]()
                
                st.divider()
                idx = lista_ids.index(clase_actual)
                b1, b2 = st.columns(2)
                
                with b1:
                    if idx > 0:
                        if st.button(f"⬅️ {clases_dict[lista_ids[idx-1]]['label']}", use_container_width=True):
                            st.session_state.clase_target = lista_ids[idx-1]
                            st.rerun()
                
                with b2:
                    if idx < len(lista_ids) - 1:
                        if st.button(f"{clases_dict[lista_ids[idx+1]]['label']} ➡️", use_container_width=True):
                            st.session_state.clase_target = lista_ids[idx+1]
                            st.rerun()
                    else:
                        st.success("🏁 Eje completado")

if __name__ == "__main__":
    main()
