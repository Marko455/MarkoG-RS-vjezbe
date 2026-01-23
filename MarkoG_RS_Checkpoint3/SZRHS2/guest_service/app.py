from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from typing import Optional, List

DB = "guests.db"
app = FastAPI()


def get_db():
    return sqlite3.connect(DB)


class GuestIn(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None


class GuestOut(BaseModel):
    id: int
    name: str
    email: Optional[str]
    phone: Optional[str]


@app.post("/guests")
def add_guest(guest: GuestIn):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO guests (name, email, phone) VALUES (?, ?, ?)",
        (guest.name, guest.email, guest.phone),
    )
    guest_id = cur.lastrowid
    conn.commit()
    conn.close()

    return {"guest_id": guest_id}


@app.get("/guests", response_model=List[GuestOut])
def list_guests():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM guests")
    rows = cur.fetchall()
    conn.close()

    return [
        {"id": g[0], "name": g[1], "email": g[2], "phone": g[3]}
        for g in rows
    ]
