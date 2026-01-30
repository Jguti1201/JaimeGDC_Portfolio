import streamlit as st
from style import apply_global_style

apply_global_style()

st.markdown(
    """
    <style>
    /* Reduce el espacio superior de la app */
    .block-container {
        padding-top: 1rem;  /* Ajusta este valor: 0.5rem si quieres aún menos espacio */
        padding-bottom: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Opcional: reduce márgenes de títulos */
    h1, h2, h3 {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.set_page_config(layout="wide")
st.title("👤 About Me")

# -------- PROFESSIONAL EXPERIENCE --------
st.markdown("## 💼 Professional Experience")

# AI Strategy Consultant - DXC Technology
st.markdown(
    """
    **AI Strategy Consultant**  
    *DXC Technology — Madrid*  
    *Aug 2025 – Present*  

    - 📊 Designed and implemented enterprise AI adoption strategies aligned with ISO/IEC 42001.  
    - 🗂 Defined corporate AI roadmaps, use case catalogs, and prioritization frameworks.  
    - 🤝 Collaborated with multidisciplinary teams to evaluate, structure, and deliver data-driven initiatives.  
    - 🧩 Managed AI project portfolios, ensuring alignment between strategy, technology, and business needs.  
    - 🏆 Created training materials, awareness campaigns, and workshops to drive AI adoption.  

    **Soft Skills Developed:** Strategic thinking, leadership, cross-functional collaboration, stakeholder communication, adaptability.
    """
)

# Data Scientist & AI Consultant - KPMG
st.markdown(
    """
    **Data Scientist & AI Consultant**  
    *KPMG — Madrid*  
    *Oct 2023 – Oct 2025*  

    - 🤖 Developed and deployed data science and generative AI solutions across legal, audit, and financial consulting domains.  
    - 📝 Built intelligent assistants (KAI Legal, Audit, Deals) using NLP, embeddings, and vector search to enhance information accessibility.  
    - ☁️ Integrated Python-based AI pipelines with Azure AI and Azure OpenAI services.  
    - 🎯 Optimized AI model performance using prompt engineering, embeddings, and semantic search techniques.  
    - 📊 Designed dashboards and visualizations to communicate insights effectively to technical and non-technical stakeholders.  

    **Soft Skills Developed:** Problem-solving, analytical thinking, teamwork, communication, innovation mindset, adaptability.
    """
)

# Business Analytics Intern - Neovantas
st.markdown(
    """
    **Business Analytics Intern**  
    *Neovantas — Madrid*  
    *Jun 2022 – Aug 2022*  

    - 🧮 Collected, cleaned, and analyzed large datasets to extract actionable insights.  
    - 📈 Built forecasting models to predict customer satisfaction and business outcomes.  
    - 📊 Created interactive dashboards with Python and Power BI to visualize insights.  
    - 💡 Applied statistical analysis for trend identification and data-driven recommendations.  

    **Soft Skills Developed:** Attention to detail, analytical reasoning, data storytelling, time management, collaborative mindset.
    """
)
# -------- EDUCATION --------
st.markdown("## 🎓 Education")

st.markdown(
    """
    - **Master’s in Sports Big Data** (In Progress)  
      Universidad Europea — Madrid  

    - **Bachelor’s in Mathematics & Engineering Science**  
      Millikin University, USA
    """
)

# -------- LANGUAGES & SOFT SKILLS --------
st.markdown("## 🗣 Languages & Soft Skills")

st.markdown(
    """
    **Languages:** Spanish (Native), English (Fluent)

    **Soft Skills Highlighted Across Roles:**  
    - Impact-driven mindset 💪  
    - Strong collaboration 🤝  
    - Problem-solving & adaptability 🧠  
    - Strategic thinking 🎯  
    - Effective communication 🗣  
    - Innovation & creativity 💡
    """
)
