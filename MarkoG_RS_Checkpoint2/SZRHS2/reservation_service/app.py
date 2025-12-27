from aiohttp import web, ClientSession
import sqlite3
from datetime import date

DB = "reservations.db"
ROOM_SERVICE = "http://localhost:8001"

app = web.Application()

def get_db():
    return sqlite3.connect(DB)

async def check_in(request):
    data = await request.json()
    room_id = data["room_id"]

    async with ClientSession() as session:
        await session.put(
            f"{ROOM_SERVICE}/rooms/{room_id}",
            json={"available": 0}
        )

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO reservations VALUES (NULL, ?, ?, ?, NULL, 1)",
        (data["guest_id"], room_id, date.today().isoformat())
    )
    conn.commit()
    conn.close()

    return web.json_response({"status": "checked in"})

async def check_out(request):
    data = await request.json()
    room_id = data["room_id"]

    async with ClientSession() as session:
        await session.put(
            f"{ROOM_SERVICE}/rooms/{room_id}",
            json={"available": 1}
        )

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE reservations SET check_out = ?, active = 0 WHERE id = ?",
        (date.today().isoformat(), data["reservation_id"])
    )
    conn.commit()
    conn.close()

    return web.json_response({"status": "checked out"})

app.add_routes([
    web.post("/checkin", check_in),
    web.post("/checkout", check_out)
])

web.run_app(app, port=8003)
