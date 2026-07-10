import streamlit as st
from style import apply_global_style

apply_global_style()

st.set_page_config(
    layout="wide",
    page_title="Data Science & Analytics Projects"
)

# --------------------
# GLOBAL STYLE
# --------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E2A47;
        color: white;
    }

    h1, h2, h3, h4 {
        color: white;
    }

    p, li {
        color: white;
        font-size: 0.95rem;
    }

    a {
        color: #4DA3FF;
        font-weight: 600;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    hr {
        border: 1px solid #1E4F8A;
        margin: 2rem 0;
    }

    .section-header {
        background: linear-gradient(90deg, #143A63, #0E2A47);
        padding: 1.2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
    }

    .project-card {
        background-color: #143A63;
        padding: 1.4rem;
        border-radius: 12px;
        height: 100%;
        box-shadow: 0 6px 16px rgba(0,0,0,0.25);
    }

    .tech-badge {
        display: inline-block;
        background-color: #1E4F8A;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.75rem;
        margin-right: 6px;
        margin-top: 6px;
    }

    /* Reduce el espacio superior de la app */
    .block-container {
        padding-top: 1rem;  /* Ajusta este valor: 0.5rem si quieres aún menos espacio */
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------
# PAGE TITLE
# --------------------
st.title("📊 Data Science & Analytics Projects")

st.markdown(
    """
    A curated selection of projects focused on **data-driven decision making,
    predictive modeling, and business intelligence**, developed using industry-standard tools.
    """
)

# --------------------
# REUSABLE PROJECT CARD
# --------------------
def project_card(title, description, tech, link):
    tech_html = "".join([f"<span class='tech-badge'>{t}</span>" for t in tech])
    return f"""
    <div class="project-card">
        <h4>{title}</h4>
        <p>{description}</p>
        {tech_html}
        <br><br>
        <a href="{link}" target="_blank">🔗 View on GitHub</a>
    </div>
    """

# ====================
# FLAGSHIP PROJECT: RAYO SCOUTING
# ====================
st.markdown(
    """
    <div class="section-header">
        <h2>⚡ Flagship Project: Rayo Vallecano Scout IA</h2>
        <p>Enterprise-scale analytics platform for sports intelligence and strategic decision support.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    project_card(
        "⚡ Rayo Vallecano Scout IA — Intelligent Scouting & Market Analysis",
        """Comprehensive platform for player analysis, market intelligence, and scouting support for Rayo Vallecano's sports direction.
        The system integrates multi-source data ingestion, advanced analytics, tactical clustering, AI-powered recommendations, and automated reporting.
        
        **Key Features:**
        • Multi-source data scraping (Transfermarkt, SofaScore) with incremental checkpointing
        • ETL pipelines: data cleaning, normalization, feature engineering (p90 metrics, percentiles)
        • Advanced analytics: tactical clustering by position, player similarity analysis (cosine similarity), adaptation scoring
        • Streamlit dashboard: executive overview, market explorer, player comparator, watchlist, AI assistant
        • Generative AI: conversational profile search (OpenAI), technical analysis (Anthropic Claude), automated PDF reporting
        • Business impact: 80% reduction in initial scouting analysis time, data-driven decision making with full traceability
        
        **Architecture:** Data Ingestion → ETL Processing → Analytics & Intelligence → Interactive Presentation Layer
        """,
        ["Python", "Pandas/NumPy", "Scikit-learn", "Streamlit", "OpenAI/Claude", "Selenium", "BeautifulSoup", "Clustering", "Prompt Engineering"],
        "https://github.com/Jguti1201/rayo_scouting_web"
    ),
    unsafe_allow_html=True
)

st.markdown("---")

# ====================
# PYTHON PROJECTS
# ====================

st.markdown(
    """
    <div class="section-header">
        <h2>🐍 Python Projects</h2>
        <p>End-to-end data science workflows: data preparation, modeling, and deployment.</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        project_card(
            "Automatic Call Categorization",
            "Machine learning project for classifying 21,915 call records into dissatisfaction "
            "and non-dissatisfaction using metrics, transcriptions, neural networks, and active learning.",
            ["Python", "TensorFlow", "Keras", "SHAP", "NLP", "Active Learning"],
            "https://github.com/Jguti1201/Automatic-Call-Categorization"
        ),
        unsafe_allow_html=True
    )
    

with col2:
    st.markdown(
        project_card(
            "Insurance NPS Analysis",
            "Data analysis project for insurance claims and NPS surveys from an Insurance company, "
            "including data cleaning, exploratory analysis, feature selection, and predictive modeling.",
            ["Python", "Pandas", "Scikit-learn", "Featurewiz", "EDA"],
            "https://github.com/Jguti1201/An-lisis-Aseguradora-nps"
        ),
        unsafe_allow_html=True
    )

# Espacio vertical antes de la segunda fila
st.markdown("<br><br>", unsafe_allow_html=True)
# ====================
# NUEVOS PROYECTOS DE LALIGA
# ====================
col3, col4 = st.columns(2)

with col3:
    st.markdown(
        project_card(
            "LaLiga Web Scraping",
            "Automated extraction of LaLiga 2025-26 match results, teams, scores, "
            "and statistics using Selenium and BeautifulSoup.",
            ["Python", "Selenium", "BeautifulSoup", "JSON"],
            "https://github.com/Jguti1201/Poryecto-Web-Scrapping-LaLiga"
        ),
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        project_card(
            "LaLiga Match Analytics Visualization",
            "Visualization dashboard for LaLiga 2025-26 results and player statistics, "
            "including goals, assists, cards, and match performance metrics.",
            ["Python", "Streamlit", "Plotly", "Pandas"],
            "https://github.com/Jguti1201/LaLiga-Match-Analytics-Visualization"
        ),
        unsafe_allow_html=True
    )

st.markdown("---")


# ====================
# R PROJECTS
# ====================
st.markdown(
    """
    <div class="section-header">
        <h2>📈 R Projects</h2>
        <p>Statistical modeling, web scraping, and analytical rigor for LaLiga data exploration.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Primera fila de proyectos
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        project_card(
            "🔹 Analisis Interactivo de Rendimiento de Jugadores",
            "Aplicación Shiny para explorar estadísticas de jugadores de LaLiga: filtrado por posición, equipo y jugador, visualizaciones interactivas y tablas exportables.",
            ["R", "Shiny", "ggplot2", "plotly", "DT"],
            "https://github.com/Jguti1201/Analisis-Interactivo-de-Rendimiento-de-Jugadores-de-LaLiga-Shiny-"
        ),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        project_card(
            "🔹 Predicción de Resultados de la Liga",
            "Proyecto de Machine Learning en R para predecir resultados de partidos de LaLiga usando Random Forest y análisis de métricas históricas de equipos y goles.",
            ["R", "caret", "randomForest", "ggplot2"],
            "https://github.com/Jguti1201/Proyecto-ML---Predicci-n-de-resultados-de-la-Liga-en-R"
        ),
        unsafe_allow_html=True
    )

# Espacio vertical antes de la segunda fila
st.markdown("<br><br>", unsafe_allow_html=True)

# Segunda fila de proyectos
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        project_card(
            "🔹 LaLiga Data Scraper & Analysis",
            "Scraping de datos oficiales de LaLiga, limpieza y análisis exploratorio con visualizaciones de goles, puntos y diferencias de goles por equipo.",
            ["R", "rvest", "dplyr", "ggplot2", "lubridate"],
            "https://github.com/Jguti1201/La-liga-data-secrapper-analysis-with-R"
        ),
        unsafe_allow_html=True
    )

with col2:
    st.write("")  # Puedes dejarlo vacío si no hay cuarto proyecto

st.markdown("---")
# ====================
# POWER BI PROJECTS
# ====================
st.markdown(
    """
    <div class="section-header">
        <h2>📊 Power BI Projects</h2>
        <p>Interactive dashboards focused on business performance and KPIs.</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        project_card(
            "Power BI – Data Roles & Salaries",
            "Dashboard on data professionals: roles, salary averages, preferred programming languages, "
            "country distribution, and satisfaction (work–life balance & pay).",
            ["Power BI", "Data Viz", "HR Analytics", "Survey"],
            "https://github.com/Jguti1201/PowerBi_DataAnalysisjobs/blob/main/PowerBI_Analisis_profesionales_en_analista_de_datos.pbix"
        ),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        project_card(
            "Power BI – F1 Data Analysis",
            "Dashboard exploring Formula 1 statistics: podium finishes by nationality, race counts by circuit, "
            "driver nationality distribution, and average positions of top drivers (Alonso, Hamilton, Schumacher).",
            ["Power BI", "Sports Analytics", "Visualization", "F1"],
            "https://github.com/Jguti1201/PowerBi_DataAnalysisjobs/blob/main/PowerBI_F1stats.pbix"
        ),
        unsafe_allow_html=True
    )

st.markdown("---")

# ====================
# SQL PROJECTS
# ====================
st.markdown(
    """
    <div class="section-header">
        <h2>🗄️ SQL Projects</h2>
        <p>Data extraction, transformation and analytical querying on large datasets.</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        project_card(
            "SQL – Spotify Music Database Analysis",
            "SQL exploration of Spotify datasets: identifies the most popular artists, tracks, albums, and genres using "
            "aggregate functions (AVG, MAX), GROUP BY, ORDER BY, LIMIT, and subqueries to match user-preferred artists.",
            ["SQL", "PostgreSQL", "Data Analysis", "Music Analytics"],
            "https://github.com/Jguti1201/SQL_spotify/blob/main/Spotify_exploration.sql"
        ),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        project_card(
            "SQL – Sports Injury Management Database",
            "Full SQL project designing a complete relational database for players, injuries, treatments, and specialists. "
            "Includes DDL creation (tables, PK/FK constraints), extensive data insertion, and analytical queries for filtering, "
            "searching, ordering, and aggregating information related to injuries and medical treatments.",
            ["SQL", "Database Design", "MySQL", "Sports Analytics"],
            "https://github.com/Jguti1201/SQL_spotify"
        ),
        unsafe_allow_html=True
    )
