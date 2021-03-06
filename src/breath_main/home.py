# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt6 UI code generator 6.2.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class HomeWindow(QWidget):
	def __init__(self, parent=None):
		super(HomeWindow, self).__init__(parent)

		layout = QVBoxLayout()
		
		self.title = QLabel("Bem-Vindo a plataforma BReATH")
		font = QFont()
		font.setPointSize(20)
		self.title.setFont(font)
		self.title.setObjectName("title")
		self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.title)
		
		self.lgn_text = QLabel("Por favor faca login para continuar")
		self.lgn_text.setObjectName("lgn_text")
		font = QFont()
		font.setPointSize(16)
		self.lgn_text.setFont(font)
		self.lgn_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.lgn_text)
		
		self.lgn_btn = QPushButton("Login")
		self.lgn_btn.setObjectName("lgn_btn")

		layout.addWidget(self.lgn_btn)
		
		self.reg_text = QLabel("ou registre-se")
		self.reg_text.setObjectName("reg_text")
		font = QFont()
		font.setPointSize(16)
		self.reg_text.setFont(font)
		self.reg_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
		layout.addWidget(self.reg_text)
		
		self.reg_btn = QPushButton("Registro")
		self.reg_btn.setObjectName("reg_btn")
		layout.addWidget(self.reg_btn)

		self.setLayout(layout)


