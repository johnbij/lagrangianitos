import streamlit as st
import os
from contenidos import BIBLIOTECA_CONTENIDOS

def main():
    st.set_page_config(page_title="Lagrangianitos", layout="centered")

    # --- ESTADO DE LA SESIÓN ---
    if 'page' not in st.session_state:
        st.session_state.page = "Inicio"
    if 'materia_sel' not in st.session_state:
        st.session_state.materia_sel = None
    if 'eje_sel' not in st.session_state:
        st.session_state.eje_sel = None
    if 'unidad_idx' not in st.session_state:
        st.session_state.unidad_idx = 0

    # --- NAVEGACIÓN: BOTÓN VOLVER ---
    if st.session_state.page != "Inicio":
        if st.button("⬅️ Volver al Inicio"):
            st.session_state.page = "Inicio"
            st.session_state.materia_sel = None
            st.session_state.eje_sel = None
            st.session_state.unidad_idx = 0
            st.rerun()

    # --- PÁGINA: INICIO ---
    if st.session_state.page == "Inicio":
        st.title("🚀 Lagrangianitos")
        st.subheader("Selecciona tu Materia")
        
        materias = list(BIBLIOTECA_CONTENIDOS.keys())
        for mat in materias:
            if st.button(f"📚 {mat}", use_container_width=True):
                st.session_state.materia_sel = mat
                st.session_state.page = "Ejes"
                st.rerun()
        
        st.divider()
        if st.button("📂 Biblioteca PDFs", use_container_width=True):
            st.session_state.page = "PDFs"
            st.rerun()

    # --- PÁGINA: SELECCIÓN DE EJE Y CLASE ---
    elif st.session_state.page == "Ejes":
        mat = st.session_state.materia_sel
        st.header(f"🎯 {mat}")
        
        # 1. Selector de Eje
        ejes_disponibles = list(BIBLIOTECA_CONTENIDOS[mat].keys())
        eje_sel = st.selectbox("Selecciona un Eje:", ["-- Selecciona --"] + ejes_disponibles)
        
        if eje_sel != "-- Selecciona --":
            st.session_state.eje_sel = eje_sel
            unidades_dict = BIBLIOTECA_CONTENIDOS[mat][eje_sel]
            
            if unidades_dict:
                unidades_lista = list(unidades_dict.keys())
                
                # 2. Selector de Unidad (Clase)
                unidad_id = st.selectbox(
                    "Selecciona la Clase:", 
                    unidades_lista, 
                    index=st.session_state.unidad_idx
                )
                
                # --- RENDER DE CONTENIDO ---
                datos = unidades_dict[unidad_id]
                st.divider()
                st.title(f"📖 {unidad_id}: {datos['titulo']}")
                
                # Video
                st.video(f"https://www.youtube.com/watch?v={datos['video_id']}")
                
                # Espacio para el contenido (clases.py)
                st.info("💡 Tip: Revisa el material de apoyo antes de contestar el cuestionario.")
                
                # Cuestionario
                with st.expander(f"❓ {datos['cuestionario']}"):
                    st.write("Selecciona la alternativa correcta:")
                    # Ejemplo de pregunta
                    st.radio("1. ¿Cuál es el conjunto vacío?", ["A", "B", "C", "D"], key=f"q1_{unidad_id}")

                # --- BOTÓN SIGUIENTE CLASE ---
                st.divider()
                curr_idx = unidades_lista.index(unidad_id)
                if curr_idx < len(unidades_lista) - 1:
                    if st.button("Próxima Clase ➡️"):
                        st.session_state.unidad_idx = curr_idx + 1
                        st.rerun()
                else:
                    st.success("✅ ¡Completaste todos los videos de este eje!")
            else:
                st.warning("Próximamente contenido para este eje.")

    # --- PÁGINA: PDFs ---
    elif st.session_state.page == "PDFs":
        st.header("📂 Biblioteca de Guías")
        ruta_pdfs = "pdfs"
        
        if not os.path.exists(ruta_pdfs):
            os.makedirs(ruta_pdfs)
            
        archivos = [f for f in os.listdir(ruta_pdfs) if f.endswith('.pdf')]
        
        if archivos:
            for pdf in archivos:
                col1, col2 = st.columns([3, 1])
                col1.write(f"📄 {pdf}")
                with open(os.path.join(ruta_pdfs, pdf), "rb") as f:
                    col2.download_button("Descargar", f, file_name=pdf, key=pdf)
        else:
            st.info("No hay guías disponibles todavía. Sube tus archivos a la carpeta 'pdfs'.")

if __name__ == "__main__":
    main()
