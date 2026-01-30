import streamlit as st

def apply_global_style():
    st.markdown(
        """
        <style>
        .stApp { background-color: #0E2A47; color: white; }

        header[data-testid="stHeader"] {
            background-color: #0E2A47;
            border-bottom: 1px solid #1E4F8A;
        }

        section[data-testid="stSidebar"] {
            background-color: #143A63;
            border-right: 1px solid #1E4F8A;
        }

        section[data-testid="stSidebar"] * {
            color: white;
        }

        a { color: #4DA3FF; font-weight: 600; text-decoration: none; }
        a:hover { text-decoration: underline; }

        hr { border: 1px solid #1E4F8A; }
        </style>
        """,
        unsafe_allow_html=True
    )
