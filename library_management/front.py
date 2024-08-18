import tkinter as tk
from tkinter import ttk
from library_management import Book, User, Library
from data import users, books
import uuid


manager = Library()

for user in users:
    id = uuid.uuid4()
    for key, value in user.items():
        name = key
    email = user[name]["email"]
    password = user[name]["password"]
    manager.users[id] = User(id, name, email, password)

for book in books:
    for key, value in book.items():
        title = key
        author = value["author"]
    id = uuid.uuid4()
    manager.books.append(Book(title, author, id))


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management")
        self.frames = {}

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky="EW")

        log_in_frame = UserLoginFrame(container, self)
        log_in_frame.grid(row=0, column=0)

        main_frame = MainView(container)
        main_frame.grid(row=0, column=0)
        main_frame.columnconfigure(0, weight=1)

        log_in_frame.tkraise()

        self.frames[UserLoginFrame] = log_in_frame
        self.frames[MainView] = main_frame
        
            
    def show_frame(self, container, u_name, u_password):
        if manager.verify_user(u_name.get(), u_password.get()):
            login_frame = self.frames[UserLoginFrame]
            login_frame.destroy()
            frame = self.frames[container]
            frame.tkraise()
        else:
            print("wrong pass or there is not user")
            return


class UserLoginFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.password = tk.StringVar()
        self.name = tk.StringVar()

        text_name = ttk.Label(self, text="Enter your name")
        text_name.grid(row=0, column=0)
        name_input = ttk.Entry(self, textvariable=self.name)
        name_input.grid(row=0, column=1)
        text_pass = ttk.Label(self, text="Enter your password")
        text_pass.grid(row=1, column=0)
        pass_input = ttk.Entry(self, textvariable=self.password)
        pass_input.grid(row=1, column=1)
        btn_login = ttk.Button(self, text="Login", command =lambda: controller.show_frame(MainView, self.name, self.password))
        btn_login.grid(row=2, column=0)
        btn_register = ttk.Button(self, text="register")
        btn_register.grid(row=2, column=1)


class MainView(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.search_text = tk.StringVar()
        search_btn = ttk.Button(self, text="search", )
        search_btn.grid(row=0, column=0)
        search_input = ttk.Entry(self, textvariable=self.search_text)
        search_input.grid(row=0, column=1)

window = Window()
window.mainloop()
