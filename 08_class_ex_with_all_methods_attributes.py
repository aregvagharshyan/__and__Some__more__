### Here is some examples with all attributes and methods ###

# Create a Vehicle Class
# Requirements:
# Class Attributes:
# total_vehicles (tracks the total number of Vehicle instances).
# Instance Attributes (self attributes):
# brand (brand name of the vehicle).
# model (model name).
# year (year of manufacture).
# Instance Methods (self methods):
# info() – returns a string containing the vehicle's details.
# Class Methods:
# get_total_vehicles() – returns the total number of created vehicles.
# Static Methods:
# is_vintage(year) – returns True if the vehicle is older than 25 years, otherwise False

class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Vehicle.total_vehicles += 1

    def info(self):
        return f'Vehicle details: brand - {self.brand}, model - {self.model}, year - {self.year}'

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @staticmethod
    def is_vintage(year):
        return 2025 - year > 25

car_1 = Vehicle('Toyota', 'Corolla', 2002)
car_2 = Vehicle('Opel', 'Vectra', 1993)
print(car_1.info())
print(car_2.info())
print(Vehicle.get_total_vehicles())
print(Vehicle.is_vintage(1993))

# Create a BankAccount Class
# Requirements:
# Class Attributes:
# total_accounts (keeps track of the total number of accounts created).
# Instance Attributes (self attributes):
# owner (account owner's name).
# balance (current balance, default is 0).
# Instance Methods (self methods):
# deposit(amount) – adds money to the balance.
# withdraw(amount) – subtracts money if there are sufficient funds, otherwise prints an error.
# get_balance() – returns the current balance.
# Class Methods:
# get_total_accounts() – returns the total number of created bank accounts.
# Static Methods:
# is_valid_amount(amount) – returns True if the amount is positive, otherwise False

class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        BankAccount.total_accounts += 1
    def deposit(self, amount):

        self.balance += amount
        return self.balance
    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance += amount
            return self.balance
        return f'Not enough balance'

    def get_balance(self):
        return self.balance

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

person_1 = BankAccount('Areg', 2500)
person_2 = BankAccount('Mels', 1500)
person_1.deposit(250)
person_1.withdraw(100)
print(BankAccount.get_total_accounts())
print(BankAccount.is_valid_amount(-1000))

# Create a Library Class
# Requirements:
# Class Attributes:
# total_books (tracks the total number of books in the library).
# Instance Attributes (self attributes):
# name (library name).
# books (a dictionary where keys are book titles and values are quantities).
# Instance Methods (self methods):
# add_book(title, quantity) – adds books to the library and updates total_books.
# borrow_book(title) – reduces the quantity if available, otherwise prints "Book not available".
# get_books() – returns a list of available books.
# Class Methods:
# get_total_books() – returns the total number of books across all libraries.
# Static Methods:
# is_valid_book_title(title) – returns True if the title is a non-empty string, otherwise False

class Library:
    total_books = 0

    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, title, quantity):
        if Library.is_valid_book_title(title) and quantity > 0:
            self.books[title] = quantity
            Library.total_books += quantity

    def borrow_book(self, title):
        if title in self.books and self.books[title] > 0:
            self.books[title] -= 1
            Library.total_books -= 1
            return f'The {title} book is borrowed'
        return f'Book not available'

    def get_books(self):
        return list(self.books.keys())

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    @staticmethod
    def is_valid_book_title(title):
        return title != ''

lib1 = Library("City Library")
lib2 = Library("Community Library")
lib1.add_book("Python Programming", 5)
lib1.add_book("Data Science", 3)
lib2.add_book("Machine Learning", 4)
lib2.add_book("Deep Learning", 2)
print(lib1.borrow_book("Python Programming"))
print(lib2.borrow_book("Machine Learning"))
print("Books in City Library:", lib1.get_books())
print("Books in Community Library:", lib2.get_books())
print("Total books in all libraries:", Library.get_total_books())
print("Is 'AI Basics' a valid title?", Library.is_valid_book_title("AI Basics"))
print("Is '' a valid title?", Library.is_valid_book_title(""))

