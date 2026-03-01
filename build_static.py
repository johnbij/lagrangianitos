"""
Build script para generar el sitio estático con stlite.

Lee todos los archivos .py del proyecto y genera un index.html
que ejecuta la app Streamlit en el navegador usando stlite (WebAssembly).

Uso: python build_static.py
"""

import base64
import json
import os
import shutil

OUTPUT_DIR = "site"
ENTRYPOINT = "app.py"

STLITE_VERSION = "0.73.0"

REQUIREMENTS = ["matplotlib", "pandas", "numpy", "pytz"]

EXCLUDE_DIRS = {".git", "__pycache__", "site", ".devcontainer", ".github", ".streamlit"}

PDF_DIR = "pdfs"


def collect_python_files(root="."):
    """Recolecta todos los archivos .py del proyecto."""
    py_files = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fname in filenames:
            if fname.endswith(".py") and fname != "build_static.py":
                full_path = os.path.join(dirpath, fname)
                rel_path = os.path.relpath(full_path, root)
                with open(full_path, "r", encoding="utf-8") as f:
                    py_files[rel_path] = f.read()
    return py_files


def collect_pdf_files(pdf_dir):
    """Recolecta archivos PDF y retorna sus rutas relativas."""
    pdfs = []
    if os.path.isdir(pdf_dir):
        for fname in os.listdir(pdf_dir):
            if fname.endswith(".pdf"):
                pdfs.append(os.path.join(pdf_dir, fname))
    return pdfs


def generate_html(py_files):
    """Genera el HTML con stlite mountable."""
    files_js_entries = []
    for path, content in sorted(py_files.items()):
        escaped = json.dumps(content)
        files_js_entries.append(f"        {json.dumps(path)}: {escaped}")

    files_js = ",\n".join(files_js_entries)
    requirements_js = json.dumps(REQUIREMENTS)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lagrangianitos — PAES M1</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐉</text></svg>" />
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@stlite/mountable@{STLITE_VERSION}/build/stlite.css"
  />
  <style>
    html, body {{
      margin: 0;
      padding: 0;
      height: 100%;
      overflow: hidden;
    }}
    #root {{
      height: 100vh;
    }}
    /* Loading spinner */
    .stlite-loading {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      color: white;
      font-family: sans-serif;
    }}
    .stlite-loading .dragon {{
      font-size: 80px;
      animation: pulse 2s infinite;
    }}
    .stlite-loading .text {{
      margin-top: 20px;
      font-size: 20px;
      font-weight: bold;
      letter-spacing: 2px;
    }}
    .stlite-loading .subtext {{
      margin-top: 10px;
      font-size: 14px;
      opacity: 0.7;
    }}
    @keyframes pulse {{
      0%   {{ transform: scale(1);   opacity: 1; }}
      50%  {{ transform: scale(1.1); opacity: 0.8; }}
      100% {{ transform: scale(1);   opacity: 1; }}
    }}
  </style>
</head>
<body>
  <div id="root">
    <div class="stlite-loading">
      <div class="dragon">🐉</div>
      <div class="text">LAGRANGIANITOS</div>
      <div class="subtext">Cargando aplicación...</div>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@{STLITE_VERSION}/build/stlite.js"></script>
  <script>
    stlite.mount({{
      requirements: {requirements_js},
      entrypoint: {json.dumps(ENTRYPOINT)},
      files: {{
{files_js}
      }}
    }},
    document.getElementById("root")
    );
  </script>
</body>
</html>"""
    return html


def build():
    """Ejecuta el proceso de build completo."""
    print(f"🔨 Construyendo sitio estático en '{OUTPUT_DIR}/'...")

    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("📄 Recolectando archivos Python...")
    py_files = collect_python_files(".")
    print(f"   Encontrados: {len(py_files)} archivos .py")

    print("📝 Generando index.html con stlite...")
    html = generate_html(py_files)
    index_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"   ✅ {index_path} generado")

    print("📂 Copiando PDFs...")
    pdfs = collect_pdf_files(PDF_DIR)
    if pdfs:
        pdf_out = os.path.join(OUTPUT_DIR, PDF_DIR)
        os.makedirs(pdf_out, exist_ok=True)
        for pdf_path in pdfs:
            dest = os.path.join(OUTPUT_DIR, pdf_path)
            shutil.copy2(pdf_path, dest)
            print(f"   📄 {pdf_path} → {dest}")
    else:
        print("   ⚠️  No se encontraron PDFs")

    nojekyll_path = os.path.join(OUTPUT_DIR, ".nojekyll")
    with open(nojekyll_path, "w") as f:
        pass
    print(f"   ✅ {nojekyll_path} creado")

    print(f"\n🎉 Build completado: {OUTPUT_DIR}/")
    print(f"   Para probar localmente: python -m http.server -d {OUTPUT_DIR}")


if __name__ == "__main__":
    build()
