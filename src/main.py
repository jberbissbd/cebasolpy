from formats.missatgeria import Solicitud_PVGis
from majordoms.pvgis import Consultor_Produccio_Sistema

Prova = Solicitud_PVGis(45.0, 8.0, 15.5, 14)
Capullo = Consultor_Produccio_Sistema(Prova)
Capullo.proporcionar_resposta_pvgis()
