class Hotel:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.rating = 0
        self.num_rooms = 0
        self.rooms = []

class HotelRoom(Hotel):
    def __init__(self):
        super().__init__()
        self.room_number = 0
        self.room_type = ""
        self.price_per_night = 0.0
        self.is_available = True
