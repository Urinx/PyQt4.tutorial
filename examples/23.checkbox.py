#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.cb=QtGui.QCheckBox('Show title',self)
		self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
		self.cb.move(10,10)
		self.cb.toggle()
		self.cb.stateChanged.connect(self.changeTitle)

		self.setWindowTitle('Checkbox')
		self.setGeometry(300,300,250,150)

	def changeTitle(self):
		if self.cb.isChecked():
			self.setWindowTitle('Checkbox')
		else:
			self.setWindowTitle('Not check')
	
if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())