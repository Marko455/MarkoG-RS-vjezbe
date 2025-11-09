#1. Koristeći funkciju map, kvadrirajte duljine svih nizova u listi:
nizovi = ["jabuka", "kruška", "banana", "naranča"]

kvadrirane_duljine = list(map(lambda niz: len(niz) ** 2, nizovi))

print(kvadrirane_duljine)

#2. Koristeći funkciju filter, filtrirajte samo brojeve koji su veći od 5:
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

veci_od_5 = list(filter(lambda x: x > 5, brojevi))
print(veci_od_5)

#3. Koristeći odgovarajuću funkciju višeg reda i lambda izraz (bez comprehensiona), pohranite u varijablu transform rezultat kvadriranja 
# svih brojeva u listi gdje rezultat mora biti rječnik gdje su ključevi originalni brojevi, a vrijednosti kvadrati tih brojeva:
brojevi = [10, 5, 12, 15, 20]

transform = dict(map(lambda x: (x, x ** 2), brojevi))
print(transform)

#4. Koristeći funkcije all i map, provjerite jesu li svi studenti punoljetni:
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = all(map(lambda s: s["godine"] >= 18, studenti))
print(svi_punoljetni)


