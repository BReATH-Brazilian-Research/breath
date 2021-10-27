import sys
from ui import HomeWindow, UIToolTab
from login import Login, Register
from PyQt6.QtWidgets import (QLineEdit, QPushButton, QApplication, QMainWindow, QVBoxLayout, QDialog, QWidget)
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setGeometry(0, 0, 1000, 1000)

		self.startHomeWindow()

	def startUIToolTab(self):
		self.ToolTab = UIToolTab(self)
		self.setWindowTitle("UIToolTab")
		self.setCentralWidget(self.ToolTab)
		self.ToolTab.CPSBTN.clicked.connect(self.startHomeWindow)
		self.show()

	def startHomeWindow(self):
		self.Window = HomeWindow(self)
		self.setCentralWidget(self.Window)
		self.Window.reg_btn.clicked.connect(self.startLogin)
		self.show()
	
	def startLogin(self):
		self.Window = Login(self)
		self.setWindowTitle("Login")
		self.setCentralWidget(self.Window)
		self.Window.lgn_btn.clicked.connect(self.startUIToolTab)
		self.Window.reg_btn.clicked.connect(self.startRegister)
		self.show()

	def startRegister(self):
		self.Window = Register(self)
		self.setWindowTitle("Register")
		self.setCentralWidget(self.Window)
		self.Window.reg_btn.clicked.connect(self.startUIToolTab)
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainWindow()
	sys.exit(app.exec())