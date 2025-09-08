import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import database
from tkinter import messagebox

class ReservationsPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = ttk.Label(self, text="📑 Reservations List", font=("Segoe UI", 18, "bold"))
        title.pack(pady=20)

        style = ttk.Style()
        style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)

        self.tree = ttk.Treeview(
            self,
            columns=("id","name","flight","from","to","date","seat"),
            show="headings",
            bootstyle="info"
        )
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        headings = ["ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for col, text in zip(self.tree["columns"], headings):
            self.tree.heading(col, text=text)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=15)

        ttk.Button(btn_frame, text="✏ Edit", bootstyle="warning-outline", width=15,
                   command=self.edit_reservation).grid(row=0, column=0, padx=15)
        ttk.Button(btn_frame, text="🗑 Delete", bootstyle="danger-outline", width=15,
                   command=self.delete_reservation).grid(row=0, column=1, padx=15)
        ttk.Button(btn_frame, text="⬅ Back", bootstyle="secondary-outline", width=15,
                   command=lambda: controller.show_frame("HomePage")).grid(row=0, column=2, padx=15)

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for res in database.get_reservations():
            self.tree.insert("", "end", values=res)

    def edit_reservation(self):
        selected = self.tree.selection()
        if selected:
            res_id = self.tree.item(selected[0])["values"][0]
            self.controller.show_frame("EditReservationPage", res_id)

    def delete_reservation(self):
        selected = self.tree.selection()
        if selected:
            res_id = self.tree.item(selected[0])["values"][0]
            database.delete_reservation(res_id)
            self.refresh()
            messagebox.showinfo("Deleted", "Reservation removed successfully.")
