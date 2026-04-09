import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Pobreza en Colombia 2018–2024",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================
# CONFIGURACIÓN VISUAL
# =========================
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1300px;
    }
    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 55%, #2563eb 100%);
        padding: 2.5rem 2rem;
        border-radius: 24px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    }
    .hero h1 {
        font-size: 2.6rem;
        margin-bottom: 0.6rem;
    }
    .hero p {
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 0;
        opacity: 0.95;
    }
    .section-card {
        background: #ffffff;
        border: 1px solid rgba(15, 23, 42, 0.08);
        padding: 1.2rem 1.2rem;
        border-radius: 20px;
        box-shadow: 0 6px 22px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }
    .insight-box {
        background: #f8fafc;
        border-left: 5px solid #2563eb;
        padding: 1rem 1rem;
        border-radius: 14px;
        margin-top: 0.8rem;
        margin-bottom: 1rem;
    }
    .year-box {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid rgba(37, 99, 235, 0.12);
        padding: 1rem;
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.05);
        min-height: 220px;
    }
    .metric-note {
        font-size: 0.92rem;
        color: #475569;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# DATOS
# =========================
monetaria = pd.DataFrame(
    {
        "Año": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
        "Pobreza monetaria (%)": [34.7, 35.7, 42.5, 39.3, 36.6, 33.0, 31.8],
        "Contexto": [
            "Crecimiento insuficiente, alta informalidad y presión del flujo migratorio sobre empleos e ingresos de baja calificación.",
            "Cambio metodológico del DANE, mayor costo de vida reconocido y estallido social por falta de oportunidades.",
            "Pandemia, confinamiento, caída abrupta del empleo e ingresos; Ingreso Solidario amortiguó parcialmente el deterioro.",
            "Rebote económico con Paro Nacional, bloqueos e inflación de alimentos que redujeron el efecto del crecimiento.",
            "Recuperación de servicios, pero con inflación alta por guerra en Ucrania y encarecimiento de la canasta básica.",
            "Caída de la inflación de alimentos y apoyo de Renta Ciudadana; la mejora depende más de transferencias que de ingresos autónomos.",
            "Menor inflación, pero persistencia del desempleo, restricción fiscal y dudas sobre la sostenibilidad de subsidios.",
        ],
    }
)

ipm = pd.DataFrame(
    {
        "Año": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
        "IPM (%)": [8.0, 7.2, 7.5, 6.5, 5.2, 4.9, 4.6],
        "Contexto": [
            "Persisten privaciones en educación, vivienda y servicios; los cambios estructurales avanzan lentamente.",
            "El deterioro social y laboral evidencia limitaciones en oportunidades y calidad de vida.",
            "Aunque la crisis fue fuerte, las condiciones estructurales no cambian con la misma velocidad que los ingresos.",
            "La recuperación es gradual; las mejoras estructurales requieren continuidad en política pública.",
            "Se observa una reducción más clara del IPM, asociada a avances acumulados en condiciones de vida.",
            "La tendencia descendente continúa, mostrando mejoras lentas pero sostenidas en privaciones básicas.",
            "El IPM sigue bajando, lo que sugiere avances estructurales, aunque aún persisten brechas territoriales y sociales.",
        ],
    }
)

hechos = {
    2018: "Llegada de Iván Duque, crecimiento económico insuficiente y fuerte inserción migratoria en el mercado informal.",
    2019: "Actualización metodológica del DANE, aumento del costo de vida reconocido y protestas por falta de oportunidades.",
    2020: "Choque de la pandemia, pérdida masiva de ingresos y creación de Ingreso Solidario como respuesta estatal.",
    2021: "Rebote económico, Paro Nacional, bloqueos y presión inflacionaria sobre alimentos.",
    2022: "Inflación alta por guerra en Ucrania y crisis de contenedores, con recuperación del empleo en servicios.",
    2023: "Menor inflación de alimentos y expansión de Renta Ciudadana, pero con desaceleración productiva.",
    2024: "Desinflación parcial, desempleo persistente y menor margen fiscal para sostener subsidios.",
}

resumen_indicadores = [
    {
        "nombre": "Pobreza monetaria",
        "texto": "Mide la proporción de personas cuyos ingresos no alcanzan para cubrir necesidades básicas.",
    },
    {
        "nombre": "Pobreza monetaria extrema",
        "texto": "Identifica a la población con ingresos insuficientes incluso para cubrir una canasta básica de alimentos.",
    },
    {
        "nombre": "Brecha de pobreza",
        "texto": "Muestra qué tan lejos están los hogares pobres de superar la línea de pobreza.",
    },
    {
        "nombre": "IPM",
        "texto": "Evalúa privaciones en educación, vivienda, trabajo, salud y acceso a servicios básicos.",
    },
    {
        "nombre": "Coeficiente de Gini",
        "texto": "Permite observar la desigualdad en la distribución del ingreso.",
    },
]

# =========================
# SIDEBAR / NAVEGACIÓN
# =========================
with st.sidebar:
    st.title("Navegación")
    pagina = st.radio(
        "Ir a",
        [
            "Inicio",
            "Indicadores clave",
            "Pobreza monetaria",
            "Pobreza multidimensional",
            "Línea de tiempo 2018–2024",
            "Conclusiones y recomendaciones",
        ],
    )
    st.markdown("---")
    mostrar_contexto = st.toggle("Mostrar contexto explicativo", value=True)
    st.caption("App base en Streamlit para presentar la investigación de forma visual e interpretativa.")

# =========================
# FUNCIONES DE APOYO
# =========================
def grafico_linea(df, x, y, titulo, etiqueta):
    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        title=titulo,
        line_shape="linear",
    )
    fig.update_traces(
        mode="lines+markers",
        line=dict(width=4),
        marker=dict(size=9),
        hovertemplate=f"<b>Año</b>: %{{x}}<br><b>{etiqueta}</b>: %{{y}}<extra></extra>",
    )
    fig.update_layout(
        title_font_size=26,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=70, b=20),
        xaxis_title="Año",
        yaxis_title=etiqueta,
        height=500,
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor="rgba(148,163,184,0.25)")
    return fig


