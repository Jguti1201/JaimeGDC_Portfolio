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

# External Global Solutions Architect - Deloitte
st.markdown(
    """
    **External Global Solutions Architect**  
    *Deloitte — Madrid (Supporting a Leading Spanish Banking Group)*  
    *Current*  

    Supporting a leading Spanish banking group's digital transformation and enterprise innovation as part of the Global Solutions Architect (GSA) team.
    
    **Key Responsibilities:**
    
    **🎯 Demand Management & Architecture Governance**
    - Identify and prioritize technology initiatives aligned with the banking group's global and local business strategies
    - Evaluate architectural impact and validate alignment with enterprise architecture standards
    - Communicate technical constraints and opportunities to business stakeholders
    
    **🤝 Solutions Architecture Support**
    - Facilitate design decisions for enterprise transformation projects
    - Validate solution alignment with global strategy while supporting local market needs
    - Identify synergies and opportunities for component reuse across initiatives
    
    **🏛️ Generative AI & Machine Learning Architecture**
    - Design channel-specific AI integration strategies (digital, mobile, presencial, APIs)
    - Develop LLM connection patterns and prompt engineering strategies maintaining security and regulatory compliance
    - Define Azure AI ecosystem approaches (Azure OpenAI, Document Intelligence, Cognitive Search)
    - Establish Databricks ML platform patterns for model training, experiment tracking (MLflow), and data governance (Delta Lake)
    - Design machine learning pipelines for predictive analytics and decision support systems
    - Define AWS infrastructure approaches when needed (EC2, Lambda, S3, DynamoDB, OpenSearch, Kinesis, Athena)
    - Establish data architecture patterns for AI-enabled solutions (Data Lakes, Warehouses, embeddings, vector search)
    
    **📚 Architecture Evolution & Knowledge Management**
    - Build centralized knowledge base of architectural patterns and best practices
    - Drive adoption of new technologies (Azure, Databricks, Generative AI) across the Solutions Architect community
    - Facilitate cross-geography knowledge transfer and lessons learned sharing
    
    **🔧 Technical Domains:** Generative AI, LLMs, Azure, AWS, Databricks, Big Data, Machine Learning, Microservices, Data Platforms, Banking Architecture
    
    **Soft Skills Developed:** Strategic thinking, stakeholder management, cross-functional leadership, technical communication, adaptability.
    """
)

