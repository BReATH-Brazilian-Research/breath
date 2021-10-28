import sys
from PyQt6.QtWidgets import (QLabel, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QDialog, QWidget)
from PyQt6.QtGui import QFont

class HomeWindow(QWidget):
	def __init__(self, parent=None):
		super(HomeWindow, self).__init__(parent)
		# header
		self.setWindowTitle('BReATH')

		# stylesheet
		stylesheet = (
			'background-color: green'
		)
		#self.setStyleSheet(stylesheet)
		
		# Create widgets
		self.label = QLabel("Ola vc acaba de entrar no BReATH\n Voce precisa fazer login ou se registrar para continuar")
		self.label.setFixedSize(500,100)
		self.label.setFont(QFont('Times New Roman', 15))

		self.lgn_btn = QPushButton("Login")
		self.reg_btn = QPushButton("Register")
		self.reg_btn.setFixedSize(300,20)
		self.reg_btn.move(30,100)
		
		# Create layout and add widgets
		layout = QVBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(self.lgn_btn)
		layout.addWidget(self.reg_btn)
		
		# Set dialog layout
		self.setLayout(layout)

class UIToolTab(QWidget):
	def __init__(self, parent=None):
		super(UIToolTab, self).__init__(parent)
		self.CPSBTN = QPushButton("text2", self)
		self.CPSBTN.move(100, 350)
