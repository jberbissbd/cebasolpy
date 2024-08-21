import dataclasses
from dataclasses import dataclass


@dataclass
class Solicitud_PVGis:
    lat: float
    lon: float
    peakpower: float
    loss: float
    outputformat: str = "json"
    browser: int = 1


@dataclass
class Potencia_PVGis:
    _1: float = 0
    _2: float = 0
    _3: float = 0
    _4: float = 0
    _5: float = 0
    _6: float = 0
    _7: float = 0
    _8: float = 0
    _9: float = 0
    _10: float = 0
    _11: float = 0
    _12: float = 0
