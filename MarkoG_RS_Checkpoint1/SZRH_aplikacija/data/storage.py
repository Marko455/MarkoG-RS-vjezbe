# storage.py
import sqlite3
from datetime import datetime
from data.models import HotelRoom, Reservation

DB_NAME = "hotel.db"

# --------------------- Kod za incijalizaciju baze podataka ----------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            room_number INTEGER PRIMARY KEY,
            room_type TEXT,
            price_per_night REAL,
            is_available INTEGER
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER,
            guest_name TEXT,
            check_in TEXT,
            check_out TEXT
        )
    """)

    conn.commit()
    conn.close()

# --------------------- Unos(rezerviranje) i brisanje(oslobađanje) hotelskih soba ----------------------

def unesi_sobu(room: HotelRoom):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO rooms VALUES (?, ?, ?, ?)
    """, (room.room_number, room.room_type, room.price_per_night, int(room.is_available)))
    conn.commit()
    conn.close()


def ispisi_sve_sobe():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    rows = c.fetchall()
    conn.close()

    return [HotelRoom(*row) for row in rows]


def pronadi_sobu(room_number):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM rooms WHERE room_number=?", (room_number,))
    row = c.fetchone()
    conn.close()
    return HotelRoom(*row) if row else None


def oslobodi_sobu(room_number, available):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "UPDATE rooms SET is_available=? WHERE room_number=?",
        (1 if available else 0, room_number)
    )
    conn.commit()
    conn.close()


# --------------------- Funkcije rezervacije ----------------------

def izradi_rezervaciju(room_number, guest_name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO reservations (room_number, guest_name, check_in, check_out)
        VALUES (?, ?, ?, NULL)
    """, (room_number, guest_name, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def zatvori_rezervaciju(room_number):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        UPDATE reservations
        SET check_out=?
        WHERE room_number=? AND check_out IS NULL
    """, (datetime.now().isoformat(), room_number))
    conn.commit()
    conn.close()


def ispis_povijesti_rez():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM reservations ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    return [Reservation(*row) for row in rows]
