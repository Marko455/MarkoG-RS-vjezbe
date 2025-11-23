import sqlite3
from data.models import Hotel, HotelRoom

DB_PATH = "hotel_data.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hotels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            rating INTEGER,
            num_rooms INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hotel_id INTEGER,
            room_number INTEGER,
            room_type TEXT,
            price_per_night REAL,
            is_available INTEGER,
            FOREIGN KEY (hotel_id) REFERENCES hotels(id)
        )
    """)

    conn.commit()
    conn.close()

def save_hotel(hotel: Hotel):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO hotels (name, address, rating, num_rooms)
        VALUES (?, ?, ?, ?)
    """, (hotel.name, hotel.address, hotel.rating, hotel.num_rooms))

    hotel_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return hotel_id

def save_room(hotel_id: int, room: HotelRoom):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO rooms (hotel_id, room_number, room_type, price_per_night, is_available)
        VALUES (?, ?, ?, ?, ?)
    """, (
        hotel_id,
        room.room_number,
        room.room_type,
        room.price_per_night,
        1 if room.is_available else 0,
    ))

    conn.commit()
    conn.close()

def load_rooms(hotel_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT room_number, room_type, price_per_night, is_available
        FROM rooms WHERE hotel_id = ?
    """, (hotel_id,))

    rows = cursor.fetchall()
    conn.close()

    rooms = []
    for r in rows:
        room = HotelRoom()
        room.room_number = r[0]
        room.room_type = r[1]
        room.price_per_night = r[2]
        room.is_available = bool(r[3])
        rooms.append(room)

    return rooms

def load_hotels():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, address, rating, num_rooms FROM hotels")
    rows = cursor.fetchall()
    conn.close()

    hotels = []

    for r in rows:
        hotel = Hotel()
        hotel.id = r[0]
        hotel.name = r[1]
        hotel.address = r[2]
        hotel.rating = r[3]
        hotel.num_rooms = r[4]
        hotel.rooms = load_rooms(hotel.id)

        hotels.append(hotel)

    return hotels
