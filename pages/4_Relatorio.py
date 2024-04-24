import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('clinidb.db')

# Função para carregar os dados do banco de dados
def load_data():
    query = "SELECT * FROM atendimento"
    data = pd.read_sql_query(query, conn)
    return data

# Carregar os dados
data = load_data()

# Converter as colunas para o tipo string e remover ponto e vírgula
data['temperatura'] = data['temperatura'].astype(str).str.replace(',', '')
data['peso'] = data['peso'].astype(str).str.replace('.', '')
data['matricula'] = data['matricula'].astype(str).str.replace(',', '')
data['senha'] = data['senha'].astype(str).str.replace(',', '')

# Mostrar os dados em uma tabela
st.write("## Dados dos Atendimentos")
st.write(data)

# Estatísticas básicas
st.write("## Estatísticas Básicas")
st.write(data.describe())

# Visualização de Dados
st.write("## Visualização de Dados")

# Escolha do tipo de visualização
visualization_type = st.selectbox("Selecione o tipo de visualização", ["Contagem de Atendimentos por Especialidade", "Gráfico de Barras Horizontal", "Gráfico de Dispersão"])

# Contagem de atendimentos por especialidade
if visualization_type == "Contagem de Atendimentos por Especialidade":
    st.write("### Contagem de Atendimentos por Especialidade")
    especialidade_counts = data['especialidade'].value_counts()
    st.plotly_chart(px.pie(values=especialidade_counts, names=especialidade_counts.index, title='Contagem de Atendimentos por Especialidade'))

# Gráfico de Barras Horizontal
elif visualization_type == "Gráfico de Barras Horizontal":
    st.write("### Gráfico de Barras Horizontal")
    col1, col2 = st.columns(2)
    selected_column = col1.selectbox("Selecione a coluna para o eixo x", data.columns)
    col2.write("Selecione a coluna para o eixo y")
    selected_column_y = col2.selectbox("Selecione a coluna para o eixo y", data.columns)
    st.plotly_chart(px.bar(data, x=selected_column, y=selected_column_y, title='Gráfico de Barras Horizontal'))

# Gráfico de Dispersão
else:
    st.write("### Gráfico de Dispersão")
    col1, col2 = st.columns(2)
    selected_column_x = col1.selectbox("Selecione a coluna para o eixo x", data.columns)
    col2.write("Selecione a coluna para o eixo y")
    selected_column_y = col2.selectbox("Selecione a coluna para o eixo y", data.columns)
    st.plotly_chart(px.scatter(data, x=selected_column_x, y=selected_column_y, title='Gráfico de Dispersão'))

# Fechar a conexão com o banco de dados
conn.close()
