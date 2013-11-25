#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle('box layout')
	 	self.resize(300,150)
		
		okButton=QtGui.QPushButton('OK')
		cancelBuntton=QtGui.QPushButton('Cancel')
		okButton.connect(okButton,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))
		cancelBuntton.connect(cancelBuntton,QtCore.SIGNAL('clicked()'),QtGui.qApp,QtCore.SLOT('quit()'))

		hbox=QtGui.QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(okButton)
		hbox.addWidget(cancelBuntton)

		vbox=QtGui.QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)

		self.setLayout(vbox)

app=QtGui.QApplication(sys.argv)
ex=Example()
ex.show()
sys.exit(app.exec_())