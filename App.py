import streamlit as st
import requests
import base64

# Configuración de la página
st.set_page_config(
    page_title="Visor de CV",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Visor de CV desde GitHub Pages")

# URL del PDF en GitHub Pages
pdf_url = "https://nestum447.github.io/Perfil_Proyectos/CV_2025081711042143.pdf"

# Descargar PDF desde GitHub Pages
response = requests.get(pdf_url)

if response.status_code == 200:
    # Convertir a base64
    pdf_base64 = base64.b64encode(response.content).decode("utf-8")

    # Mostrar PDF en la app con scroll
    pdf_display = f"""
    <iframe src="data:application/pdf;base64,{pdf_base64}" 
            width="80%" height="800px" 
            style="border:none;" type="application/pdf"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Botón de descarga
    st.download_button(
        label="📥 Descargar CV",
        data=response.content,
        file_name="CV.pdf",
        mime="application/pdf"
    )
else:
    st.error("⚠️ No se pudo cargar el PDF desde GitHub Pages.")
