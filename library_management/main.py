import tkinter as tk
from tkinter import ttk
from library_managment import Book, User, Library
from data import users
import uuid


manager = Library()


for user in users:
    id = uuid.uuid4()
    for key, value in user.items():
        name = key
    email = user[name]["email"]
    password = user[name]["password"]
    manager.users[id] = User(id, name, email, password)
    
# clear login frame
def clear():
    widgets = root.grid_slaves()
    for item in widgets:
        item.destroy()

def check():
    if manager.verify_user(name.get(), password.get()):
        clear()
        main_view()
    else:
        print("wrong pass or there is not user")



root = tk.Tk()
root.title("Library Management System")
root.columnconfigure(0, weight=1)
root.geometry("1000x500")
def login_view():
    frame = ttk.Frame(root).grid(row=0, column=0)
    text_name = ttk.Label(frame, text="Enter your name")
    text_name.grid(row=0, column=0)
    global name
    name = tk.StringVar()
    name_input = ttk.Entry(frame, textvariable=name)
    name_input.grid(row=0, column=1)
    text_pass = ttk.Label(frame, text="Enter your password")
    text_pass.grid(row=1, column=0)
    global password
    password = tk.StringVar()
    pass_input = ttk.Entry(frame, textvariable=password)
    pass_input.grid(row=1, column=1)
    btn_frame = ttk.Frame(root)
    btn_frame.grid(row=2, column=0)
    btn_login = ttk.Button(btn_frame, text="Login", command = check)
    btn_login.grid(row=2, column=0)
    btn_register = ttk.Button(btn_frame, text="register")
    btn_register.grid(row=2, column=1)
    
    
login_view()

def main_view():
    frame = ttk.Frame(root).grid(row=0, column=0)
    search_btn = ttk.Button(frame, text="search")
    search_btn.grid(row=0, column=0)
    search_text = tk.StringVar()
    search_input = ttk.Entry(frame, textvariable=search_text)
    search_input.grid(row=0, column=1)

root.mainloop()