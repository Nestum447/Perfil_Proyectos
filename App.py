import streamlit as st
import fitz  # PyMuPDF
import requests
import io

st.set_page_config(page_title="Visor de CV", layout="wide")

st.title("📄 Visor de CV desde GitHub Pages")

pdf_url = "https://nestum447.github.io/Perfil_Proyectos/CV_2025081711042143.pdf"

# Descargar PDF
response = requests.get(pdf_url)
if response.status_code == 200:
    pdf_data = response.content

    # Abrir PDF con PyMuPDF
    doc = fitz.open(stream=pdf_data, filetype="pdf")

    # Mostrar cada página como imagen
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap()
        img = io.BytesIO(pix.tobytes("png"))
        st.image(img, caption=f"Página {page_num+1}")
else:
    st.error("⚠️ No se pudo cargar el PDF.")
