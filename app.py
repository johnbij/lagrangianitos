import streamlit as st
from contenidos import CONTENIDOS
import textwrap # <--- NUEVO: Para limpiar sangrías del Markdown

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

# ==========================================
# 2. FUNCIONES DE DATOS
# ==========================================

def cargar_usuario(u, p):
    # TODO: Implement authentication via a new data source.
    # Google Sheets authentication has been removed.
    return None

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
                    st.rerun()
                else: st.error("Error")
    else:
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
