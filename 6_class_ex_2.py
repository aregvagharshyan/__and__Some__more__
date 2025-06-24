# Create a Library class that manages books. Each book has a title, author, and year of publication.
# Requirements:
# The library stores books in a dictionary where keys are book titles and values are tuples (author, year, copies).
# Implement the following methods:
# add_book(title, author, year, copies): Adds a book or updates copies if it already exists.
# borrow_book(title): If the book exists and has copies, reduce copies by 1. Otherwise, return "Book unavailable".
# return_book(title): Increases the number of available copies.
# get_books_by_author(author): Returns a list of book titles by the given author.

class Library:
    def __init__(self):
        self.dict = {}

    def add_book(self, title, author, year, copies):
        tuple_1 = (author, year, copies)
        if title in self.dict:
            existing_author, existing_year, existing_copies = self.dict[title]
            self.dict[title] = (existing_author, existing_year, existing_copies + copies)
            return self.dict
        else:
            self.dict[title] = tuple_1
            return self.dict

    def borrow_book(self, title):
        if title in self.dict:
            author, year, copies = self.dict[title]
            if copies > 0:
                self.dict[title] = (author, year, copies - 1)
                return self.dict
            else:
                return "No copies available"
        else:
            return "Book unavailable"

    def return_book(self, title):
        if title in self.dict:
            author, year, copies = self.dict[title]
            self.dict[title] = (author, year, copies + 1)
            return self.dict
        else:
            return "Book unavailable"

    def get_books_by_author(self,author):
        return [key for key, value in self.dict.items() if value[0] == author]

library = Library()
print(library.add_book("1984", "George Orwell", 1949, 3))
print(library.add_book("Animal Farm", "George Orwell", 1945, 2))
print(library.add_book("1984", "George Orwell", 1949, 1))
print(library.borrow_book("1984"))
print(library.get_books_by_author("George Orwell"))

# Create a Bank class that manages user accounts. Each user has a unique account number and balance.
# Requirements:
# Store accounts in a dictionary {account_number: (name, balance)}.
# Implement these methods:
# create_account(name): Generates a unique account number (random 6-digit int) and initializes balance to 0.
# deposit(account_number, amount): Adds money to the account.
# withdraw(account_number, amount): Deducts money if sufficient funds exist; otherwise, return "Insufficient funds".
# transfer(from_acc, to_acc, amount): Moves money between accounts.


import random

class Bank:
    def __init__(self):
        self.dict = {}

    def create_account(self, name):
        acc_number = random.randint(100000, 999999)
        while acc_number in self.dict:
            acc_number = random.randint(100000, 999999)
        self.dict[acc_number] = (name, 0)
        return acc_number

    def deposit(self, account_number, amount):
        if account_number in self.dict:
            x, y = self.dict[account_number]
            self.dict[account_number] = (x, y + amount)
            return self.dict
        else:
            return 'Not account like this'

    def withdraw(self, account_number, amount):
        if account_number in self.dict:
            x, y = self.dict[account_number]
            if y >= amount:
                self.dict[account_number] = (x, y - amount)
                return self.dict
            else:
                return 'Insufficient funds'
        else:
            return 'Not account like this'

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.dict and to_acc in self.dict:
            x, y = self.dict[from_acc]
            a, b = self.dict[to_acc]
            if amount <= y:
                self.dict[from_acc] = (x, y - amount)
                self.dict[to_acc] = (a, b + amount)
                return self.dict
            else:
                return 'Insufficient funds in 1st account'
        else:
            return 'Problem with accounts'

bank = Bank()
acc1 = bank.create_account("Alice")
acc2 = bank.create_account("Bob")

print(bank.deposit(acc1, 500))
print(bank.transfer(acc1, acc2, 200))
print(bank.withdraw(acc1, 400))

# Create a CoursePlatform class where users can enroll in courses and complete lessons.
# Requirements:
# Store courses in a dictionary {course_name: {lesson_titles}}.
# Store user progress in {username: {course_name: set(completed_lessons)}}.
# Implement these methods:
# add_course(course_name, lessons): Adds a course with a list of lessons.
# enroll_user(username, course_name): Enrolls a user in a course.
# complete_lesson(username, course_name, lesson): Marks a lesson as completed.
# progress(username, course_name): Returns the percentage of lessons completed.

