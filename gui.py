import sys
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QWidget, QLabel, QTextEdit, QGridLayout, QVBoxLayout


class ModulMapa(QWidget):

    def __init__(self, latitut, longitut):
        super(ModulMapa, self).__init__()
        self.latitut = latitut
        self.longitut = longitut
        self.visor_mapa = QWebEngineView()
        self.distribucio = QVBoxLayout()
        self.setLayout(self.distribucio)
        coordenades = f"{self.latitut},{self.longitut}"
        self.visor_mapa.load(QUrl(f"https://wego.here.com/?map={coordenades},18,satellite"))
        self.distribucio.addWidget(self.visor_mapa)

    def refrescarmapa(self):
        self.visor_mapa.reload()


class VisorCoordenades(QWidget):

    def __init__(self):
        super(VisorCoordenades, self).__init__()
        self.lat_etiqueta = QLabel("Latitut: ")
        self.lat_coord = QTextEdit()
        self.lon_etiqueta = QLabel("Longitut")
        self.lon_coord = QTextEdit()
        self.visor_distribucio = QGridLayout()
        self.mapa = ModulMapa(41.53639, 2.10468)
        self.situar_elements()

    def situar_elements(self):
        self.visor_distribucio.addWidget(self.lat_etiqueta, 0, 0)
        self.visor_distribucio.addWidget(self.lat_coord, 0, 1)
        self.visor_distribucio.addWidget(self.lon_etiqueta, 1, 0)
        self.visor_distribucio.addWidget(self.lon_coord, 1, 1)
        self.visor_distribucio.addWidget(self.mapa, 2, 0,1,1)
        self.setLayout(self.visor_distribucio)
