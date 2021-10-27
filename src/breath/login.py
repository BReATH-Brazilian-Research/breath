import sys
from PyQt6.QtWidgets import (QLineEdit, QPushButton, QVBoxLayout, QDialog)

class Login(QDialog):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		# Create widgets
		self.login = QLineEdit("Login")
		self.password = QLineEdit("Password")
		self.lgn_btn = QPushButton("Login")
		self.reg_btn = QPushButton("Register")
		# Create layout and add widgets
		layout = QVBoxLayout()
		layout.addWidget(self.login)
		layout.addWidget(self.password)
		layout.addWidget(self.lgn_btn)
		layout.addWidget(self.reg_btn)
		# Set dialog layout
		self.setLayout(layout)
		# Add button signal to greetings slot
		self.lgn_btn.clicked.connect(self.greetings)

	# Greets the user
	def greetings(self):
		print(f"Hello {self.login.text()}")


class Register(QDialog):
	def __init__(self, parent=None):
		super(Register, self).__init__(parent)
		# Create widgets
		self.account = QLineEdit("Account")
		self.password = QLineEdit("Password")
		self.confirm = QLineEdit("Repeat Password")
		self.reg_btn = QPushButton("Register")
		# Create layout and add widgets
		layout = QVBoxLayout()
		layout.addWidget(self.account)
		layout.addWidget(self.password)
		layout.addWidget(self.confirm)
		layout.addWidget(self.reg_btn)
		# Set dialog layout
		self.setLayout(layout)
		# Add button signal to greetings slot
		self.reg_btn.clicked.connect(self.greetings)

	# Greets the user
	def greetings(self):
		print(f"Hello {self.account.text()}")