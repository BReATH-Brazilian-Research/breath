import streamlit as st
import time, datetime
import numpy as np

# our components
from menu import Menu
from login import LogIn
from registrar import Registrar

@st.cache
def navigate(link):    
    st.session_state.actual_page = link

login_btn = st.sidebar.button(label='Login', key="btn_login", on_click=navigate('Login'))
Register_btn = st.sidebar.button(label='Registrar', key="btn_register", on_click=navigate('Registrar'))
Profile_btn = st.sidebar.button(label='Perfil do usuário', key="btn_profile", on_click=navigate('Perfil do usuário'))

if (st.session_state.btn_register == True):
    Registrar()
elif (st.session_state.btn_login == True):
    LogIn()
else:
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
    	chosen = st.radio(
    		'Sorting hat',
    		("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    	st.write(f"You are in {chosen} house!")






    st.title('Counter Example using Callbacks with kwargs')
    if 'count' not in st.session_state:
        st.session_state.count = 0

    def increment_counter(increment_value=0):
        st.session_state.count += increment_value

    def decrement_counter(decrement_value=0):
        st.session_state.count -= decrement_value

    st.button('Increment', on_click=increment_counter,
    	kwargs=dict(increment_value=5))

    st.button('Decrement', on_click=decrement_counter,
    	kwargs=dict(decrement_value=1))

    st.write('Count = ', st.session_state.count)











    st.title('Counter Example')
    if 'last_updated' not in st.session_state:
        st.session_state.last_updated = 0
    if 'count' not in st.session_state:
        st.session_state.count = 0
        st.session_state.last_updated = datetime.time(0,0)

    def update_counter():
        st.session_state.count += st.session_state.increment_value
        st.session_state.last_updated = st.session_state.update_time

    with st.form(key='my_form'):
        st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
        st.number_input('Enter a value', value=0, step=1, key='increment_value')
        submit = st.form_submit_button(label='Update', on_click=update_counter)

    st.write('Current Count = ', st.session_state.count)
    st.write('Last Updated = ', st.session_state.last_updated)