class CoursePlatform:
    def __init__(self):
        self.courses = {}
        self.user_progress = {}

    def add_course(self, course_name, lessons):
        self.courses[course_name] = lessons
        return self.courses

    def enroll_user(self, username, course_name):
        self.user_progress[username] = {course_name: set()}
        return self.user_progress

    def complete_lesson(self, username, course_name, lesson):
        if username in self.user_progress and course_name in self.courses:
            self.user_progress[username][course_name].add(lesson)
            return self.user_progress
        else:
            return 'Not username or course like this'

    def progress(self, username, course_name):
        if username in self.user_progress and course_name in self.courses:
            total_lessons = len(self.courses[course_name])
            completed_lessons = len(self.user_progress[username].get(course_name, []))
            return (completed_lessons / total_lessons) * 100
        else:
            return 'Invalid username or course name'

platform = CoursePlatform()
print(platform.add_course("Python Basics", ["Variables", "Loops", "Functions"]))
platform.enroll_user("Alice", "Python Basics")

platform.complete_lesson("Alice", "Python Basics", "Variables")
print(platform.progress("Alice", "Python Basics"))

# Create a SocialMedia class where users can follow each other and make posts.
# Requirements:
# Store user details in {username: {"posts": [], "followers": set(), "following": set()}}.
# Implement these methods:
# create_user(username): Creates a new user profile.
# post(username, message): Adds a post to the user’s feed.
# follow(follower, following): One user follows another.
# get_feed(username): Returns posts from the user and people they follow.

class SocialMedia:
    def __init__(self):
        self.user = {}

    def create_user(self, username):
        self.user[username] = {'posts': [], 'followers': set(), 'followings': set()}
        return self.user

    def post(self, username, message):
        if username in self.user:
            self.user[username]['posts'].append(message)
            return self.user
        else:
            return 'Not username like this'

    def follow(self, follower, following):
        if follower in self.user and following in self.user:
            self.user[follower]['followings'].add(following)
            self.user[following]['followers'].add(follower)
            return self.user
        else:
            return 'Not username like this'

    def get_feed(self, username):
        if username in self.user:
            list_feed = [post for following in self.user[username]['followings'] for post in self.user[following]['posts']]
            return list_feed
        else:
            return 'Not username like this'

app = SocialMedia()
print(app.create_user("Alice"))
print(app.create_user("Bob"))
print(app.post("Alice", "Hello, world!"))
print(app.follow("Bob", "Alice"))
print(app.get_feed("Bob"))

# Objective: Create an Inventory class that manages a store's stock.
# The inventory should store items in a dictionary: {item_name: (price, stock)}.
# Implement the following methods:
# add_item(item_name, price, stock): Adds a new item or updates an existing item’s price and stock.
# remove_item(item_name): Removes an item from the inventory.
# update_stock(item_name, stock): Updates the stock of an existing item.
# purchase_item(item_name, quantity): Decreases the stock of an item after a purchase, or returns a message if the stock is insufficient.
# get_item_info(item_name): Returns the price and stock of the item.

class Inventory:
    def __init__(self):
        self.store = {}

    def add_item(self, item_name, price, stock):
        if item_name in self.store:
            old_price, old_stock = self.store[item_name]
            self.store[item_name] = (old_price + price, old_stock + stock)
            return f'{item_name} added to Inventory'
        else:
            self.store[item_name] = (price, stock)
            return f'{item_name} added to Inventory'

    def remove_item(self, item_name):
        self.store.pop(item_name, f'{item_name} is missing')
        return f'{item_name} removed from Inventory'

    def update_stock(self, item_name, stock):
        if item_name in self.store:
            price, old_stock = self.store[item_name]
            self.store[item_name] = (price, old_stock + stock)
            return f'{item_name} is updated'
        else:
            return f'Name is missing'

    def purchase_item(self, item_name, quantity):
        price, old_quantity = self.store[item_name]
        if quantity <= old_quantity:
            self.store[item_name] = (price, old_quantity - quantity)
            return f'{item_name} is purchased'
        else:
            return 'The stock is insufficient'

    def get_item_info(self, item_name):
        for price, stock in self.store.values():
            return f'The price of {item_name} is {price}, and stock is {stock}:'
        return f'Not enough data!'

