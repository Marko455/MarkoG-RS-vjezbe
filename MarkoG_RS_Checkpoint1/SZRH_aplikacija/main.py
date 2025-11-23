import asyncio
from data.storage import init_db, load_hotels, save_hotel, save_room
from core.services import book_room, release_room, find_available_room
from data.models import Hotel, HotelRoom


async def list_hotels(hotels):
    print("\n--- HOTELI ---")
    for idx, hotel in enumerate(hotels):
        print(f"{idx + 1}. {hotel.name} ({hotel.address}) - {len(hotel.rooms)} rooms")


async def list_available_rooms(hotel):
    print(f"\n--- Slobodne sobe {hotel.name} ---")
    available = [r for r in hotel.rooms if r.is_available]

    if not available:
        print("Nema slobodnih soba.")
    else:
        for idx, room in enumerate(available):
            print(f"{idx + 1}. Room {room.room_number} - {room.room_type} - ${room.price_per_night}")


async def run_app():
    init_db()

    print("Ucitavanje hotela...")
    hotels = load_hotels()

    if not hotels:

        hotel = Hotel()
        hotel.name = "Grand Plaza"
        hotel.address = "123 Main Street"
        hotel.rating = 5
        hotel.num_rooms = 2

        hotel_id = save_hotel(hotel)

        room1 = HotelRoom()
        room1.room_number = 101
        room1.room_type = "Single"
        room1.price_per_night = 100

        room2 = HotelRoom()
        room2.room_number = 102
        room2.room_type = "Double"
        room2.price_per_night = 150

        save_room(hotel_id, room1)
        save_room(hotel_id, room2)

        hotels = load_hotels()


    while True:
        print("\n======================")
        print("SISTEM REZERVIRANJA HOTELSKIH SOBA")
        print("======================")
        print("1. Izlistaj popis hotela")
        print("2. Provjeri slobodne sobe")
        print("3. Rezerviraj sobu")
        print("4. Oslobodi sobu")
        print("5. Izadi")
        choice = input("Odaberite izbor: ")

        if choice == "1":
            await list_hotels(hotels)

        elif choice == "2":
            await list_hotels(hotels)
            h = int(input("Izaberite hotelski broj: ")) - 1
            await list_available_rooms(hotels[h])

        elif choice == "3":
            await list_hotels(hotels)
            h = int(input("Izaberite hotelski broj: ")) - 1
            hotel = hotels[h]

            await list_available_rooms(hotel)
            rnum = int(input("Unesite broj sobe koje zelite rezervirati: "))

            # Find the actual room
            room = next((x for x in hotel.rooms if x.room_number == rnum), None)

            if room and room.is_available:
                await book_room(room)
                print(f"Soba {room.room_number} je uspijesno rezervirana!")
            else:
                print("Pogresan izbor ili je soba vec rezervirana.")

        elif choice == "4":
            await list_hotels(hotels)
            h = int(input("Izaberite hotelski broj: ")) - 1
            hotel = hotels[h]

            print("\n--- REZERVIRANE SOBE ---")
            booked = [r for r in hotel.rooms if not r.is_available]

            if not booked:
                print("Nema rezerviranih soba.")
                continue

            for room in booked:
                print(f"Soba {room.room_number}")

            rnum = int(input("Unesite broj sobe za osloboditi: "))

            room = next((x for x in hotel.rooms if x.room_number == rnum), None)

            if room and not room.is_available:
                await release_room(room)
                print(f"Soba {room.room_number} je oslobodena!")
            else:
                print("Krivi izbor.")

        elif choice == "5":
            print("Dovidenja!")
            break

        else:
            print("Pogresan izbor.")

asyncio.run(run_app())
