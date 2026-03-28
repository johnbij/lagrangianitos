import streamlit as st
import os
# Importamos el diccionario maestro desde contenidos.py
from contenidos import CONTENIDOS

def main():
    st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="centered")

    # --- 1. GESTIÓN DE ESTADOS (Navegación) ---
    if 'page' not in st.session_state:
        st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state:
        st.session_state.materia_sel = None
    if 'clase_idx' not in st.session_state:
        st.session_state.clase_idx = 0

    # --- 2. BOTÓN VOLVER (Siempre visible si no estás en el inicio) ---
    if st.session_state.page != "Inicio":
        if st.button("⬅️ Volver al Menú Principal"):
            st.session_state.page = "Inicio"
            st.session_state.materia_sel = None
            st.session_state.clase_idx = 0
            st.rerun()

    # --- 3. PÁGINA DE INICIO (Botones de Materias) ---
    if st.session_state.page == "Inicio":
        st.markdown("<h1 style='text-align:center;'>🐉 Lagrangianitos</h1>", unsafe_allow_html=True)
        st.subheader("Selecciona tu área de entrenamiento:")
        
        # Creamos los botones basados en las llaves de CONTENIDOS (Mate, Física, etc.)
        for materia in CONTENIDOS.keys():
            if st.button(materia, use_container_width=True):
                st.session_state.materia_sel = materia
                st.session_state.page = "Visor"
                st.rerun()
        
        st.divider()
        if st.button("📂 Biblioteca de PDFs", use_container_width=True):
            st.session_state.page = "PDFs"
            st.rerun()

    # --- 4. VISOR DE CLASES (La "Magia" de los desplegables) ---
    elif st.session_state.page == "Visor":
        materia_data = CONTENIDOS[st.session_state.materia_sel]
        st.title(f"{st.session_state.materia_sel}")

        # Nivel 1: Selector de Eje (Subcategoría)
        ejes = list(materia_data["subcategorias"].keys())
        eje_sel = st.selectbox("🎯 Selecciona un Eje:", ejes)

        # Nivel 2: Selector de Clase (Unidad)
        clases_dict = materia_data["subcategorias"][eje_sel]
        
        if clases_dict:
            ids_clases = list(clases_dict.keys())
            
            # Formateamos el selector para que muestre el "label" (ej: "📖 N01: Teoría...")
            clase_id = st.selectbox(
                "📖 Selecciona la Clase:",
                ids_clases,
                index=min(st.session_state.clase_idx, len(ids_clases)-1),
                format_func=lambda x: clases_dict[x]["label"]
            )

            st.divider()

            # --- EJECUCIÓN DEL RENDER (Contenido de la clase) ---
            render_func = clases_dict[clase_id]["render"]
            try:
                # Esto llama a render_N01(), render_A01(), etc.
                render_func()
            except Exception as e:
                st.error(f"Hubo un problema al cargar el contenido: {e}")

            # --- BOTÓN SIGUIENTE CLASE (Al final del texto) ---
            st.divider()
            curr_idx = ids_clases.index(clase_id)
            
            if curr_idx < len(ids_clases) - 1:
                proxima_clase_nombre = clases_dict[ids_clases[curr_idx + 1]]["label"]
                if st.button(f"Siguiente: {proxima_clase_nombre} ➡️", use_container_width=True):
                    st.session_state.clase_idx = curr_idx + 1
                    st.rerun()
            else:
                st.success("🎉 ¡Has completado todas las clases de este eje!")
        else:
            st.info("Aún no hay clases cargadas en este eje. ¡Vuelve pronto!")

    # --- 5. BIBLIOTECA DE PDFs ---
    elif st.session_state.page == "PDFs":
        st.header("📂 Biblioteca de Guías y Recursos")
        ruta = "pdfs"
        if not os.path.exists(ruta): os.makedirs(ruta)
        
        archivos = [f for f in os.listdir(ruta) if f.endswith('.pdf')]
        if archivos:
            for pdf in archivos:
                col_txt, col_btn = st.columns([3, 1])
                col_txt.write(f"📄 {pdf}")
                with open(os.path.join(ruta, pdf), "rb") as f:
                    col_btn.download_button("Descargar", f, file_name=pdf, key=pdf)
        else:
            st.info("La carpeta de PDFs está vacía. Sube archivos para verlos aquí.")

if __name__ == "__main__":
    main()
