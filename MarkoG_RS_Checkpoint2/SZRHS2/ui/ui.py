import tkinter as tk
from tkinter import messagebox
import api

root = tk.Tk()
root.title("Hotel Reception System")
root.geometry("500x600")

# --- Add Guest ---
tk.Label(root, text="Add Guest", font=("Arial", 14)).pack()

guest_name = tk.Entry(root)
guest_name.pack()

guest_email = tk.Entry(root)
guest_email.pack()

def add_guest():
    res = api.add_guest(guest_name.get(), guest_email.get())
    messagebox.showinfo("Guest Added", f"Guest ID: {res['guest_id']}")

tk.Button(root, text="Add Guest", command=add_guest).pack(pady=5)


# --- Add Room ---
tk.Label(root, text="Add Room", font=("Arial", 14)).pack()

room_number = tk.Entry(root)
room_number.pack()

room_type = tk.Entry(root)
room_type.pack()

room_price = tk.Entry(root)
room_price.pack()

def add_room():
    api.add_room(room_number.get(), room_type.get(), float(room_price.get()))
    messagebox.showinfo("Success", "Room added")

tk.Button(root, text="Add Room", command=add_room).pack(pady=5)


# --- Rooms List ---
tk.Label(root, text="Rooms", font=("Arial", 14)).pack()

room_list = tk.Listbox(root, width=60)
room_list.pack()

def refresh_rooms():
    room_list.delete(0, tk.END)
    for r in api.get_rooms():
        status = "Available" if r["available"] else "Occupied"
        room_list.insert(tk.END, f"ID {r['id']} | Room {r['number']} | {status}")

tk.Button(root, text="Refresh Rooms", command=refresh_rooms).pack(pady=5)


# --- Check-in ---
tk.Label(root, text="Check-in", font=("Arial", 14)).pack()

ci_guest = tk.Entry(root)
ci_guest.insert(0, "Guest ID")
ci_guest.pack()

ci_room = tk.Entry(root)
ci_room.insert(0, "Room ID")
ci_room.pack()

def check_in():
    api.check_in(int(ci_guest.get()), int(ci_room.get()))
    messagebox.showinfo("Check-in", "Guest checked in")
    refresh_rooms()

tk.Button(root, text="Check In", command=check_in).pack(pady=5)


# --- Check-out ---
tk.Label(root, text="Check-out", font=("Arial", 14)).pack()

co_res = tk.Entry(root)
co_res.insert(0, "Reservation ID")
co_res.pack()

co_room = tk.Entry(root)
co_room.insert(0, "Room ID")
co_room.pack()

def check_out():
    api.check_out(int(co_res.get()), int(co_room.get()))
    messagebox.showinfo("Check-out", "Guest checked out")
    refresh_rooms()

tk.Button(root, text="Check Out", command=check_out).pack(pady=5)

root.mainloop()
