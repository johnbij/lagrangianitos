import streamlit as st
from datetime import datetime
import pytz
import time

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 1. CONFIGURACIÓN Y ESTADOS :::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.set_page_config(page_title="Lagrangianitos Hub", page_icon="🐉", layout="wide")

if 'eje_actual' not in st.session_state: st.session_state.eje_actual = None
if 'sub_eje_actual' not in st.session_state: st.session_state.sub_eje_actual = None
if 'sub_seccion_actual' not in st.session_state: st.session_state.sub_seccion_actual = None
if 'clase_seleccionada' not in st.session_state: st.session_state.clase_seleccionada = None

if 'cronometro_activo' not in st.session_state: st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state: st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. EL "MATADOR" DE CAJAS Y ARREGLO DE CELULAR :::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    /* 1. Mata el espacio blanco de arriba y los contenedores vacíos */
    .block-container { padding-top: 1rem !important; }
    [data-testid="stVerticalBlock"] > div:empty { display: none !important; }
    div[data-testid="stVerticalBlock"] > div:has(div[class*="stMarkdown"] > p:empty) { display: none !important; }

    /* 2. Estilo de los Headers */
    .header-azul { background-color: #3b71ca; padding: 10px; border-radius: 12px 12px 0 0; color: white; text-align: center; }
    .header-rojo { background-color: #cc0000; padding: 8px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 12px 12px; margin-bottom: 15px; font-size: 14px; }
    
    /* 3. Cronómetro (Azul Digital) */
    .crono-box { background-color: white; padding: 5px; border-radius: 10px; text-align: center; border: 2px solid #3b71ca; margin-bottom: 10px; }
    .crono-font { font-family: 'Courier New', monospace; font-size: 28px; font-weight: bold; color: #3b71ca; }

    /* 4. BOTONES RESPONSIVOS (Para que no se desarmen en el celu) */
    .nav-container { display: flex; justify-content: space-between; gap: 5px; margin-bottom: 15px; }
    .nav-btn { flex: 1; padding: 10px 5px; background: #f8f9fa; border: 1px solid #ddd; border-radius: 8px; text-align: center; font-weight: bold; cursor: pointer; text-decoration: none; color: black; font-size: 14px; }

    /* 5. Estilo de la Clase (Pegada arriba) */
    .clase-white-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e0e0e0;
        margin-top: -20px; /* Sube el contenido para borrar el aire */
    }
    </style>
    """, unsafe_allow_html=True)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 3. BARRA LATERAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with st.sidebar:
    st.markdown("# 🚀 Perfil\n**Barton**")
    st.divider()
    menu = st.radio("Ir a:", ["🏠 Dashboard PAES", "📂 Biblioteca de PDFs"])
    st.divider()
    st.write("Sólo existen dos días en el año en los que no se puede hacer nada... Dalai Lama")

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 4. DASHBOARD :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    # Cabecera
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><b>🐉 Lagrangianitos. M1</b><br><small>📍 Santiago | {ahora.strftime("%H:%M")}</small></div>', unsafe_allow_html=True)
    dias_paes = (datetime(2026, 6, 15, tzinfo=zona_cl) - ahora).days
    st.markdown(f'<div class="header-rojo">⏳ Días: {dias_paes} </div>', unsafe_allow_html=True)

    # Cronómetro
    col_btn, col_timer = st.columns([1, 2])
    with col_btn:
        if not st.session_state.cronometro_activo:
            if st.button("▶️ Iniciar"): 
                st.session_state.tiempo_inicio = time.time()
                st.session_state.cronometro_activo = True
                st.rerun()
        else:
            if st.button("⏹️ Parar"): 
                st.session_state.cronometro_activo = False
                st.rerun()
    with col_timer:
        if st.session_state.cronometro_activo:
            t = int(time.time() - st.session_state.tiempo_inicio)
            st.markdown(f'<div class="crono-box"><span class="crono-font">{t//60:02d}:{t%60:02d}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="crono-box" style="opacity:0.3;"><span class="crono-font">00:00</span></div>', unsafe_allow_html=True)

    # NAVEGACIÓN (Botones que NO se desarman en el celu)
    st.write("Ir a:")
    c1, c2, c3, c4, c5 = st.columns(5)
    if c1.button("🏠"): st.session_state.eje_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if c2.button("N"): st.session_state.eje_actual = "🔢 Números"; st.session_state.clase_seleccionada = None; st.rerun()
    if c3.button("A"): st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
    if c4.button("G"): st.session_state.eje_actual = "📐 Geometría"; st.rerun()
    if c5.button("D"): st.session_state.eje_actual = "📊 Datos"; st.rerun()

    st.divider()

    # --- LÓGICA DE CONTENIDO ---
    if st.session_state.eje_actual == "🔢 Números" and st.session_state.clase_seleccionada is None:
        st.subheader("🛡️ Conjuntos")
        if st.button("📖 N01: Teoría de Conjuntos"): 
            st.session_state.clase_seleccionada = "N01"
            st.rerun()
    
    elif st.session_state.clase_seleccionada == "N01":
        # BOTÓN VOLVER PEGADO A LA CLASE
        if st.button("🔙 Volver"): 
            st.session_state.clase_seleccionada = None
            st.rerun()

        st.markdown('<div class="clase-white-box">', unsafe_allow_html=True)
        st.markdown("""
# <span style="color:darkblue">N01: Teoría de Conjuntos</span>
## <span style="color:darkblue">El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal
Aprender Teoría de Conjuntos es aprender a clasificar el caos. Todo gran sistema se basa en quién pertenece a qué bajo reglas claras.

---

### 🛡️ 2. El Marco de Referencia
* **El Universo ($\mathcal{U}$):** El contexto total.
* **El Vacío ($\emptyset$):** Sin elementos.
* **Pertenencia ($\in$):** Relación elemento-conjunto.

> **Típ:** ... Si $A \subset B$, entonces $A \cap B = A$ y $A \cup B = B$.

---

### 🛡️ 3. Operaciones Clave
* **Unión ($\cup$):** Juntar todo.
* **Intersección ($\cap$):** Solo lo común.
* **Potencia:** Total subconjuntos = $2^n$.

---

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".  
> — **Georg Cantor**
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        st.info("Selecciona un eje arriba para empezar.")

# Auto-refresh del cronómetro
if st.session_state.cronometro_activo:
    time.sleep(1)
    st.rerun()
    
