import streamlit as st
import os
from contenidos import CONTENIDOS

def scroll_top():
    # Inyecta un pequeño JS para subir al inicio de la página
    st.components.v1.html(
        "<script>window.parent.document.querySelector('section.main').scrollTo(0,0);</script>",
        height=0,
    )

def main():
    st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

    if 'page' not in st.session_state:
        st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state:
        st.session_state.materia_sel = None
    if 'clase_idx' not in st.session_state:
        st.session_state.clase_idx = 0

    if st.session_state.page != "Inicio":
        if st.button("⬅️ Volver al Menú Principal"):
            st.session_state.page = "Inicio"
            st.session_state.materia_sel = None
            st.session_state.clase_idx = 0
            st.rerun()

    if st.session_state.page == "Inicio":
        st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos</h1>", unsafe_allow_html=True)
        for materia in CONTENIDOS.keys():
            if st.button(materia, use_container_width=True):
                st.session_state.materia_sel = materia
                st.session_state.page = "Visor"
                st.rerun()

    elif st.session_state.page == "Visor":
        materia_data = CONTENIDOS[st.session_state.materia_sel]
        ejes = list(materia_data["subcategorias"].keys())
        eje_sel = st.selectbox("🎯 Selecciona un Eje:", ejes)
        
        clases_dict = materia_data["subcategorias"][eje_sel]
        ids_clases = list(clases_dict.keys())

        # Selector de clase
        clase_id = st.selectbox(
            "📖 Selecciona la Clase:",
            ids_clases,
            index=min(st.session_state.clase_idx, len(ids_clases)-1),
            format_func=lambda x: clases_dict[x]["label"]
        )

        st.divider()

        # Renderizar contenido
        if "render" in clases_dict[clase_id]:
            clases_dict[clase_id]["render"]()

        st.divider()

        # Botón Siguiente con Scroll al inicio
        curr_idx = ids_clases.index(clase_id)
        if curr_idx < len(ids_clases) - 1:
            if st.button(f"Siguiente: {ids_clases[curr_idx+1]} ➡️", use_container_width=True):
                st.session_state.clase_idx = curr_idx + 1
                scroll_top() # Sube la página
                st.rerun()
        else:
            st.success("🎉 ¡Eje completado!")

if __name__ == "__main__":
    main()
