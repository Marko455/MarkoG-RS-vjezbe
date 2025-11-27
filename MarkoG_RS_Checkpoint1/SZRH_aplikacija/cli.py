# gui.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from data.models import ispis, HotelRoom
from data.storage import (
    ispisi_sve_sobe,
    pronadi_sobu,
    izradi_rezervaciju,
    zatvori_rezervaciju,
    oslobodi_sobu,
    ispis_povijesti_rez,
    init_db,
    unesi_sobu,
)

# --------------------- initial rooms setup ---------------------
def seed_rooms():
    rooms = [
        HotelRoom(101, "Single", 120),
        HotelRoom(102, "Double", 150),
        HotelRoom(103, "Double", 160),
        HotelRoom(201, "Suite", 260),
    ]
    for r in rooms:
        unesi_sobu(r)


# --------------------- GUI Core ---------------------

class HotelGUI:
    def __init__(self, root):
        self.root = root
        root.title("Hotelski sistem rezervacija soba")
        root.geometry("520x400")

        self.build_ui()
        self.load_rooms()

    def build_ui(self):
        # Frame
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        # Table
        self.tree = ttk.Treeview(frame, columns=("type", "price", "status"), show="headings")
        self.tree.heading("type", text="Tip sobe")
        self.tree.heading("price", text="Cijena")
        self.tree.heading("status", text="Dostupnost")
        self.tree.column("type", width=130)
        self.tree.column("price", width=90)
        self.tree.column("status", width=120)
        self.tree.pack(fill="both", expand=True)

        # Buttons
        btns = ttk.Frame(frame)
        btns.pack(pady=10)

        ttk.Button(btns, text="Rezerviraj", command=self.book_room).grid(row=0, column=0, padx=4)
        ttk.Button(btns, text="Oslobodi", command=self.release_room).grid(row=0, column=1, padx=4)
        ttk.Button(btns, text="Osvjezi", command=self.load_rooms).grid(row=0, column=2, padx=4)
        ttk.Button(btns, text="Povijest", command=self.show_history).grid(row=0, column=3, padx=4)
        ttk.Button(btns, text="Filtriraj", command=self.filter_dialog).grid(row=0, column=4, padx=4)

    # ----------------- functions ------------------

    def load_rooms(self, filter_fn=None):
        rooms = ispisi_sve_sobe()
        if filter_fn:
            rooms = list(filter(filter_fn, rooms))

        self.tree.delete(*self.tree.get_children())

        for r in rooms:
            status = "Slobodno" if r.is_available else "Rezervirano"
            self.tree.insert("", "end", iid=r.room_number, values=(r.room_type, r.price_per_night, status))

    def get_selected_room(self):
        selected = self.tree.focus()
        if not selected:
            return None
        return pronadi_sobu(int(selected))

    def book_room(self):
        room = self.get_selected_room()

        if not room:
            messagebox.showwarning("Izaberite sobu", "Prvo izaberite sobu.")
            return

        if not room.is_available:
            messagebox.showerror("Zauzeta", "Soba je vec rezervirana.")
            return

        guest = simpledialog.askstring("Ime gosta", "Unesite ime gosta:")
        if not guest:
            return

        izradi_rezervaciju(room.room_number, guest)
        oslobodi_sobu(room.room_number, False)
        self.load_rooms()
        messagebox.showinfo("Rezervirano", f"Soba {room.room_number} rezervirana za {guest}")

    def release_room(self):
        room = self.get_selected_room()

        if not room:
            messagebox.showwarning("Izaberite sobu", "Prvo izaberite sobu.")
            return

        if room.is_available:
            messagebox.showerror("Vec oslobodena", "Soba je vec oslobodena.")
            return

        zatvori_rezervaciju(room.room_number)
        oslobodi_sobu(room.room_number, True)
        self.load_rooms()
        messagebox.showinfo("Oslobodena", f"Soba {room.room_number} je oslobodena")

    def show_history(self):
        history = ispis_povijesti_rez()
        if not history:
            messagebox.showinfo("Povijest", "Jos nema rezervacija.")
            return

        txt = ""
        for r in history:
            txt += (
                f"ID {r.reservation_id} | Soba {r.room_number} | Gost {r.guest_name}\n"
                f"Check-in: {r.check_in}\n"
                f"Check-out: {r.check_out}\n\n"
            )
        messagebox.showinfo("Povijest rezervacija", txt)

    def filter_dialog(self):
        win = tk.Toplevel(self.root)
        win.title("Filtrirajte sobe")
        win.geometry("300x200")

        def apply():
            t = type_var.get()
            maxp = price_var.get()

            def fn(r):
                ok = True
                if t != "":
                    ok &= r.room_type == t
                if maxp:
                    ok &= r.price_per_night <= float(maxp)
                return ok

            self.load_rooms(filter_fn=fn)
            win.destroy()

        type_var = tk.StringVar()
        price_var = tk.StringVar()

        ttk.Label(win, text="Tip sobe:").pack()
        ttk.Entry(win, textvariable=type_var).pack()

        ttk.Label(win, text="Maksimalna cijena:").pack()
        ttk.Entry(win, textvariable=price_var).pack()

        ttk.Button(win, text="Primijeni filtre", command=apply).pack(pady=8)


# ------------------ run ------------------
if __name__ == "__main__":
    init_db()
    seed_rooms()

    root = tk.Tk()
    HotelGUI(root)
    root.mainloop()
