from pydantic import BaseModel
from typing import List, TypedDict


class StolInfo(TypedDict):
    broj: int
    lokacija: str


class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float


class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Jelo]
    ukupna_cijena: float
