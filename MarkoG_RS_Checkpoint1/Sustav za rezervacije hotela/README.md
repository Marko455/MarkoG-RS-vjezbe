Svrha aplikacije: Rezerviranje hotelskih soba
Instalacija:
    Kloniranje ili preuzimanje programa sa Githuba
Naredba za pokretanje:
    Pokrenite vlastiti Anaconda PowerShell, i kopirajte putanju direktoriju (C:\Users\...\MarkoG_RS_Checkpoint1\SZRH_aplikacija)
    Jednom kada se nalazite u direktoriju pokrenite aplikaciju sa naredbom "py main.py"
Implementacija:
    Python aplikacija rezerviranja hotelskih soba je objektno orijentirani program koristeći asinkrone funkcijonalnosti.
    Aplikacija se sastoji od četiri glavne Python datoteke: main.py, services.py, storage.py i models.py
    Main.py - glavni pokretač aplikacije u kojoj se nalazi korisničko sučelje (izbornik), funkcije za ispisivanje popisa slobodnih
        i rezerviranih hotelskih soba, rezerviranje soba, provjeravanje određene sobe ako je slobodna i oslobodavanje sobe u slučaju
        da korisnik odustaje od rezervacije.
    Models.py - datoteka u kojoj su definirane klase koje predstavljavju hotel i hotelsku sobu koje će biti korištene za izradu istovrsnih objekata
        spremljenih u SQL Lite bazi podataka ovisno koju opciju korisnik izabere.
    Storage.py - sadrži program inicijalizacije SQL Lite baze podataka i sve njezine funkcije za spremanje objekata i
        queryanje objekata(hotelskih soba)
    Services.py - Python datoteka koja sadrži sve asinkrone funckije koje će biti korištene u Main.py programu.

Upute korištenja:
    Za pokretanje aplikacije sustava rezerviranja hotelskih soba, korisnik mora koristeći terminal ući u direktorij
    "cd C:\Users\...\MarkoG_RS_Checkpoint1\SZRH_aplikacija" i unijeti naredbu "py main.py". Nakon uspiješnog pokretanja korisniku
    je predstavljen jednostavno korisničko sučelje koje se sastoji od izbornika nudeći mogućnosti: "Izlistaj popis hotela", "Provjeri slobodne sobe", "Rezerviraj sobu", "Oslobodi sobu" i "Izađi"
    Svaka mogućnost je indeksirana brojem od 1 do 5.
    Od korisnika se traži da odabere jednu od prije navedenih mogućnosti unosom broja od 1 do 5. ("Odaberite izbor: ")
    "Izlistaj popis hotela" - Prikazuje sve hotele spremljenih u bazi podataka
    "Provjeri slobodne sobe" - Od korisnika traži da unese indeks hotela, te prikazuje sve slobodne sobe u navedenom hotelu
    "Rezerviraj sobu" - Za rezerviranje sobe korisnik mora odabrati holel, provjeriti stanje soba i unijeti broj sobe koju želi, ako je soba
        sloboda, rezervacija će biti uspiješna, u suprotnom korisnik će dobiti povratnu informaciju da soba nije slobodna
    "Oslobodi sobu" - U slučaju da korisnik želi odustati od rezervacije hotelske sobe i osloboditi sobu za druge korisnike, mora samo unijeti
        broj sobe koju je rezervirao
    "Izađi" - Peta mogućnost izbornika koja prekida rad cijele aplikacije

