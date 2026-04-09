import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------
st.set_page_config(
    page_title="Boletín: Pobreza en Colombia (2018–2024)",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# ESTILOS
# -----------------------------
st.markdown("""
<style>
    .main {
        background: linear-gradient(180deg, #f7f9fc 0%, #ffffff 100%);
    }

    .hero {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #2563eb 100%);
        padding: 2.2rem;
        border-radius: 24px;
        color: white;
        box-shadow: 0 10px 30px rgba(37, 99, 235, 0.18);
        margin-bottom: 1.2rem;
    }

    .hero h1 {
        font-size: 2.2rem;
        margin-bottom: 0.3rem;
    }

    .hero p {
        font-size: 1.02rem;
        opacity: 0.95;
        line-height: 1.6;
    }

    .question-box {
        background: #eff6ff;
        border-left: 6px solid #2563eb;
        padding: 1rem 1.1rem;
        border-radius: 16px;
        margin-top: 1rem;
        color: #0f172a;
    }

    .section-title {
        font-size: 1.7rem;
        font-weight: 700;
        margin-top: 1.4rem;
        margin-bottom: 0.8rem;
        color: #0f172a;
    }

    .card {
        background: white;
        padding: 1.2rem;
        border-radius: 20px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.07);
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }

    .mini-card {
        background: #ffffff;
        padding: 1rem;
        border-radius: 18px;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
        border: 1px solid #e5e7eb;
        height: 100%;
    }

    .insight {
        background: #f8fafc;
        border-left: 5px solid #2563eb;
        padding: 1rem;
        border-radius: 14px;
        margin-top: 0.8rem;
        color: #1e293b;
        line-height: 1.65;
    }

    .timeline-box {
        background: linear-gradient(180deg, #ffffff 0%, #f8fbff 100%);
        border: 1px solid #dbeafe;
        border-radius: 20px;
        padding: 1.2rem;
        box-shadow: 0 8px 20px rgba(37, 99, 235, 0.08);
        margin-bottom: 1rem;
    }

    .year-badge {
        display: inline-block;
        background: #2563eb;
        color: white;
        font-weight: 700;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        margin-bottom: 0.6rem;
        font-size: 0.95rem;
    }

    .compare-box {
        background: white;
        padding: 1rem;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }

    .conclusion-box {
        background: linear-gradient(135deg, #eff6ff 0%, #ffffff 100%);
        padding: 1.3rem;
        border-radius: 22px;
        border: 1px solid #bfdbfe;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.09);
        line-height: 1.7;
        margin-bottom: 1rem;
    }

    .ref-box {
        background: #0f172a;
        color: white;
        padding: 1.2rem;
        border-radius: 20px;
        line-height: 1.8;
        margin-top: 1rem;
    }

    .small-muted {
        color: #475569;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# DATOS
# -----------------------------
df_indicadores = pd.DataFrame({
    "Año": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Pobreza Monetaria": [34.7, 35.7, 42.5, 39.3, 36.6, 33.0, 32.5],
    "Pobreza Extrema": [8.2, 9.6, 15.1, 12.2, 13.8, 11.4, 11.0],
    "Desempleo": [9.7, 10.5, 15.9, 13.7, 11.2, 10.2, 10.6],
    "Inflación": [3.18, 3.80, 1.61, 5.62, 13.12, 9.28, 7.0],
    "Crecimiento PIB": [2.6, 3.3, -6.8, 10.6, 7.3, 0.6, 1.2],
    "Gini": [0.517, 0.526, 0.544, 0.523, 0.539, 0.518, 0.551]
})

df_pobreza = pd.DataFrame({
    "Año": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Pobreza Monetaria": [35.5, 36.5, 43.1, 39.7, 36.6, 34.6, 31.8]
})

df_ipm = pd.DataFrame({
    "Año": [2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "IPM": [8.0, 7.2, 7.5, 6.5, 5.2, 4.9, 4.6]
})

timeline_data = {
    2018: {
        "titulo": "Crecimiento insuficiente y presión migratoria",
        "texto": """La economía colombiana creció 2,6%, pero ese crecimiento no fue suficiente para reducir de manera importante la pobreza. La pobreza monetaria se ubicó en 34,7% y el coeficiente de Gini en 0,517, mostrando que la desigualdad seguía alta. Además, la llegada masiva de población migrante desde Venezuela presionó el mercado laboral informal, especialmente en sectores como comercio, construcción y servicios. A esto se sumó la llegada del gobierno de Iván Duque, con una agenda centrada en la llamada “Economía Naranja”, que no logró absorber con fuerza la mano de obra más vulnerable."""
    },
    2019: {
        "titulo": "Nueva metodología, más pobreza visible y tensión social",
        "texto": """En 2019 el DANE actualizó la metodología de medición de pobreza, lo que permitió mostrar de forma más precisa la situación real de muchos hogares. La pobreza monetaria subió a 35,7%, la pobreza extrema a 9,6% y el Gini empeoró a 0,526. Aunque el PIB creció 3,3%, el desempleo llegó a 10,5%, reflejando que el crecimiento económico no estaba generando suficiente empleo formal. Ese mismo año aumentó la tensión social con el paro del 21N, donde se evidenció el malestar de amplios sectores de la población frente a la desigualdad, el desempleo y la falta de oportunidades."""
    },
    2020: {
        "titulo": "Pandemia, confinamiento y fuerte deterioro social",
        "texto": """El 2020 fue el año más crítico del periodo analizado. La pandemia y las cuarentenas afectaron fuertemente a un país con alta informalidad laboral. La pobreza monetaria subió a 42,5%, la pobreza extrema a 15,1%, el desempleo alcanzó niveles históricos y el Gini llegó a 0,544. Muchas familias perdieron de forma repentina sus ingresos, lo que se reflejó en fenómenos como los trapos rojos en barrios populares. Frente a esto, el gobierno creó Ingreso Solidario y otras ayudas que evitaron un deterioro aún mayor, aunque no lograron impedir el fuerte aumento de la pobreza."""
    },
    2021: {
        "titulo": "Rebote económico, inflación y estallido social",
        "texto": """Aunque en 2021 la economía creció 10,6%, la mejora no se tradujo de forma inmediata en bienestar para los hogares. La pobreza monetaria bajó solo a 39,3% y la pobreza extrema se mantuvo alta en 12,2%. A esto se sumó el inicio de un fuerte aumento en la inflación, sobre todo en alimentos, lo que afectó más a los hogares de bajos ingresos. Ese año también estuvo marcado por el Paro Nacional, detonando por la reforma tributaria, pero alimentado por un malestar social acumulado desde años atrás. En medio de este contexto, el país avanzó con el Estatuto Temporal de Protección para migrantes venezolanos."""
    },
    2022: {
        "titulo": "Inflación desbordada y cambio político",
        "texto": """En 2022 la economía siguió creciendo, con un PIB de 7,3%, y la pobreza monetaria bajó a 36,6%. Sin embargo, el mayor problema fue la inflación, que cerró en 13,12%, encareciendo especialmente los alimentos y afectando con más fuerza a los hogares pobres. Aunque hubo una recuperación económica, el costo de vida redujo el impacto positivo de esa mejora. Este año también marcó un cambio político importante con la llegada de Gustavo Petro a la presidencia, lo que abrió una nueva etapa enfocada en justicia social, reforma tributaria y ampliación de políticas sociales."""
    },
    2023: {
        "titulo": "Menor crecimiento, pero caída de la pobreza por subsidios",
        "texto": """En 2023 el PIB solo creció 0,6%, pero la pobreza monetaria cayó a 33,0% y la pobreza extrema a 11,4%. Esta reducción no se explicó tanto por la fuerza del mercado laboral, sino principalmente por la caída en la inflación de alimentos y por la ampliación de transferencias monetarias, especialmente a través de Renta Ciudadana. A pesar de esta mejora, surgieron dudas sobre su sostenibilidad, ya que sectores clave como la construcción mostraron debilidad y la inversión privada cayó. En otras palabras, la pobreza bajó, pero con bases todavía frágiles."""
    },
    2024: {
        "titulo": "Desaceleración, límite fiscal y reto de sostenibilidad",
        "texto": """En 2024 la inflación comenzó a bajar y volvió a un dígito, lo que dio algo de alivio a los hogares. Sin embargo, el desempleo se mantuvo alrededor del 10% y la creación de empleo siguió débil. Además, el gobierno enfrentó restricciones fiscales más fuertes, lo que limitó la capacidad de seguir reduciendo la pobreza mediante subsidios. En este contexto, el gran reto pasó a ser la reactivación económica sostenible, basada en empleo formal e inversión, más que en transferencias temporales. También persistieron problemas estructurales en seguridad y desigualdad territorial, especialmente en zonas rurales."""
    }
}

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("Navegación")
seccion = st.sidebar.radio(
    "Ir a:",
    [
        "Inicio",
        "Introducción",
        "Línea del tiempo",
        "Gráficas e indicadores",
        "Comparativa con El Salvador",
        "Conclusiones",
        "Referencias"
    ]
)

st.sidebar.markdown("### Resumen rápido")
st.sidebar.metric("Pobreza monetaria 2024", "32,5%")
st.sidebar.metric("Pobreza extrema 2024", "11,0%")
st.sidebar.metric("IPM 2024", "4,6")

# -----------------------------
# HERO
# -----------------------------
if seccion == "Inicio":
    st.markdown("""
    <div class="hero">
        <h1>Boletín: Pobreza monetaria y multidimensional en Colombia (2018–2024)</h1>
        <p>
            Un análisis visual e interpretativo sobre la evolución reciente de la pobreza en Colombia,
            incorporando indicadores monetarios, multidimensionales, contexto económico y una comparación
            internacional con El Salvador.
        </p>
        <div class="question-box">
            <strong>Pregunta problema:</strong><br>
            ¿Qué tan extendida, profunda y estructural es la pobreza en Colombia según los principales
            indicadores monetarios y multidimensionales?
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.markdown("""
    <div class="mini-card">
        <h4>Extensión</h4>
        <p class="small-muted">
            La pobreza monetaria muestra cuántas personas no alcanzan ingresos suficientes para cubrir una canasta básica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    c2.markdown("""
    <div class="mini-card">
        <h4>Profundidad</h4>
        <p class="small-muted">
            La pobreza extrema y la persistencia de carencias revelan qué tan severas son las limitaciones que enfrentan muchos hogares.
        </p>
    </div>
    """, unsafe_allow_html=True)
    c3.markdown("""
    <div class="mini-card">
        <h4>Estructura</h4>
        <p class="small-muted">
            El IPM ayuda a ver que la pobreza no es solo falta de ingreso, sino también rezagos en educación, trabajo, vivienda y servicios.
        </p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# INTRODUCCIÓN
# -----------------------------
if seccion == "Introducción":
    st.markdown('<div class="section-title">Introducción</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1.3, 1])

    with col1:
        st.markdown("""
        <div class="card">
            <p>
            El periodo de análisis comprendido entre 2018 y 2024 fue seleccionado porque permite observar de manera clara los cambios más recientes en la evolución de la pobreza en Colombia. En estos años se presentan hechos clave que afectan directamente las condiciones de vida de la población, como el impacto de la pandemia en 2020 y la recuperación económica que se da en los años posteriores.
            </p>
            <p>
            Además, este rango de tiempo resulta interesante porque permite comparar distintas etapas del país: un periodo previo a la pandemia, el choque económico que esta generó y el proceso de ajuste que vino después. Esto hace posible entender no solo cómo cambia la pobreza en momentos de crisis, sino también qué tan efectiva ha sido la recuperación.
            </p>
            <p>
            Por otro lado, trabajar con este periodo facilita enfocarse en dinámicas actuales, lo que permite que el análisis sea más relevante y cercano a la realidad que vive el país hoy en día, en lugar de centrarse en datos más antiguos que podrían no reflejar las condiciones actuales.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="mini-card">
            <h4>¿Por qué este periodo?</h4>
            <p class="small-muted">
                Porque permite ver tres momentos distintos: etapa prepandemia, choque económico de 2020 y recuperación posterior.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mini-card">
            <h4>¿Qué aporta al análisis?</h4>
            <p class="small-muted">
                Hace posible observar cómo interactúan el mercado laboral, el crecimiento económico, la inflación y la política social.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mini-card">
            <h4>Enfoque central</h4>
            <p class="small-muted">
                Entender si la pobreza en Colombia ha sido un fenómeno transitorio o si conserva rasgos profundos y estructurales.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
        Adicionalmente, el periodo analizado abarca dos gobiernos con enfoques distintos en términos económicos y sociales. En los años previos y durante la pandemia, la pobreza estuvo fuertemente influenciada por el mercado laboral, la caída de ingresos y el desempleo. En los años más recientes, se observa un mayor énfasis en políticas sociales y transferencias monetarias dirigidas a los hogares más vulnerables. Comparar ambos contextos permite entender que la evolución de la pobreza no depende de un solo factor, sino de la combinación entre economía, empleo y política pública.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# LÍNEA DEL TIEMPO
# -----------------------------
if seccion == "Línea del tiempo":
    st.markdown('<div class="section-title">Línea del tiempo</div>', unsafe_allow_html=True)
    st.caption("Selecciona un año para ver el hecho principal y su contexto.")

    year_selected = st.select_slider(
        "Año",
        options=[2018, 2019, 2020, 2021, 2022, 2023, 2024],
        value=2020
    )

    evento = timeline_data[year_selected]

    st.markdown(f"""
    <div class="timeline-box">
        <div class="year-badge">{year_selected}</div>
        <h3 style="margin-top:0; color:#0f172a;">{evento["titulo"]}</h3>
        <p style="line-height:1.7; color:#1e293b;">{evento["texto"]}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Vista general por años")
    cols = st.columns(3)
    years = list(timeline_data.keys())

    for i, y in enumerate(years):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="mini-card">
                <h4>{y}</h4>
                <p class="small-muted"><strong>{timeline_data[y]["titulo"]}</strong></p>
                <p class="small-muted">{timeline_data[y]["texto"][:180]}...</p>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------
# GRÁFICAS E INDICADORES
# -----------------------------
if seccion == "Gráficas e indicadores":
    st.markdown('<div class="section-title">Gráficas e indicadores</div>', unsafe_allow_html=True)

    # Gráfica 1
    st.markdown("### Evolución de indicadores económicos y sociales en Colombia (2018–2024)")

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df_indicadores["Año"], y=df_indicadores["Pobreza Monetaria"],
                              mode="lines+markers", name="Pobreza Monetaria"))
    fig1.add_trace(go.Scatter(x=df_indicadores["Año"], y=df_indicadores["Pobreza Extrema"],
                              mode="lines+markers", name="Pobreza Extrema"))
    fig1.add_trace(go.Scatter(x=df_indicadores["Año"], y=df_indicadores["Desempleo"],
                              mode="lines+markers", name="Desempleo"))
    fig1.add_trace(go.Scatter(x=df_indicadores["Año"], y=df_indicadores["Inflación"],
                              mode="lines+markers", name="Inflación"))
    fig1.add_trace(go.Scatter(x=df_indicadores["Año"], y=df_indicadores["Crecimiento PIB"],
                              mode="lines+markers", name="Crecimiento PIB"))
    fig1.add_trace(go.Scatter(x=df_indicadores["Año"], y=df_indicadores["Gini"] * 100,
                              mode="lines+markers", name="Gini x100"))

    fig1.update_layout(
        height=560,
        template="plotly_white",
        xaxis_title="Año",
        yaxis_title="Valor",
        legend_title="Indicadores",
        hovermode="x unified"
    )
    st.plotly_chart(fig1, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Pico de pobreza monetaria", "42,5%", "2020")
    c2.metric("Mayor inflación", "13,12%", "2022")
    c3.metric("Mayor crecimiento PIB", "10,6%", "2021")

    st.markdown("""
    <div class="insight">
        Esta gráfica muestra que los indicadores no evolucionan de forma aislada. La pobreza monetaria y extrema empeoran con fuerza en 2020, mientras el desempleo alcanza niveles críticos. Después, la economía rebota y algunos indicadores mejoran, pero la inflación y la desigualdad continúan afectando la recuperación. En otras palabras, la salida de la crisis no fue lineal ni homogénea.
    </div>
    """, unsafe_allow_html=True)

    # Gráfica 2
    st.markdown("### Evolución de la pobreza monetaria (2018–2024)")
    fig2 = px.area(
        df_pobreza,
        x="Año",
        y="Pobreza Monetaria",
        markers=True
    )
    fig2.update_layout(
        height=500,
        template="plotly_white",
        xaxis_title="Año",
        yaxis_title="Porcentaje (%)"
    )
    st.plotly_chart(fig2, use_container_width=True)

    a1, a2 = st.columns(2)
    with a1:
        st.markdown("""
        <div class="mini-card">
            <h4>Lectura general</h4>
            <p class="small-muted">
                La gráfica de pobreza monetaria permite ver qué tan extendida ha estado la pobreza en Colombia entre 2018 y 2024, es decir, qué porcentaje de la población no contó con ingresos suficientes para cubrir una canasta básica de bienes y servicios.
            </p>
            <p class="small-muted">
                Durante los primeros años del periodo se observa un nivel alto y relativamente estable, lo que ya mostraba que una parte importante de la población vivía en condiciones económicas vulnerables.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with a2:
        st.markdown("""
        <div class="mini-card">
            <h4>Momento crítico</h4>
            <p class="small-muted">
                El cambio más fuerte se da en 2020, cuando la pobreza monetaria aumenta de manera marcada. Esto se relaciona directamente con la pandemia, las cuarentenas y la pérdida de ingresos de millones de hogares.
            </p>
            <p class="small-muted">
                Ese aumento confirma que la pobreza monetaria es muy sensible a choques económicos fuertes.
            </p>
        </div>
        """, unsafe_allow_html=True)

    b1, b2, b3 = st.columns(3)
    with b1:
        st.markdown("""
        <div class="mini-card">
            <h4>Después de 2020</h4>
            <p class="small-muted">
                A partir de 2021 se observa una reducción gradual del indicador, asociada a la reapertura económica, la recuperación parcial del empleo y el papel de las transferencias monetarias.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with b2:
        st.markdown("""
        <div class="mini-card">
            <h4>Lo que sugiere</h4>
            <p class="small-muted">
                La gráfica también muestra que el problema no depende únicamente del crecimiento económico. Puede haber recuperación macroeconómica sin una mejora suficiente e inmediata para todos los hogares.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with b3:
        st.markdown("""
        <div class="mini-card">
            <h4>Idea central</h4>
            <p class="small-muted">
                La pobreza monetaria sigue siendo un problema amplio y persistente. Aunque bajó después de la pandemia, todavía deja ver condiciones económicas muy inestables para una parte importante de la población.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Gráfica 3
    st.markdown("### Evolución del Índice de Pobreza Multidimensional (IPM) (2018–2024)")
    fig3 = px.bar(
        df_ipm,
        x="Año",
        y="IPM",
        text="IPM"
    )
    fig3.update_traces(textposition="outside")
    fig3.update_layout(
        height=500,
        template="plotly_white",
        xaxis_title="Año",
        yaxis_title="IPM (%)"
    )
    st.plotly_chart(fig3, use_container_width=True)

    d1, d2 = st.columns(2)
    with d1:
        st.markdown("""
        <div class="mini-card">
            <h4>Comportamiento del IPM</h4>
            <p class="small-muted">
                En el caso del IPM, la gráfica se comporta de una forma un poco diferente. Aunque también hay cambios en el tiempo, estos son más suaves y no tan bruscos como en la pobreza monetaria.
            </p>
            <p class="small-muted">
                Por ejemplo, en 2020 no se ve un aumento tan fuerte, lo que muestra que las condiciones de vida no cambian tan rápido como los ingresos.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with d2:
        st.markdown("""
        <div class="mini-card">
            <h4>Tendencia estructural</h4>
            <p class="small-muted">
                A lo largo de los años, el IPM ha ido bajando, lo cual es positivo porque significa que, poco a poco, han mejorado aspectos como la educación, la vivienda o el acceso a servicios. Sin embargo, este cambio es lento, lo que refleja que estos problemas son más estructurales.
            </p>
        </div>
        """, unsafe_allow_html=True)

    e1, e2, e3, e4 = st.columns(4)
    e1.markdown("""
    <div class="mini-card">
        <h4>Educación</h4>
        <p class="small-muted">Incluye problemas como bajo logro educativo o analfabetismo, que limitan oportunidades de largo plazo.</p>
    </div>
    """, unsafe_allow_html=True)

    e2.markdown("""
    <div class="mini-card">
        <h4>Trabajo</h4>
        <p class="small-muted">Incorpora desempleo de larga duración e informalidad, factores que afectan la estabilidad del ingreso.</p>
    </div>
    """, unsafe_allow_html=True)

    e3.markdown("""
    <div class="mini-card">
        <h4>Vivienda y servicios</h4>
        <p class="small-muted">Considera hacinamiento, calidad de materiales, acceso a agua y otras condiciones básicas de vida.</p>
    </div>
    """, unsafe_allow_html=True)

    e4.markdown("""
    <div class="mini-card">
        <h4>Niñez</h4>
        <p class="small-muted">La inasistencia escolar y otras carencias tempranas pueden reproducir desigualdades a futuro.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
        En general, este análisis permite entender que la pobreza en Colombia no es solo falta de dinero, sino un conjunto de limitaciones en distintas áreas de la vida. Por eso, mientras la pobreza monetaria reacciona más rápido a crisis y recuperaciones, la pobreza multidimensional revela problemas más persistentes y difíciles de resolver en el corto plazo.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# COMPARATIVA CON EL SALVADOR
# -----------------------------
if seccion == "Comparativa con El Salvador":
    st.markdown('<div class="section-title">Comparativa con El Salvador</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="compare-box">
        <h4>2018–2019: El cambio de guardia</h4>
        <p><strong>Colombia:</strong> transición a Duque, crecimiento insuficiente (2,6%) y presión por la migración venezolana.</p>
        <p><strong>El Salvador:</strong> 2019 marcó el quiebre político con la llegada de Nayib Bukele, en un país con estancamiento histórico y fuerte violencia estructural.</p>
        <p><strong>Diferencia clave:</strong> Colombia recibe migrantes; El Salvador depende de remesas. En 2019, la pobreza monetaria salvadoreña rondaba el 22,8% y las remesas representaban aproximadamente el 20% del PIB.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="compare-box">
        <h4>2020: El choque de la pandemia</h4>
        <p><strong>Colombia:</strong> la pobreza monetaria saltó a 42,5% y se creó Ingreso Solidario.</p>
        <p><strong>El Salvador:</strong> la economía cayó -7,9% y el gobierno entregó un subsidio directo de 300 dólares a la mayoría de hogares, una respuesta más simple y agresiva, aunque con mayor presión sobre la deuda pública.</p>
        <p><strong>Lectura comparada:</strong> en ambos casos la pobreza aumentó, pero en El Salvador las remesas ayudaron a amortiguar parte del golpe económico.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="compare-box">
        <h4>2021–2022: Seguridad vs. inflación</h4>
        <p><strong>Colombia:</strong> rebote económico de 10,6%, pero con Paro Nacional, conflictividad social e inflación creciente.</p>
        <p><strong>El Salvador:</strong> mientras Colombia enfrentaba protestas, El Salvador profundizó su guerra contra las pandillas y redujo drásticamente los homicidios.</p>
        <p><strong>Contraste:</strong> El Salvador no sufrió la devaluación del peso por estar dolarizado, pero la inflación de alimentos también golpeó. En 2022 llegó a 6,7%, menor que el 13,1% de Colombia, pero significativa para una economía con menor margen de ajuste monetario.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="compare-box">
        <h4>2023–2024: El modelo Bukele y el reto económico</h4>
        <p><strong>Colombia:</strong> desaceleración de 0,6% en 2023, pero caída de la pobreza apoyada en subsidios.</p>
        <p><strong>El Salvador:</strong> crecimiento moderado, alrededor del 2,4%–2,6%, con señales de aumento de pobreza extrema en 2024.</p>
        <p><strong>Dato relevante:</strong> en 2024, el 75,8% de los salvadoreños identifica la economía como su principal problema, superando incluso a la seguridad.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
        La comparación permite ver que la pobreza no responde a una sola lógica. En Colombia, el mercado laboral, la informalidad y la desigualdad tienen un peso central. En El Salvador, además de la pobreza y el bajo crecimiento, aparecen factores como la dependencia de remesas, la dolarización y el peso de la seguridad pública. Esto refuerza la idea de que las estrategias para reducir la pobreza deben adaptarse a la estructura específica de cada país.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# CONCLUSIONES
# -----------------------------
if seccion == "Conclusiones":
    st.markdown('<div class="section-title">Conclusiones</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="conclusion-box">
        El análisis del periodo 2018–2024 permite concluir que la pobreza en Colombia sigue siendo un fenómeno amplio, complejo y persistente, que no puede entenderse únicamente desde la falta de ingresos, sino como el resultado de múltiples factores económicos, sociales e institucionales que interactúan entre sí. Aunque el país ha logrado avances después del choque generado por la pandemia, esos avances todavía no son suficientes para resolver el problema de manera estructural.
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="mini-card">
            <h4>1. Alta sensibilidad de la pobreza monetaria</h4>
            <p class="small-muted">
                El fuerte deterioro de 2020 mostró que muchos hogares siguen siendo altamente vulnerables a choques económicos. La informalidad, la inestabilidad laboral y la baja capacidad de ahorro hacen que amplios sectores de la población puedan caer o recaer en pobreza con rapidez.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mini-card">
            <h4>2. El IPM cambia más lento</h4>
            <p class="small-muted">
                La reducción del Índice de Pobreza Multidimensional ha sido positiva, pero gradual. Eso confirma que las condiciones de vida, la educación, la vivienda y el acceso a oportunidades no mejoran al mismo ritmo que los ingresos.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mini-card">
            <h4>3. Crecer no basta</h4>
            <p class="small-muted">
                El crecimiento económico por sí solo no garantiza una reducción significativa de la pobreza. En varios momentos del periodo hubo expansión económica sin mejoras proporcionales en el bienestar de los hogares.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="mini-card">
            <h4>4. La inflación golpea más a los pobres</h4>
            <p class="small-muted">
                El aumento de precios, especialmente en alimentos, redujo el poder adquisitivo de los hogares más vulnerables incluso en medio de la recuperación.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mini-card">
            <h4>5. Las transferencias ayudaron, pero abren dudas</h4>
            <p class="small-muted">
                Las políticas sociales y las transferencias monetarias fueron importantes para reducir la pobreza reciente, aunque persisten interrogantes sobre su sostenibilidad en un escenario de mayores restricciones fiscales.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="mini-card">
            <h4>6. Reto hacia adelante</h4>
            <p class="small-muted">
                El desafío no es solo seguir reduciendo la pobreza, sino hacerlo de manera sostenible, con empleo formal, más productividad, fortalecimiento del capital humano y menor desigualdad territorial.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="insight">
        En conjunto, los resultados permiten afirmar que la pobreza en Colombia es simultáneamente un problema extendido, profundo y estructural. Es extendido porque afecta a una proporción significativa de la población; es profundo porque implica carencias importantes tanto en ingresos como en condiciones de vida; y es estructural porque está vinculado a problemas persistentes que no se resuelven en el corto plazo. Si no se avanza hacia un modelo de crecimiento más inclusivo y estable, existe el riesgo de que los avances recientes se reviertan ante futuros choques económicos.
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# REFERENCIAS
# -----------------------------
if seccion == "Referencias":
    st.markdown('<div class="section-title">Referencias</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="ref-box">
        DANE (2024). <i>Pobreza monetaria y desigualdad en Colombia 2023</i>. https://www.dane.gov.co<br><br>
        DANE (2024). <i>Pobreza multidimensional en Colombia 2023</i>. https://www.dane.gov.co<br><br>
        DANE. <i>Ficha metodológica de pobreza monetaria y multidimensional</i>. https://www.dane.gov.co<br><br>
        <i>Técnicas de medición económica: Metodología y aplicaciones en Colombia</i>. Cali: Editorial Universidad Icesi.<br><br>
        Banco de la República de Colombia (2023–2024). <i>Informes económicos y reportes de coyuntura</i>. https://www.banrep.gov.co<br><br>
        Fondo Monetario Internacional (2023). <i>Perspectivas económicas de Colombia</i>. https://www.imf.org<br><br>
        Banco Mundial (2023). <i>Datos de desarrollo y pobreza</i>. https://www.worldbank.org
    </div>
    """, unsafe_allow_html=True)
