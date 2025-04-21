import streamlit as st 
from reportlab.pdfgen import canvas
from io import BytesIO


def gerar_pdf(texto):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    c.drawString(100, 750, texto)
    c.save()
    buffer.seek(0)
    return buffer

st.title("Gerador de PDF 📄📁")

texto = st.text_input("Digite o texto para o PDF:")

if st.button("Gerar PDF"):
    if texto:
        pdf_buffer = gerar_pdf(texto)
        st.download_button(
            label="Clique para baixar o PDF",
            data=pdf_buffer,
            file_name="meu_arquivo.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Por favor, insira um texto antes de gerar o PDF.")

