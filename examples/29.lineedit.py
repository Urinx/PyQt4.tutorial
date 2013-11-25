#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.label=QtGui.QLabel(self)
		self.move(60,40)
		edit=QtGui.QLineEdit(self)
		edit.move(60,100)

		self.connect(edit,QtCore.SIGNAL('textChanged(QString)'),self.onChanged)
		
		self.setWindowTitle('QLineEdit')
		self.setGeometry(250,200,350,250)

	def onChanged(self,text):
		self.label.setText(text)
		self.label.adjustSize()

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())