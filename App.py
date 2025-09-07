
---

## 🛠️ Código principal (`app.py`)

```python
import streamlit as st

st.set_page_config(page_title="Visor de Documentos", layout="wide")
st.title("📁 Visor Profesional de Documentos desde GitHub")

# Diccionario con documentos y tipo
documentos = {
    "Presentación PPTX": {
        "url": "https://github.com/nestum447/Perfil_Proyectos/raw/main/docs/presentacion.pptx",
        "tipo": "pptx",
        "icono": "📊"
    },
    "Documento Word": {
        "url": "https://github.com/nestum447/Perfil_Proyectos/raw/main/docs/documento.docx",
        "tipo": "docx",
        "icono": "📄"
    },
    "Archivo PDF": {
        "url": "https://github.com/nestum447/Perfil_Proyectos/main/CV_2025081711042143.pdf ",
        "tipo": "pdf",
        "icono": "📑"
    }
}

st.subheader("Selecciona un documento para ver:")
cols = st.columns(len(documentos))

# Mostrar miniaturas con botones
doc_seleccionado = None
for i, (nombre, info) in enumerate(documentos.items()):
    with cols[i]:
        if st.button(f"{info['icono']} {nombre}"):
            doc_seleccionado = nombre

# Mostrar documento si se selecciona
if doc_seleccionado:
    doc_info = documentos[doc_seleccionado]
    url = doc_info["url"]
    tipo = doc_info["tipo"]

    st.markdown(f"### {doc_seleccionado}")

    if tipo == "pdf":
        st.markdown(f"""
        <iframe src="{url}" width="100%" height="600px" frameborder="0"></iframe>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <iframe src="https://view.officeapps.live.com/op/embed.aspx?src={url}" 
        width="100%" height="600px" frameborder="0"></iframe>
        """, unsafe_allow_html=True)
