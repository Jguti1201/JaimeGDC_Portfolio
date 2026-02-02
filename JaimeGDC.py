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
    <h3 class="subtitle">Data Scientist & AI Engineer</h3>
    """,
    unsafe_allow_html=True
)

# -------- INTRO --------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(
        """
        <div class="section-box">
        Data Scientist and Artificial Intelligence Consultant with over 2 years of experience developing advanced analytics, machine learning, and generative AI solutions in consulting environments. Strong background in mathematics and hands-on experience with Python, SQL, statistical analysis, NLP, and cloud services (Azure). I have worked on high-impact projects combining data analysis, AI models, and visualization to support business decision-making. Profile with strong analytical skills, quick learning ability, and experience collaborating with multidisciplinary teams.
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
        <strong>Data Science & Analytics</strong>
        <ul>
            <li>Machine Learning: supervised & unsupervised models</li>
            <li>Predictive Analytics & Pattern Detection</li>
            <li>Statistics & Exploratory Data Analysis (EDA)</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="section-box">
        <strong>Advanced AI</strong>
        <ul>
            <li>NLP & Semantic Search</li>
            <li>Generative AI & Prompt Engineering</li>
            <li>Embeddings & Vector Databases</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="section-box">
        <strong>Tools & Platforms</strong>
        <ul>
            <li>Python (pandas, numpy, scikit-learn), SQL</li>
            <li>Azure Cloud: Azure AI / Azure OpenAI / Azure Document Intelligence / Logic Apps / Azure Ai Search/ Azure Data Studio</li>
            <li>Power BI, Streamlit, Git, R (analytical use)</li>
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
    I am a highly adaptable Data Scientist with a strong passion for data analysis and artificial intelligence.
    My ability to learn quickly enables me to absorb new technologies and methodologies rapidly,
    allowing me to apply these skills effectively to solve complex problems.<br>

    I naturally thrive in collaborative environments, valuing the ideas and input of others to achieve shared goals.
    I communicate clearly and listen attentively to my team, which helps in building strong and effective relationships in any setting.
    My technical expertise is complemented by my ability to work cohesively within a team.<br>

    Overall, I consider myself a highly capable professional eager to tackle any challenge that comes my way.
    My strong learning capabilities, problem-solving skills, adaptability, teamwork, and effective communication
    make me a valuable asset in any environment. I am committed to continuously developing these skills to grow
    both personally and professionally.
    </div>
    """,
    unsafe_allow_html=True
)


