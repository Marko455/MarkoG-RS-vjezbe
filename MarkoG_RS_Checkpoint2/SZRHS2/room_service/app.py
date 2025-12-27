from aiohttp import web
import sqlite3

DB = "rooms.db"

@web.middleware
async def cors_middleware(request, handler):
    response = await handler(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response

app = web.Application(middlewares=[cors_middleware])

def get_db():
    return sqlite3.connect(DB)

async def list_rooms(request):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM rooms")
    rows = cur.fetchall()
    conn.close()

    return web.json_response([
        {"id": r[0], "number": r[1], "type": r[2], "price": r[3], "available": bool(r[4])}
        for r in rows
    ])

async def add_room(request):
    data = await request.json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO rooms (number, type, price, available) VALUES (?, ?, ?, 1)",
        (data["number"], data["type"], data["price"])
    )
    conn.commit()
    conn.close()

    return web.json_response({"status": "room added"})

async def set_availability(request):
    room_id = request.match_info["id"]
    data = await request.json()

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE rooms SET available = ? WHERE id = ?",
        (data["available"], room_id)
    )
    conn.commit()
    conn.close()

    return web.json_response({"status": "updated"})

app.add_routes([
    web.get("/rooms", list_rooms),
    web.post("/rooms", add_room),
    web.put("/rooms/{id}", set_availability)
])

web.run_app(app, port=8001)
