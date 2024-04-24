import streamlit as st
import sqlite3
import socket

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

# Função para conectar-se ao banco de dados
def conectar_bd():
    conn = sqlite3.connect('clinidb.db')
    cursor = conn.cursor()
    return conn, cursor

# Função para verificar o login e retornar os dados do usuário
def verificar_login(usuario, senha):
    conn, cursor = conectar_bd()
    cursor.execute("SELECT * FROM usuario WHERE login = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

# Função para verificar se o usuário e senha existem
def verificar_usuario_e_senha(usuario, senha):
    conn, cursor = conectar_bd()
    cursor.execute("SELECT * FROM usuario WHERE login = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None

# Função para atualizar o IP do usuário
def atualizar_ip_usuario(usuario, ip):
    conn, cursor = conectar_bd()
    cursor.execute("UPDATE usuario SET ip = ? WHERE login = ?", (ip, usuario))
    conn.commit()
    conn.close()

def main():
    st.title("Tela de Login")
    st.markdown("---")

    # Campos de entrada
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    # Botão de Entrar
    if st.button("Entrar"):
        if usuario and senha:
            resultado = verificar_login(usuario, senha)
            if resultado:
                st.success("Login bem sucedido!")
                # Atualizar o IP do usuário
                ip_local = socket.gethostbyname(socket.gethostname())  # Obtém o IP local
                atualizar_ip_usuario(usuario, ip_local)
                # Redirecionar para a próxima página após o login
            else:
                st.error("Usuário ou senha incorretos.")
        else:
            st.warning("Por favor, digite usuário e senha.")

    # Botão de Recuperar Senha
    if st.button("Recuperar Senha"):
        email = st.text_input("Digite seu e-mail")
        if email:
            st.success(f"Um e-mail de recuperação foi enviado para {email}")
        else:
            st.warning("Por favor, digite seu e-mail.")

    # Link para cadastrar usuário
    st.markdown("---")
    if st.checkbox("Solicitar usuário"):
        st.markdown("### Cadastro de Usuário")
        nome_completo = st.text_input("Nome Completo")
        data_nascimento = st.date_input("Data de Nascimento")
        sexo = st.radio("Sexo", ["Masculino", "Feminino"])
        setor = st.text_input("Setor")
        funcao = st.text_input("Função")
        formacao = st.text_input("Formação")
        email = st.text_input("E-mail")
        telefone = st.text_input("Telefone")
        if st.button("Cadastrar"):
            # Aqui você pode inserir os dados no banco de dados
            # Lembre-se de fazer as validações necessárias antes de inserir os dados
            st.success("Usuário cadastrado com sucesso!")

if __name__ == "__main__":
    main()
