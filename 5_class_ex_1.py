# Create a Student class with:
#
# Attributes: name, grades (list).
# Methods:
# add_grade(grade) → Adds a new grade (0-100).
# average_grade() → Returns the average grade.
# highest_grade() → Returns the highest grade.
# display_info() → Prints student's name, grades, and average.

class Student:

    def __init__(self, name):
        self.name = name
        self.grade = list()

    def add_grade(self, grade):
        if 0 < grade < 100:
            self.grade.append(grade)

    def average_grade(self):
        return sum(self.grade) // len(self.grade)

    def highest_grade(self):
        return max(self.grade)

    def display_info(self):
        print(f"The {self.name}'s grade is: {self.grade} and average is: {self.average_grade()}")

student = Student("David")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)
student.display_info()

# Create a BankAccount class with:
#
# Attributes: owner, balance, transactions (list).
# Methods:
# deposit(amount) → Increases balance and records transaction.
# withdraw(amount) → Decreases balance (if sufficient funds) and records transaction.
# transaction_history() → Displays all transactions.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.deposits = f'Deposit: {amount}'
        self.transactions.append(self.deposits)
        return self.balance, self.transactions

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdraws = f'Withdraw: {amount}'
            self.transactions.append(self.withdraws)
            return self.balance, self.transactions
        else:
            return f'Insufficient funds!'

    def transaction_history(self):
        print(f'Transaction History: {self.transactions}')

account = BankAccount("Alice", 1000)
print(account.deposit(500))
account.withdraw(200)
print(account.withdraw(2000))
account.transaction_history()

# Create a Student class with attributes:
#
# name (str)
# grades (dict, where keys are subjects and values are lists of grades)
# Methods:
#
# add_grade(subject, grade): Adds a grade to the subject. If the subject doesn't exist, add it.
# average_grade(subject): Returns the average grade for a subject.
# overall_average(): Returns the overall average of all subjects.

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        return self.grades

    def average_grade(self, subject):
        average = []
        for key, value in self.grades.items():
            if key == subject:
                average.append(value)
                return sum(average) / len(average)
            else:
                return 0
        return sum(average) / len(average)

    def overall_average(self):
        return sum(self.grades.values()) / len(self.grades)

s = Student("Alice")
s.add_grade("Math", 90)
s.add_grade("Math", 80)
s.add_grade("History", 85)
print(s.average_grade("Math"))  # Output: 85.0
print(s.overall_average())      # Output: 85.0

# Create a WordTracker class that stores unique words from given sentences.
#
# Attributes:
#
# words (set) to store unique words
# Methods:
#
# add_sentence(sentence): Adds words from the sentence to the set.
# contains_word(word): Checks if a word exists in the set.
# get_all_words(): Returns all stored words as a sorted list.

class WordTracker:
    def __init__(self):
        self.words = set()

    def add_sentence(self, sentence):
        self.words.update(sentence.split())
        return self.words

    def contains_word(self, word):
        return word in self.words

    def get_all_words(self):
        return sorted(self.words)

tracker = WordTracker()
print(tracker.add_sentence("Hello world"))
print(tracker.add_sentence("Hello Python"))
print(tracker.contains_word("world"))
print(tracker.get_all_words())

# Create a Person class with:
#
# name (str)
# birth_date (tuple in format (year, month, day))
# Methods:
#
# age(current_year): Returns the person's age.

class Person:
    def __init__(self, name = str, birth_date = tuple()):
        self.name = name
        self.birth_date = birth_date

    def age(self, current_year):
        return current_year - self.birth_date[0]

p = Person("John", (1990, 5, 21))
print(p.age(2025))

# Create a BankAccount class with:
#
# Attributes: owner and balance (default 0).
# Methods:
# deposit(amount) → adds money to the balance.
# withdraw(amount) → subtracts money if balance is enough.
# display_balance() → prints the current balance.

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return 'Not enough balance'

    def display_balance(self):
        return print(f'{self.balance}$')

