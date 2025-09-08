import streamlit as st
import requests

st.set_page_config(page_title="Visor de CV", layout="wide")

st.title("📄 Visor de CV desde GitHub Pages")

pdf_url = "https://nestum447.github.io/Perfil_Proyectos/CV_2025081711042143.pdf"

# Link para abrir en otra pestaña
st.markdown(f"[🔗 Abrir CV en otra pestaña]({pdf_url})")

# Botón de descarga
response = requests.get(pdf_url)
if response.status_code == 200:
    st.download_button(
        label="📥 Descargar CV",
        data=response.content,
        file_name="CV.pdf",
        mime="application/pdf"
    )
else:
    st.error("⚠️ No se pudo cargar el PDF.")
