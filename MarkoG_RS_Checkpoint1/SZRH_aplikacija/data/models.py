class HotelRoom:
    def __init__(self, room_number, room_type, price_per_night, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = float(price_per_night)
        self.is_available = bool(is_available)


class Reservation:
    def __init__(self, reservation_id, room_number, guest_name, check_in, check_out=None):
        self.reservation_id = reservation_id
        self.room_number = room_number
        self.guest_name = guest_name
        self.check_in = check_in
        self.check_out = check_out


def ispis(rooms):
    print("\n📋 Room List:")
    for r in rooms:
        status = "Available" if r.is_available else "Booked"
        print(f"- Room {r.room_number} | {r.room_type} | ${r.price_per_night}/night | {status}")
    print()