Svrha aplikacije: Rezerviranje hotelskih soba
Instalacija:
    Kloniranje ili preuzimanje programa sa Githuba
Naredba za pokretanje:
    Pokrenite vlastiti Anaconda PowerShell, i kopirajte putanju direktoriju (C:\Users\...\MarkoG_RS_Checkpoint1\SZRH_aplikacija)
    Jednom kada se nalazite u direktoriju pokrenite aplikaciju sa naredbom "py main.py"
Implementacija:
    Python aplikacija rezerviranja hotelskih soba je objektno orijentirani program koristeći funkcijonalnosti modula i paketa.
    Aplikacija se sastoji od tri glavne Python datoteke: main.py, storage.py i models.py
    Main.py - glavni pokretač aplikacije u kojoj se nalazi korisničko sučelje (izbornik), funkcije za ispisivanje popisa slobodnih
        i rezerviranih hotelskih soba, rezerviranje soba, oslobađanje sobe, povijest rezerviranja i filtriranje (provjeravanje) određene sobe ako je slobodna ovisno o tipu i maksimalnoj cijeni
        da korisnik odustaje od rezervacije.
    Models.py - datoteka u kojoj su definirane klase koje predstavljavju hotel i hotelsku sobu koje će biti korištene za izradu istovrsnih objekata
        spremljenih u SQL Lite bazi podataka ovisno koju opciju korisnik izabere.
    Storage.py - sadrži program inicijalizacije SQL Lite baze podataka i sve njezine funkcije za spremanje objekata i
        queryanje objekata(hotelskih soba)

Upute korištenja:
    Za pokretanje aplikacije sustava rezerviranja hotelskih soba, korisnik mora koristeći terminal ući u direktorij
    "cd C:\Users\...\MarkoG_RS_Checkpoint1\SZRH_aplikacija" i unijeti naredbu "py main.py". Nakon uspiješnog pokretanja korisniku
    je predstavljen jednostavno korisničko sučelje koje se sastoji od izbornika nudeći mogućnosti: "Pregled soba", "Rezerviranje sobe", "Oslobadanje sobe", "Povijest rezerviranja", "Filtriranje soba" i "Izlaz"
    Svaka mogućnost je indeksirana brojem od 1 do 6.
    Od korisnika se traži da odabere jednu od prije navedenih mogućnosti unosom broja od 1 do 6. ("Odaberite izbor: ")
    "Pregled soba" - Prikazuje sve hotele spremljenih u bazi podataka
    "Rezerviranje sobe" - Od korisnika traži da unese indeks hotela i ime gosta kojem će soba pripadati, u slučaju da je unio indeks sobe
        koji je zauzet, pokazati će se povratna informacija "Soba je vec rezervirana", ako nije došlo do greške, korisniku dobiva poruku
        "Rezervirana soba: [broj sobe] za [ime gosta]."
    "Oslobadanje sobe" - U slučaju da je korisnik gotov sa odstajanjem ili želi otkazati sobu time da je  oslobodi za drugog korisnika,
        korisnik   mora unijeti broj svoje sobe, ovisno o stanju zauzetosti sobe, povratna informacija može biti "Soba je već oslobođena", "Krivi unos" u slučaju da je unijo krivi tip podatka i "Soba ne postoji u sistemu" ako je unijo broj sobe koji nije registriran u bazi podataka ili jednostavno ne postoji.
    "Povijest rezerviranja" - jednostavno ispisuje sve sobe i njihove korisnike koji su rezervirali i/ili oslobodili sobu
    "Filtriranje sobe" - Peta mogućnost izbornika koja omogućuje korisniku da pretraži sobu ovisnu o poželjnom tipu sobe, najvećoj cijeni
        koju je korisnik voljan platiti i po zauzetosti.

