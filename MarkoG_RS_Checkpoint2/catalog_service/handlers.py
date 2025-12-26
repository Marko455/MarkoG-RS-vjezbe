from aiohttp import web

# -----------------------------
# Hotels
# -----------------------------
async def list_hotels(request):
    db = request.app["db"]
    cursor = db.execute("SELECT id, name, city FROM hotels")
    hotels = [
        {"id": row[0], "name": row[1], "city": row[2]}
        for row in cursor.fetchall()
    ]
    return web.json_response(hotels)


async def get_hotel(request):
    db = request.app["db"]
    hotel_id = request.match_info["id"]

    cursor = db.execute(
        "SELECT id, name, city FROM hotels WHERE id = ?",
        (hotel_id,)
    )
    row = cursor.fetchone()

    if not row:
        raise web.HTTPNotFound()

    return web.json_response({
        "id": row[0],
        "name": row[1],
        "city": row[2]
    })


async def create_hotel(request):
    db = request.app["db"]
    data = await request.json()

    cursor = db.execute(
        "INSERT INTO hotels (name, city) VALUES (?, ?)",
        (data["name"], data["city"])
    )
    db.commit()

    return web.json_response(
        {"id": cursor.lastrowid},
        status=201
    )


async def update_hotel(request):
    db = request.app["db"]
    hotel_id = request.match_info["id"]
    data = await request.json()

    db.execute(
        "UPDATE hotels SET name = ?, city = ? WHERE id = ?",
        (data["name"], data["city"], hotel_id)
    )
    db.commit()

    return web.json_response({"status": "updated"})


async def delete_hotel(request):
    db = request.app["db"]
    hotel_id = request.match_info["id"]

    db.execute("DELETE FROM hotels WHERE id = ?", (hotel_id,))
    db.commit()

    return web.json_response({"status": "deleted"})


# -----------------------------
# Rooms
# -----------------------------
async def list_rooms_for_hotel(request):
    db = request.app["db"]
    hotel_id = request.match_info["id"]

    cursor = db.execute(
        "SELECT id, number, room_type, price FROM rooms WHERE hotel_id = ?",
        (hotel_id,)
    )
    rooms = [
        {
            "id": row[0],
            "number": row[1],
            "room_type": row[2],
            "price": row[3]
        }
        for row in cursor.fetchall()
    ]

    return web.json_response(rooms)


async def get_room(request):
    db = request.app["db"]
    room_id = request.match_info["id"]

    cursor = db.execute(
        "SELECT id, hotel_id, number, room_type, price FROM rooms WHERE id = ?",
        (room_id,)
    )
    row = cursor.fetchone()

    if not row:
        raise web.HTTPNotFound()

    return web.json_response({
        "id": row[0],
        "hotel_id": row[1],
        "number": row[2],
        "room_type": row[3],
        "price": row[4]
    })


async def create_room(request):
    db = request.app["db"]
    data = await request.json()

    cursor = db.execute(
        """
        INSERT INTO rooms (hotel_id, number, room_type, price)
        VALUES (?, ?, ?, ?)
        """,
        (
            data["hotel_id"],
            data["number"],
            data["room_type"],
            data["price"]
        )
    )
    db.commit()

    return web.json_response(
        {"id": cursor.lastrowid},
        status=201
    )


async def update_room(request):
    db = request.app["db"]
    room_id = request.match_info["id"]
    data = await request.json()

    db.execute(
        """
        UPDATE rooms
        SET number = ?, room_type = ?, price = ?
        WHERE id = ?
        """,
        (
            data["number"],
            data["room_type"],
            data["price"],
            room_id
        )
    )
    db.commit()

    return web.json_response({"status": "updated"})


async def delete_room(request):
    db = request.app["db"]
    room_id = request.match_info["id"]

    db.execute("DELETE FROM rooms WHERE id = ?", (room_id,))
    db.commit()

    return web.json_response({"status": "deleted"})
