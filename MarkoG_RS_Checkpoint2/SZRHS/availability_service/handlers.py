from aiohttp import web

# -----------------------------
# Availability check
# -----------------------------
async def check_availability(request):
    db = request.app["db"]

    room_id = request.query.get("room_id")
    date_from = request.query.get("from")
    date_to = request.query.get("to")

    if not all([room_id, date_from, date_to]):
        raise web.HTTPBadRequest(text="Missing query parameters")

    cursor = db.execute(
        """
        SELECT 1 FROM reservations
        WHERE room_id = ?
          AND status IN ('held', 'confirmed')
          AND NOT (
              date_to <= ? OR date_from >= ?
          )
        """,
        (room_id, date_from, date_to)
    )

    available = cursor.fetchone() is None

    return web.json_response({
        "room_id": room_id,
        "available": available
    })


# -----------------------------
# Hold room
# -----------------------------
async def hold_room(request):
    db = request.app["db"]
    data = await request.json()

    room_id = data["room_id"]
    date_from = data["date_from"]
    date_to = data["date_to"]

    # Check for conflicts
    cursor = db.execute(
        """
        SELECT 1 FROM reservations
        WHERE room_id = ?
          AND status IN ('held', 'confirmed')
          AND NOT (
              date_to <= ? OR date_from >= ?
          )
        """,
        (room_id, date_from, date_to)
    )

    if cursor.fetchone():
        raise web.HTTPConflict(text="Room not available")

    cursor = db.execute(
        """
        INSERT INTO reservations (room_id, date_from, date_to, status)
        VALUES (?, ?, ?, 'held')
        """,
        (room_id, date_from, date_to)
    )
    db.commit()

    return web.json_response(
        {"hold_id": cursor.lastrowid},
        status=201
    )


# -----------------------------
# Confirm booking
# -----------------------------
async def confirm_room(request):
    db = request.app["db"]
    data = await request.json()

    hold_id = data["hold_id"]

    cursor = db.execute(
        "UPDATE reservations SET status = 'confirmed' WHERE id = ?",
        (hold_id,)
    )

    if cursor.rowcount == 0:
        raise web.HTTPNotFound(text="Hold not found")

    db.commit()
    return web.json_response({"status": "confirmed"})


# -----------------------------
# Release hold
# -----------------------------
async def release_room(request):
    db = request.app["db"]
    data = await request.json()

    hold_id = data["hold_id"]

    cursor = db.execute(
        "DELETE FROM reservations WHERE id = ? AND status = 'held'",
        (hold_id,)
    )

    if cursor.rowcount == 0:
        raise web.HTTPNotFound(text="Hold not found or already confirmed")

    db.commit()
    return web.json_response({"status": "released"})
