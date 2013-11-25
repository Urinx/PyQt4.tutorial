#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.label=QtGui.QLabel('Ubuntu',self)
		self.label.move(50,150)

		combo=QtGui.QComboBox(self)
		combo.addItem('Ubuntu')
		combo.addItem('Mandriva')
		combo.addItem('Fedora')
		combo.addItem('Red Hat')
		combo.addItem('Gentoo')
		combo.move(50,50)
		self.connect(combo,QtCore.SIGNAL('activated(QString)'),self.onActivated)

		self.setWindowTitle('QComboBox')
		self.setGeometry(250,200,350,250)

	def onActivated(self,text):
		self.label.setText(text)
		self.label.adjustSize()

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())