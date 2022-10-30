from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QLabel
from agents_interficie import ProjecteInterficie
from gui import  VisorCoordenades
import sys

from PySide6.QtCore import Qt, QUrl


a = ProjecteInterficie()
llistat = []
for projecte in a.projectes:
    info_buscada = [projecte.id,projecte.data,projecte.codi,projecte.client.nom,projecte.tarifa.descripcio,
                    projecte.tipus.codi]
    llistat.append(info_buscada)
print(llistat)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    visor = VisorCoordenades()
    visor.show()

    sys.exit(app.exec())



