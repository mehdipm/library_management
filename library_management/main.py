import tkinter as tk
from tkinter import ttk
from library_managment import Book, User, Library
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


    
# clear login frame
def clear():
    widgets = root.grid_slaves()
    for item in widgets:
        item.destroy()
    
def check(user_name, user_pass):
    if manager.verify_user(user_name.get(), user_pass.get()):
        clear()
        for key, value in manager.users.items():
            if value.name == user_name.get():
                global entered_id
                entered_id = key
        main_view()
        for book in manager.books:
            if book.title == book_given.get():
                id = book.uni_id
        show_return_book()
        
    else:
        print("wrong pass or there is not user")
        return


    
def search_successfull():
    for book in manager.books:
        if search_text.get() == book.title:
            show_borrow(book.uni_id)
            return True
        else:
            # TODO message for not exist
            pass



def login_view():
    frame = ttk.Frame(root).grid(row=0, column=0)
    text_name = ttk.Label(frame, text="Enter your name")
    text_name.grid(row=0, column=0)
    name = tk.StringVar()
    name_input = ttk.Entry(frame, textvariable=name)
    name_input.grid(row=0, column=1)
    text_pass = ttk.Label(frame, text="Enter your password")
    text_pass.grid(row=1, column=0)
    password = tk.StringVar()
    pass_input = ttk.Entry(frame, textvariable=password)
    pass_input.grid(row=1, column=1)
    btn_frame = ttk.Frame(root)
    btn_frame.grid(row=2, column=0)
    btn_login = ttk.Button(btn_frame, text="Login", command =lambda: check(name, password))
    btn_login.grid(row=2, column=0)
    btn_register = ttk.Button(btn_frame, text="register")
    btn_register.grid(row=2, column=1)
    return (name, password)
    
    
def main_view():
    frame = ttk.Frame(root).grid(row=0, column=0)
    search_btn = ttk.Button(frame, text="search", command=search_successfull)
    search_btn.grid(row=0, column=0)
    global search_text
    search_text = tk.StringVar()
    search_input = ttk.Entry(frame, textvariable=search_text)
    search_input.grid(row=0, column=1)


def show_borrow(book_id):
    frame = ttk.Frame(root)
    frame.grid(row=1, column=0)
    btn = ttk.Button(frame, text="borrow", command=lambda: manager.borrow_book(book_id, entered_id))
    btn.grid(row=2)

def show_return_book(book_id, user_id):
    frame= ttk.Frame(root)
    frame.grid(row=3, column=0)
    global book_given
    book_given = tk.StringVar()
    lib_book = ttk.Entry(frame, textvariable=book_given)
    lib_book.grid(row=0, column=0)
    btn = ttk.Button(frame, text="return book", command=manager.return_book(book_id, user_id))
    btn.grid(row=1, column=0)

root = tk.Tk()
root.title("Library Management System")
root.columnconfigure(0, weight=1)
root.geometry("1000x500")
user_info = login_view()
root.mainloop()