import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Boletín: Pobreza monetaria y multidimensional en Colombia (2018–2024)", layout="wide")

# =========================
# ESTILO
# =========================
st.markdown("""
<style>
.hero {background: linear-gradient(135deg,#1e3a8a,#2563eb);padding:2rem;border-radius:20px;color:white;margin-bottom:1.5rem}
.card {background:#f8fafc;padding:1.2rem;border-radius:15px;margin-bottom:1rem;border-left:5px solid #2563eb}
.box {background:white;padding:1rem;border-radius:12px;box-shadow:0 4px 12px rgba(0,0,0,0.05);margin-bottom:1rem}
.highlight {background:#e0f2fe;padding:1rem;border-radius:12px;margin-bottom:1rem}
</style>
""", unsafe_allow_html=True)

# =========================
# DATOS
# =========================

df_full = pd.DataFrame({
    "Año": [2018,2019,2020,2021,2022,2023,2024],
    "Pobreza Monetaria": [34.7,35.7,42.5,39.3,36.6,33.0,32.5],
    "Pobreza Extrema": [8.2,9.6,15.1,12.2,13.8,11.4,11.0],
    "Desempleo": [9.7,10.5,15.9,13.7,11.2,10.2,10.6],
    "Inflación": [3.18,3.80,1.61,5.62,13.12,9.28,7.0],
    "PIB": [2.6,3.3,-6.8,10.6,7.3,0.6,1.2],
    "Gini": [0.517,0.526,0.544,0.523,0.539,0.518,0.551]
})

df_pobreza = pd.DataFrame({
    "Año": [2018,2019,2020,2021,2022,2023,2024],
    "Pobreza": [35.5,36.5,43.1,39.7,36.6,34.6,31.8]
})

df_ipm = pd.DataFrame({
    "Año": [2018,2019,2020,2021,2022,2023,2024],
    "IPM": [8.0,7.2,7.5,6.5,5.2,4.9,4.6]
})

pagina = st.sidebar.radio("Secciones", [
    "Introducción",
    "Línea del tiempo",
    "Gráficas e indicadores",
    "Comparativa internacional",
    "Conclusiones"
])

# =========================
# INTRODUCCIÓN
# =========================
if pagina == "Introducción":
    st.markdown("<div class='hero'><h1>Boletín: Pobreza monetaria y multidimensional en Colombia (2018–2024)</h1></div>", unsafe_allow_html=True)

    st.markdown("### Pregunta problema")
    st.markdown("¿Qué tan extendida, profunda y estructural es la pobreza en Colombia según los principales indicadores monetarios y multidimensionales?")

    st.markdown("### Contexto del análisis")

    st.markdown("<div class='box'>El periodo 2018–2024 permite observar la evolución reciente de la pobreza, incluyendo el impacto de la pandemia y la recuperación económica posterior.</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>Se pueden comparar tres etapas: antes de pandemia, crisis y recuperación.</div>", unsafe_allow_html=True)
        st.markdown("<div class='card'>El análisis se enfoca en dinámicas actuales y relevantes.</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>Incluye dos gobiernos con enfoques distintos.</div>", unsafe_allow_html=True)
        st.markdown("<div class='card'>La pobreza depende de economía, empleo y política pública.</div>", unsafe_allow_html=True)

# =========================
# LINEA DEL TIEMPO
# =========================
elif pagina == "Línea del tiempo":
    st.title("Línea del tiempo")

    eventos = {
        2018: "Crecimiento insuficiente y presión migratoria",
        2019: "Nueva metodología y tensión social",
        2020: "Pandemia y crisis",
        2021: "Rebote e inflación",
        2022: "Inflación y cambio político",
        2023: "Subsidios y reducción",
        2024: "Desaceleración y reto fiscal"
    }

    for año, texto in eventos.items():
        st.markdown(f"<div class='box'><b>{año}</b><br>{texto}</div>", unsafe_allow_html=True)

# =========================
# GRAFICAS
# =========================
elif pagina == "Gráficas e indicadores":
    st.title("Gráficas e indicadores")

    st.subheader("Indicadores económicos y sociales")
    fig1 = px.line(df_full, x="Año", y=df_full.columns[1:], markers=True)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Pobreza monetaria")
    fig2 = px.line(df_pobreza, x="Año", y="Pobreza", markers=True)
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<div class='highlight'>La pobreza aumenta en 2020 por la pandemia y luego cae gradualmente, pero sigue siendo alta.</div>", unsafe_allow_html=True)

    st.subheader("IPM")
    fig3 = px.line(df_ipm, x="Año", y="IPM", markers=True)
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("<div class='highlight'>El IPM baja lentamente, reflejando mejoras estructurales.</div>", unsafe_allow_html=True)

# =========================
# COMPARATIVA
# =========================
elif pagina == "Comparativa internacional":
    st.title("Comparativa Colombia vs El Salvador")

    st.markdown("<div class='box'><b>2018-2019:</b> Diferencias en migración y estructura económica.</div>", unsafe_allow_html=True)
    st.markdown("<div class='box'><b>2020:</b> Ambos países golpeados por pandemia.</div>", unsafe_allow_html=True)
    st.markdown("<div class='box'><b>2021-2022:</b> Seguridad vs crisis social.</div>", unsafe_allow_html=True)
    st.markdown("<div class='box'><b>2023-2024:</b> Retos económicos persistentes.</div>", unsafe_allow_html=True)

# =========================
# CONCLUSIONES
# =========================
elif pagina == "Conclusiones":
    st.title("Conclusiones")

    st.markdown("""La pobreza en Colombia es estructural, sensible a crisis y depende de múltiples factores como empleo, inflación y políticas públicas. Aunque hay mejoras, siguen siendo frágiles y requieren soluciones de largo plazo.""")
