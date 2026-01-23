from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3

DB = "rooms.db"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    return sqlite3.connect(DB)


class RoomIn(BaseModel):
    number: str
    type: str
    price: float


class RoomAvailability(BaseModel):
    available: int


class RoomOut(BaseModel):
    id: int
    number: str
    type: str
    price: float
    available: bool


@app.get("/rooms", response_model=List[RoomOut])
def list_rooms():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM rooms")
    rows = cur.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "number": r[1],
            "type": r[2],
            "price": r[3],
            "available": bool(r[4]),
        }
        for r in rows
    ]


@app.post("/rooms")
def add_room(room: RoomIn):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO rooms (number, type, price, available) VALUES (?, ?, ?, 1)",
        (room.number, room.type, room.price),
    )
    conn.commit()
    conn.close()

    return {"status": "room added"}


@app.put("/rooms/{id}")
def set_availability(id: int, data: RoomAvailability):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE rooms SET available = ? WHERE id = ?",
        (data.available, id),
    )
    conn.commit()
    conn.close()

    return {"status": "updated"}
