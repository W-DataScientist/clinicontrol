import streamlit as st

# Adicione o código CSS para ocultar o cabeçalho
hide_header_style = """
<style>
    header.st-emotion-cache-18ni7ap {
        display: none;
    }
</style>
"""
# Use o componente st.markdown para inserir o estilo embutido na página
st.markdown(hide_header_style, unsafe_allow_html=True)

st.title("Em construção")