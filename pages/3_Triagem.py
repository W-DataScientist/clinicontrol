import streamlit as st
import sqlite3
from datetime import datetime
import socket
#import pyautogui
import time

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

# Função para obter o IP da máquina local
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

# Função para criar a conexão com o banco de dados
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Função para conectar-se ao banco de dados e verificar se o IP local existe na tabela usuario
def check_local_ip_in_db():
    local_ip = get_local_ip()
    conn = sqlite3.connect('clinidb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ip FROM usuario WHERE ip = ?", (local_ip,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Função para conectar-se ao banco de dados e verificar se a matrícula existe na tabela colaborador
def check_matricula_in_db(matricula):
    conn = create_connection('clinidb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT matricula FROM colaborador WHERE matricula = ?", (matricula,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

# Função para inserir um novo atendimento no banco de dados
def insert_atendimento(conn, atendimento):
    sql = ''' INSERT INTO atendimento(matricula, date, hora, preferencial, pressao, peso, altura, temperatura, especialidade, atestado, exame, encaminhamento, observacoes, sala, atendente, tipo, queixa, status)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, atendimento)
    conn.commit()
    return cur.lastrowid

# Interface do Streamlit
def main():
    st.title("Triagem de atendimento")

    # Conectar ao banco de dados
    conn = create_connection("clinidb.db")

    if conn:
        # Obter data e hora atuais
        now = datetime.now()
        date = now.strftime("%d/%m/%y")
        hora = now.strftime("%H:%M:%S")

        # Obter informações do usuário
        atendente = st.text_input("Atendente")
        
        # Adicionar a escolha de matrícula: "Paciente Externo", "Sem Matrícula" e "Matrícula"
        opcoes_matricula = ["Paciente Externo", "Sem Matrícula", "Matrícula"]
        matricula_opcao = st.selectbox("Matrícula", opcoes_matricula)

        if matricula_opcao == "Sem Matrícula":
            matricula = "Sem Matrícula"
        elif matricula_opcao == "Paciente Externo":
            matricula = "Paciente Externo"
        else:
            matricula = st.text_input("Número de Matrícula")

        # Obter informações do atendimento
        queixa = st.text_area("Queixa")

        # Layout para os campos Peso, Altura, Temperatura e Pressão
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            peso = st.slider("Peso (kg)", min_value=30, max_value=170, step=1)
        with col2:
            altura = st.slider("Altura (cm)", min_value=50, max_value=200, step=1)
        with col3:
            temperatura = st.slider("Temperatura (°C)", min_value=36, max_value=42, step=1)
        with col4:
            pressao = st.text_input("Pressão")

        # Layout para os campos Tipo, Preferencial, Especialidade e Sala
        col5, col6, col7, col8 = st.columns(4)
        with col5:
            tipo = st.radio("Tipo de atendimento", ['Normal', 'Urgente', 'Emergência'])
        with col6:
            preferencial = st.radio("Preferencial", ['Sim', 'Não'])
        with col7:
            especialidade = st.radio("Especialidade", ["Médico", "Audiometria", "Fisioterapia", "Vacina"])
        with col8:
            sala = st.radio("Sala", ["01", "02"])

        # Layout para os campos Atestado, Exame e Encaminhamento
        col9, col10, col11 = st.columns(3)
        with col9:
            atestado = st.checkbox("Atestado")
        with col10:
            exame = st.checkbox("Exame")
        with col11:
            encaminhamento = st.checkbox("Encaminhamento")

        # Continuar com os campos restantes
        observacoes = st.text_area("Observações")

        # Verificar se todos os campos obrigatórios foram preenchidos
        if atendente and matricula and queixa and pressao and peso and altura and temperatura:
            # Verificar se o usuário quer inserir o atendimento
            if st.button("Inserir Atendimento"):
                status = "aguardando"
                atendimento = (matricula, date, hora, preferencial, pressao, peso, altura, temperatura, especialidade, atestado, exame, encaminhamento, observacoes, sala, atendente, tipo, queixa, status)
                insert_atendimento(conn, atendimento)
                st.success("Triagem inserida!")
                time.sleep(3)
                pyautogui.press('f5')          
        else:
            st.warning("Por favor, preencha todos os campos obrigatórios.")

    else:
        st.error("Erro ao conectar ao banco de dados")

if __name__ == "__main__":
    main()
