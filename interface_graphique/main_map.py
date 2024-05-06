# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:13:59 2024

@author: loeva
"""

import sys
from map import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from choix_attaque import Ui_Dialog


class CarteWindow (QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(CarteWindow, self).__init__(parent)
        self.setupUi(self)
        
    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            print("appui bouton gauche")
    
class XXXXDlg(QDialog):
    """CRS dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)
        
    def accept(self):
    # On a cliqué sur OK dans la boite de dialogue
    # ....
        super().accept()

if __name__ == "__main__":
    def run_app():
        app = QApplication(sys.argv)
        mainWin = CarteWindow()
        mainWin.show()
        app.exec_()
    run_app()
