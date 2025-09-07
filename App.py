import streamlit as st

st.set_page_config(page_title="Visor de CV", layout="wide")
st.title("📄 Visor de CV desde GitHub")

# URL RAW del PDF en tu repositorio
pdf_url = "https://github.com/nestum447/Perfil_Proyectos/raw/main/CV_2025081711042143.pdf"

# Mostrar PDF en iframe
st.markdown(f"""
<iframe src="{pdf_url}" width="100%" height="800px" frameborder="0"></iframe>
""", unsafe_allow_html=True)
