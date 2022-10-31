import sqlite3
import unittest
import random
import secrets
from agents_bbdd import ConnectorBBDD, ConnectorTaula, ConnectorProjectes, ConnectorClients, ConnectorTipus, \
    ConnectorTarifa, ConnectorSituacions, ConnectorOperadors, ConnectorInstaladors
from missatges import ProjecteBBDD, ClientBBDD, SituacionsBBDD, TipusBBDD, TarifesBBDD, InstaladorBBDD, OperadorsBBDD


class tests_bbdd_atributs(unittest.TestCase):

    def test_localitzacio_bbdd(self):
        mostra = ConnectorBBDD()
        assert isinstance(mostra.localitzacio, str), "Localització base de dades del conector general no retorna un " \
                                                     "text o string"

    def test_conexio_bbdd(self):
        mostra_connexio = ConnectorTaula("prova")
        assert isinstance(mostra_connexio.localitzacio, str), "Localització base de dades del conector de taules no " \
                                                              "retorna un text o string"

    def test_connexio_bbdd(self):
        mostra_connexio = ConnectorTaula("prova")
        conexio_test = mostra_connexio.connexio
        assert isinstance(conexio_test, sqlite3.Connection), "Connector del conector de taules no crea la connexio"

    def test_cursor_bbdd(self):
        mostra_connexio = ConnectorTaula("prova")
        cursor_test = mostra_connexio.cursor
        assert isinstance(cursor_test, sqlite3.Cursor), "Cursor del conector de taules no crea un cursor"


class tests_agents_bbdd_parametre_taula(unittest.TestCase):

    def test_taula_projectes(self):
        projectes_prova = ConnectorProjectes()
        assert projectes_prova.taula == "projectes", "EL connector de projectes no té el parametre taula configurat " \
                                                     "correctament."

    def test_taula_clients(self):
        clients_prova = ConnectorClients()
        assert clients_prova.taula == "clients", "EL connector de clients no té el parametre taula configurat " \
                                                 "correctament."

    def test_taula_tipus(self):
        tipus_prova = ConnectorTipus()
        assert tipus_prova.taula == "tipus_projectes", "El connector de tipologies no té el parametre taula " \
                                                       "configurat correctament."

    def test_taula_tarifa(self):
        tarifa_prova = ConnectorTarifa()
        assert tarifa_prova.taula == "tarifes", "El connector de tarifes no té el parametre taula " \
                                                "configurat correctament."

    def test_taula_situacions(self):
        situacio_prova = ConnectorSituacions()
        assert situacio_prova.taula == "estats_projecte", "El connector de situacions no té el parametre taula " \
                                                          "configurat correctament."

    def test_taula_operadors(self):
        operador_prova = ConnectorOperadors()
        assert operador_prova.taula == "operadors", "El connector d'operadors no té el parametre taula " \
                                                    "configurat correctament."

    def test_taula_instaladors(self):
        instalador_prova = ConnectorInstaladors()
        assert instalador_prova.taula == "instaladors", "El connector d'operadors no té el parametre taula " \
                                                        "configurat correctament."


class tests_agents_bbdd_lectura_taula(unittest.TestCase):
    """Si no es produeix un error, la lectura de la base de dades ha de retornar una llista."""

    def test_taula_projectes(self):
        projectes_prova = ConnectorProjectes()
        assert isinstance(projectes_prova.projectes, list), "Error en la lectura de la taula projectes"

    def test_taula_clients(self):
        clients_prova = ConnectorClients()
        assert isinstance(clients_prova.clients, list), "Error en la lectura de la taula clients"

    def test_taula_tipus(self):
        tipus_prova = ConnectorTipus()
        assert isinstance(tipus_prova.tipus, list), "Error en la lectura de la taula tipus"

    def test_taula_tarifes(self):
        tarifa_prova = ConnectorTarifa()
        assert isinstance(tarifa_prova.tarifes, list), "Error en la lectura de la taula tarifes"

    def test_taula_situacions(self):
        situacio_prova = ConnectorSituacions()
        assert isinstance(situacio_prova.situacions, list), "Error en la lectura de la taula situacions"

    def test_taula_operadors(self):
        operador_prova = ConnectorOperadors()
        assert isinstance(operador_prova.operadors, list), "Error en la lectura de la taula operadors"

    def test_taula_instaladors(self):
        instalador_prova = ConnectorInstaladors()
        assert isinstance(instalador_prova.instaladors, list), "Error en la lectura de la taula instaladors"


