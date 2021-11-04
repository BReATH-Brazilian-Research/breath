import sys
from PyQt6.QtWidgets import (QLabel, QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QDialog, QWidget)
from PyQt6.QtGui import QFont

class HomeWindow(object):
	def __init__(self, bd, parent=None):
		super(HomeWindow, self).__init__(parent)
		# header
		self.setWindowTitle('BReATH')
		
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(541, 566)
		self.verticalLayoutWidget = QtWidgets.QWidget(Form)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 391, 441))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
		font = QtGui.QFont()
		font.setPointSize(20)
		self.title.setFont(font)
		self.title.setObjectName("title")
		self.verticalLayout.addWidget(self.title)
		self.lgn_text = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.lgn_text.setObjectName("lgn_text")
		self.verticalLayout.addWidget(self.lgn_text)
		self.lgn_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.lgn_btn.setObjectName("lgn_btn")
		self.verticalLayout.addWidget(self.lgn_btn)
		self.reg_text = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.reg_text.setObjectName("reg_text")
		self.verticalLayout.addWidget(self.reg_text)
		self.reg_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
		self.reg_btn.setObjectName("reg_btn")
		self.verticalLayout.addWidget(self.reg_btn)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.title.setText(_translate("Form", "  Bem vindo ao Sistema Breath"))
		self.lgn_text.setText(_translate("Form", "    Por favor faça seu login para que possamos continuar"))
		self.lgn_btn.setText(_translate("Form", "Login"))
		self.reg_text.setText(_translate("Form", "       Ou faça seu registro caso seja seu primeiro acesso"))
		self.reg_btn.setText(_translate("Form", "Registro"))


class UIToolTab(QWidget):
	def __init__(self, parent=None):
		super(UIToolTab, self).__init__(parent)
		self.CPSBTN = QPushButton("text2", self)
		self.CPSBTN.move(100, 350)
