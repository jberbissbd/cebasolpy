import os.path
import sqlite3
import sys
from os.path import dirname


class ConnectorBBDD:
    """Classe per a determinar la localitzacio de la base de dades"""

    def __init__(self):
        self.localitzacio = os.path.abspath("dades/principal.sqlite")


class ConnectorTaula(ConnectorBBDD):
    """Classe genèrica per conectar amb la base de dades"""

    def __init__(self):
        super().__init__()
        self.connexio = sqlite3.connect(self.localitzacio)
        self.cursor = self.connexio.cursor()
        self.taula = None


class ConnectorProjectes(ConnectorTaula):

    def __init__(self):
        super().__init__()
        self.taula = "projectes"

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            return resultat_lectura
        except sqlite3.OperationalError as error:
            return error
