# Parametres obtinguts de https://joint-research-centre.ec.europa.eu/photovoltaic-geographical-information-system
# -pvgis/getting-started-pvgis/api-non-interactive-service_en

import dataclasses

import requests

from formats.missatgeria import Solicitud_PVGis, Potencia_PVGis


class Consultor_Produccio_Sistema:
    def __init__(self, instalacio: Solicitud_PVGis):
        self.url = "https://re.jrc.ec.europa.eu/api/PVcalc"
        self.parametres: dict = dataclasses.asdict(instalacio)
        self.latitut = self.parametres["lat"]
        self.longitud = self.parametres["lon"]
        self.potencia = self.parametres["peakpower"]
        self.perdues = self.parametres["loss"]
        self.resultat_consulta = None

    def realitzar_consulta(self):
        print("Consultant PVGIS...")
        ordre_consulta = requests.get(self.url, params=self.parametres)
        if ordre_consulta.status_code == 200:
            return ordre_consulta.json()
        else:
            raise ConnectionError(f"Codi: {ordre_consulta.status_code} Motiu: {ordre_consulta.reason}")

    def proporcionar_resposta_pvgis(self):
        """
        Converteix la resposta de PVGIS a instancia de Potencia_PVGis
        i l'assigna a self.resultat_consulta

        :return:
        produccio_sistema: dataclass Potencia_PVGis
        """
        dades_mesos=self.realitzar_consulta()["outputs"]["monthly"]["fixed"]
        print("Resposta PVGIS convertida a Potencia_PVGis")
        produccions_mensuals = [dades_mesos[i]["E_m"] for i in range(len(dades_mesos))]
        produccio_sistema = Potencia_PVGis(*produccions_mensuals)  # Potencia_PVGis(*)
        self.resultat_consulta = produccio_sistema
        return produccio_sistema

