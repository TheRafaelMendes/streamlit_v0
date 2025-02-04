import streamlit as st

# Credenciais fixas (só você conhece)
USERNAME = "meu_login"
PASSWORD = "minha_senha"

# Verifica se a variável de autenticação já existe; se não, define como False.
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Se o usuário ainda não fez login, mostra o formulário de login.
if not st.session_state.authenticated:
    st.title("Login do Aplicativo")
    
    # Cria os campos de entrada para login e senha
    user_input = st.text_input("Login")
    pass_input = st.text_input("Senha", type="password")
    
    # Botão de login
    if st.button("Entrar"):
        # Verifica se as credenciais estão corretas
        if user_input == USERNAME and pass_input == PASSWORD:
            st.session_state.authenticated = True
            st.success("Login efetuado com sucesso!")
        else:
            st.error("Login ou senha incorretos.")
    
    # Interrompe a execução do resto do código se não estiver autenticado.
    st.stop()

# Se o usuário passou no login, o restante do código é executado.
st.title("Cortador de Link")

# Campo para o usuário inserir um link
link = st.text_input("Digite um link:")

# Se o usuário digitou algo, o código corta as 5 últimas letras do link
if link:
    link_modificado = link[:-5]  # Fatiamento: pega tudo do início até 5 posições antes do final
    st.write("Link modificado:", link_modificado)

# Botões adicionais para demonstrar interatividade
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
    
