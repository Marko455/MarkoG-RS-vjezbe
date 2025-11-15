import asyncio

baza_korisnika = [
  {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
  {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
  {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
  {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]
baza_lozinka = [
  {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
  {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
  {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
  {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autentifikacija(korisnici):
    print("autentificiram...")
    rezultat1 = [korisnik if korisnik["korisnicko_ime"] in korisnik["email"] else "Korisnikn ije pronađen." for korisnik in korisnici]
    await asyncio.sleep(3)
    return rezultat1

async def autorizacija(rezultat1):
    print("autoriziram...")
    rezultat2 = ["Uspijesna autorizacija" if lozinka["korisnicko_ime"] == rezultat1["korisnicko_ime"] else "Neuspijena autorizacija" for lozinka in baza_lozinka]
    await asyncio.sleep(2)

async def main():
    task1 = asyncio.create_task(autentifikacija(baza_korisnika))
    rezultat_task1 = await task1
    task2 = asyncio.create_task(autorizacija(rezultat_task1))
    rezultat_task2 = await task2
    print(rezultat_task1)
    print(rezultat_task2)

asyncio.run(main())