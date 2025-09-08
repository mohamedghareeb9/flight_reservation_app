import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class App(ttk.Window):
    def __init__(self):
        super().__init__(title="✈ Flight Reservation System", themename="cosmo")
        self.geometry("1000x650")

        database.init_db()

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True, padx=15, pady=15)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name, *args):
        frame = self.frames[page_name]
        if page_name == "ReservationsPage":
            frame.refresh()
        elif page_name == "EditReservationPage":
            frame.load_reservation(*args)
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
