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
        External Global Solutions Architect specializing in enterprise digital transformation, cloud architecture, and generative AI integration.
        Currently supporting a leading Spanish banking group in designing scalable solutions that combine advanced analytics, machine learning, and LLM technologies.
        Experienced in designing architecture patterns, managing technology initiatives, and driving innovation across cloud platforms (Azure, AWS) and modern data ecosystems (Databricks, Data Lakes).
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
        <strong>Cloud & AI Platforms</strong>
        <ul>
            <li>Azure: AI Services, OpenAI, Document Intelligence, Databricks</li>
            <li>AWS: EC2, Lambda, S3, DynamoDB, OpenSearch, Kinesis, Athena</li>
            <li>Generative AI & LLMs: Prompt Engineering, RAG, Embeddings</li>
            <li>MLOps: Model Training, Monitoring, Deployment</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="section-box">
        <strong>Data & ML</strong>
        <ul>
            <li>Big Data: Hadoop, Spark, Kafka</li>
            <li>Data Platforms: Databricks, Data Lakes, Data Warehouses</li>
            <li>Machine Learning: Scikit-learn, TensorFlow, MLflow</li>
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
    
    Currently at Deloitte, I work with a leading Spanish banking group's architectural team to:
    <ul>
        <li>Design functional and technical solutions aligned with business strategy</li>
        <li>Manage demand for technology initiatives and innovation</li>
        <li>Build reusable patterns for generative AI, cloud infrastructure, and data platforms</li>
        <li>Support Architecture evolution and best practice dissemination across geographies</li>
    </ul>
    
    I thrive in collaborative, multi-disciplinary environments where I can bridge business and technology perspectives.
    My analytical mindset, combined with strong communication skills, enables me to work effectively with senior stakeholders and technical teams across different cultures.<br><br>
    
    Currently expanding expertise in machine learning platforms through Databricks professional certification, combining enterprise architecture thinking with hands-on ML engineering.
    Continuously learning and adapting to new technologies, I am committed to driving organizational transformation and delivering measurable business value through innovative solutions.
    </div>
    """,
    unsafe_allow_html=True
)
