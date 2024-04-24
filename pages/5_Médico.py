import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

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

# Função para formatar a data para dd/mm/aaaa
def formatar_data(data):
    partes = data.split(' ')[0].split('-')
    dia = partes[2]
    mes = partes[1]
    ano = partes[0]
    return '{}/{}/{}'.format(dia, mes, ano)

# Função para calcular a idade atual com base na data de nascimento
def calcular_idade(nascimento):
    hoje = datetime.today()
    nascimento = datetime.strptime(nascimento, "%Y-%m-%d %H:%M:%S")
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

# Função para remover a vírgula da matrícula, se aplicável
def remover_virgula(matricula):
    if isinstance(matricula, str):
        return matricula.replace(',', '')
    elif isinstance(matricula, (int, float)):
        return str(matricula).replace(',', '')
    else:
        return matricula

# Conexão com o banco de dados
conn = sqlite3.connect('clinidb.db')
c = conn.cursor()

# Consulta ao banco de dados para obter os dados da tabela "atendimento" e "colaborador"
c.execute("SELECT at.matricula, col.nome, col.nascimento, at.peso, at.pressao, at.temperatura, col.funcao, col.altura, at.queixa FROM atendimento AS at INNER JOIN colaborador AS col ON at.matricula = col.matricula WHERE at.status = 'aguardando'")
data = c.fetchall()
df = pd.DataFrame(data, columns=['Matrícula', 'Nome', 'Nascimento', 'Peso', 'Pressão', 'Temperatura', 'Função', 'Queixa', 'Altura'])

# Formatando a coluna "Matrícula" para remover a vírgula
df['Matrícula'] = df['Matrícula'].apply(remover_virgula)

# Calculando a idade atual e adicionando a coluna "Idade"
df['Idade'] = df['Nascimento'].apply(calcular_idade)

# Interface do Streamlit
st.title('Sequencia de atendimentos')

# Mostrar os dados na interface
st.write(df)

# Fechar a conexão com o banco de dados
conn.close()
