import streamlit as st
from style import apply_global_style

apply_global_style()

# --------------------
# Page config
# --------------------
st.set_page_config(
    layout="wide",
    page_title="AI Solutions & Generative AI"
)

# --------------------
# Custom CSS (Blue + White)
# --------------------
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background-color: #0E2A47;
        color: white;
    }

    /* Titles */
    h1, h2, h3, h4 {
        color: white;
    }

    /* Text */
    p, li, span, div {
        color: white;
    }

    /* Links */
    a {
        color: #4DA3FF;
        text-decoration: none;
        font-weight: 600;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Horizontal line */
    hr {
        border: 1px solid #1E4F8A;
    }

    /* Project cards */
    .project-card {
        background-color: #143A63;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
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
# Header
# --------------------
st.title("🤖 AI Solutions & Generative AI")

st.markdown(
    """
    AI-driven solutions focused on **NLP, Generative AI, and intelligent systems**  
    deployed in real consulting and product environments.
    """
)

# --------------------
# Function for project card
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
# --------------------
# Projects data
# --------------------
projects = [
    {
        "title": "Intelligent Padel Racket Recommender",
        "description": (
            "AI-powered recommendation system designed to help padel players choose "
            "the most suitable racket based on their playing style, skill level, "
            "injury constraints, and budget. The solution combines semantic embeddings, "
            "domain-specific documentation, and generative AI to deliver explainable "
            "and personalized recommendations."
        ),
        "tech": "Azure OpenAI, NLP, embeddings, vector similarity, Python, Streamlit",
        "link": "https://github.com/Jguti1201/Recomendador-de-palas-de-padel"
    },
    {
        "title": "LUC-IA – AI Assistant for Dentistry",
        "description": (
            "Generative AI assistant specialized in dentistry, built using a "
            "Retrieval-Augmented Generation (RAG) architecture. The system ingests "
            "clinical and technical PDF documentation, performs semantic search over "
            "vector embeddings, and generates accurate, referenced answers to support "
            "information retrieval in professional dental contexts."
        ),
        "tech": "OpenAI, LangChain, FAISS, NLP, RAG, Python, Streamlit",
        "link": "https://github.com/Jguti1201/IA-odontologa"
    }
]


# --------------------
# Projects section
# --------------------
st.header("🚀 AI Projects")

for p in projects:
    st.markdown(
        project_card(p["title"], p["description"], p["tech"], p["link"]),
        unsafe_allow_html=True
    )
