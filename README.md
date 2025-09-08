Flight Reservation App

A desktop application built with Python, Tkinter, and SQLite that allows users to book, view, edit, and delete flight reservations.

This project was developed as a learning project to demonstrate GUI development, database integration, and CRUD operations in Python.

🚀 Features

📝 Book a Flight – Add new reservations with passenger and flight details.

📋 View Reservations – Display all reservations in a clean, tabular format.

✏️ Edit Reservations – Update existing reservation details.

🗑 Delete Reservations – Remove reservations with a single click.

💾 SQLite Database – Lightweight database with persistent storage.

🎨 Modern UI – Styled Tkinter interface inspired by professional booking apps.

🛠️ Technologies Used

Python 3

Tkinter (GUI)

SQLite3 (database)

PyInstaller (to export .exe)

Git/GitHub (version control)

📂 Project Structure
flight_reservation_app/
│── main.py              # Main application entry point
│── database.py          # Database setup & queries (SQLite)
│── home.py              # Home Page UI
│── booking.py           # Flight Booking Page
│── reservations.py      # Reservations List Page
│── edit_reservation.py  # Edit Reservation Page
│── flights.db           # SQLite database file (auto-created)
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation
│── .gitignore           # Ignore cache and build files

▶️ Getting Started
1. Clone the repository
git clone https://github.com/mohamedghareeb9/flight_reservation_app.git
cd flight_reservation_app

2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python main.py

📦 Export to EXE (Windows)

You can package the app into a .exe file using PyInstaller:

Install PyInstaller:

pip install pyinstaller


Build the executable:

pyinstaller --onefile main.py


The .exe will be generated inside the dist/ folder.

📸 Sample UI

✨ Clean and modern Tkinter interface with easy navigation between pages.


📜 License

This project is licensed under the MIT License – free to use and modify.
