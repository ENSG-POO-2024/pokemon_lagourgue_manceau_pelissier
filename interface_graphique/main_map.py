# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:26:24 2024

@author: loeva
"""
import sys
from pokedeck import Ui_pokedeck
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt, QEvent, QPoint
from PyQt5.uic import loadUi  # Importez la fonction loadUi pour charger le fichier UI


from map import Ui_MainWindow  # Importez la classe générée par pyuic5

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Utilisez la classe générée par Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connectez les signaux et les slots pour gérer les événements de clavier
        self.ui.tete_perso.setFocus()  # Assurez-vous que le QLabel du perso a le focus pour recevoir les événements de clavier
        self.ui.tete_perso.installEventFilter(self)
        
        loadUi("map.ui", self)  # Chargez le fichier UI de la fenêtre principale
        # Connectez le bouton pour ouvrir la boîte de dialogue
        self.bouton_pokedeck.clicked.connect(self.open_dialog)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Left:
                self.move_square(-10, 0)
                return True
            elif key == Qt.Key_Right:
                self.move_square(10, 0)
                return True
            elif key == Qt.Key_Up:
                self.move_square(0, -10)
                return True
            elif key == Qt.Key_Down:
                self.move_square(0, 10)
                return True
        return super().eventFilter(source, event)

    def move_square(self, dx, dy):
        square_pos = self.ui.tete_perso.pos()
        new_pos = square_pos + QPoint(dx, dy)
    
        # Récupérer les dimensions de l'image
        image_width = self.ui.herbe_barriere.width()
        image_height = self.ui.herbe_barriere.height()
    
        # Récupérer les dimensions du carré
        square_width = self.ui.tete_perso.width()
        square_height = self.ui.tete_perso.height()
    
        # Limites de déplacement
        min_x = 0
        max_x = image_width - square_width
        min_y = 0
        max_y = image_height - square_height  # Prend en compte la hauteur du carré
    
        # Vérifier les limites de déplacement
        new_pos.setX(max(min(new_pos.x(), max_x), min_x))
        new_pos.setY(max(min(new_pos.y(), max_y), min_y))
    
        # Déplacer le carré
        self.ui.tete_perso.move(new_pos)
        
        #récuperer les coord du perso
        tete_perso_pos = self.ui.tete_perso.pos()
        print("Coordonnées du carré : ", tete_perso_pos.x(), tete_perso_pos.y())
        
    def open_dialog(self):
        # Créez une instance de la boîte de dialogue
        dialog = PokedeckDlg()
        dialog.exec_()  # Affichez la boîte de dialogue de manière modale



class PokedeckDlg(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("pokedeck.ui", self)  # Chargez le fichier UI de la boîte de dialogue


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    window.tete_perso.setFocus()
    sys.exit(app.exec_())
