import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        title = ttk.Label(self, text="✈ Flight Reservation System", font=("Segoe UI", 22, "bold"))
        title.pack(pady=40)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20)

        ttk.Button(btn_frame, text="📖 Book Flight", bootstyle="success", width=20,
                   command=lambda: controller.show_frame("BookingPage")).grid(row=0, column=0, padx=20, pady=15)

        ttk.Button(btn_frame, text="📑 View Reservations", bootstyle="info", width=20,
                   command=lambda: controller.show_frame("ReservationsPage")).grid(row=1, column=0, padx=20, pady=15)
