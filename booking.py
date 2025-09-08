import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import database

class BookingPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        card = ttk.Labelframe(self, text="✈ Book Your Flight", padding=20, bootstyle="primary")
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

        ttk.Button(btn_frame, text="✅ Submit", bootstyle="success-outline", width=18,
                   command=self.book_flight).pack(side="left", padx=15)
        ttk.Button(btn_frame, text="⬅ Back", bootstyle="secondary-outline", width=18,
                   command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=15)

    def book_flight(self):
        values = [e.get() for e in self.entries.values()]
        if all(values):
            database.add_reservation(*values)
            messagebox.showinfo("Success", "🎉 Flight booked successfully!")
            for entry in self.entries.values():
                entry.delete(0, "end")
        else:
            messagebox.showwarning("Input Error", "⚠ All fields are required")