class tests_agents_bbdd_contingut_no_buit(unittest.TestCase):
    """Si no es produeix un error, la lectura de la base de dades ha de retornar una llista."""

    def test_taula_projectes(self):
        projectes_prova = ConnectorProjectes()
        assert len(projectes_prova.projectes) > 0, "Lectura de la taula projectes retorna un resultat buit"

    def test_taula_clients(self):
        clients_prova = ConnectorClients()
        assert len(clients_prova.clients) > 0, "Lectura de la taula clients retorna un resultat buit"

    def test_taula_tipus(self):
        tipus_prova = ConnectorTipus()
        assert len(tipus_prova.tipus) > 0, "Lectura de la taula tipus retorna un resultat buit"

    def test_taula_tarifes(self):
        tarifa_prova = ConnectorTarifa()
        assert len(tarifa_prova.tarifes) > 0, "Lectura de la taula tarifes retorna un resultat buit"

    def test_taula_situacions(self):
        situacio_prova = ConnectorSituacions()
        assert len(situacio_prova.situacions) > 0, "Lectura de la taula situacions retorna un resultat buit"

    def test_taula_operadors(self):
        operador_prova = ConnectorOperadors()
        assert len(operador_prova.operadors) > 0, "Lectura de la taula operadors retorna un resultat buit"

    def test_taula_instaladors(self):
        instalador_prova = ConnectorInstaladors()
        assert len(instalador_prova.instaladors) > 0, "Lectura de la taula instaladors retorna un resultat buit"


class tests_agents_bbdd_formats(unittest.TestCase):
    """Si no es produeix un error, la lectura de la base de dades ha de retornar una llista."""

    def test_taula_projectes(self):
        projectes_prova = ConnectorProjectes()
        format_projectes = secrets.choice(projectes_prova.projectes)
        assert isinstance(format_projectes, ProjecteBBDD), "Error en el format de la lectura de la taula projectes"

    def test_taula_clients(self):
        clients_prova = ConnectorClients()
        format_clients = secrets.choice(clients_prova.clients)
        assert isinstance(format_clients, ClientBBDD), "Error en el format de la lectura de la taula clients"

    def test_taula_tipus(self):
        tipus_prova = ConnectorTipus()
        format_tipus = secrets.choice(tipus_prova.tipus)
        assert isinstance(format_tipus, TipusBBDD), "Error en el format de la lectura de la taula tipus"

    def test_taula_tarifes(self):
        tarifa_prova = ConnectorTarifa()
        format_tarifa = secrets.choice(tarifa_prova.tarifes)
        assert isinstance(format_tarifa, TarifesBBDD), "Error en el format de la lectura de la taula tarifa"

    def test_taula_situacions(self):
        situacio_prova = ConnectorSituacions()
        format_situacio = secrets.choice(situacio_prova.situacions)
        assert isinstance(format_situacio, SituacionsBBDD), "Error en el format de la lectura de la taula situacions"

    def test_taula_operadors(self):
        operador_prova = ConnectorOperadors()
        format_operador = secrets.choice(operador_prova.operadors)
        assert isinstance(format_operador, OperadorsBBDD), "Error en el format de la lectura de la taula operadors"

    def test_taula_instaladors(self):
        instalador_prova = ConnectorInstaladors()
        format_instalador = secrets.choice(instalador_prova.instaladors)
        assert isinstance(format_instalador, InstaladorBBDD), "Error en el format de la lectura de la taula instaladors"

    connector_bbdd_prova = ConnectorBBDD()
    connector_bbdd_prova.localitzacio = "prova"
    connector_taula_prova = ConnectorTaula(connector_bbdd_prova)
