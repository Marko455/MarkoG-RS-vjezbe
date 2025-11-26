# main.py
from data.models import HotelRoom, ispis
from data.storage import (
    init_db,
    unesi_sobu,
    ispisi_sve_sobe,
    pronadi_sobu,
    izradi_rezervaciju,
    zatvori_rezervaciju,
    oslobodi_sobu,
    ispis_povijesti_rez
)

# ---------------------- Inicijalne hotelske sobe za testiranje ----------------------

def seed_rooms():
    rooms = [
        HotelRoom(101, "Single", 120),
        HotelRoom(102, "Double", 150),
        HotelRoom(103, "Double", 160),
        HotelRoom(201, "Suite", 260),
    ]
    for room in rooms:
        unesi_sobu(room)

# ---------------------- Funkcija filtriranje soba, dali bile slobodne ili po vrsti ----------------------

def filter_rooms():
    rooms = ispisi_sve_sobe()
    print("\nFiltriraj po:")
    print("1) Zauzetosti")
    print("2) Tipu")
    print("3) Maksimalnoj cijeni")
    print("4) Odustani")

    option = input("Vas odabir: ")

    if option == "1":
        rooms = [r for r in rooms if r.is_available]
    elif option == "2":
        t = input("Unesite tip (Single/Double/Suite): ")
        rooms = [r for r in rooms if r.room_type.lower() == t.lower()]
    elif option == "3":
        price = float(input("Unesite maksimalnu cijenu: "))
        rooms = [r for r in rooms if r.price_per_night <= price]
    else:
        return

    ispis(rooms)


# ---------------------- Korisničko sučelje ----------------------

def main():
    init_db()
    seed_rooms()

    while True:
        print("\n Hotelski sistem rezervacija soba")
        print("1. Pregled soba")
        print("2. Rezerviranje sobe")
        print("3. Oslobadanje sobe")
        print("4. Povijest rezerviranja")
        print("5. Filtriranje soba")
        print("6. Izlaz")

        choice = input("> ")

        if choice == "1":
            ispis(ispisi_sve_sobe())

        elif choice == "2":
            try:
                room_num = int(input("Broj sobe: "))
                guest = input("Ime gosta: ")
            except:
                print("Krivi unos.")
                continue

            room = pronadi_sobu(room_num)

            if not room:
                print("Soba nije pronadena.")
            elif not room.is_available:
                print("Soba je vec rezervirana.")
            else:
                izradi_rezervaciju(room_num, guest)
                oslobodi_sobu(room_num, False)
                print(f"Rezervirana soba: {room_num} za {guest}.")

        elif choice == "3":
            try:
                room_num = int(input("Broj sobe: "))
            except:
                print("Krivi unos.")
                continue

            room = pronadi_sobu(room_num)

            if not room:
                print("Soba ne postoji u sistemu.")
            elif room.is_available:
                print("Soba je vec oslobodena.")
            else:
                zatvori_rezervaciju(room_num)
                oslobodi_sobu(room_num, True)
                print("Soba oslobodena.")

        elif choice == "4":
            history = ispis_povijesti_rez()
            print("\n Povijest rezerviranja")
            for r in history:
                print(f"[{r.reservation_id}] "
                      f"Soba {r.room_number} | Gost {r.guest_name} | "
                      f"Pocetak {r.check_in} | Kraj {r.check_out}")

        elif choice == "5":
            filter_rooms()

        elif choice == "6":
            print("Dovidenja!")
            break

        else:
            print("Krivi izbor")


if __name__ == "__main__":
    main()
