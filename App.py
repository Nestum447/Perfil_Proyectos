import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Visor de CV",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Visor de CV desde GitHub Pages")

# URL del PDF en GitHub Pages
pdf_url = "https://nestum447.github.io/Perfil_Proyectos/CV_2025081711042143.pdf"

# Mostrar PDF en iframe
st.markdown(
    f"""
    <div style="text-align: center;">
        <iframe src="{pdf_url}" width="80%" height="800px" frameborder="0"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("Visualización directa desde GitHub Pages. Usa scroll para navegar el documento.")