st.markdown("---")

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
    - 🔬 Applied machine learning techniques for classification, clustering, and predictive modeling tasks.

    **Soft Skills Developed:** Problem-solving, analytical thinking, teamwork, communication, innovation mindset, adaptability.
    """
)

st.markdown("---")

# AI Strategy Consultant - DXC Technology
st.markdown(
    """
    **AI Strategy Consultant**  
    *DXC Technology — Madrid*  
    *Aug 2025 – Oct 2025*  

    - 📊 Designed and implemented enterprise AI adoption strategies aligned with ISO/IEC 42001.  
    - 📋 Defined corporate AI roadmaps, use case catalogs, and prioritization frameworks.  
    - 🤝 Collaborated with multidisciplinary teams to evaluate, structure, and deliver data-driven initiatives.  
    - 🛠️ Managed AI project portfolios, ensuring alignment between strategy, technology, and business needs.  
    - 🎓 Created training materials, awareness campaigns, and workshops to drive AI adoption.  

    **Soft Skills Developed:** Strategic thinking, leadership, cross-functional collaboration, stakeholder communication, adaptability.
    """
)

st.markdown("---")

# Business Analytics Intern - Neovantas
st.markdown(
    """
    **Business Analytics Intern**  
    *Neovantas — Madrid*  
    *Jun 2022 – Aug 2022*  

    - 🧮 Collected, cleaned, and analyzed large datasets to extract actionable insights.  
    - 📈 Built forecasting models to predict customer satisfaction and business outcomes.  
    - 📊 Created interactive dashboards with Python and Power BI to visualize insights.  
    - 📉 Applied statistical analysis for trend identification and data-driven recommendations.  

    **Soft Skills Developed:** Attention to detail, analytical reasoning, data storytelling, time management, collaborative mindset.
    """
)

st.markdown("---")

# -------- EDUCATION & CERTIFICATIONS --------
st.markdown("## 🎓 Education & Certifications")

st.markdown(
    """
    - **Databricks Certified Associate: Machine Learning** (In Progress)  
      Specialization in ML workflows, model training, MLflow, and Delta Lake
    
    - **Master's in Sports Big Data** (In Progress)  
      Universidad Europea — Madrid  

    - **Bachelor's in Mathematics & Engineering Science**  
      Millikin University, USA
    """
)

st.markdown("---")

# -------- TECHNICAL COMPETENCIES --------
st.markdown("## 🔧 Technical Competencies")

st.markdown(
    """
    **Cloud Platforms & AI Services:**
    - **Azure:** Azure OpenAI, Azure AI Document Intelligence, Azure Cognitive Search, Azure Data Studio, Logic Apps, Azure AI Services
    - **AWS:** EC2, Lambda, App Runner, S3, DynamoDB, OpenSearch, Kinesis, Athena, VPC, IAM
    - **Databricks:** ML Platform, MLflow (experiment tracking), Delta Lake (data governance), notebooks, job orchestration
    - Serverless architectures and event-driven design
    
    **Generative AI & LLMs:**
    - OpenAI (GPT-4, ChatGPT), Anthropic (Claude), Hugging Face, LangChain
    - Prompt Engineering and Fine-tuning
    - RAG (Retrieval-Augmented Generation), Embeddings, Vector Databases (FAISS)
    - Semantic Search and NLP
    
    **Data Platforms & Big Data:**
    - Databricks: ML workflows, model management, distributed computing
    - Big Data: Hadoop, Spark, Apache Kafka
    - Data Lakes and Data Warehouses
    - Databases: SQL (PostgreSQL, MySQL), NoSQL (DynamoDB, Elasticsearch, Couchbase)
    - ETL/ELT Pipelines and Data Orchestration
    
    **Machine Learning & Analytics:**
    - Scikit-learn: Classification, Regression, Clustering
    - Deep Learning: TensorFlow, Keras, PyTorch
    - MLflow: Experiment tracking, model registry, deployment
    - Predictive Analytics and Statistical Modeling
    - Feature Engineering and Model Evaluation
    
    **Programming & Tools:**
    - Python (Pandas, NumPy, Scikit-learn, Streamlit, FastAPI, Flask, PySpark)
    - R (Statistical Analysis, Shiny, ggplot2)
    - SQL (Complex queries, optimization, window functions)
    - Jupyter Notebooks, Git, Docker, CI/CD
    - Power BI, Tableau, Excel (Advanced)
    
    **Banking & Finance Domain:**
    - Retail, Enterprise, and CIB architecture
    - Regulatory compliance (AML, GDPR, regulatory frameworks)
    - Financial processes and business model understanding
    - Risk management and compliance patterns
    """
)

st.markdown("---")

# -------- LANGUAGES & SOFT SKILLS --------
st.markdown("## 🗣️ Languages & Professional Attributes")

st.markdown(
    """
    **Languages:**
    - Spanish (Native)
    - English (Fluent - B2/C1)

    **Key Professional Attributes:**  
    - 🎯 Strategic Thinking — Aligns technology initiatives with business objectives
    - 🤝 Collaborative Leadership — Bridges technical and business stakeholders
    - 💡 Innovation Mindset — Drives adoption of emerging technologies (AI, ML, Cloud)
    - 📊 Analytical Rigor — Data-driven decision making and evidence-based approaches
    - 🔄 Adaptability — Thrives in evolving, multi-geographic environments
    - 🗣️ Clear Communication — Effective across technical and executive audiences
    - 📚 Continuous Learning — Committed to staying current (Databricks certification, AI evolution)
    - 🏗️ Architectural Thinking — Views problems through scalability and long-term sustainability lenses
    """
)

st.markdown("---")

st.markdown(
    """
    **Philosophy:** I believe in translating complex business challenges into elegant, scalable technical solutions.
    Technology should drive measurable business value while maintaining architectural coherence, regulatory compliance, and organizational learning.
    I'm committed to leveraging emerging technologies (Generative AI, Machine Learning, Cloud Platforms) responsibly and strategically.
    """
)
