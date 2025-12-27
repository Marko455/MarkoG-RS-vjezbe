from aiohttp import web
import sqlite3

DB = "guests.db"
app = web.Application()

def get_db():
    return sqlite3.connect(DB)

async def add_guest(request):
    data = await request.json()

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO guests (name, email, phone) VALUES (?, ?, ?)",
        (data["name"], data.get("email"), data.get("phone"))
    )
    guest_id = cur.lastrowid
    conn.commit()
    conn.close()

    return web.json_response({"guest_id": guest_id})

async def list_guests(request):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM guests")
    rows = cur.fetchall()
    conn.close()

    return web.json_response([
        {"id": g[0], "name": g[1], "email": g[2], "phone": g[3]}
        for g in rows
    ])

app.add_routes([
    web.post("/guests", add_guest),
    web.get("/guests", list_guests)
])

web.run_app(app, port=8002)
