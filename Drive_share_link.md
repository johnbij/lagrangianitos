# Drive (fuente de contenidos)

https://drive.google.com/drive/folders/1Y3m0ezKcVU40M4rBlqxEfMVMrL7HNYFP

## Reporte rápido del contenido actual en la web

- **Ejes temáticos en dashboard:** 4 (Números, Álgebra, Geometría, Datos y Azar).
- **Clases teóricas publicadas:** 65 (N01-N35, A01-A05, F01-F05, G01-G05, P01-P05, V01-V05, D01-D05, PB01-PB05).
- **Ejercitaciones en espera (placeholder):** 20 (NE01-NE05, AE01-AE05, GE01-GE05, DE01-DE05).
- **Biblioteca de PDFs:** ahora se renderiza **dinámicamente** leyendo todo `*.pdf` dentro de `/pdfs`, para que cualquier archivo sincronizado desde Drive aparezca automáticamente en la web.

## Flujo recomendado para sincronizar Drive → Web

1. Descargar el material del Drive compartido.
2. Guardar los archivos PDF en `/pdfs` del repositorio.
3. Ejecutar la app (`python -m streamlit run app.py`) y verificar que aparezcan en **📂 Biblioteca de PDFs**.
4. Si un PDF requiere título/descripción personalizada, agregarlo en `PDF_META` dentro de `app.py`.