def tarjeta_indicador(nombre, texto):
    st.markdown(
        f"""
        <div class='section-card'>
            <h4 style='margin-bottom:0.45rem'>{nombre}</h4>
            <p style='margin-bottom:0; color:#475569; line-height:1.6'>{texto}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# PÁGINAS
# =========================
if pagina == "Inicio":
    st.markdown(
        """
        <div class='hero'>
            <h1>Pobreza en Colombia 2018–2024</h1>
            <p>
                Una visualización interactiva para entender qué tan extendida, profunda y estructural
                es la pobreza en Colombia, combinando indicadores monetarios y multidimensionales
                con el contexto económico, social y político de cada año.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Periodo", "2018–2024")
    col2.metric("Indicadores base", "5")
    col3.metric("Enfoque", "Monetario + estructural")

    st.markdown("### Pregunta de investigación")
    st.markdown(
        "¿Qué tan extendida, profunda y estructural es la pobreza en Colombia según los principales indicadores monetarios y multidimensionales?"
    )

    st.markdown("### Qué encontrará la persona que visite esta página")
    a, b = st.columns([1.1, 1])
    with a:
        st.markdown(
            """
            - Una explicación clara de los principales indicadores.
            - La evolución reciente de la pobreza monetaria y del IPM.
            - El contexto detrás de cada cambio, para que los datos no se vean aislados.
            - Una lectura final con conclusiones y recomendaciones.
            """
        )
    with b:
        st.markdown(
            """
            <div class='insight-box'>
                <strong>Idea central</strong><br>
                La pobreza no es solamente falta de ingreso. También es una acumulación de privaciones
                en condiciones de vida, acceso a servicios, empleo de calidad y oportunidades.
            </div>
            """,
            unsafe_allow_html=True,
        )

elif pagina == "Indicadores clave":
    st.title("Indicadores clave del boletín")
    st.write(
        "Estos indicadores permiten mirar la pobreza desde varias dimensiones: cuántas personas están en esa condición, qué tan profunda es la privación y qué tan estructurales son las carencias."
    )

    c1, c2 = st.columns(2)
    for i, item in enumerate(resumen_indicadores):
        with c1 if i % 2 == 0 else c2:
            tarjeta_indicador(item["nombre"], item["texto"])

    st.markdown("### Cómo leerlos en conjunto")
    st.markdown(
        "Cuando se analizan de manera articulada, estos indicadores muestran que un hogar puede mejorar ligeramente sus ingresos sin haber superado privaciones estructurales en vivienda, educación o acceso a servicios. Por eso la lectura del boletín no se limita a una sola cifra."
    )

elif pagina == "Pobreza monetaria":
    st.title("Pobreza monetaria en Colombia")
    st.write(
        "Esta sección muestra la evolución de la pobreza monetaria y la acompaña con una interpretación del contexto para que el dato no se lea de forma aislada."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("2018", "34.7%")
    col2.metric("Pico 2020", "42.5%", "+7.8 pp vs. 2018")
    col3.metric("2024", "31.8%", "-10.7 pp vs. pico")

    st.plotly_chart(
        grafico_linea(
            monetaria,
            "Año",
            "Pobreza monetaria (%)",
            "Evolución de la pobreza monetaria en Colombia (2018–2024)",
            "Pobreza monetaria (%)",
        ),
        use_container_width=True,
    )

    st.markdown(
        """
        <div class='insight-box'>
            <strong>Lectura general</strong><br>
            La pobreza monetaria reacciona con mucha fuerza a los choques económicos. En 2020 aumenta de forma abrupta por la pérdida de empleo e ingresos durante la pandemia. Después baja gradualmente, pero su mejora sigue condicionada por la informalidad, la inflación y la capacidad del mercado laboral para generar ingresos estables.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if mostrar_contexto:
        st.markdown("### Contexto por año")
        for _, row in monetaria.iterrows():
            with st.expander(f"{int(row['Año'])} · {row['Pobreza monetaria (%)']}%"):
                st.write(row["Contexto"])

elif pagina == "Pobreza multidimensional":
    st.title("Pobreza multidimensional en Colombia")
    st.write(
        "El IPM permite observar la pobreza como una suma de privaciones. Su comportamiento suele ser más estable que el de la pobreza monetaria porque refleja condiciones estructurales que cambian lentamente."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("2018", "8.0%")
    col2.metric("2024", "4.6%", "-3.4 pp")
    col3.metric("Tendencia", "Descendente")

    st.plotly_chart(
        grafico_linea(
            ipm,
            "Año",
            "IPM (%)",
            "Índice de Pobreza Multidimensional en Colombia (2018–2024)",
            "IPM (%)",
        ),
        use_container_width=True,
    )

    st.markdown(
        """
        <div class='insight-box'>
            <strong>Lectura general</strong><br>
            A diferencia de la pobreza monetaria, el IPM no muestra saltos tan bruscos ante una crisis puntual. Esto sugiere que educación, vivienda, acceso a servicios y otras condiciones de vida mejoran o empeoran en plazos más largos y dependen de políticas sostenidas.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if mostrar_contexto:
        st.markdown("### Contexto por año")
        for _, row in ipm.iterrows():
            with st.expander(f"{int(row['Año'])} · {row['IPM (%)']}%"):
                st.write(row["Contexto"])

elif pagina == "Línea de tiempo 2018–2024":
    st.title("Línea de tiempo interpretativa")
    st.write(
        "Aquí se resume el hecho económico, social o político más relevante de cada año para relacionarlo con la evolución de la pobreza."
    )

    cols = st.columns(2)
    years = list(hechos.keys())
    for i, year in enumerate(years):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class='year-box'>
                    <h3 style='margin-bottom:0.4rem'>{year}</h3>
                    <p style='margin-bottom:0; color:#475569; line-height:1.65'>{hechos[year]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")

elif pagina == "Conclusiones y recomendaciones":
    st.title("Conclusiones y recomendaciones")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Conclusiones")
        st.markdown(
            """
            1. La pobreza en Colombia tiene una doble dimensión: responde a choques económicos de corto plazo, pero también refleja problemas estructurales de largo plazo.
            2. La pandemia mostró la fragilidad del mercado laboral, especialmente por la alta informalidad.
            3. La recuperación posterior no ha sido suficiente para garantizar mejoras sostenidas por sí sola.
            4. El descenso del IPM sugiere avances en condiciones de vida, pero estos son graduales y requieren continuidad institucional.
            5. Las transferencias monetarias ayudaron a contener el deterioro, aunque no reemplazan la necesidad de empleo formal y productividad.
            """
        )

    with c2:
        st.markdown("### Recomendaciones")
        st.markdown(
            """
            1. Fortalecer la generación de empleo formal y estable.
            2. Reducir la dependencia de ingresos precarios e informales.
            3. Mantener políticas sociales focalizadas, pero conectadas con capacidades productivas.
            4. Proteger el poder adquisitivo de los hogares frente a la inflación de alimentos.
            5. Sostener inversiones en educación, vivienda, servicios públicos y desarrollo territorial.
            """
        )

    st.markdown(
        """
        <div class='insight-box'>
            <strong>Cierre</strong><br>
            Superar la pobreza exige combinar crecimiento económico inclusivo, empleo de calidad, estabilidad macroeconómica y políticas sociales sostenidas. La mejora reciente existe, pero puede ser frágil si no se traduce en oportunidades duraderas para los hogares.
        </div>
        """,
        unsafe_allow_html=True,
    )