# Create a Restaurant Class
# Requirements:
# Class Attributes:
# total_restaurants (keeps track of the total number of restaurants created).
# Instance Attributes (self attributes):
# name (restaurant name).
# menu (a dictionary where keys are dish names and values are their prices).
# Instance Methods (self methods):
# add_dish(dish, price) – adds a dish to the menu.
# update_price(dish, new_price) – updates the price of a dish if it exists.
# get_menu() – returns the restaurant's menu as a dictionary.
# order(dish) – returns the price if available, otherwise prints "Dish not available".
# Class Methods:
# get_total_restaurants() – returns the total number of restaurants created.
# Static Methods:
# is_valid_dish_name(dish) – returns True if the dish name is a non-empty string, otherwise False

class Restaurant:
    total_restaurants = 0

    def __init__(self, name):
        self.name = name
        self.menu = {}
        Restaurant.total_restaurants += 1

    def add_dish(self, dish, price):
        if Restaurant.is_valid_dish_name(dish) and price > 0:
            self.menu[dish] = price
            return f'{dish} was added:'
        return f'Not valid dish or price!'

    def update_price(self, dish, new_price):
        if dish in self.menu:
            self.menu[dish] = new_price
            return f'{dish} was updated:'
        return f'{dish} is not in menu!'

    def get_menu(self):
        return self.menu

    def order(self, dish):
        self.menu.get(dish, "Dish not available.")

    @classmethod
    def get_total_restaurants(cls):
        return cls.total_restaurants

    @staticmethod
    def is_valid_dish_name(dish):
        return dish != ''

restaurant1 = Restaurant('Kacin')
restaurant2 = Restaurant('Opera')
restaurant1.add_dish("Pasta", 12.99)
restaurant1.add_dish("Burger", 8.99)
restaurant2.add_dish("Pizza", 10.99)
restaurant2.add_dish("Salad", 6.99)
restaurant1.update_price("Pasta", 14.99)
print("Menu of Gourmet Delights:", restaurant1.get_menu())
print("Menu of Quick Bites:", restaurant2.get_menu())
print("Ordering Pasta:", restaurant1.order("Pasta"))
print("Ordering Sushi:", restaurant2.order("Sushi"))
print("Total restaurants:", Restaurant.get_total_restaurants())
print("Is 'Steak' a valid dish name?", Restaurant.is_valid_dish_name("Steak"))
print("Is '' a valid dish name?", Restaurant.is_valid_dish_name(""))

# Create a Library class with the following functionalities:
# A class attribute total_libraries to track the number of library instances.
# An __init__ method that initializes the library's name and an empty dictionary books (where keys are book titles and values are availability as True/False).
# An add_book(book_name) method that adds a book to the library (if it is a valid name).
# A borrow_book(book_name) method that marks a book as borrowed (False) if available.
# A return_book(book_name) method that marks the book as available (True).
# A get_books() method that returns the library's book collection.
# A get_total_libraries() class method that returns the number of libraries.
# A static method is_valid_book_name(book_name) that ensures the name is not an empty string

class Library:
    total_libraries = 0

    def __init__(self, name):
        self.name = name
        self.books ={}
        Library.total_libraries += 1

    def add_book(self, book_name):
        if Library.is_valid_book_name(book_name):
            self.books[book_name] = True
            return f'{book_name} was added.'
        return f'Valid name!'

    def borrow_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name] is True:
                self.books[book_name] = False
                return f'{book_name} is borrowed.'
            return f'{book_name} was already borrowed.'
        return f"{book_name} isn't in Library!"

    def return_book(self, book_name):
        if book_name in self.books:
            if self.books[book_name] is False:
                self.books[book_name] = True
                return f'{book_name} is returned.'
            return f'{book_name} was already returned.'
        return f'{book_name} isn\'t in Library'

    def get_books(self):
        return list(self.books.keys())

    @classmethod
    def get_total_libraries(cls):
        return cls.total_libraries

    @staticmethod
    def is_valid_book_name(book_name):
        return book_name != ''

