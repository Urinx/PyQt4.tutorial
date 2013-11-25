#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore
class Button(QtGui.QPushButton):
	def __init__(self,title,parent):
		super(Button, self).__init__(title,parent)
	
	def mouseMoveEvent(self,e):
		if e.buttons()!=QtCore.Qt.RightButton:
			return
		mimeData=QtCore.QMimeData()
		drag=QtGui.QDrag(self)
		drag.setMimeData(mimeData)
		drag.setHotSpot(e.pos()-self.rect().topLeft())
		dropAction=drag.start(QtCore.Qt.MoveAction)	
	
	def mousePressEvent(self,e):
		QtGui.QPushButton.mousePressEvent(self,e)
		if e.button()==QtCore.Qt.LeftButton:
			print 'press'

class Example(QtGui.QWidget):
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Click or Move')
		self.setGeometry(300,300,280,150)
		self.setAcceptDrops(True)

		self.button=Button('Button',self)
		self.button.move(100,65)

	def dragEnterEvent(self,e):
		e.accept()

	def dropEvent(self,e):
		position=e.pos()
		self.button.move(position)
		e.setDropAction(QtCore.Qt.MoveAction)
		e.accept()

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	ex=Example()
	ex.show()
	sys.exit(app.exec_())