obj = BankAccount('Areg', 2500)
print(obj.deposit(500))
print(obj.withdraw(3500))
obj.display_balance()

# Create a Temperature class with:
#
# An attribute celsius.
# Methods:
# to_fahrenheit() → converts Celsius to Fahrenheit.
# to_kelvin() → converts Celsius to Kelvin.
# display() → prints all temperatures.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return float(self.celsius + 273.15)

    def display(self):
        print(self.celsius, self.to_fahrenheit(), self.to_kelvin())

obj = Temperature(32)
obj.display()

# Create a Rectangle class with:
#
# Attributes: width and height.
# Methods:
# area() → returns the area of the rectangle.
# perimeter() → returns the perimeter.
# display() → prints the width, height, area, and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def display(self):
        print(f'''The Width is: {self.width}
The Height is: {self.height}
The area is: {self.area()}
The Perimeter is: {self.perimeter()}''')

obj = Rectangle(5, 8)
obj.display()

# Create a Counter class with:
#
# An attribute count (default 0).
# Methods:
# increment() → increases count by 1.
# decrement() → decreases count by 1 (but not below 0).
# reset() → resets count to 0.
# display() → prints the current count.

class Counter:
    def __init__(self, count = 0):
        self.count = count

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        if self.count > 0:
            self.count -= 1
            return self.count

    def reset(self):
        self.count = 0
        return self.count

    def display(self):
        print(f'Current count = {self.count}')

obj = Counter(5)
obj.display()

# Create an Employee class with:
#
# Attributes: name, salary, and bonus_percentage.
# Methods:
# calculate_total_salary() → returns salary + bonus.
# display_info() → prints the employee's name and total salary.

class Employee:
    def __init__(self, name, salary, bonus_percentage):
        self.name = name
        self.salary = salary
        self.bonus_percentage = bonus_percentage

    def calculate_total_salary(self):
        return int(self.salary + (self.salary * self.bonus_percentage / 100))

    def display_info(self):
        print(f'The total of {self.name} is {self.calculate_total_salary()}')

obj = Employee("Areg", 300000, 10)
obj.display_info()

# Task:
# Create a Book class with:
#
# Attributes: title, author, and pages.
# Methods:
# display_info() → prints the book's details.
# is_long() → returns True if pages > 300, otherwise False

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(self.title, self.author, self.pages, 'pages :')

    def is_long(self):
        return True if self.pages > 300 else False

obj = Book('Hannibal Lector', 'Mark', 333)
obj.display_info()
obj.is_long()

# Create a Car class with:
#
# Attributes: brand, speed (default 0).
# Methods:
# accelerate(amount) → increases speed.
# brake(amount) → decreases speed (but not below 0).
# display_speed() → prints current speed.

class Car:
    def __init__(self, brand, speed = 0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        return self.speed

    def brake(self, amount):
        if self.speed >= 0:
            self.speed -= amount
            return self.speed

    def display_speed(self):
        print(f'Current speed: {self.speed}')

obj = Car('Subaru', 70)
obj.accelerate(40)
obj.display_speed()

# Task:
# Create a ShoppingCart class with:
#
# Attribute: items (default empty list).
# Methods:
# add_item(name, price) → adds item as a tuple (name, price).
# remove_item(name) → removes an item by name.
# total_cost() → returns total price of items.
# display_cart() → prints all items and total cost.

class ShoppingCart:
    def __init__(self, items):
        self.items = []

    def add_item(self, name, price):
        return self.items.append((name, price))

    def remove_item(self, name):
        return [(item, price) for item, price in self.items if item != name]

    def total_cost(self):
        return sum(price for _, price in self.items)

    def display_cart(self):
        for item, price in self.items:
            print(f"- {item}: ${price}")
        print(f"Total: ${self.total_cost()}")

cart = ShoppingCart([])
cart.add_item("Laptop", 1000)
cart.add_item("Mouse", 50)
cart.display_cart()
cart.remove_item("Mouse")
cart.display_cart()

