#! /usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore
class Main(QtGui.QWidget):
	def __init__(self):
		super(Main,self).__init__()
		
		self.setWindowTitle("Splash")
		self.resize(300,250)
		self.move(300,300)

class Splash(QtGui.QSplashScreen):
	def __init__(self):
		super(Splash, self).__init__()
		self.setPixmap(QtGui.QPixmap("img/apple.png"))
		self.show()
		
		self.timer=QtCore.QBasicTimer()
		self.step=0
		self.timer.start(30,self)

	def timerEvent(self,event):
		if self.step>=30:
			self.timer.stop()
			self.finish(m)
			m.show()
		self.step+=1

if __name__=='__main__':
	app=QtGui.QApplication(sys.argv)
	splash=Splash()
	app.processEvents()
	m=Main()
	sys.exit(app.exec_())