# -*- coding: utf-8 -*-
"""
Created on Sun May  5 15:21:48 2024

@author: loeva
"""

import sys
from debut_combat import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication

class XXXXWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(XXXXWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = XXXXWindow()
        mainWin.show()
        app.exec_()
    run_app()      