inventory = Inventory()
print(inventory.add_item("Laptop", 1000, 10))
print(inventory.add_item("Phone", 500, 15))
print(inventory.purchase_item("Laptop", 2))
print(inventory.update_stock("Phone", 20))
print(inventory.get_item_info("Laptop"))
print(inventory.remove_item("Phone"))

# Objective: Create a MovieRental class that allows users to rent and return movies.
# Store the movies in a dictionary: {movie_title: (genre, copies_available)}.
# Implement the following methods:
# add_movie(movie_title, genre, copies): Adds a new movie or updates the number of copies.
# rent_movie(movie_title): Decreases the number of available copies after renting, or returns a message if the movie is unavailable.
# return_movie(movie_title): Increases the number of available copies when a movie is returned.
# get_movie_info(movie_title): Returns the genre and the number of available copies of the movie.

class MovieRental:
    def __init__(self):
        self.store = dict()

    def add_movie(self, movie_title, genre, copies):
        if movie_title not in self.store:
            self.store[movie_title] = (genre, copies)
            return f'{movie_title} added in store'
        else:
            genre, old_copies = self.store[movie_title]
            self.store[movie_title] = (genre, old_copies + copies)
            return f'{movie_title} is updated'

    def rent_movie(self, movie_title):
        if movie_title in self.store:
            genre, old_copies = self.store[movie_title]
            self.store[movie_title] = (genre, old_copies - 1)
            return f'{movie_title} is rented'
        else:
            return f'Movie is unavailable'

    def return_movie(self, movie_title):
        if movie_title in self.store:
            genre, old_copies = self.store[movie_title]
            self.store[movie_title] = (genre, old_copies + 1)
            return f'{movie_title} is returned'
        else:
            return f'Movie is unavailable'

    def get_movie_info(self, movie_title):
        for genre, copies in self.store.values():
            return f'Genre of {movie_title} is: {genre}, There are {copies} copies'
        return f''
movie_rental = MovieRental()
print(movie_rental.add_movie("Inception", "Sci-Fi", 5))
print(movie_rental.add_movie("Titanic", "Romance", 3))
print(movie_rental.rent_movie("Inception"))
print(movie_rental.return_movie("Titanic"))
print(movie_rental.get_movie_info("Inception"))

# Objective: Create a Student class to manage students enrolled in multiple courses.
# Store students in a dictionary: {student_id: {"name": student_name, "courses": {course_name: [grades]}}}.
# Implement the following methods:
# add_student(student_id, student_name): Adds a new student.
# enroll_in_course(student_id, course_name): Enrolls a student in a course.
# add_grade(student_id, course_name, grade): Adds a grade for a student in a course.
# get_average_grade(student_id, course_name): Returns the average grade for a student in a course.
# get_overall_average(student_id): Returns the overall average grade of the student across all courses.

class Student:
    def __init__(self):
        self.store = {}

    def add_student(self, student_id, student_name):
        self.store[student_id] = {"name": student_name, "courses": {}}
        return f'{student_name} added.'

    def enroll_in_course(self, student_id, course_name):
        if student_id in self.store:
            self.store[student_id]['courses'][course_name] = []
            return f'The student {student_id} enrolls in {course_name} course.'
        return "Student not found."

    def add_grade(self, student_id, course_name, grade):
        if student_id in self.store and course_name in self.store[student_id]['courses']:
            self.store[student_id]['courses'][course_name].append(grade)
            return f'The student {student_id} adds grade {grade} to {course_name}.'
        return "Invalid student ID or course name."

    def get_average_grade(self, student_id, course_name):
        if student_id in self.store and course_name in self.store[student_id]['courses']:
            grades = self.store[student_id]['courses'][course_name]
            return sum(grades) / len(grades) if grades else "No grades available."
        return "Invalid student ID or course name."

    def get_overall_average(self, student_id):
        if student_id in self.store:
            grades = [grade for course in self.store[student_id]['courses'].values() for grade in course]
            return sum(grades) / len(grades) if grades else "No grades available."
        return "Student not found."

