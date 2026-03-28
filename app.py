import streamlit as st
from contenidos import CONTENIDOS

def scroll_to_top():
    """Inyecta JavaScript para volver arriba al cambiar de clase."""
    st.components.v1.html(
        """
        <script>
            var mainContent = window.parent.document.querySelector('section.main');
            if (mainContent) {
                mainContent.scrollTo({top: 0, behavior: 'auto'});
            }
        </script>
        """,
        height=0,
    )

def login():
    st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos Hub</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        user = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")
        if st.button("Ingresar", use_container_width=True):
            # ACCESO PARA TI: admin / admin
            if user == "admin" and password == "admin":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos")

def main():
    st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        login()
        return

    # --- ESTADOS DE NAVEGACIÓN ---
    if 'page' not in st.session_state:
        st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state:
        st.session_state.materia_sel = None
    if 'eje_sel' not in st.session_state:
        st.session_state.eje_sel = None
    if 'clase_idx' not in st.session_state:
        st.session_state.clase_idx = 0

    with st.sidebar:
        st.title("🚀 Navegación")
        if st.button("🏠 Menú Principal", use_container_width=True):
            st.session_state.page = "Inicio"
            st.rerun()
        st.divider()
        if st.button("🚪 Cerrar Sesión", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    if st.session_state.page == "Inicio":
        st.markdown("<h1 style='text-align:center;'>📚 Entrenamiento M1</h1>", unsafe_allow_html=True)
        materias = list(CONTENIDOS.keys())
        cols = st.columns(len(materias))
        for i, materia in enumerate(materias):
            with cols[i]:
                if st.button(materia, use_container_width=True, height=100):
                    st.session_state.materia_sel = materia
                    st.session_state.page = "Visor"
                    st.session_state.eje_sel = list(CONTENIDOS[materia]["subcategorias"].keys())[0]
                    st.session_state.clase_idx = 0
                    st.rerun()

    elif st.session_state.page == "Visor":
        materia_data = CONTENIDOS[st.session_state.materia_sel]
        col_eje, col_clase = st.columns(2)
        ejes_list = list(materia_data["subcategorias"].keys())
        
        with col_eje:
            idx_eje = ejes_list.index(st.session_state.eje_sel) if st.session_state.eje_sel in ejes_list else 0
            eje_escogido = st.selectbox("🎯 Eje Temático:", ejes_list, index=idx_eje)
            if eje_escogido != st.session_state.eje_sel:
                st.session_state.eje_sel = eje_escogido
                st.session_state.clase_idx = 0
                st.rerun()

        clases_dict = materia_data["subcategorias"][st.session_state.eje_sel]
        ids_clases = list(clases_dict.keys())
        
        with col_clase:
            idx_clase = min(st.session_state.clase_idx, len(ids_clases) - 1)
            clase_id = st.selectbox(
                "📖 Clase:", ids_clases, index=idx_clase,
                format_func=lambda x: clases_dict[x]["label"]
            )
            if ids_clases.index(clase_id) != st.session_state.clase_idx:
                st.session_state.clase_idx = ids_clases.index(clase_id)
                st.rerun()

        st.divider()
        if "render" in clases_dict[clase_id]:
            clases_dict[clase_id]["render"]()

        st.divider()
        c1, spacer, c2 = st.columns([1, 2, 1])
        with c1:
            if st.session_state.clase_idx > 0:
                if st.button("⬅️ Clase Anterior", use_container_width=True):
                    st.session_state.clase_idx -= 1
                    scroll_to_top()
                    st.rerun()
        with c2:
            if st.session_state.clase_idx < len(ids_clases) - 1:
                if st.button("Siguiente Clase ➡️", use_container_width=True):
                    st.session_state.clase_idx += 1
                    scroll_to_top()
                    st.rerun()

if __name__ == "__main__":
    main()
