from proizvodi import Proizvod
from narudzbe import Narudzba

proizvodi_za_dodavanje = [
    {"naziv": "Laptop", "cijena": 5000, "dostupna_kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "dostupna_kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "dostupna_kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "dostupna_kolicina": 100}
]

proizvodi = [Proizvod(p["naziv"], p["cijena"], p["dostupna_kolicina"])for p in proizvodi_za_dodavanje]

skladiste =[]
def dodaj_proizvod(proizvod):
    skladiste.append(proizvod)

for proizvod in proizvodi:
    dodaj_proizvod(proizvod)

for p in skladiste:
    p.ispis()