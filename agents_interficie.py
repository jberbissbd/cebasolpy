from datetime import datetime

from agents_bbdd import ConnectorProjectes, ConnectorClients, ConnectorTipus, ConnectorTarifa, ConnectorSituacions
from agents_bbdd import ConnectorOperadors, ConnectorInstaladors
from missatges import ProjecteGUI
from dateutil import parser

projectes = ConnectorProjectes()
dades_clients = ConnectorClients()
tipologia = ConnectorTipus()
tarifes = ConnectorTarifa()
situacions = ConnectorSituacions()
operadors = ConnectorOperadors()
instaladors = ConnectorInstaladors()


class ProjecteInterficie:
    def __init__(self):
        self.clients = dades_clients.clients
        self.tipus = tipologia.tipus
        self.tarifa = tarifes.tarifes
        self.situacio = situacions.situacions
        self.operador = operadors.operadors
        self.instaladors = instaladors.instaladors
        self.projectes = self.lectura_projectes()

    def lectura_projectes(self):
        dades_projecte_bbdd = projectes.projectes
        # Convertim els projectes a llistes de Python:
        llista_projectes = []
        projectes_codificats = []
        for element in dades_projecte_bbdd:
            llista_element = [element.id, element.descripcio, element.data, element.codi, element.client, element.tipus,
                              element.tarifa, element.situacio, element.operador, element.instalador]
            llista_projectes.append(llista_element)
        # Reemplacem els ids de cada element per totes les dades de l'element corresponent:
        for projecte in llista_projectes:
            projecte[2] = datetime.date(parser.parse(projecte[2]))
            projecte[4] = self.obtencio_client_projecte(projecte[4])
            projecte[5] = self.obtencio_tipus_projecte(projecte[5])
            projecte[6] = self.obtencio_tarifa_projecte(projecte[6])
            projecte[7] = self.obtencio_situacio_projecte(projecte[7])
            projecte[8] = self.obtencio_operador_projecte(projecte[8])
            projecte[9] = self.obtencio_instalador_projecte(projecte[9])
        # Convertim cada element de la llista al format de missatgeria:
        for projecte in llista_projectes:
            projecte_codificat = ProjecteGUI(projecte[0],projecte[1],projecte[2],projecte[3],projecte[4],projecte[5],
                                          projecte[6],projecte[7],projecte[8],projecte[9])
            projectes_codificats.append(projecte_codificat)
        return projectes_codificats

    def obtencio_client_projecte(self, numero_client):
        """Retorna el client especific corresponent al numero de client"""
        client_correcte = None
        for client in self.clients:
            if client.id == numero_client:
                client_correcte = client
            else:
                continue
        if client_correcte is not None:
            return client_correcte
        raise LookupError

    def obtencio_tipus_projecte(self, numero_tipus):
        """Retorna el tipus especific corresponent al numero de tipus"""
        tipus_correcte = None
        for tipus in self.tipus:
            if tipus.id == numero_tipus:
                tipus_correcte = tipus
            else:
                continue
        if tipus_correcte is not None:
            return tipus_correcte
        raise LookupError

    def obtencio_tarifa_projecte(self, numero_tarifa):
        """Retorna la tarifa especifica corresponent a l'ID de tarifa"""
        tarifa_correcte = None
        for tarifa in self.tarifa:
            if tarifa.id == numero_tarifa:
                tarifa_correcte = tarifa
            else:
                continue
        if tarifa_correcte is not None:
            return tarifa_correcte
        raise LookupError

    def obtencio_situacio_projecte(self, numero_situacio):
        """Retorna la situació especifica corresponent a l'ID' de situació"""
        situacio_correcte = None
        for situacio in self.situacio:
            if situacio.id == numero_situacio:
                situacio_correcte = situacio
            else:
                continue
        if situacio_correcte is not None:
            return situacio_correcte
        raise LookupError("No s'ha trobat la referència de situació")

    def obtencio_operador_projecte(self, numero_operador):
        """Retorna l'operadpor especific corresponent al numero d'operador'"""
        operador_correcte = None
        for operador in self.operador:
            if operador.id == numero_operador:
                operador_correcte = operador
            else:
                continue
        if operador_correcte is not None:
            return operador_correcte
        raise LookupError("No s'ha trobat la referència d'operador")

    def obtencio_instalador_projecte(self, numero_instalador):
        """Retorna l'operadpor especific corresponent al numero d'instalador'"""
        instalador_correcte = None
        for instalador in self.instaladors:
            if instalador.id == numero_instalador:
                instalador_correcte = instalador
            else:
                continue
        if instalador_correcte is not None:
            return instalador_correcte
        raise LookupError("No s'ha trobat la referència d'operador")


a = ProjecteInterficie()
a.lectura_projectes()
