import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('◀', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forwad_btn = QAction('▶',self)
        forwad_btn.triggered.connect(self.browser.back)
        navbar.addAction(forwad_btn)

        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

       



app = QApplication(sys.argv)
QApplication.setApplicationName('Tech Browser')
window = MainWindow()
app.exec()
