from pydantic import BaseModel, Field
from datetime import datetime

class Izdavac(BaseModel):
    naziv: str
    adresa: str


class Knjiga(BaseModel):
    naslov: str
    autor_ime: str
    autor_prezime: str
    godina_izdavanja: int = Field(
        default_factory=lambda: datetime.now().year
    )
    broj_stranica: int
    izdavac: Izdavac
