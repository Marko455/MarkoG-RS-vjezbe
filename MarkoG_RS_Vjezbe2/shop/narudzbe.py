from proizvodi import Proizvod
class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena=ukupna_cijena

def napravi_narudzbu(proizvodi):
    for proizvod in proizvodi:
        if(proizvod.dostupna_kolicina<=0 and type(proizvodi)==list and type(dict) in proizvodi):
            print(f"Proizvod {proizvod} nije dostupan.")
        else:
            narudzba1 = Narudzba(proizvodi)