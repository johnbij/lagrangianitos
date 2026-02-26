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

# ESTADOS DEL CRONÓMETRO
if 'cronometro_activo' not in st.session_state: st.session_state.cronometro_activo = False
if 'tiempo_inicio' not in st.session_state: st.session_state.tiempo_inicio = None

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::: 2. ESTILOS CSS :::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

st.markdown("""
    <style>
    .header-azul { background-color: #3b71ca; padding: 15px; border-radius: 15px 15px 0 0; color: white; text-align: center; }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header { font-size: 14px; opacity: 0.9; }
    .header-rojo { background-color: #cc0000; padding: 10px; color: white; display: flex; justify-content: space-around; border-radius: 0 0 15px 15px; }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* CRONÓMETRO BARTON: Fondo blanco, Números Azules */
    .crono-container-barton { 
        background-color: white; padding: 10px; border-radius: 10px; 
        text-align: center; border: 2px solid #3b71ca;
    }
    .crono-digital-azul { font-family: 'Courier New', monospace; font-size: 32px; font-weight: bold; color: #3b71ca; }
    
    [data-testid="stHorizontalBlock"] button { width: 100% !important; min-height: 55px !important; font-size: 20px !important; font-weight: bold !important; border-radius: 8px !important; }
    .cat-container div.stButton > button { min-height: 85px !important; border-radius: 15px !important; margin-bottom: 15px !important; width: 100% !important; font-size: 18px !important; text-align: left !important; padding-left: 20px !important; border: 1px solid #e0e0e0 !important; box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important; }
    .clase-box { background-color: white; padding: 30px; border-radius: 15px; border: 1px solid #e0e0e0; color: #1a1a1a; }
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
# :::: 4. DASHBOARD PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if menu == "🏠 Dashboard PAES":
    zona_cl = pytz.timezone('America/Santiago')
    ahora = datetime.now(zona_cl)
    st.markdown(f'<div class="header-azul"><div class="titulo-header">🐉 Lagrangianitos. Tus recursos PAES M1</div><div class="info-header">📍 Santiago, Chile | 🕒 {ahora.strftime("%H:%M")}</div></div>', unsafe_allow_html=True)
    
    dias_paes = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).days
    horas_paes = (datetime(2026, 6, 15, 9, 0, 0, tzinfo=zona_cl) - ahora).seconds // 3600
    st.markdown(f'<div class="header-rojo"><div class="timer-item">⏳ Días para PAES: {dias_paes}</div><div class="timer-item">Hrs: {horas_paes}</div></div>', unsafe_allow_html=True)

    # --- SECCIÓN CRONÓMETRO ---
    st.write("")
    c_crono1, c_crono2 = st.columns([1, 3])
    with c_crono1:
        if not st.session_state.cronometro_activo:
            if st.button("▶️ Iniciar"):
                st.session_state.tiempo_inicio = time.time()
                st.session_state.cronometro_activo = True
                st.rerun()
        else:
            if st.button("⏹️ Detener"):
                st.session_state.cronometro_activo = False
                st.session_state.tiempo_inicio = None
                st.rerun()
    with c_crono2:
        if st.session_state.cronometro_activo:
            t_actual = int(time.time() - st.session_state.tiempo_inicio)
            mins, segs = divmod(t_actual, 60)
            st.markdown(f'<div class="crono-container-barton"><span class="crono-digital-azul">{mins:02d}:{segs:02d}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="crono-container-barton" style="border: 2px dashed #e0e0e0;"><span style="color:#e0e0e0; font-size:32px; font-family:Courier New; font-weight:bold;">00:00</span></div>', unsafe_allow_html=True)

    st.write("") 

    # --- NAVEGACIÓN SUPERIOR ---
    n_cols = st.columns(5)
    if n_cols[0].button("🏠", key="n_h"): st.session_state.eje_actual = None; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if n_cols[1].button("N", key="n_n"): st.session_state.eje_actual = "🔢 Números"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if n_cols[2].button("A", key="n_a"): st.session_state.eje_actual = "📉 Álgebra"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if n_cols[3].button("G", key="n_g"): st.session_state.eje_actual = "📐 Geometría"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()
    if n_cols[4].button("D", key="n_d"): st.session_state.eje_actual = "📊 Datos y Azar"; st.session_state.sub_eje_actual = None; st.session_state.sub_seccion_actual = None; st.session_state.clase_seleccionada = None; st.rerun()

    st.divider()

    # --- LÓGICA DE NAVEGACIÓN ---
    if st.session_state.eje_actual is None:
        st.markdown("### 📚 Selecciona un Eje Temático")
        e_col1, e_col2 = st.columns(2)
        if e_col1.button("🔢 Números"): st.session_state.eje_actual = "🔢 Números"; st.rerun()
        if e_col2.button("📉 Álgebra"): st.session_state.eje_actual = "📉 Álgebra"; st.rerun()
        e_col3, e_col4 = st.columns(2)
        if e_col3.button("📐 Geometría"): st.session_state.eje_actual = "📐 Geometría"; st.rerun()
        if e_col4.button("📊 Datos y Azar"): st.session_state.eje_actual = "📊 Datos y Azar"; st.rerun()
    
    # SUB-EJES DE NÚMEROS
    elif st.session_state.eje_actual == "🔢 Números" and st.session_state.sub_eje_actual is None:
        st.markdown("## 🔢 Números")
        se_col1, se_col2, se_col3 = st.columns(3)
        if se_col1.button("🛡️ 1. Conjuntos"): st.session_state.sub_eje_actual = "Conjuntos"; st.rerun()
        if se_col2.button("⚙️ 2. Operatoria"): st.session_state.sub_eje_actual = "Operatoria"; st.rerun()
        if se_col3.button("⚖️ 3. Razones y Proporciones"): st.session_state.sub_eje_actual = "Razones"; st.rerun()
        if st.button("🔙 Volver"): st.session_state.eje_actual = None; st.rerun()

    elif st.session_state.sub_seccion_actual is None:
        titulo = st.session_state.sub_eje_actual if st.session_state.eje_actual == "🔢 Números" else st.session_state.eje_actual
        st.markdown(f"## {titulo}")
        st.markdown('<div class="cat-container">', unsafe_allow_html=True)
        if st.button("📘 Teoría y Conceptos"): st.session_state.sub_seccion_actual = "Teoria"; st.rerun()
        if st.button("📝 Ejercitación"): st.session_state.sub_seccion_actual = "Ejercitacion"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("🔙 Volver"): 
            if st.session_state.eje_actual == "🔢 Números": st.session_state.sub_eje_actual = None
            else: st.session_state.eje_actual = None
            st.rerun()

    elif st.session_state.clase_seleccionada is None:
        st.subheader(f"📚 Clases de {st.session_state.sub_eje_actual if st.session_state.eje_actual == '🔢 Números' else st.session_state.eje_actual}")
        
        # FILTRO ESPECÍFICO PARA CONJUNTOS
        if st.session_state.sub_eje_actual == "Conjuntos" and st.session_state.sub_seccion_actual == "Teoria":
            clases = [
                ("📖 N01: Teoría de Conjuntos", "N01"),
                ("📖 N02: Los Números Naturales", "N02"),
                ("📖 N03: Los Números Cardinales", "N03"),
                ("📖 N04: Los Números Enteros", "N04"),
                ("📖 N05: Los Números Racionales", "N05"),
                ("📖 N06: Los Números Irracionales", "N06"),
                ("📖 N07: Los Números Reales", "N07")
            ]
            for nombre, code in clases:
                if st.button(nombre): st.session_state.clase_seleccionada = code; st.rerun()
        else:
            st.info("✨ Próximamente contenido disponible.")

        if st.button("🔙 Volver"): st.session_state.sub_seccion_actual = None; st.rerun()

    else:
        # PANTALLA DE CLASE
        st.markdown('<div class="clase-box">', unsafe_allow_html=True)
        
        if st.session_state.clase_seleccionada == "N01":
            st.markdown("""
# <span style="color:darkblue">Eje Números</span>
## <span style="color:darkblue">N01: Teoría de Conjuntos - El Lenguaje Maestro</span>

---

### 🛡️ 1. El Portal: El Viaje que Cambia la Mirada
Bienvenido a la primera página de un viaje que no tiene vuelta atrás. A menudo, nos enseñan que las matemáticas son un conjunto de reglas para calcular el vuelto o aprobar un examen, pero eso es como decir que la música es solo saber apretar teclas. Lo que hoy iniciamos es la apertura de tus ojos ante la **Gramática del Universo**.

Este eje de **Números** no se trata de hacer cuentas rápidas; se trata de aprender a clasificar el caos. Durante las próximas unidades, descubriremos que los números no están "tirados" en el espacio, sino que habitan en estructuras organizadas llamadas **Conjuntos**. Aprender Teoría de Conjuntos es aprender a pensar con orden, a establecer fronteras y a entender que todo gran sistema se basa en quién pertenece a qué y bajo qué reglas. Prepárate para una apertura de mente donde el infinito deja de ser un concepto místico y se convierte en un terreno que podemos cartografiar.

---

### 🛡️ 2. Crónica del Infinito: El Legado de Georg Cantor
A finales del siglo XIX, un hombre decidió desafiar a la teología y a la ciencia de su tiempo. **Georg Cantor** se atrevió a decir que el infinito no era un muro infranqueable, sino un jardín que podía ser medido. Cantor demostró que los conjuntos nos permiten comparar tamaños de infinitos que parecen imposibles. Su valentía permitió que hoy podamos definir con precisión quirúrgica qué es un número. En la PAES, este lenguaje es tu escudo: si dominas los conjuntos, dominas las instrucciones de la prueba.

---

### 🛡️ 3. El Marco de Referencia: Universo, Vacío y Subconjuntos
Para que exista el orden, debe existir un límite y una jerarquía clara:

* **El Universo ($\mathcal{U}$):** Es el contexto total que contiene todos los elementos de un problema. Nada existe fuera del universo.
* **El Vacío ($\emptyset$ o $\{\}$):** Un conjunto sin elementos. Es la representación de la nada matemática y es subconjunto de cualquier conjunto por definición.
* **Pertenencia ($\in$):** Relación de un **elemento** hacia un conjunto. (Ej: Manzana $\in$ Frutas).
* **Subconjunto o Inclusión ($\subset$):** Se dice que $A$ es subconjunto de $B$ ($A \subset B$) si **todos** los elementos de $A$ están también en $B$.

> **Típ:** ... Si $A \subset B$, entonces la intersección es el más pequeño ($A \cap B = A$) y la unión es el más grande ($A \cup B = B$).

---

### 🛡️ 4. Operaciones de "1000 Puntos"
Estas operaciones son las que "mueven" los elementos entre conjuntos:

| Operación | Símbolo | Significado Lógico | Carpintería Técnica |
| :--- | :---: | :--- | :--- |
| **Unión** | $\cup$ | $x \in A$ **o** $x \in B$ | Agrupar todos los elementos de ambos. |
| **Intersección** | $\cap$ | $x \in A$ **y** $x \in B$ | Solo los elementos que se repiten. |
| **Diferencia** | $-$ | $x \in A$ pero $x \notin B$ | Al primer conjunto le borras lo que sea del segundo. |
| **Complemento** | $A^c$ | $x \in \mathcal{U}$ pero $x \notin A$ | Todo lo que le falta a A para ser el Universo. |

---

### 🛡️ 5. Cardinalidad y Conjunto Potencia
* **Cardinalidad ($n$):** Llamamos cardinalidad al número de elementos únicos de un conjunto. Se denota como $\#A = n$ o $n(A)$.
* **Regla de Oro de la Unión:** $\#(A \cup B) = \#A + \#B - \#(A \cap B)$.
* **Conjunto Potencia:** Es el conjunto formado por todos los subconjuntos posibles de $A$.
* **Total de Subconjuntos:** Si la cardinalidad de un conjunto es $n$, el total de subconjuntos que se pueden formar es:
$$2^n$$

> **Típ:** ... El total de subconjuntos siempre incluye al **Vacío** y al **propio conjunto $A$**. Si agregas un elemento a la bolsa, el conjunto potencia crece al doble.

---

### 🛡️ 6. Cartografía Visual (Diagramas de Venn-Euler)
Para dominar la PAES, debes "ver" la operación antes de calcularla. Los diagramas de Venn-Euler nos permiten visualizar las relaciones entre conjuntos de manera intuitiva. Cada círculo representa un conjunto, y las superposiciones muestran las intersecciones. El rectángulo exterior representa el Universo.

---

> "En matemáticas, el arte de proponer una pregunta debe ser de mayor valor que resolverla".
> — **Georg Cantor**
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"# Clase {st.session_state.clase_seleccionada}")
            st.markdown(f"Contenido en desarrollo para la sesión {st.session_state.clase_seleccionada}...")
        
        st.markdown('</div>', unsafe_allow_html=True)
        if st.button("🔙 Volver al listado"): st.session_state.clase_seleccionada = None; st.rerun()

# Refresco para el cronómetro
if st.session_state.cronometro_activo:
    time.sleep(1)
    st.rerun()
    
