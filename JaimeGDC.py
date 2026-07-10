import streamlit as st
from style import apply_global_style

apply_global_style()


st.set_page_config(
    page_title="Jaime Gutiérrez de Calderón",
    page_icon="🤖",
    layout="wide"
)

# -------- GLOBAL STYLE --------
st.markdown(
    """
    <style>
    /* App background */
    .stApp {
        background-color: #0E2A47;
        color: white;
    }
    
    /* Reduce el espacio superior de la app */
    .block-container {
        padding-top: 1rem;  /* antes podía ser 3-4rem por defecto */
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Titles */
    h1, h2, h3, h4 {
        color: white;
    }

    /* Subtitle custom color */
    .subtitle {
        color: #9FC5FF;
        margin-top: 5px;
    }

    /* Text */
    p, li, span, div {
        color: white;
    }

    /* Links */
    a {
        color: #4DA3FF;
        font-weight: 600;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Horizontal rule */
    hr {
        border: 1px solid #1E4F8A;
    }

    /* Info box override */
    div[data-testid="stInfo"] {
        background-color: #143A63;
        border-left: 6px solid #4DA3FF;
        color: white;
    }

    /* Section blocks */
    .section-box {
        background-color: #143A63;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------- HEADER --------
st.markdown(
    """
    <h1 style="margin-bottom:0;">Jaime Gutiérrez de Calderón</h1>
    <h3 class="subtitle">Solutions Architect | Data Science | Generative AI</h3>
    """,
    unsafe_allow_html=True
)

# -------- INTRO --------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
        <div class="section-box">
        External Global Solutions Architect at Deloitte, supporting BBVA's digital transformation and enterprise innovation.
        I specialize in designing enterprise architectures, generative AI integration, cloud solutions (AWS), and data-driven decision support.
        Experienced in translating complex business needs into scalable technical solutions across banking and financial services.
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="section-box">
        <strong>📍 Madrid, Spain</strong><br>
        <strong>📧 Email:</strong> jaimegutierrezdecalderon12@gmail.com<br>
        <strong>📞 Phone:</strong> +34 609 724 692<br><br>

        🔗 <a href="https://github.com/jguti1201" target="_blank">GitHub</a>
        </div>
        """,
        unsafe_allow_html=True
    )


# -------- SKILLS --------
st.subheader("Technical Focus")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="section-box">
        <strong>Enterprise Architecture</strong>
        <ul>
            <li>Solutions Design (Functional & Technical)</li>
            <li>Demand Management & Prioritization</li>
            <li>Architecture Patterns & Best Practices</li>
            <li>Systems Integration & Microservices</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="section-box">
        <strong>Cloud & AI</strong>
        <ul>
            <li>AWS: EC2, Lambda, S3, DynamoDB, OpenSearch, Kinesis, Athena</li>
            <li>Generative AI & LLMs Integration</li>
            <li>Prompt Engineering & Semantic Search</li>
            <li>RAG & Vector Embeddings</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="section-box">
        <strong>Data & Analytics</strong>
        <ul>
            <li>Big Data: Hadoop, Spark, Kafka</li>
            <li>Data Lakes & Data Warehouses</li>
            <li>Machine Learning & Predictive Analytics</li>
            <li>Banking Domain: Retail, Enterprise, CIB</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------- ABOUT ME --------
st.subheader("About Me")

st.markdown(
    """
    <div class="section-box">
    I am a Solutions Architect with a strong passion for enterprise innovation and data-driven transformation.
    My experience spans designing scalable architectures, managing complex technical initiatives, and supporting strategic decision-making through analytics and AI.<br><br>
    
    Currently at Deloitte, I work with BBVA's Global Solutions Architect team to:
    <ul>
        <li>Design functional and technical solutions aligned with business strategy</li>
        <li>Manage demand for technology initiatives and innovation</li>
        <li>Build reusable patterns for generative AI, cloud infrastructure, and data platforms</li>
        <li>Support Architecture evolution and best practice dissemination</li>
    </ul>
    
    I thrive in collaborative, multi-disciplinary environments where I can bridge business and technology perspectives.
    My analytical mindset, combined with strong communication skills, enables me to work effectively with senior stakeholders and technical teams across different geographies and cultures.
    <br><br>
    
    Continuously learning and adapting to new technologies, I am committed to driving organizational transformation and delivering measurable business value through innovative solutions.
    </div>
    """,
    unsafe_allow_html=True
)
