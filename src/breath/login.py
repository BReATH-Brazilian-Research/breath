import streamlit as st
import time, datetime
import numpy as np
import hashlib as hl

# from user import oauth
# from user import registrar

class LogIn:
    def __init__(self) -> None:
        # Título da página
        st.title("Entre no nosso site!")
        st.text("Faça seu login ou realize seu cadastro.")
        
        # Caixas de Input
        st.text_input("Email", key="email_typed")
        st.text_input("Senha", type="password", key="senha_typed")
        print(st.session_state.email, st.session_state.senha)

        # Botões
        left_column, center_column, right_column = st.columns(3)
        left_column.button("Entrar com Google", key="button_google_login")
        center_column.button("Entrar", key="button_login")
        right_column.button("Cadastrar", key="button_cadastro")

        # Interação com botão de Login
        if st.session_state.button_login == True:
            st.session_state.email = st.session_state.email_typed
            st.session_state.senha = self.crypto(st.session_state.senha_typed)
            
            if self.__VerificaHash(self, self.__VerificaEmail) == True:
                # Entra no app -> Proxima pagina
                pass
            else:
                print("Email ou Senha incorretos")

            st.session_state.google_login = False
            st.session_state.button_cadastro = False

        #Interação com o botão de Cadastro
        if st.session_state.button_cadastro == True:
            # registrar.Registrar()
            # Invoca o código do Lucas
            # Vai pra pagina dele
            pass

        # Interação com o botão de Login com o Google
        if st.session_state.google_login == True:
          
            # oauth.google_oauth_login()
          
            st.session_state.button_login = False
            st.session_state.button_cadastro = False
          


    def crypto(self, password):
        return hl.sha512(str.encode(password)).hexdigest()


    def __VerificaEmail(self):
        
        return False

    def __VerificaHash(self, email_flag):
        if email_flag == True:
            pass

        return False
        

if __name__ == "__main__":
    LogIn()