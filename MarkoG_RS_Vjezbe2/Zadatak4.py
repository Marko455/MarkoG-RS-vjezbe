class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza
    def ispisAuta(self):
        print("Marka: "+self.marka+" Model: "+self.model+" Godina proizvodnje:",self.godina_proizvodnje,"Kilometraza:",self.kilometraza)
auto = Automobil("Ford","Mustang", 2025, 5)
auto.ispisAuta()

import math
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def zbroj(self):
        print("Zbroj:", self.a+self.b)
    def oduz(self):
        print("Oduz:", self.a - self.b)
    def mnoz(self):
        print("Mnoz:", self.a*self.b)
    def djelj(self):
        if self.b !=0:
            print("Djelj:", self.a/self.b)
        else:
            print("Nemoj dijeliti sa nulom.")
    def poten(self):
        print("Poten:",self.a**self.b)
    def korj(self):
        print("Korj:", math.sqrt(self.a), math.sqrt(self.b))
kal = Kalkulator(1,1)
kal.zbroj()

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
        self.studenti_objekti=[]
        self.prsjk=0
        self.najbolji_student=""
    def dodajStdn(self, s):
        self.studenti_objekti.append(s)
    def prosjek(self):
        self.prsjk= [sum(student["ocjene"])/len(student["ocjene"]) for student in self.studenti_objekti]
        self.najbolji_student=[max(self.prsjk) for student in self.studenti_objekti]

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
lista = [Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]) for student in studenti]


class Krug:
    def __init__(self, radijus):
        self.radijus = radijus
    def opseg(self):
        print("Opseg:", 2*self.radijus*3.14 )
    def povrsina(self):
        print("Povrsina:", 3.14*self.radijus**2)
krug1 = Krug(5)
krug1.opseg()
krug1.povrsina()

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa
    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Menadzer(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")
    def give_raise(self, radnik, povecanje):
        radnik.placa+=povecanje

radnik = Radnik("Marko","programer",50)
menadzer = Menadzer("Marko","menadzer",50, "ljudski resursi")
radnik.work()
menadzer.give_raise(radnik, 50)
print(radnik.placa)
