import streamlit as st
import pandas as pd
import sqlite3 
import hashlib

from breath.user.registrar import Registrar
from breath.user.oauth import google_oauth_login
from breath.user.db import *

# Security
#passlib,hashlib,bcrypt,scrypt

# DB Management


# DB  Functions




def main():
    if "logado" not in st.session_state:
        st.session_state.logado = False 
    
    conn = sqlite3.connect('data.db')
    bd = BD(conn)

    menu = ["Home", "Login", "Registrar"]
    escolha = st.sidebar.selectbox("Menu", menu)

    if escolha == "Home":
        st.subheader("Home")

    elif escolha == "Login":
        st.subheader("Login")

        if st.session_state.logado:
            st.success("Você já está logado como {}".format(st.session_state.email))
        else:
            st.sidebar.button("Login com Google", key="button_google_login")   

            username = st.sidebar.text_input("Nome de usuário")
            password = st.sidebar.text_input("Senha", type='password')

            if st.sidebar.button("Login") or st.session_state.button_google_login:
                if st.session_state.button_google_login:
                    google_oauth_login()

                    username = st.session_state.email
                    password = st.session_state.senha

                hashed_pswd = make_hashes(password)

                result = bd.login_user(username, check_hashes(password,hashed_pswd))
                if result:
                    st.success("Logado como {}".format(username))
                else:
                    st.warning("Login incorreto")

    elif escolha == "Registrar":
        Registrar()

        if st.session_state.logado:
            bd.add_userdata(st.session_state.email,make_hashes(st.session_state.senha))
            st.success("Você está logado")


if __name__ == '__main__':
	main()


