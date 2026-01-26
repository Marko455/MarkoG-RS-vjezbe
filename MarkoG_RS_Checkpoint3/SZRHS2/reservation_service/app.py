from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import sqlite3
from datetime import date
import httpx

DB = "reservations.db"
ROOM_SERVICE = "http://room_service:8001"

app = FastAPI()


def get_db():
    return sqlite3.connect(DB)


class CheckInRequest(BaseModel):
    guest_id: int
    room_id: int


class CheckOutRequest(BaseModel):
    reservation_id: int
    room_id: int


@app.post("/checkin")
async def check_in(data: CheckInRequest):
    async with httpx.AsyncClient() as client:
        await client.put(
            f"{ROOM_SERVICE}/rooms/{data.room_id}",
            json={"available": 0},
        )

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO reservations VALUES (NULL, ?, ?, ?, NULL, 1)",
        (data.guest_id, data.room_id, date.today().isoformat()),
    )
    conn.commit()
    conn.close()

    return {"status": "checked in"}


@app.post("/checkout")
async def check_out(data: CheckOutRequest):
    async with httpx.AsyncClient() as client:
        await client.put(
            f"{ROOM_SERVICE}/rooms/{data.room_id}",
            json={"available": 1},
        )

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE reservations SET check_out = ?, active = 0 WHERE id = ?",
        (date.today().isoformat(), data.reservation_id),
    )
    conn.commit()
    conn.close()

    return {"status": "checked out"}
