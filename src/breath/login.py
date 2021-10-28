import sys
from PyQt6.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QDialog)
import pandas as pd
import hashlib
from user.db import *

class Login(QDialog):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		# Create widgets
		self.login_text = QLineEdit("Login")
		self.password = QLineEdit("Password")
		self.lgn_btn = QPushButton("Login")
		self.reg_btn = QPushButton("Register")
		self.return_btn = QPushButton("Return")
		# Create layout and add widgets
		layout = QVBoxLayout()
		layout.addWidget(self.login_text)
		layout.addWidget(self.password)
		layout.addWidget(self.lgn_btn)
		layout.addWidget(self.reg_btn)
		layout.addWidget(self.return_btn)
		# Set dialog layout
		self.setLayout(layout)
		# Add button signal to login slot
		self.lgn_btn.clicked.connect(self.login)

	# Greets the user
	def login(self):
		hashed_pswd = make_hashes(self.password.text())
		result = self.bd.login_user(self.login_text.text(), check_hashes(self.password.text(),hashed_pswd))
		if result:
			print('vc esta logado')
		else:
			print('nao encontramos esta credencial')


class Register(QDialog):
	def __init__(self, parent=None):
		super(Register, self).__init__(parent)

		# Create widgets
		self.account = QLineEdit("Account")
		self.password = QLineEdit("Password")
		self.confirm = QLineEdit("Repeat Password")
		self.reg_btn = QPushButton("Register")
		self.return_btn = QPushButton("Return")
		# Create layout and add widgets
		layout = QVBoxLayout()
		layout.addWidget(self.account)
		layout.addWidget(self.password)
		layout.addWidget(self.confirm)
		layout.addWidget(self.reg_btn)
		layout.addWidget(self.return_btn)
		# Set dialog layout
		self.setLayout(layout)
		# Add button signal to register slot
		self.reg_btn.clicked.connect(self.register)

	# Greets the user
	def register(self):
		self.bd.add_userdata(self.account.text(),make_hashes(self.password.text()))
		print(self.bd.view_all_users())
		print("Você está logado")