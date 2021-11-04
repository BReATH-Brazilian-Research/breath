import streamlit as st

class Menu:
	def __init__(self):
		login_btn = st.sidebar.button(label='Login', on_click=self.navigate('Login'))
		Register_btn = st.sidebar.button(label='Registrar', on_click=self.navigate('Registrar'))
		Profile_btn = st.sidebar.button(label='Perfil do usuário', on_click=self.navigate('Perfil do usuário'))
		placeholder_btn = st.sidebar.button(label='Botao genérico', on_click=self.navigate('Botao genérico'))


		# Add a slider to the sidebar:
		year_slider = st.sidebar.slider(
			'Selecione intervalode  tempo',
			2000, 2021, (2000, 2005)
		)

	def navigate(self,link):	
		st.session_state.actual_page = link