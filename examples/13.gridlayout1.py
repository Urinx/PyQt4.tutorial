#! /usr/bin/python
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle('grid layout')
	 	self.resize(300,150)
	 	names=['Cls','Bck','','Close','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
	 	grid=QtGui.QGridLayout()
	 	j=0
	 	pos=[
	 	(0,0),(0,1),(0,2),(0,3),
	 	(1,0),(1,1),(1,2),(1,3),
	 	(2,0),(2,1),(2,2),(2,3),
	 	(3,0),(3,1),(3,2),(3,3),
	 	(4,0),(4,1),(4,2),(4,3),
	 	]
	 	for i in names:
	 		button=QtGui.QPushButton(i)
	 		if j==2:
	 			#addWidget(widget,row,column)
	 			grid.addWidget(QtGui.QLabel(''),0,2)
	 		else:
	 			grid.addWidget(button,pos[j][0],pos[j][1])
	 		j=j+1
	 	self.setLayout(grid)

app=QtGui.QApplication(sys.argv)
ex=Example()
ex.show()
sys.exit(app.exec_())