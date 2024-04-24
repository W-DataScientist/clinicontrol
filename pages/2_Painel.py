import streamlit as st
import time
from datetime import datetime

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
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>Fulando de tal</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>Senha: C0245</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>Cód. 6548</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>Consulta</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>Sala-01</h1>"
    "</div>"
    "<div style='background-color: " + cor_cinza_claro + "; width:50%; height:450px; padding:5px; border-radius:0px; line-height: 1;'>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>C0245</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>C0845</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>C2545</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>C0285</h1>"
    "<h1 style='text-align:center; margin: 0;font-family: Microsoft Yi Baiti;'>C0237</h1>"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

# Criar uma área estática para a data e hora
data_hora_placeholder = st.empty()
# Função para mostrar a hora em tempo real
@st.cache_data(ttl=1)  # Cache com tempo de vida curto para evitar que o conteúdo seja atualizado a cada segundo
def obter_data_hora():
    agora = datetime.now()
    return agora.strftime("%d/%m/%Y - %H:%M:%S")

# Mostrar a hora em tempo real
while True:
    data_hora_atual = obter_data_hora()
    
    # Atualizar o conteúdo da área estática com a nova hora
    data_hora_placeholder.write(
        f"""
        <div style="background-color: {cor_verde}; padding: 0px; border-radius: 0px; margin-bottom: -10px;">
            <h1 style="color: white; text-align: center; margin: 0;font-family: Microsoft Yi Baiti;">{data_hora_atual}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Aguardar um segundo antes de atualizar novamente
    time.sleep(1)
