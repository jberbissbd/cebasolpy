import datetime
from dataclasses import dataclass


@dataclass(repr=False)
class ProjecteBBDD:
    id: int
    descripcio: str
    data: datetime.date
    codi: str
    client: int
    tipus: int
    tarifa: int
    situacio: int
    operador: int
    instalador: int


@dataclass(repr=False)
class ClientBBDD:
    id: int
    codi: int
    nom: str


@dataclass(repr=False)
class TipusBBDD:
    id: int
    codi: int
    descripcio: str


@dataclass(repr=False)
class TarifesBBDD:
    id: int
    descripcio: str


@dataclass(repr=False)
class SituacionsBBDD:
    id: int
    descripcio: str


@dataclass(repr=False)
class OperadorsBBDD:
    id: int
    codi: int
    nom: str

@dataclass(repr=False)
class InstaladorBBDD:
    id: int
    nom: str
    codi: int

@dataclass(repr=False)
class ProjecteGUI:
    id: int
    descripcio: str
    data: datetime.date
    codi: str
    client: ClientBBDD
    tipus: TipusBBDD
    tarifa: TarifesBBDD
    situacio: SituacionsBBDD
    operador: OperadorsBBDD
    instalador: InstaladorBBDD