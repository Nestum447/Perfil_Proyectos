import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Visor de CV",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Visor de CV desde GitHub")

# URL RAW del PDF en tu repositorio
pdf_url = "https://github.com/nestum447/Perfil_Proyectos/main/CV_2025081711042143.pdf"

st.markdown(
    f"""
    <div style="text-align: center;">
        <iframe src="{pdf_url}" width="80%" height="800px" frameborder="0"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("Visualización directa desde GitHub. Puede usar scroll para navegar el documento.")
