# app.py

import streamlit as st
import pandas as pd

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

st.set_page_config(
    page_title="Portafolio de Ética Empresarial",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTILOS CSS
# ============================================================

st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 45%, #ffffff 100%);
            color: #111827;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #111827 0%, #1e3a8a 100%);
        }

        section[data-testid="stSidebar"] * {
            color: white;
        }

        .main-title {
            font-size: 3.2rem;
            font-weight: 900;
            color: #0f172a;
            text-align: center;
            line-height: 1.1;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            font-size: 1.25rem;
            color: #475569;
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .institution {
            text-align: center;
            color: #64748b;
            font-weight: 600;
            margin-bottom: 0.2rem;
        }

        .hero {
            background: linear-gradient(135deg, #1e3a8a, #2563eb, #0f766e);
            padding: 2rem;
            border-radius: 28px;
            color: white;
            box-shadow: 0 18px 40px rgba(30, 58, 138, 0.28);
            margin: 1.5rem 0 2rem 0;
        }

        .hero h2 {
            color: white;
            font-size: 1.8rem;
            margin-bottom: 0.7rem;
        }

        .hero p {
            color: #e0f2fe;
            font-size: 1.08rem;
            line-height: 1.7;
            margin-bottom: 0;
        }

        .section-title {
            font-size: 2.1rem;
            font-weight: 850;
            color: #0f172a;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
        }

        .subsection-title {
            font-size: 1.35rem;
            font-weight: 800;
            color: #1e293b;
            margin-bottom: 0.6rem;
        }

        .card {
            background: rgba(255, 255, 255, 0.95);
            padding: 1.45rem;
            border-radius: 22px;
            border: 1px solid rgba(226, 232, 240, 0.9);
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
            margin-bottom: 1.2rem;
        }

        .card-blue {
            background: white;
            padding: 1.45rem;
            border-radius: 22px;
            border-left: 7px solid #2563eb;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
            margin-bottom: 1.2rem;
        }

        .card-green {
            background: white;
            padding: 1.45rem;
            border-radius: 22px;
            border-left: 7px solid #0f766e;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
            margin-bottom: 1.2rem;
        }

        .card-orange {
            background: white;
            padding: 1.45rem;
            border-radius: 22px;
            border-left: 7px solid #f97316;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
            margin-bottom: 1.2rem;
        }

        .card-purple {
            background: white;
            padding: 1.45rem;
            border-radius: 22px;
            border-left: 7px solid #7c3aed;
            box-shadow: 0 10px 28px rgba(15, 23, 42, 0.08);
            margin-bottom: 1.2rem;
        }

        .text {
            text-align: justify;
            line-height: 1.75;
            font-size: 1.03rem;
            color: #334155;
        }

        .quote-box {
            background: #f8fafc;
            padding: 1.3rem;
            border-radius: 18px;
            border-left: 6px solid #64748b;
            color: #334155;
            font-style: italic;
            line-height: 1.7;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
            margin-bottom: 1.2rem;
        }

        .tag {
            display: inline-block;
            background: #e0f2fe;
            color: #075985;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            font-size: 0.88rem;
            font-weight: 700;
            margin-right: 0.4rem;
            margin-bottom: 0.4rem;
        }

        .footer {
            text-align: center;
            color: #64748b;
            font-size: 0.9rem;
            margin-top: 3rem;
            padding-top: 1.2rem;
            border-top: 1px solid #cbd5e1;
        }

        div[data-testid="stMetric"] {
            background-color: white;
            padding: 1rem;
            border-radius: 18px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 8px 22px rgba(15, 23, 42, 0.07);
        }

        div[data-testid="stMetricValue"] {
            color: #1e3a8a;
            font-weight: 900;
        }

        div[data-testid="stDataFrame"] {
            border-radius: 18px;
            overflow: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# DATOS DEL PORTAFOLIO
# ============================================================

evidencias = pd.DataFrame({
    "Título": [
        "Desarrollo y libertad",
        "El 1%, por el 1%, para el 1%",
        "Desigualdad: ¿Qué podemos hacer?",
        "Health, Inequality and Economic Development",
        "¿Qué es y para qué sirve la ética?",
        "Hacia una economía cordial",
        "Economía con sentido moral",
        "El capital en el siglo XXI",
        "Creating Capabilities",
        "The Social Responsibility of Business",
        "La gran transformación",
        "A Theory of Justice"
    ],
    "Autor": [
        "Amartya Sen",
        "Joseph Stiglitz",
        "Anthony Atkinson",
        "Angus Deaton",
        "Adela Cortina",
        "Patrici Calvo",
        "Patrici Calvo",
        "Thomas Piketty",
        "Martha Nussbaum",
        "Milton Friedman",
        "Karl Polanyi",
        "John Rawls"
    ],
    "Tipo de contenido": [
        "Conceptual",
        "Crítico",
        "Informativo",
        "Conceptual",
        "Conceptual",
        "Conceptual",
        "Conceptual",
        "Conceptual",
        "Conceptual",
        "Normativo",
        "Conceptual",
        "Conceptual"
    ],
    "Formato": [
        "Libro digital",
        "Libro digital",
        "Libro digital",
        "Libro digital",
        "Video",
        "Digital",
        "Digital",
        "Libro digital",
        "Libro digital",
        "Artículo",
        "Libro digital",
        "Libro digital"
    ],
    "Aporte principal": [
        "Permite entender el desarrollo como expansión de libertades y capacidades humanas.",
        "Cuestiona la concentración de la riqueza y sus efectos sobre la democracia y la justicia social.",
        "Analiza alternativas para enfrentar la desigualdad económica.",
        "Relaciona salud, desigualdad y desarrollo económico.",
        "Explica la función social de la ética en la vida colectiva.",
        "Propone una economía orientada por valores de cordialidad, justicia y responsabilidad.",
        "Presenta herramientas para gestionar la ética en organizaciones y empresas.",
        "Muestra cómo el capital tiende a concentrarse cuando no existen mecanismos de regulación.",
        "Amplía el enfoque de capacidades hacia una visión de dignidad y justicia.",
        "Defiende la maximización del beneficio como responsabilidad principal de la empresa.",
        "Advierte sobre los riesgos sociales de un mercado desregulado.",
        "Propone principios de justicia para organizar las instituciones sociales y económicas."
    ]
})

categorias = pd.DataFrame({
    "Categoría de análisis": [
        "Crítica al crecimiento económico como indicador de bienestar",
        "Enfoques del desarrollo centrados en la persona",
        "Fundamentos de la ética en la economía y la empresa",
        "Debate normativo sobre el papel de la empresa"
    ],
    "Autores principales": [
        "Joseph Stiglitz, Angus Deaton, Anthony Atkinson, Thomas Piketty",
        "Amartya Sen, Martha Nussbaum",
        "Adela Cortina, Patrici Calvo",
        "Milton Friedman, John Rawls, Karl Polanyi"
    ],
    "Tipo de contenido": [
        "Crítico e informativo",
        "Conceptual",
        "Conceptual",
        "Normativo y conceptual"
    ],
    "Aporte al problema": [
        "Evidencian que el crecimiento económico puede coexistir con desigualdad, concentración de riqueza y exclusión social.",
        "Proponen que el desarrollo debe medirse a partir de las capacidades y oportunidades reales de las personas.",
        "Plantean que la actividad económica debe orientarse al bien común, incorporando valores como justicia, responsabilidad y sostenibilidad.",
        "Permiten contrastar posturas: desde la maximización del beneficio como objetivo empresarial hasta la necesidad de justicia social y regulación del mercado."
    ]
})

argumentos = [
    "Autores como Stiglitz o Deaton muestran que el crecimiento puede coexistir con desigualdad y exclusión, lo que evidencia que la rentabilidad empresarial por sí sola no asegura justicia social.",
    "Sen plantea que el verdadero progreso se mide por las capacidades y oportunidades de las personas, lo que implica que las empresas también deben considerar su impacto social.",
    "Cortina y Calvo sostienen que la economía y las empresas deben guiarse por principios éticos y por el bien común, ya que la actividad económica afecta directamente a la sociedad.",
    "Stiglitz, Deaton y Piketty muestran que el crecimiento económico puede coexistir con desigualdad, lo que demuestra que la rentabilidad no garantiza bienestar colectivo.",
    "Sen y Nussbaum plantean que el desarrollo debe medirse en términos de capacidades humanas, lo que implica que las empresas tienen un impacto directo en la calidad de vida.",
    "Polanyi argumenta que el mercado desregulado puede generar desequilibrios sociales, por lo que la economía debe estar subordinada a principios sociales y éticos.",
    "Rawls propone que la justicia económica debe beneficiar a los más desfavorecidos, lo que cuestiona modelos empresariales centrados únicamente en el lucro.",
    "En contraste, Friedman sostiene que la empresa debe enfocarse en maximizar beneficios, lo que refleja la tensión entre eficiencia económica y responsabilidad social."
]

analisis_autores = {
    "Joseph Stiglitz y Thomas Piketty": (
        "Permiten comprender cómo los beneficios económicos tienden a concentrarse incluso en situaciones de crisis global. "
        "En el caso de la pandemia, las empresas farmacéuticas incrementaron significativamente sus ingresos mientras persistían "
        "desigualdades profundas entre países y sectores sociales. Esto confirma que el mercado, por sí solo, no distribuye "
        "equitativamente los beneficios del crecimiento económico."
    ),
    "Amartya Sen y Martha Nussbaum": (
        "Desde el enfoque de capacidades, el desarrollo no consiste únicamente en producir riqueza, sino en garantizar "
        "oportunidades reales para que las personas vivan dignamente. El acceso a la salud y a las vacunas constituye una "
        "condición básica para el bienestar. Por ello, cuando millones de personas no pudieron acceder oportunamente a tratamientos "
        "médicos, se limitó directamente su libertad y su calidad de vida."
    ),
    "Adela Cortina y Patrici Calvo": (
        "Permiten cuestionar el papel de las empresas frente al bien común. Aunque las farmacéuticas actuaron dentro de la lógica "
        "del mercado y generaron innovación científica, el caso evidencia que las decisiones empresariales tienen consecuencias "
        "sociales profundas. Desde esta perspectiva, la ética empresarial implica asumir responsabilidad frente al impacto social "
        "de la actividad económica."
    ),
    "Karl Polanyi": (
        "Ayuda a comprender que un mercado completamente desregulado puede subordinar las necesidades humanas a la lógica económica. "
        "En este caso, la salud, que debería entenderse como un derecho humano fundamental, terminó dependiendo en gran medida de la "
        "capacidad de pago de los países y de las dinámicas del mercado internacional."
    ),
    "John Rawls": (
        "Permite analizar si las desigualdades generadas durante la pandemia beneficiaron realmente a los más desfavorecidos. "
        "Desde esta perspectiva, una sociedad justa debe organizar sus instituciones económicas de modo que las desigualdades "
        "favorezcan a quienes están en peores condiciones. Sin embargo, el acceso desigual a las vacunas mostró que muchos sectores "
        "vulnerables quedaron excluidos de beneficios esenciales."
    ),
    "Milton Friedman": (
        "Podría justificar que las empresas farmacéuticas actuaran principalmente buscando maximizar beneficios para sus accionistas, "
        "siempre dentro de las reglas del mercado. No obstante, esta postura resulta insuficiente frente a una crisis sanitaria mundial "
        "donde estaban en juego derechos fundamentales como la vida y la salud."
    )
}

# ============================================================
# FUNCIONES DE DISEÑO
# ============================================================

def card(title, text, style="card-blue"):
    st.markdown(
        f"""
        <div class="{style}">
            <div class="subsection-title">{title}</div>
            <p class="text">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def paragraph_card(text, style="card"):
    st.markdown(
        f"""
        <div class="{style}">
            <p class="text">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def quote(text):
    st.markdown(
        f"""
        <div class="quote-box">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )


def section_title(text):
    st.markdown(
        f'<h2 class="section-title">{text}</h2>',
        unsafe_allow_html=True
    )


def tags(items):
    html = "".join([f'<span class="tag">{item}</span>' for item in items])
    st.markdown(html, unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.title("Portafolio")
    st.write("Ética empresarial, economía y bienestar colectivo")

    st.markdown("---")

    st.subheader("Datos generales")
    st.write("Universidad Santo Tomás")
    st.write("Dirección de Humanidades")
    st.write("Integrantes: Luis Becerra y Juan Corredor")

    st.markdown("---")

    st.subheader("Pregunta guía")
    st.write("¿Puede una empresa ser ética en un mercado que prioriza la maximización del beneficio?")

    st.markdown("---")

    st.subheader("Ejes")
    st.write("Crecimiento económico")
    st.write("Ética empresarial")
    st.write("Bienestar colectivo")
    st.write("Justicia social")


# ============================================================
# PORTADA
# ============================================================

st.markdown('<p class="institution">Universidad Santo Tomás</p>', unsafe_allow_html=True)
st.markdown('<p class="institution">Dirección de Humanidades</p>', unsafe_allow_html=True)

st.markdown(
    '<h1 class="main-title">Portafolio de Ética Empresarial</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Empresa, economía y bienestar: el crecimiento económico no garantiza justicia ni bienestar colectivo</p>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero">
        <h2>Pregunta central del portafolio</h2>
        <p>
            ¿Puede una empresa ser ética en un mercado que prioriza la maximización del beneficio?
            Esta pregunta orienta el análisis sobre la tensión entre rentabilidad, responsabilidad social,
            justicia económica y bienestar colectivo.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Fases", "3")

with col2:
    st.metric("Evidencias", "12")

with col3:
    st.metric("Categorías", "4")

with col4:
    st.metric("Caso aplicado", "COVID-19")

tags(
    [
        "Ética empresarial",
        "Economía",
        "Bienestar colectivo",
        "Justicia social",
        "Responsabilidad social",
        "Desigualdad"
    ]
)

# ============================================================
# PESTAÑAS PRINCIPALES
# ============================================================

tabs = st.tabs([
    "Inicio",
    "Fase 1",
    "Evidencias",
    "Fase 2",
    "Fase 3",
    "Conclusión",
    "Fuentes"
])

# ============================================================
# INICIO
# ============================================================

with tabs[0]:
    section_title("Presentación del portafolio")

    paragraph_card(
        """
        Este portafolio reúne un proceso de análisis ético, económico y social sobre el papel de la empresa 
        en las economías contemporáneas. El punto de partida es una tensión fundamental: aunque el crecimiento 
        económico suele presentarse como sinónimo de progreso, este no siempre garantiza justicia social, 
        reducción de desigualdades ni bienestar colectivo.
        """
    )

    paragraph_card(
        """
        A través de diferentes autores y evidencias, se examina si la empresa puede actuar éticamente dentro 
        de un mercado orientado por la maximización del beneficio. El portafolio se organiza en tres fases: 
        formulación del problema, organización y reflexión de evidencias, y aplicación del análisis a un caso 
        concreto: la industria farmacéutica durante la pandemia del COVID-19.
        """,
        style="card-green"
    )

    st.markdown('<h3 class="subsection-title">Estructura general del trabajo</h3>', unsafe_allow_html=True)

    estructura = pd.DataFrame({
        "Fase": ["Fase 1", "Fase 2", "Fase 3"],
        "Contenido": [
            "Selección del tema-problema, planteamiento del problema, contexto y esquema argumentativo.",
            "Organización de las mejores evidencias y reflexión crítica sobre los documentos recolectados.",
            "Aplicación del marco teórico al caso de la industria farmacéutica durante la pandemia del COVID-19."
        ],
        "Propósito": [
            "Definir el problema ético central.",
            "Interpretar las evidencias desde categorías de análisis.",
            "Relacionar teoría y realidad mediante un caso actual."
        ]
    })

    st.dataframe(estructura, use_container_width=True, hide_index=True)

    st.markdown('<h3 class="subsection-title">Ruta argumentativa</h3>', unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        card(
            "1. Problema",
            "El crecimiento económico y la rentabilidad empresarial no garantizan por sí solos justicia social ni bienestar colectivo.",
            style="card-blue"
        )

    with col_b:
        card(
            "2. Evidencias",
            "Los autores seleccionados permiten contrastar enfoques económicos, éticos y políticos sobre el papel de la empresa.",
            style="card-green"
        )

    with col_c:
        card(
            "3. Caso aplicado",
            "La industria farmacéutica durante la pandemia muestra la tensión entre innovación, lucro y acceso desigual a la salud.",
            style="card-orange"
        )

# ============================================================
# FASE 1
# ============================================================

with tabs[1]:
    section_title("Fase 1: selección del tema-problema")

    card(
        "Tema-problema",
        "Empresa, economía y bienestar: el crecimiento económico no garantiza justicia ni bienestar colectivo.",
        style="card-blue"
    )

    card(
        "Planteamiento del problema",
        """
        En las economías contemporáneas, el éxito empresarial suele medirse principalmente a través de 
        indicadores financieros como las utilidades, la rentabilidad o el crecimiento del mercado. Bajo esta lógica, 
        muchas empresas operan en un entorno competitivo donde la maximización del beneficio se convierte en el 
        objetivo central. Sin embargo, esta prioridad plantea un dilema ético: si el mercado premia principalmente 
        la eficiencia económica y la generación de ganancias, ¿hasta qué punto las empresas pueden actuar de forma 
        verdaderamente ética?
        """,
        style="card-green"
    )

    paragraph_card(
        """
        Diversos autores han cuestionado la idea de que el crecimiento económico o la generación de riqueza garanticen 
        automáticamente bienestar social. Economistas como Joseph Stiglitz o Angus Deaton han mostrado que el crecimiento 
        puede coexistir con desigualdad o exclusión, mientras que pensadores como Amartya Sen sostienen que el verdadero 
        desarrollo debe medirse por las capacidades y oportunidades reales de las personas. Desde la ética, autores como 
        Adela Cortina y Patrici Calvo argumentan que la economía y las empresas deben orientarse al bien común y no solo 
        a la eficiencia o al beneficio económico.
        """,
        style="card"
    )

    paragraph_card(
        """
        En este contexto surge la pregunta central de este trabajo: ¿puede una empresa ser ética en un mercado que prioriza 
        la maximización del beneficio? Este interrogante conduce a reflexionar sobre si el lucro es compatible con la 
        responsabilidad social y sobre la posibilidad de que las empresas generen simultáneamente valor económico y valor social.
        """,
        style="card-purple"
    )

    card(
        "Contexto",
        """
        Durante gran parte del siglo XX, especialmente desde el auge de las políticas neoliberales, se consolidó la idea 
        de que la función principal de la empresa es maximizar las ganancias para sus accionistas. Este enfoque, asociado 
        a la teoría económica tradicional, sostiene que el mercado asigna eficientemente los recursos y que el crecimiento 
        económico terminará beneficiando al conjunto de la sociedad.
        """,
        style="card-orange"
    )

    paragraph_card(
        """
        No obstante, las crisis económicas, el aumento de la desigualdad y los problemas sociales y ambientales han puesto 
        en duda esta visión. Investigaciones recientes muestran que el crecimiento económico no siempre se traduce en bienestar 
        colectivo, y que muchas veces los beneficios del mercado se concentran en determinados grupos. Frente a estas críticas, 
        han surgido nuevas perspectivas que proponen repensar el papel de la empresa dentro de la sociedad.
        """,
        style="card"
    )

    paragraph_card(
        """
        Conceptos como la responsabilidad social empresarial o el valor compartido sugieren que las empresas pueden generar 
        beneficios económicos mientras contribuyen al desarrollo social, la sostenibilidad ambiental y la reducción de desigualdades. 
        Desde esta perspectiva, la ética empresarial no se entiende como un obstáculo para el mercado, sino como un elemento 
        necesario para que la actividad económica contribuya realmente al bienestar colectivo.
        """,
        style="card-green"
    )

    st.markdown('<h3 class="subsection-title">Esquema argumentativo</h3>', unsafe_allow_html=True)

    for i, argumento in enumerate(argumentos, start=1):
        card(f"Argumento {i}", argumento, style="card-blue")

    quote(
        """
        Por lo tanto, el lucro no es incompatible con la ética, pero tampoco es suficiente para garantizar bienestar. 
        La empresa ética es aquella que reconoce su papel dentro de la sociedad y orienta su actividad no solo a la generación 
        de beneficios, sino también a la reducción de desigualdades, el fortalecimiento de capacidades humanas y la promoción 
        del bien común.
        """
    )

# ============================================================
# EVIDENCIAS
# ============================================================

with tabs[2]:
    section_title("Recogida inicial de evidencias")

    paragraph_card(
        """
        En esta sección se sistematizan las fuentes principales del portafolio. Las evidencias combinan libros, artículos, 
        videos y documentos digitales que permiten analizar la relación entre empresa, ética, crecimiento económico y bienestar social.
        """,
        style="card"
    )

    st.dataframe(evidencias, use_container_width=True, hide_index=True)

    st.markdown('<h3 class="subsection-title">Lectura general de las evidencias</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        card(
            "Evidencias económicas",
            """
            Stiglitz, Deaton, Atkinson y Piketty permiten cuestionar la idea de que el crecimiento económico garantice 
            automáticamente bienestar colectivo. Sus aportes muestran que la riqueza puede crecer mientras persisten 
            desigualdades profundas.
            """,
            style="card-blue"
        )

    with col2:
        card(
            "Evidencias éticas y políticas",
            """
            Sen, Nussbaum, Cortina, Calvo, Rawls y Polanyi amplían el análisis hacia la dignidad humana, la justicia 
            distributiva, la regulación del mercado y el bien común.
            """,
            style="card-green"
        )

    card(
        "Tensión central",
        """
        La selección de evidencias muestra que el debate no está solamente en si las empresas deben generar beneficios, 
        sino en si esos beneficios pueden articularse con responsabilidad social, sostenibilidad y justicia.
        """,
        style="card-orange"
    )

# ============================================================
# FASE 2
# ============================================================

with tabs[3]:
    section_title("Fase 2: organización y reflexión sobre las evidencias")

    paragraph_card(
        """
        En esta fase se realizó una selección rigurosa de evidencias con el objetivo de sustentar el problema central: 
        la tensión entre crecimiento económico, ética empresarial y bienestar colectivo. Se priorizaron autores clave 
        del pensamiento económico, político y ético como Amartya Sen, Joseph Stiglitz, Thomas Piketty, Karl Polanyi, 
        John Rawls y Milton Friedman, lo que permite abordar el problema desde múltiples perspectivas.
        """,
        style="card-blue"
    )

    st.markdown('<h3 class="subsection-title">Categorías de análisis</h3>', unsafe_allow_html=True)
    st.dataframe(categorias, use_container_width=True, hide_index=True)

    st.markdown('<h3 class="subsection-title">Reflexión sobre las evidencias</h3>', unsafe_allow_html=True)

    paragraph_card(
        """
        El análisis conjunto de las evidencias permitió identificar una tensión estructural entre la lógica del mercado 
        y las exigencias éticas de la sociedad. Por un lado, la perspectiva de Milton Friedman sostiene que la responsabilidad 
        principal de la empresa es maximizar las ganancias dentro de las reglas del mercado. Sin embargo, esta visión resulta 
        limitada frente a los problemas actuales de desigualdad y exclusión.
        """,
        style="card"
    )

    paragraph_card(
        """
        Autores como Joseph Stiglitz, Anthony Atkinson y Thomas Piketty demuestran que el crecimiento económico no se distribuye 
        de manera equitativa, lo que cuestiona la idea de que el mercado por sí solo garantiza bienestar. Esto evidencia que la 
        eficiencia económica no necesariamente implica justicia social.
        """,
        style="card-green"
    )

    paragraph_card(
        """
        En contraste, el enfoque de capacidades de Amartya Sen y Martha Nussbaum introduce una visión más completa del desarrollo, 
        centrada en la dignidad y las oportunidades de las personas. Esta perspectiva permite replantear el papel de la empresa 
        como un actor que influye directamente en la calidad de vida de la sociedad.
        """,
        style="card-purple"
    )

    paragraph_card(
        """
        Desde la ética, las propuestas de Adela Cortina y Patrici Calvo muestran que la actividad empresarial debe orientarse al 
        bien común, integrando valores como la responsabilidad, la justicia y la sostenibilidad.
        """,
        style="card-orange"
    )

    paragraph_card(
        """
        Finalmente, autores como John Rawls y Karl Polanyi permiten comprender que el mercado no es una estructura neutral, sino 
        una institución que debe estar regulada para evitar desigualdades extremas y proteger a la sociedad.
        """,
        style="card"
    )

    quote(
        """
        En síntesis, la reflexión evidencia que la empresa sí puede ser ética, pero no bajo una lógica puramente economicista. 
        Esto exige una transformación en la forma de entender el éxito empresarial, integrando el valor económico con el valor social.
        """
    )

# ============================================================
# FASE 3
# ============================================================

with tabs[4]:
    section_title("Fase 3: caso aplicado")

    st.markdown(
        """
        <div class="hero">
            <h2>La industria farmacéutica durante la pandemia del COVID-19</h2>
            <p>
                Crecimiento económico y desigualdad en el acceso a las vacunas.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    paragraph_card(
        """
        Uno de los acontecimientos más representativos para analizar la relación entre empresa, ética y bienestar colectivo fue 
        el comportamiento de varias empresas farmacéuticas durante la pandemia del COVID-19. Este caso permite observar cómo, 
        en un contexto de crisis sanitaria global, coexistieron enormes beneficios económicos empresariales con profundas 
        desigualdades sociales en el acceso a medicamentos y vacunas.
        """,
        style="card-blue"
    )

    paragraph_card(
        """
        Durante la pandemia, compañías farmacéuticas lograron desarrollar vacunas en tiempos récord gracias a procesos de 
        investigación científica apoyados tanto por inversión privada como por recursos públicos provenientes de distintos gobiernos. 
        Empresas como Pfizer, Moderna y AstraZeneca obtuvieron ganancias millonarias debido a la alta demanda mundial de vacunas 
        y tratamientos médicos. Desde la lógica económica tradicional, este resultado podría interpretarse como un éxito empresarial 
        basado en la innovación, la eficiencia y la rentabilidad.
        """,
        style="card"
    )

    paragraph_card(
        """
        Sin embargo, el acceso desigual a las vacunas mostró importantes tensiones éticas. Mientras los países desarrollados 
        aseguraban millones de dosis para sus poblaciones, muchos países de bajos ingresos enfrentaban escasez, retrasos y 
        dificultades para acceder a tratamientos básicos. Esta situación evidenció que el crecimiento económico y las ganancias 
        corporativas no necesariamente garantizan bienestar colectivo ni justicia social.
        """,
        style="card-orange"
    )

    st.markdown('<h3 class="subsection-title">Análisis del caso desde los autores</h3>', unsafe_allow_html=True)

    estilos = ["card-blue", "card-green", "card-orange", "card-purple", "card", "card-blue"]

    for index, (autor, idea) in enumerate(analisis_autores.items()):
        card(autor, idea, style=estilos[index % len(estilos)])

    quote(
        """
        El caso confirma la idea central del proyecto: una empresa puede ser ética, pero solo si reconoce que su función social 
        va más allá de generar ganancias y contribuye efectivamente al desarrollo humano y al bienestar colectivo.
        """
    )

# ============================================================
# CONCLUSIÓN
# ============================================================

with tabs[5]:
    section_title("Conclusión general")

    paragraph_card(
        """
        El portafolio permite concluir que el crecimiento económico, aunque importante, no puede entenderse como garantía automática 
        de justicia ni de bienestar colectivo. La empresa cumple un papel central en la sociedad, pero su legitimidad no depende 
        únicamente de su capacidad para generar ganancias, sino también de su impacto sobre las personas, las comunidades y las 
        condiciones de vida.
        """,
        style="card-green"
    )

    paragraph_card(
        """
        Los autores analizados muestran que el mercado, cuando funciona sin principios éticos ni regulación social, puede profundizar 
        desigualdades y concentrar beneficios. Por ello, la ética empresarial no debe ser vista como un elemento externo o decorativo, 
        sino como una condición necesaria para que la actividad económica contribuya realmente al bien común.
        """,
        style="card-blue"
    )

    paragraph_card(
        """
        El caso de la industria farmacéutica durante la pandemia del COVID-19 evidencia esta tensión de manera clara. Aunque las empresas 
        generaron innovación y beneficios económicos, el acceso desigual a las vacunas mostró que la lógica del mercado no siempre responde 
        adecuadamente a las necesidades humanas fundamentales.
        """,
        style="card-orange"
    )

    paragraph_card(
        """
        En consecuencia, una empresa sí puede ser ética, pero solo si reconoce que su responsabilidad va más allá del lucro. Esto implica 
        integrar el valor económico con el valor social, promover la justicia distributiva, respetar la dignidad humana y orientar sus 
        decisiones hacia un desarrollo más sostenible, responsable y solidario.
        """,
        style="card-purple"
    )

    st.markdown(
        """
        <div class="hero">
            <h2>Idea final</h2>
            <p>
                El lucro no es incompatible con la ética, pero tampoco es suficiente para garantizar bienestar.
                La ética empresarial es una condición necesaria para que el mercado tenga legitimidad social.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# FUENTES
# ============================================================

with tabs[6]:
    section_title("Fuentes y evidencias utilizadas")

    paragraph_card(
        """
        Las fuentes utilizadas permiten construir una discusión amplia sobre crecimiento económico, desigualdad, ética empresarial, 
        desarrollo humano, justicia social y regulación del mercado. Se incluyen autores económicos, éticos y políticos para lograr 
        una lectura integral del problema.
        """,
        style="card"
    )

    st.dataframe(evidencias, use_container_width=True, hide_index=True)

    st.markdown('<h3 class="subsection-title">Fuentes con enlaces disponibles</h3>', unsafe_allow_html=True)

    fuentes = [
        {
            "nombre": "Desarrollo y libertad - Amartya Sen",
            "url": "https://indigenasdelperu.wordpress.com/wp-content/uploads/2015/09/desarrollo_y_libertad_-_amartya_sen.pdf"
        },
        {
            "nombre": "El 1%, por el 1%, para el 1% - Joseph Stiglitz",
            "url": "https://revistas.uexternado.edu.co/index.php/diver/article/view/3742/3886"
        },
        {
            "nombre": "Health, Inequality and Economic Development - Angus Deaton",
            "url": "https://www.princeton.edu/~deaton/downloads/Health_Inequality_and_Economic_Development.pdf"
        },
        {
            "nombre": "¿Qué es y para qué sirve la ética? - Adela Cortina",
            "url": "https://www.youtube.com/watch?v=JspFfzuJvec"
        },
        {
            "nombre": "Hacia una economía cordial - Patrici Calvo",
            "url": "https://www.scielo.cl/scielo.php?script=sci_arttext&pid=S0718-92732016000200002"
        },
        {
            "nombre": "Economía con sentido moral - Patrici Calvo",
            "url": "https://www.scielo.org.mx/pdf/trf/n50/n50a9.pdf"
        }
    ]

    for fuente in fuentes:
        st.markdown(f"- [{fuente['nombre']}]({fuente['url']})")

    quote(
        """
        Nota: algunas obras del portafolio se registran como libros digitales sin enlace específico dentro del documento base. 
        En caso de entrega académica, se recomienda completar la referencia bibliográfica en formato APA según la edición consultada.
        """
    )

# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown(
    """
    <div class="footer">
        Portafolio de Ética Empresarial | Universidad Santo Tomás | Dirección de Humanidades
    </div>
    """,
    unsafe_allow_html=True
)