library1 = Library("Central Library")
library2 = Library("City Library")
library1.add_book("Harry Potter")
library1.add_book("The Hobbit")
library2.add_book("1984")
library2.add_book("To Kill a Mockingbird")
library1.borrow_book("Harry Potter")
library2.borrow_book("1984")
library1.return_book("Harry Potter")
library2.return_book("1984")
print("Books in Central Library:", library1.get_books())
print("Books in City Library:", library2.get_books())
print("Is 'Pride and Prejudice' a valid book name?", Library.is_valid_book_name("Pride and Prejudice"))
print("Is '' a valid book name?", Library.is_valid_book_name(""))
print("Total libraries:", Library.get_total_libraries())

# Create a BankAccount class with the following features:
# A class attribute total_accounts to track the number of accounts.
# An __init__ method that initializes the account holder's name, balance, and a unique account number.
# A deposit(amount) method to add money to the account.
# A withdraw(amount) method to withdraw money if there are sufficient funds.
# A get_balance() method to return the account balance.
# A class method get_total_accounts() to return the total number of accounts.
# A static method is_valid_amount(amount) that checks if the amount is positive.

class BankAccount:
    total_accounts = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return f'Not enough balance!'

    def get_balance(self):
        return self.balance

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)
account1.deposit(200)
account2.deposit(100)
account1.withdraw(500)
account2.withdraw(200)
print(f"Alice's balance: {account1.get_balance()}")
print(f"Bob's balance: {account2.get_balance()}")
print("Is 500 a valid amount?", BankAccount.is_valid_amount(500))
print("Is -100 a valid amount?", BankAccount.is_valid_amount(-100))
print("Total accounts:", BankAccount.get_total_accounts())

# Create a MovieTheater class with these functionalities:
# A class attribute total_theaters to track the number of theaters.
# An __init__ method that initializes the theater name and an empty dictionary movies (where keys are movie titles and values are the number of available seats).
# An add_movie(movie_name, seats) method to add a movie with available seats.
# A book_ticket(movie_name, num_tickets) method to book tickets if enough seats are available.
# A get_movies() method that returns all movies and available seats.
# A class method get_total_theaters() to return the total number of theaters.
# A static method is_valid_movie_name(movie_name) that ensures the name is not empty.

class MovieTheater:
    total_theaters = 0

    def __init__(self, name):
        self.name = name
        self.theater = {}
        MovieTheater.total_theaters += 1

    def add_movie(self, movie_name, seats):
        if MovieTheater.is_valid_movie_name(movie_name) and seats > 0:
            self.theater[movie_name] = seats
            return f'{movie_name} is added.'
        return f'Invalid name or no seats!'

    def book_ticket(self, movie_name, num_tickets):
        if MovieTheater.is_valid_movie_name(movie_name):
            if self.theater[movie_name] > num_tickets:
                self.theater[movie_name] -= num_tickets
                return f'Tickets booked for {movie_name}.'
            return 'Not enough tickets!'
        return f'Invalid name!'

    def get_movies(self):
        return {x: k for x, k in self.theater.items() if k > 0}

    @classmethod
    def get_total_theaters(cls):
        return cls.total_theaters

    @staticmethod
    def is_valid_movie_name(movie_name):
        return movie_name != ''

theater1 = MovieTheater("Sunset Cinemas")
theater2 = MovieTheater("Starview Theater")
theater1.add_movie("Avengers: Endgame", 50)
theater1.add_movie("The Lion King", 30)
theater2.add_movie("Inception", 40)
theater2.add_movie("Jurassic World", 20)
theater1.book_ticket("Avengers: Endgame", 5)
theater2.book_ticket("Inception", 10)
print("Movies in Sunset Cinemas:", theater1.get_movies())
print("Movies in Starview Theater:", theater2.get_movies())
print("Is 'Interstellar' a valid movie name?", MovieTheater.is_valid_movie_name("Interstellar"))
print("Is '' a valid movie name?", MovieTheater.is_valid_movie_name(""))
print("Total theaters:", MovieTheater.get_total_theaters())