import streamlit as st
import time
from datetime import datetime
import pytz

# Configurar a página antes de qualquer outra função Streamlit
st.set_page_config(layout="wide")

# Adicione o código CSS para ocultar o cabeçalho
st.markdown("""
    <style>
    .st-emotion-cache-1avcm0n {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)


# Adicione o código CSS para ocultar o side bar
st.markdown("""
    <style>
    .st-emotion-cache-1cypcdb {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)


# Definir a cor de fundo da página
cor_fundo = "#dcdcdc"  # Você pode substituir pela cor desejada

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {cor_fundo};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Definir cores
cor_verde = "#20b3a3"
cor_cinza_claro = "#d3d3d3"

# Layout inferior
st.write(
    "<div style='display:flex;justify-content:space-between;'>"
    "<div style='background-color: " + cor_verde + "; width:150%; padding:0px; border-radius:0px; margin-right: 5px;'>"
    "<h1 style='color:white;text-align:center;font-family: Microsoft Yi Baiti;'>ATENDIMENTO</h1></div>"
    "<div style='background-color: " + cor_verde + "; width:50%; padding:0px; border-radius:0px; margin-left: 1px;'>"
    "<h1 style='color:white;text-align:center;font-family: Microsoft Yi Baiti;'>PRÓXIMOS</h1></div>"
    "</div>",
    unsafe_allow_html=True,
)

# Adicionar espaço entre as seções
st.write("")

# Conteúdo principal
st.write(
    "<div style='padding-bottom: 10px; display: flex; justify-content: space-between;'>"
    "<div style='background-color: " + cor_cinza_claro + "; width:150%; height:450px; padding:5px; border-radius:0px; margin-right: 5px; line-height: 1;'>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>Fulando de tal</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>Senha: C0246</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>Cód. 6548</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>Consulta</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>Sala-01</h1>"
    "</div>"
    "<div style='background-color: " + cor_cinza_claro + "; width:50%; height:450px; padding:5px; border-radius:0px; line-height: 1;'>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>C0245</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>C0845</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>C2545</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>C0285</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;color: black;'>C0237</h1>"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

# Criar uma área estática para a data e hora
data_hora_placeholder = st.empty()

# Função para obter a data e hora atual no fuso horário de Brasília
def obter_data_hora_brasilia():
    # Definir o fuso horário de Brasília
    fuso_brasilia = pytz.timezone('America/Sao_Paulo')
    # Obter a hora atual
    data_hora_atual = datetime.now()
    # Converter para o fuso horário de Brasília
    data_hora_brasilia = data_hora_atual.astimezone(fuso_brasilia)
    # Formatar a data e hora como string
    data_hora_formatada = data_hora_brasilia.strftime("%d/%m/%Y - %H:%M:%S")
    return data_hora_formatada

# Mostrar a hora em tempo real
while True:
    data_hora_atual_brasilia = obter_data_hora_brasilia()
    
    # Atualizar o conteúdo da área estática com a nova hora
    data_hora_placeholder.write(
        f"""
        <div style="background-color: {cor_verde}; padding: 0px; border-radius: 0px; margin-bottom: -10px;">
            <h1 style="color: white; text-align: center; margin: 0;font-family: Microsoft Yi Baiti;">{data_hora_atual_brasilia}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Aguardar um segundo antes de atualizar novamente
    time.sleep(1)
