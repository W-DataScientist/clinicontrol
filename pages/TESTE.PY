import streamlit as st
import sqlite3
import pandas as pd

# Conectar ao banco de dados
conn = sqlite3.connect('clinidb.db')
c = conn.cursor()

# Função para carregar os dados de uma tabela
def load_data(table_name):
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    return df

# Título da página
st.title('Visualizador db')

# Opções para selecionar a tabela
table_option = st.sidebar.selectbox('Selecione a tabela:', ('usuario', 'atendimento', 'colaborador'))

# Carregar e exibir os dados da tabela selecionada
st.write(f"### Tabela: {table_option}")
df = load_data(table_option)
st.write(df)

# Fechar a conexão com o banco de dados
conn.close()
