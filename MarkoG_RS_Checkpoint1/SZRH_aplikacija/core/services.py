from data.models import Hotel
from data.models import HotelRoom

async def book_room(room: HotelRoom):
    if room.is_available:
        room.is_available = False
        return True
    return False


async def release_room(room: HotelRoom):
    if not room.is_available:
        room.is_available = True
        return True
    return False


async def find_available_room(hotel: Hotel):
    for room in hotel.rooms:
        if isinstance(room, HotelRoom) and room.is_available:
            return room
    return None
