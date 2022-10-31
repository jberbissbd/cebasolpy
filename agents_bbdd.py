import os.path
import sqlite3
from missatges import ProjecteBBDD, ClientBBDD, TipusBBDD, TarifesBBDD, SituacionsBBDD, OperadorsBBDD, InstaladorBBDD


class ConnectorBBDD:
    """Classe per a determinar la localitzacio de la base de dades"""

    def __init__(self):
        self.localitzacio = os.path.abspath("dades/principal.sqlite")


class ConnectorTaula(ConnectorBBDD):
    """Classe genèrica per connectar amb la base de dades"""

    def __init__(self, taula):
        super().__init__()
        self.taula = taula
        try:
            self.connexio = sqlite3.connect(self.localitzacio)
            self.cursor = self.connexio.cursor()
        except sqlite3.OperationalError:
            raise sqlite3.OperationalError


class ConnectorProjectes(ConnectorTaula):

    def __init__(self):
        super().__init__(taula="projectes")
        self.projectes = self.lectura_taula()

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            missatge_retorn = []
            for resultat_individual in resultat_lectura:
                resultat_formatat = ProjecteBBDD(resultat_individual[0], resultat_individual[1], resultat_individual[
                    2], resultat_individual[3], resultat_individual[4], resultat_individual[5], resultat_individual[6],
                                                 resultat_individual[7], resultat_individual[8], resultat_individual[9])
                missatge_retorn.append(resultat_formatat)
            self.cursor.close()
            return missatge_retorn
        except sqlite3.OperationalError as error:
            return error

    def nou_registre(self, missatge_creacio: list):
        for nou_registre in missatge_creacio:
            try:
                ordre_registre = f"INSERT INTO {self.taula} (projecte_desc,projecte_data,projecte_codi," \
                                 f"projecte_client,projecte_tipus,projecte_tarifa,projecte_situacio," \
                                 f"projecte_operador," \
                                 f"projecte_instalador) VALUES (?,?,?,?,?,?,?,?,?)"
                valors = nou_registre[0], nou_registre[1], nou_registre[2], nou_registre[3], nou_registre[4], \
                         nou_registre[5], nou_registre[6], nou_registre[7], nou_registre[8]
                self.cursor.execute(ordre_registre, valors)
                self.connexio.commit()

            except sqlite3.OperationalError as error:
                return error
        self.cursor.close()
        return True


class ConnectorClients(ConnectorTaula):
    def __init__(self):
        super().__init__(taula="clients")
        self.clients = self.lectura_taula()

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            missatge_retorn = []
            for resultat_individual in resultat_lectura:
                resultat_formatat = ClientBBDD(resultat_individual[0], resultat_individual[1], resultat_individual[2])
                missatge_retorn.append(resultat_formatat)
            self.cursor.close()
            return missatge_retorn
        except sqlite3.OperationalError as error:
            return error


class ConnectorTipus(ConnectorTaula):
    def __init__(self):
        super().__init__(taula="tipus_projectes")
        self.tipus = self.lectura_taula()

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            missatge_retorn = []
            for resultat_individual in resultat_lectura:
                resultat_formatat = TipusBBDD(resultat_individual[0], resultat_individual[1], resultat_individual[2])
                missatge_retorn.append(resultat_formatat)
            self.cursor.close()
            return missatge_retorn
        except sqlite3.OperationalError as error:
            return error


class ConnectorTarifa(ConnectorTaula):
    def __init__(self):
        super().__init__(taula="tarifes")
        self.tarifes = self.lectura_taula()

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            missatge_retorn = []
            for resultat_individual in resultat_lectura:
                resultat_formatat = TarifesBBDD(resultat_individual[0], resultat_individual[1])
                missatge_retorn.append(resultat_formatat)
            self.cursor.close()
            return missatge_retorn
        except sqlite3.OperationalError as error:
            return error


class ConnectorSituacions(ConnectorTaula):
    def __init__(self):
        super().__init__(taula="estats_projecte")
        self.situacions = self.lectura_taula()

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            missatge_retorn = []
            for resultat_individual in resultat_lectura:
                resultat_formatat = SituacionsBBDD(resultat_individual[0], resultat_individual[1])
                missatge_retorn.append(resultat_formatat)
            self.cursor.close()
            return missatge_retorn
        except sqlite3.OperationalError as error:
            return error


class ConnectorOperadors(ConnectorTaula):
    def __init__(self):
        super().__init__(taula="operadors")
        self.operadors = self.lectura_taula()

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            missatge_retorn = []
            for resultat_individual in resultat_lectura:
                resultat_formatat = OperadorsBBDD(resultat_individual[0], resultat_individual[1],resultat_individual[2])
                missatge_retorn.append(resultat_formatat)
            self.cursor.close()
            return missatge_retorn
        except sqlite3.OperationalError as error:
            return error


class ConnectorInstaladors(ConnectorTaula):
    def __init__(self):
        super().__init__(taula="instaladors")
        self.instaladors = self.lectura_taula()

    def lectura_taula(self):
        try:
            ordre_lectura = f"SELECT * FROM {self.taula}"
            resultat_lectura = self.cursor.execute(ordre_lectura).fetchall()
            missatge_retorn = []
            for resultat_individual in resultat_lectura:
                resultat_formatat = InstaladorBBDD(resultat_individual[0], resultat_individual[1],
                                                   resultat_individual[2])
                missatge_retorn.append(resultat_formatat)
            self.cursor.close()
            return missatge_retorn
        except sqlite3.OperationalError as error:
            return error
