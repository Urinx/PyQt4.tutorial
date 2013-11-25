#! /usr/bin/python
import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle('grid layout')
	 	self.resize(350,300)

	 	title=QtGui.QLabel('Title')
	 	author=QtGui.QLabel('Author')
	 	review=QtGui.QLabel('Review')

	 	titleEdit=QtGui.QLineEdit()
	 	authorEdit=QtGui.QLineEdit()
	 	reviewEdit=QtGui.QTextEdit()

	 	grid=QtGui.QGridLayout()
	 	grid.setSpacing(10)
	 	grid.addWidget(title,1,0)
	 	grid.addWidget(titleEdit,1,1)
	 	grid.addWidget(author,2,0)
	 	grid.addWidget(authorEdit,2,1)
	 	grid.addWidget(review,3,0)
	 	grid.addWidget(reviewEdit,3,1,5,1)

	 	self.setLayout(grid)

app=QtGui.QApplication(sys.argv)
ex=Example()
ex.show()
sys.exit(app.exec_())