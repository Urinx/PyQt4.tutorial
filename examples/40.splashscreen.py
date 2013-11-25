#! /usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore
class Main(QtGui.QWidget):
	def __init__(self):
		super(Main,self).__init__()
		
		self.setWindowTitle("Splash")
		self.resize(300,250)
		self.move(300,300)
		QtCore.QThread.sleep(2)

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	splash=QtGui.QSplashScreen(QtGui.QPixmap("img/apple.png"))
	splash.show()
	app.processEvents()
	m=Main()
	m.show()
	splash.finish(m)
	sys.exit(app.exec_())