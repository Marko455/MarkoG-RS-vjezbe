from pydantic import BaseModel, EmailStr, Field
from typing import List, Literal

Ovlast = Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]


class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: EmailStr
    ovlasti: List[Ovlast] = Field(default_factory=list)
