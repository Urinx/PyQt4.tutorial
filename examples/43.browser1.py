#!/usr/bin/env python
import sys
from PyQt4 import QtGui,QtCore,QtWebKit

app=QtGui.QApplication(sys.argv)
web=QtWebKit.QWebView()
web.load(QtCore.QUrl("http://google.hk"))
web.show()
sys.exit(app.exec_())