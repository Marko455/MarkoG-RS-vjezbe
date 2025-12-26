from aiohttp import web
from datetime import datetime
import requests

AVAILABILITY_URL = "http://localhost:8003"

# -----------------------------
# Create booking
# -----------------------------
async def create_booking(request):
    db = request.app["db"]
    data = await request.json()

    user_id = data["user_id"]
    room_id = data["room_id"]
    date_from = data["date_from"]
    date_to = data["date_to"]

    # 1️⃣ Hold room
    hold_response = requests.post(
        f"{AVAILABILITY_URL}/availability/hold",
        json={
            "room_id": room_id,
            "date_from": date_from,
            "date_to": date_to
        }
    )

    if hold_response.status_code != 201:
        raise web.HTTPConflict(text="Room not available")

    hold_id = hold_response.json()["hold_id"]

    # 2️⃣ Save booking
    cursor = db.execute(
        """
        INSERT INTO bookings (
            user_id, room_id, date_from, date_to,
            status, hold_id, created_at
        )
        VALUES (?, ?, ?, ?, 'confirmed', ?, ?)
        """,
        (
            user_id,
            room_id,
            date_from,
            date_to,
            hold_id,
            datetime.utcnow().isoformat()
        )
    )
    db.commit()

    booking_id = cursor.lastrowid

    # 3️⃣ Confirm availability
    requests.post(
        f"{AVAILABILITY_URL}/availability/confirm",
        json={"hold_id": hold_id}
    )

    return web.json_response(
        {"booking_id": booking_id},
        status=201
    )


# -----------------------------
# Get booking
# -----------------------------
async def get_booking(request):
    db = request.app["db"]
    booking_id = request.match_info["id"]

    cursor = db.execute(
        """
        SELECT id, user_id, room_id, date_from, date_to, status
        FROM bookings WHERE id = ?
        """,
        (booking_id,)
    )
    row = cursor.fetchone()

    if not row:
        raise web.HTTPNotFound()

    return web.json_response({
        "id": row[0],
        "user_id": row[1],
        "room_id": row[2],
        "date_from": row[3],
        "date_to": row[4],
        "status": row[5]
    })


# -----------------------------
# Cancel booking
# -----------------------------
async def cancel_booking(request):
    db = request.app["db"]
    booking_id = request.match_info["id"]

    cursor = db.execute(
        "SELECT hold_id FROM bookings WHERE id = ? AND status = 'confirmed'",
        (booking_id,)
    )
    row = cursor.fetchone()

    if not row:
        raise web.HTTPNotFound(text="Booking not found or already cancelled")

    hold_id = row[0]

    # Release availability (safe even if already confirmed)
    requests.post(
        f"{AVAILABILITY_URL}/availability/release",
        json={"hold_id": hold_id}
    )

    db.execute(
        "UPDATE bookings SET status = 'cancelled' WHERE id = ?",
        (booking_id,)
    )
    db.commit()

    return web.json_response({"status": "cancelled"})
