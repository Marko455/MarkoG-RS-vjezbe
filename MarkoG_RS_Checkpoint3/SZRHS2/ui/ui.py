import tkinter as tk
from tkinter import messagebox
import api

root = tk.Tk()
root.title("Hotel Reception System")
root.geometry("520x650")
root.configure(bg="#f4f4f4")

FONT_TITLE = ("Arial", 14, "bold")
FONT_LABEL = ("Arial", 10)
FONT_ENTRY = ("Arial", 10)


def section(parent, title):
    frame = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid", padx=10, pady=10)
    tk.Label(frame, text=title, font=FONT_TITLE, bg="#ffffff").pack(anchor="w", pady=(0, 8))
    frame.pack(fill="x", padx=15, pady=10)
    return frame

guest_frame = section(root, "Dodaj gosta")

tk.Label(guest_frame, text="Ime", font=FONT_LABEL, bg="#ffffff").pack(anchor="w")
guest_name = tk.Entry(guest_frame, font=FONT_ENTRY)
guest_name.pack(fill="x", pady=3)

tk.Label(guest_frame, text="Email", font=FONT_LABEL, bg="#ffffff").pack(anchor="w")
guest_email = tk.Entry(guest_frame, font=FONT_ENTRY)
guest_email.pack(fill="x", pady=3)

def add_guest():
    res = api.add_guest(guest_name.get(), guest_email.get())
    messagebox.showinfo("Gost dodan", f"ID gosta: {res['guest_id']}")

tk.Button(guest_frame, text="Dodaj gosta", command=add_guest).pack(pady=6)



room_frame = section(root, "Dodaj sobu")

tk.Label(room_frame, text="Broj sobe", font=FONT_LABEL, bg="#ffffff").pack(anchor="w")
room_number = tk.Entry(room_frame, font=FONT_ENTRY)
room_number.pack(fill="x", pady=3)

tk.Label(room_frame, text="Vrsta sobe", font=FONT_LABEL, bg="#ffffff").pack(anchor="w")
room_type = tk.Entry(room_frame, font=FONT_ENTRY)
room_type.pack(fill="x", pady=3)

tk.Label(room_frame, text="Cijena", font=FONT_LABEL, bg="#ffffff").pack(anchor="w")
room_price = tk.Entry(room_frame, font=FONT_ENTRY)
room_price.pack(fill="x", pady=3)

def add_room():
    api.add_room(room_number.get(), room_type.get(), float(room_price.get()))
    messagebox.showinfo("Uspijeh", "Soba dodana")

tk.Button(room_frame, text="Dodaj sobu", command=add_room).pack(pady=6)


rooms_frame = section(root, "Sobe")

room_list = tk.Listbox(rooms_frame, width=60, height=6)
room_list.pack(fill="x", pady=5)

def refresh_rooms():
    room_list.delete(0, tk.END)
    for r in api.get_rooms():
        status = "Slobodno" if r["available"] else "Zauzeto"
        room_list.insert(tk.END, f"ID {r['id']} | Room {r['number']} | {status}")

tk.Button(rooms_frame, text="Osvjezi sobe", command=refresh_rooms).pack(pady=5)


checkin_frame = section(root, "Check in")

ci_guest = tk.Entry(checkin_frame, font=FONT_ENTRY)
ci_guest.insert(0, "ID gosta")
ci_guest.pack(fill="x", pady=3)

ci_room = tk.Entry(checkin_frame, font=FONT_ENTRY)
ci_room.insert(0, "ID sobe")
ci_room.pack(fill="x", pady=3)

def check_in():
    api.check_in(int(ci_guest.get()), int(ci_room.get()))
    messagebox.showinfo("Check in", "Gost checked in")
    refresh_rooms()

tk.Button(checkin_frame, text="Check In", command=check_in).pack(pady=6)



checkout_frame = section(root, "Check out")

co_res = tk.Entry(checkout_frame, font=FONT_ENTRY)
co_res.insert(0, "ID rezervacije")
co_res.pack(fill="x", pady=3)

co_room = tk.Entry(checkout_frame, font=FONT_ENTRY)
co_room.insert(0, "ID sobe")
co_room.pack(fill="x", pady=3)

def check_out():
    api.check_out(int(co_res.get()), int(co_room.get()))
    messagebox.showinfo("Check-out", "Gost checked out")
    refresh_rooms()

tk.Button(checkout_frame, text="Check Out", command=check_out).pack(pady=6)


root.mainloop()
