import requests

ROOM_SERVICE = "http://room_service:8001"
GUEST_SERVICE = "http://guest_service:8002"
RESERVATION_SERVICE = "http://reservation_service:8003"


def add_guest(name, email):
    r = requests.post(
        f"{GUEST_SERVICE}/guests",
        json={"name": name, "email": email}
    )
    return r.json()


def add_room(number, room_type, price):
    requests.post(
        f"{ROOM_SERVICE}/rooms",
        json={"number": number, "type": room_type, "price": price}
    )


def get_rooms():
    r = requests.get(f"{ROOM_SERVICE}/rooms")
    return r.json()


def check_in(guest_id, room_id):
    requests.post(
        f"{RESERVATION_SERVICE}/checkin",
        json={"guest_id": guest_id, "room_id": room_id}
    )


def check_out(reservation_id, room_id):
    requests.post(
        f"{RESERVATION_SERVICE}/checkout",
        json={"reservation_id": reservation_id, "room_id": room_id}
    )
