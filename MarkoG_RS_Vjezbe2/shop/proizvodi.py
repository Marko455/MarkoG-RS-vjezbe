class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina=dostupna_kolicina
    def ispis(self):
        print(self.naziv, self.cijena, self.dostupna_kolicina)



