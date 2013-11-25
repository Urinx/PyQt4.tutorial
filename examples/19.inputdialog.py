#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		button=QtGui.QPushButton('Dialog',self)
		button.setFocusPolicy(QtCore.Qt.NoFocus)
		button.move(20,20)
		self.connect(button,QtCore.SIGNAL('clicked()'),self.showDialog)
		self.setFocus()

		self.label=QtGui.QLineEdit(self)
		self.label.move(130,22)

		self.setWindowTitle('InputDialog')
		self.setGeometry(300,300,350,80)

	def showDialog(self):
		text,ok=QtGui.QInputDialog.getText(self,'Input Dialog','enter your name:')
		if ok:
			self.label.setText(str(text))
	
if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())