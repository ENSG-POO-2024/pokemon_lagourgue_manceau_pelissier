# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:58:15 2024

@author: loeva
"""

import sys
from map import Ui_MainWindow

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