student_management = Student()
print(student_management.add_student(1, "Alice"))
print(student_management.enroll_in_course(1, "Math"))
print(student_management.add_grade(1, "Math", 90))
print(student_management.add_grade(1, "Math", 85))
print(student_management.get_average_grade(1, "Math"))
print(student_management.get_overall_average(1))

# Objective: Create a Hotel class to manage room reservations.
# Store rooms in a dictionary: {room_number: {"status": "available" or "booked", "guest_name": None or guest_name}}.
# Implement the following methods:
# book_room(room_number, guest_name): Books a room for a guest.
# cancel_booking(room_number): Cancels a room booking.
# get_room_status(room_number): Returns the status of a room (whether it’s available or booked, and the guest name if booked).

class Hotel:
    def __init__(self):
        self.store = dict()

    def book_room(self, room_number, guest_name):
        self.store[room_number] = {"status": 'booked', 'guest_name': guest_name}
        return f'{guest_name} booked the {room_number} room'

    def cancel_booking(self, room_number):
        self.store[room_number] = {'status': 'available', 'guest_name': None}
        return f'The {room_number} room is canceled'

    def get_room_status(self, room_number):
        return f'The {room_number}: {self.store[room_number]}'

hotel = Hotel()
print(hotel.book_room(101, "John Doe"))
print(hotel.book_room(102, "Jane Smith"))
print(hotel.get_room_status(101))
print(hotel.cancel_booking(102))
print(hotel.get_room_status(102))

# Objective: Create a TaskManager class to handle tasks.
# Store tasks in a dictionary: {task_id: {"task_name": name, "status": "pending" or "completed"}}.
# Implement the following methods:
# add_task(task_name): Adds a new task with a unique ID.
# mark_completed(task_id): Marks a task as completed.
# get_task_status(task_id): Returns the current status of a task.
# get_all_pending_tasks(): Returns a list of all pending tasks.

import random

class TaskManager:
    def __init__(self):
        self.store = {}

    def add_task(self, task_name):
        while True:
            unique_id = random.randint(1, 99)
            if unique_id not in self.store:
                break
        self.store[unique_id] = {"task_name": task_name, "status": "pending"}
        return unique_id

    def mark_completed(self, task_id):
        self.store[task_id]['status'] = 'completed'
        return f'{task_id} - task is completed'

    def get_task_status(self, task_id):
        return f'The status of - {task_id}: {self.store[task_id]['status']}'

    def get_all_pending_tasks(self):
        pending_tasks = [i['task_name'] for i in self.store.values() if i["status"] == 'pending']
        return pending_tasks

task_manager = TaskManager()
task_id1 = task_manager.add_task("Complete Python assignment")
task_id2 = task_manager.add_task("Attend team meeting")
task_manager.mark_completed(task_id1)
print(task_manager.get_task_status(task_id1))
print(task_manager.get_all_pending_tasks())

# Objective: Implement a StoreInventory class to manage products in a store.
# Methods to Implement:
# add_product(name, price, stock) → Adds a new product or updates stock if the product exists.
# update_price(name, new_price) → Updates the price of an existing product.
# purchase_product(name, quantity) → Reduces stock when a product is purchased.
# get_product_info(name) → Returns a tuple with price and stock of a product.
# apply_discount(percent) → Uses map() to reduce prices of all products by a percentage.
# list_available_products() → Uses dictionary comprehension to return available products.

