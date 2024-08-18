import uuid

class Book:
    def __init__(self, title, author, uni_id):
        self.title = title
        self.author = author
        self.uni_id = uni_id
        self.is_borrowed = False
        self.borrowed_by = None

    def __str__(self):
        borrowed_status = f"Yes, by {self.borrowed_by}" if self.borrowed_by else "no"
        return(f"Title: {self.title}, "
               f"Author: {self.author}, "
               f"BookID: {self.uni_id}, "
               f"Borrowed: {borrowed_status}")
    
class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.email = email
        self.borrowed_books = []

    def __str__(self):
        return f"User Id: {self.user_id}, Name: {self.name}, Email: {self.email}, Password: {self.password}"

    

class Library:
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"book {book.title} added to the library.")

    def list_books(self):
        if not self.books:
            print("no such books in the library")
        for book in self.books:
            print(book)


    def borrow_book(self, uni_id, user_id):
        if user_id not in self.users:
            print("user does not exist")
            return
        for book in self.books:
            if book.uni_id == uni_id and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = user_id
                self.users[user_id].borrowed_books.append(book.uni_id)
                print(f"User {self.users[user_id].name} has borrowed {book.title}.")
                return 
        print("Book not available")

    # def borrow_book(self, uni_id):
    #     for book in self.books:
    #         if book.uni_id == uni_id and not book.is_borrowed:
    #             book.is_borrowed = True
    #             print(f"you have borrowed: {book.title}.")
    #             return
    #     print("Book is not available. or has been borrowed")
        
    def return_book(self, uni_id, user_id):
        for book in self.books:
            if book.uni_id == uni_id and book.is_borrowed and book.borrowed_by == user_id:
                book.is_borrowed = False
                book.borrowed_by = None
                print(f"user {self.users[user_id].name} has returned: {book.title}")
                return
        print("Book is not available. Or has not been borrowed")

    def add_user(self, user):
        if user.user_id in self.users:
            print(f"User Id {user.user_id} already exist")
            return
        self.users[user.user_id] = user
        print(f"User {user.name} added with ID {user.user_id}.")

    def verify_user(self, input_name, input_password):
        for id,user in self.users.items():
            if not user.name == input_name:
                print("not exist")
                return False
            if user.password == input_password:
                return True
            else:
                print("wrong pass")
                return False

    def is_exist(self, user_input):
        for book in self.books:
            if user_input.get() == book.title:
                return True
            else:
                return False

    
    def list_users(self):
        if not self.users:
            print("No users registered.")
            return
        for user in self.users:
            obj = self.users[user]
            print(obj)

    def update_user(self, user_id, name=None, email=None):
        if user_id not in self.users:
            print("User not found")
            return
        if name:
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
        print(f"User {user_id} updated.")

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} deleted.")
        else:
            print('user not found')

# book1 = Book("Python Crash Course", "Eric Matthes", uuid.uuid4())
# book2 = Book("Automate the boring stuff with python", "Al swetgart", "1593279922")
# book3 = Book("Effective Java", "Joshua Bloch", "0134685997")
# book4 = Book("The pragmatic programmer", "Andrew Hunt and David thomas", "0135957052")

# print(book1)


# library = Library()

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# library.add_book(book4)

    
# library.add_user(User("001", "mehdi", "mehdip.m909@gmail.com"))
# library.add_user(User("002", "hamed", "hamed@gmail.com"))

# library.list_users()

# library.update_user("002", "Fazel", "fazel@gmail.com")

# library.list_users()

# print()

# library.delete_user("002")

# library.list_users()
