Ovo je jednostavna aplikacija za rezerviranje hotelskih soba gostima koristeći mikroservisnu arhitekturu. Projekt se sastoji od
tri mikroservisa, guest_service, reservation_service, room_service i jednog korisničkog sučelja. Svaki mikroservis
se pokreće odvojeno, ima vlastitu bazu podataka, exposa svoj API i je implementiran koristeći aiohttp Python biblioteku

guest_service - je zadužen za upravljanje gostima hotela, to jest: upisuje novog gosta u sistem sa njihovim podacima,
                i dijeli te podatke sa ostalim servisima. Korištene tehnologije su atiohttp, sqlite3 i http. Sastoji se
                tri datoteke app.py, init_db.py i db.py

room_serivivce - je zadužen za upravljanje hotelskim sobama, to jest: unosi hotelske sobe u sistem sa nazivom (niz brojeva),
                 cijenom i tipom sobe (dvokreventa, jednokrevetna, itd.). Aiohttp, sqlite3 i http su korišteni za izradu ovog
                 servisa. Sastoji se od tri datoteke app.py, init_db.py i db.py

reservation_ service - je zadužen za upravljanje rezervacijama. Zaposlenik mora unijeti id korisnika i id soba u kojoj želi
                       ostati. Tehnologije korištene za izradu ovog servisa su aiohttp, http i sqlite3. Servis se sastoji od
                       tri datoteke app.py, init_db.py i db.py

ui - jednostavno korisničko sučelje izrađeno pomoću tkintera, sastoji se od api.py i ui.py datoteka. api.py datoteka sadrži
     sve rute na koje treba ui komunicirati kada se pokrene koristeći http protokol.

Pokretanje aplikacije:
1. Svaki servis se pokreće zasebno, što znači da moraš otvoriti terminal na putanji svakog direktorija servisa u kojoj se
   nalaze njegove datoteke, ako pokrećeš po prvi put, onda moraš prvo unijeti naredbu "python init_db.py" i onda "python app.py"
   Ponovi iste naredbe za ostala dva servisa. Za pokretanje Tkinter korisničkog sučelja trebaš otvoriti njegov direktorij u
   terminalu i unijeti naredbe "python ui.py" i to je to.