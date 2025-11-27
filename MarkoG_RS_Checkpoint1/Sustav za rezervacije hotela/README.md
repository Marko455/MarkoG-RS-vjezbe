Svrha aplikacije: Rezerviranje hotelskih soba
Instalacija:
    Kloniranje ili preuzimanje programa sa Githuba
Naredba za pokretanje:
    Pokrenite vlastiti Anaconda PowerShell, i kopirajte putanju direktoriju (C:\Users\...\MarkoG_RS_Checkpoint1\SZRH_aplikacija)
    Jednom kada se nalazite u direktoriju pokrenite aplikaciju sa naredbom "py cli.py"

Upute korištenja:
    Za pokretanje aplikacije sustava rezerviranja hotelskih soba, korisnik mora koristeći terminal ući u direktorij
    "cd C:\Users\...\MarkoG_RS_Checkpoint1\SZRH_aplikacija" i unijeti naredbu "py cli.py". Nakon uspiješnog pokretanja korisniku
    je predstavljen jednostavno korisničko sučelje koje se sastoji od izbornika nudeći mogućnosti: "Pregled soba", "Rezerviranje sobe", "Oslobadanje sobe", "Povijest rezerviranja", "Filtriranje soba" i "Izlaz"
    Svaka mogućnost je prikazan Tkinter korisničkim sučeljem.
    Od korisnika se traži da odabere jednu od prije navedenih mogućnosti
    "Pregled soba" - Prikazuje sve hotele spremljenih u bazi podataka
    "Rezerviranje sobe" - Od korisnika traži da unese indeks hotela i ime gosta kojem će soba pripadati, u slučaju da je unio indeks sobe
        koji je zauzet, pokazati će se povratna informacija "Soba je vec rezervirana", ako nije došlo do greške, korisniku dobiva poruku
        "Rezervirana soba: [broj sobe] za [ime gosta]."
    "Oslobadanje sobe" - U slučaju da je korisnik gotov sa odstajanjem ili želi otkazati sobu time da je  oslobodi za drugog korisnika,
        korisnik   mora unijeti broj svoje sobe, ovisno o stanju zauzetosti sobe, povratna informacija može biti "Soba je već oslobođena", "Krivi unos" u slučaju da je unijo krivi tip podatka i "Soba ne postoji u sistemu" ako je unijo broj sobe koji nije registriran u bazi podataka ili jednostavno ne postoji.
    "Povijest rezerviranja" - jednostavno ispisuje sve sobe i njihove korisnike koji su rezervirali i/ili oslobodili sobu
    "Filtriranje sobe" - Peta mogućnost izbornika koja omogućuje korisniku da pretraži sobu ovisnu o poželjnom tipu sobe, najvećoj cijeni
        koju je korisnik voljan platiti i po zauzetosti.

Implementacija:
    Python aplikacija rezerviranja hotelskih soba je objektno orijentirani program koristeći funkcijonalnosti modula i paketa.
    Aplikacija se sastoji od tri glavne Python datoteke: main.py, cli.py, storage.py i models.py
    cli.py - glavni pokretač aplikacije u kojoj se nalazi korisničko sučelje (izbornik), funkcije za ispisivanje popisa slobodnih
        i rezerviranih hotelskih soba, rezerviranje soba, oslobađanje sobe, povijest rezerviranja i filtriranje (provjeravanje) određene sobe ako je slobodna ovisno o tipu i maksimalnoj cijeni
        da korisnik odustaje od rezervacije.
    Models.py - datoteka u kojoj su definirane klase koje predstavljavju hotel i hotelsku sobu koje će biti korištene za izradu istovrsnih objekata
        spremljenih u SQL Lite bazi podataka ovisno koju opciju korisnik izabere.
    Storage.py - Modul zadužen je za upravljanje bazom podataka hotela koristeći SQLite i definira funkcije za dodavanje soba, 
        dohvat  soba te rukovanje rezervacijama. Radi se o backend dijelu sustava to jeste, logiku pohrane i dohvaćanja podataka.
        Funkcija init_db() kreira SQLite bazu i dvije tablice ako već ne postoje:rooms — pohranjuje hotelske sobe, reservations — povijest rezervacija. Ovim se priprema baza i strukture potrebne za rad cijelog sistema. Funkcije vezane uz sobe:
        unesi_sobu(room) Dodaje novu hotelsku sobu u bazu. Prima objekt HotelRoom (definiran u data.models). Sprema sobu u tablicu rooms.
        ispisi_sve_sobe()-Dohvaća sve sobe iz baze: Vraća listu objekata HotelRoom, konstruiranih iz redova u tablici. oslobodi_sobu(room_number, available) Ažurira status sobe: True → soba postaje dostupna (is_available = 1) False → soba postaje zauzeta (is_available = 0).
        Funkcije za rezervacije: izradi_rezervaciju(room_number, guest_name). Stvara novu rezervaciju, sprema gostovo ime, sprema trenutni datum kao check_in check_out je NULL dok rezervacija traje, koristi se automatska dodjela ID-a ovo znači da se svaka rezervacija bilježi kao jedinstveni zapis u bazi. zatvori_rezervaciju(room_number): zatvara aktivnu rezervaciju za određenu sobu, postavlja check_out na trenutni datum, ažurira samo one rezervacije koje još nemaju check_out (dakle otvorene), time sustav zadržava povijesne podatke, ne briše stare rezervacije. ispis_povijesti_rez(): dohvaća sve rezervacije u obrnutom redoslijedu (zadnje prve), rezultate pretvara u objekte Reservation, omogućuje prikaz kompletne povijesti gostiju i termina.

Koristi INSERT OR IGNORE, što znači da se soba neće duplicirati ako već postoji.
    Main.py - Ovaj Python program implementira jednostavni hotelski sustav rezervacija preko komandne linije. Pri pokretanju se inicijalizira baza (init_db) i ubacuju se početne testne sobe (seed_rooms). Korisnik preko menija može: Pregledati sve sobe, Rezervirati sobu — provjerava se dostupnost, stvara se rezervacija i soba se označava zauzetom., Osloboditi sobu — zatvara se zadnja rezervacija i soba postaje slobodna.Pregledati povijest rezervacija, Filtrirati sobe prema: dostupnosti, tipu sobe (Single/Double/Suite), maksimalnoj cijeni po noći. Sustav koristi modele i funkcije iz data.models i data.storage za pohranu i ispis podataka. Ukratko, program nudi osnovne CRUD operacije nad hotelskim sobama i rezervacijama putem jednostavnog tekstualnog sučelja.