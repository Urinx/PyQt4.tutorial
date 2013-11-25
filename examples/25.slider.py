#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		slider=QtGui.QSlider(QtCore.Qt.Horizontal,self)
		slider.setFocusPolicy(QtCore.Qt.NoFocus)
		slider.setGeometry(30,40,100,30)
		self.connect(slider,QtCore.SIGNAL('valueChanged(int)'),self.changeValue)

		self.label=QtGui.QLabel(self)
		self.label.setPixmap(QtGui.QPixmap('apple.png'))
		self.label.setGeometry(160,40,80,30)
		
		self.setWindowTitle('Slider')
		self.setGeometry(300,300,250,150)

	def changeValue(self,value):
		if value==0:
			self.label.setPixmap(QtGui.QPixmap('apple.png'))
		elif value>10 and value<=30:
			self.label.setPixmap(QtGui.QPixmap('apple2.jpg'))
		elif value>30 and value<80:
			self.label.setPixmap(QtGui.QPixmap('apple.png'))
		else:
			self.label.setPixmap(QtGui.QPixmap('apple2.jpg'))
	
if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())