class StoreInventory:
    def __init__(self):
        self.store = {}

    def add_product(self, name, price, stock):
        if name not in self.store:
            self.store[name] = {"price": price, "stock": stock}
            return f'{name} added to inventory'
        else:
            self.store[name].get('stock') + stock
            return f'{name} updated'

    def update_price(self, name, new_price):
        self.store[name].get('price') + new_price
        return f'{name}"s price was updated'

    def purchase_product(self, name, quantity):
        if name in self.store:
            if self.store[name]['stock'] > 0:
                self.store[name].get('stock') - quantity
                return f'{name} purchased successfully'
            else:
                return f'Not a {name} product in inventory'
        return f'Not a {name} product like this'

    def get_product_info(self, name):
        return self.store[name]['price'], self.store[name]['stock']

    def apply_discount(self, percent):
        reduced_prices = map(lambda x: x * (1 - percent / 100), [i['price'] for i in self.store.values()])
        return reduced_prices

    def list_available_products(self):
        return {x: k for x, k in self.store.items() if k['stock'] > 0}

store = StoreInventory()
store.add_product("Laptop", 1200, 5)
store.add_product("Phone", 600, 10)
store.update_price("Laptop", 1100)
store.purchase_product("Phone", 2)
print(store.get_product_info("Laptop"))
store.apply_discount(10)
print(store.list_available_products())

# Objective: Implement a BankAccount class to manage user accounts.
# Data Structure
# python
# Copy
# Edit
# {account_number: {"holder": name, "balance": balance, "transactions": []}}
# Methods to Implement
# create_account(account_number, holder, balance) → Adds a new bank account.
# deposit(account_number, amount) → Adds money to the account.
# withdraw(account_number, amount) → Withdraws money if the balance allows.
# get_balance(account_number) → Returns the balance of the account.
# get_transaction_history(account_number) → Returns a list of all transactions.

class BankAccount:
    def __init__(self):
        self.store = {}

    def create_account(self, account_number, holder, balance):
        self.store[account_number] = {'holder': holder, 'balance': balance, 'transactions': []}
        return f'New bank account added for {holder}'

    def deposit(self, account_number, amount):
        self.store[account_number]['balance'] += amount
        self.store[account_number]['transactions'].append(f'Deposit: {amount}')
        return f'{amount} deposit for {account_number} is successful'

    def withdraw(self, account_number, amount):
        if amount <= self.store[account_number]['balance']:
            self.store[account_number]['balance'] -= amount
            self.store[account_number]['transactions'].append(f'Withdraw: {amount}')
            return f'{amount} withdraw for {account_number} is successful'
        return f'Not enough balance'

    def get_balance(self, account_number):
        return f'Balance for {account_number} is: {self.store[account_number]['balance']}'

    def get_transaction_history(self, account_number):
        return f'Transaction for {account_number}: {self.store[account_number]['transactions']}'

bank = BankAccount()
bank.create_account(101, "Alice", 500)
bank.deposit(101, 200)
bank.withdraw(101, 100)
print(bank.get_balance(101))
print(bank.get_transaction_history(101))

# Objective: Manage users and interactions in a social media platform.
# Data Structure
# python
# Copy
# Edit
# {username: {"posts": [], "followers": set(), "following": set()}}
# Methods to Implement
# add_user(username) → Adds a new user.
# post_message(username, message) → Adds a post to the user’s list.
# follow(user1, user2) → Makes user1 follow user2.
# unfollow(user1, user2) → Removes user2 from user1's following.
# get_user_feed(username) → Returns posts of followed users.

class SocialMedia:
    def __init__(self):
        self.store = {}

    def add_user(self, username):
        self.store[username] =  {"posts": [], "followers": set(), "following": set()}
        return f'{username} added to media'

    def post_message(self, username, message):
        self.store[username]['posts'].append(message)
        return f'Message added for {username}'

    def follow(self, user_1, user_2):
        self.store[user_1]['following'].add(user_2)
        self.store[user_2]['followers'].add(user_1)
        return f'{user_1} follows {user_2}'

    def unfollow(self, user_1, user_2):
        self.store[user_1]['following'].remove(user_2)
        self.store[user_2]['followers'].remove(user_1)
        return f'{user_2} removes from {user_1}\' following'

    def get_user_feed(self, username):
        following_username = self.store[username]['following']
        posts = []
        for name in following_username:
            posts.extend(self.store[name]['posts'])
        return posts

social = SocialMedia()
social.add_user("Alice")
social.add_user("Bob")
social.post_message("Alice", "Hello, world!")
print(social.follow("Bob", "Alice"))
print(social.get_user_feed("Bob"))



















