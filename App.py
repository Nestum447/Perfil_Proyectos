import streamlit as st
import requests
from io import BytesIO
from PIL import Image
from PyPDF2 import PdfReader

st.set_page_config(page_title="Visor de CV", page_icon="📄", layout="wide")

st.title("📄 Visor de CV desde GitHub Pages")

pdf_url = "https://nestum447.github.io/Perfil_Proyectos/CV_2025081711042143.pdf"
response = requests.get(pdf_url)

if response.status_code == 200:
    pdf_bytes = BytesIO(response.content)
    reader = PdfReader(pdf_bytes)

    st.write("📄 Visualización del CV:")

    # Extraer cada página y convertirla a imagen usando Pillow
    for i, page in enumerate(reader.pages):
        # Convertimos cada página a PDF individual y luego a imagen
        pdf_page_bytes = BytesIO()
        writer = PdfReader()
        writer.add_page(page)
        # Guardamos temporalmente la página como PDF
        with open("temp_page.pdf", "wb") as f:
            writer.write(f)
        # Abrimos con PIL
        img = Image.open("temp_page.pdf")
        st.image(img, caption=f"Página {i+1}", use_column_width=True)

    # Botón de descarga
    st.download_button(
        label="📥 Descargar CV",
        data=response.content,
        file_name="CV.pdf",
        mime="application/pdf"
    )

    # Enlace de respaldo
    st.markdown(f"[🔗 Abrir CV en otra pestaña]({pdf_url})")

else:
    st.error("⚠️ No se pudo cargar el PDF desde GitHub Pages.")
