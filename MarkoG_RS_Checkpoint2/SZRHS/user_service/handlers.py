from aiohttp import web
from datetime import datetime

async def get_me(request):
    user = request["user"]
    db = request.app["db"]

    user_id = user["sub"]
    email = user.get("email")

    cursor = db.execute(
        "SELECT role FROM users WHERE id = ?",
        (user_id,)
    )
    row = cursor.fetchone()

    if not row:
        db.execute(
            "INSERT INTO users (id, email, role, created_at) VALUES (?, ?, ?, ?)",
            (user_id, email, "customer", datetime.utcnow().isoformat())
        )
        db.commit()
        role = "customer"
    else:
        role = row[0]

    return web.json_response({
        "id": user_id,
        "email": email,
        "role": role
    })
