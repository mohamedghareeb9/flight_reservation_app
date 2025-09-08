import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import database

class EditReservationPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.res_id = None

        card = ttk.Labelframe(self, text="✏ Edit Reservation", padding=20, bootstyle="warning")
        card.pack(pady=40, padx=40, fill="x")

        labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(card, text=label, font=("Segoe UI", 12)).grid(row=i, column=0, pady=10, sticky="w")
            entry = ttk.Entry(card, font=("Segoe UI", 11))
            entry.grid(row=i, column=1, pady=10, padx=10, sticky="ew")
            self.entries[label] = entry

        card.columnconfigure(1, weight=1)

        btn_frame = ttk.Frame(card)
        btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=20)

        ttk.Button(btn_frame, text="💾 Update", bootstyle="success-outline", width=18,
                   command=self.update_reservation).pack(side="left", padx=15)
        ttk.Button(btn_frame, text="⬅ Back", bootstyle="secondary-outline", width=18,
                   command=lambda: controller.show_frame("ReservationsPage")).pack(side="left", padx=15)

    def load_reservation(self, res_id):
        self.res_id = res_id
        reservation = database.get_reservation(res_id)
        if reservation:
            values = reservation[1:]
            for entry, val in zip(self.entries.values(), values):
                entry.delete(0, "end")
                entry.insert(0, val)

    def update_reservation(self):
        values = [e.get() for e in self.entries.values()]
        if all(values):
            database.update_reservation(self.res_id, *values)
            messagebox.showinfo("Updated", "Reservation updated successfully!")
            self.controller.show_frame("ReservationsPage")
        else:
            messagebox.showwarning("Input Error", "⚠ All fields are required")
