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
# Header
# --------------------
st.title("🤖 AI Solutions & Generative AI")

st.markdown(
    """
    AI-driven solutions focused on **NLP, Generative AI, LLM Integration, Machine Learning, and intelligent systems**  
    deployed in enterprise consulting, fintech, and product environments.
    """
)

# --------------------
# Function for project card
# --------------------
def project_card(title, description, tech, link):
    if isinstance(tech, str):
        tech_list = [t.strip() for t in tech.split(",")]
    else:
        tech_list = tech
    tech_html = "".join([f"<span class='tech-badge'>{t}</span>" for t in tech_list])
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
# ENTERPRISE AI ARCHITECTURE EXPERIENCE
# --------------------
st.markdown(
    """
    ## 🏛️ Enterprise AI Architecture (Deloitte - Leading Spanish Banking Group)
    
    **Current Experience:** Design and integration patterns for Generative AI in banking environments
    
    - **LLM Integration Strategies:** Designing connections to Large Language Models while maintaining security and regulatory compliance
    - **Prompt Engineering:** Developing prompt patterns and strategies for financial domain-specific use cases
    - **Semantic Search & Embeddings:** Building vector-based search systems for document retrieval and knowledge discovery
    - **Channel-Specific AI:** Tailoring AI solutions across digital, mobile, presencial, and API-based channels
    - **Azure AI Ecosystem:** Leveraging Azure OpenAI, Azure AI Document Intelligence, Azure Cognitive Search for enterprise solutions
    - **AWS Infrastructure:** Utilizing AWS services (Lambda, EC2, S3, DynamoDB, OpenSearch, Kinesis, Athena) for scalable AI pipelines
    - **Databricks ML Platform:** Designing machine learning workflows using Databricks for model training, MLflow for experiment tracking, and Delta Lake for data governance
    - **Data Integration:** Designing data architectures (Data Lakes, Data Warehouses) to support AI and analytics initiatives
    - **Governance & Compliance:** Ensuring AI solutions meet banking regulations and risk management standards
    """
)

st.markdown("---")

# --------------------
# Projects data
# --------------------
projects = [
    {
        "title": "⚡ Rayo Vallecano Scout IA — AI-Powered Scouting Platform",
        "description": (
            "Enterprise-scale AI platform for sports intelligence combining generative AI, machine learning, NLP, and advanced analytics. "
            "Features: conversational player search using OpenAI, technical analysis generation (Anthropic Claude), "
            "ML-based tactical clustering and player similarity matching, semantic similarity for recommendations, and automated PDF report generation. "
            "Demonstrates end-to-end LLM integration, prompt engineering, ML pipelines, and AI-assisted decision support."
        ),
        "tech": "OpenAI, Anthropic Claude, Streamlit, Prompt Engineering, Semantic Search, Python, NLP, Scikit-learn, Machine Learning",
        "link": "https://github.com/Jguti1201/rayo_scouting_web"
    },
    {
        "title": "Intelligent Padel Racket Recommender",
        "description": (
            "AI-powered recommendation system using Azure OpenAI and semantic embeddings. Combines domain-specific "
            "documentation with vector similarity search to deliver explainable, personalized recommendations based on "
            "playing style, skill level, injury constraints, and budget. Demonstrates RAG principles, semantic matching, "
            "and Azure AI service integration."
        ),
        "tech": "Azure OpenAI, Embeddings, Vector Similarity, Python, Streamlit, NLP, Azure Services",
        "link": "https://github.com/Jguti1201/Recomendador-de-palas-de-padel"
    },
    {
        "title": "LUC-IA – AI Assistant for Dentistry",
        "description": (
            "Specialized generative AI assistant built using Retrieval-Augmented Generation (RAG) architecture. "
            "Ingests clinical and technical PDF documentation, performs semantic search over vector embeddings, "
            "and generates accurate, referenced answers for professional dental contexts. Demonstrates LLM integration, "
            "knowledge-grounded AI systems, and enterprise AI patterns."
        ),
        "tech": "OpenAI, LangChain, FAISS, RAG, Embeddings, Vector Search, Python, Streamlit",
        "link": "https://github.com/Jguti1201/IA-odontologa"
    }
]


# --------------------
# Projects section
# --------------------
st.header("🚀 AI & Generative AI Projects")

for p in projects:
    st.markdown(
        project_card(p["title"], p["description"], p["tech"], p["link"]),
        unsafe_allow_html=True
    )
