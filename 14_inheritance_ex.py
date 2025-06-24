class Animal:
    def make_sound(self):
        return NotImplementedError
class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        return 'Woof'
class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        return 'Meow'
class Bird(Animal):
    def make_sound(self):
        super().make_sound()
        return 'Chirp'
animals = [Dog(), Cat(), Bird()]
for animal in animals:
    print(animal.make_sound())

#

class BankAccount:
    def __init__(self, amount):
        self.amount = amount
        self.count = 0
    def deposit(self, amount):
        self.amount += amount
        return self.amount
    def withdraw(self, amount):
        if amount > self.amount:
            return f"Not enough money!"
        self.amount -= amount
        self.count += 1
        return self.amount
class SavingsAccount(BankAccount):
    def __init__(self, amount):
        super().__init__(amount)
    def deposit(self, amount):
        return super().deposit(amount)
    def withdraw(self, amount):
        result = super().withdraw(amount)
        if self.count > 3:
            return f'Warning its limited with 3 per month!'
        return result
acc = SavingsAccount(1000)
print(acc.withdraw(100))
print(acc.withdraw(100))
print(acc.withdraw(100))
print(acc.withdraw(100))

#

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base = base_salary
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculate_salary(self):
        return self.base
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def calculate_salary(self):
        return self.base
employees = [Manager("Alice", 5000), Developer("Bob", 4000)]
for emp in employees:
    print(f"{emp.name} earns {emp.calculate_salary()}")

#

class Shape:
    def draw(self):
        return NotImplementedError
class Circle(Shape):
    def draw(self):
        super().draw()
        return print("Drawing a circle")
class Square(Shape):
    def draw(self):
        super().draw()
        return print("Drawing a square")
class Triangle(Shape):
    def draw(self):
        super().draw()
        return print("Drawing a triangle")
shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()

#

class Notification:
    def send(self):
        return NotImplementedError
class EmailNotification(Notification):
    def send(self, message):
        super().send()
        return print(f'Sending email: {message}')
class SMSNotification(Notification):
    def send(self, message):
        super().send()
        return print(f'Sending SMS: {message}')
class PushNotification(Notification):
    def send(self, message):
        super().send()
        return print(f'Sending push: {message}')
notifications = [EmailNotification(), SMSNotification(), PushNotification()]
for notif in notifications:
    notif.send("System update at 3 PM")

#

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Book(Product):
    def __init__(self, name, price, title):
        super().__init__(name, price)
        self.title = title
    def get_details(self):
        return (f'name: {self.name}, '
                f'price: {self.price}, '
                f'title: {self.title}')
class Electronics(Product):
    def __init__(self, name, price, title):
        super().__init__(name, price)
        self.title = title
    def get_details(self):
        return (f'name: {self.name}, '
                f'price: {self.price}, '
                f'title: {self.title}')
class Clothing(Product):
    def __init__(self, name, price, title):
        super().__init__(name, price)
        self.title = title
    def get_details(self):
        return (f'name: {self.name}, '
                f'price: {self.price}, '
                f'title: {self.title}')
products = [
    Book("1984", 15, "George Orwell"),
    Electronics("Headphones", 90, "Sony"),
    Clothing("Jacket", 120, "L")
]
for p in products:
    print(p.get_details())

#

class Vehicle:
    def move(self):
        return NotImplementedError
class Car(Vehicle):
    def move(self):
        super().move()
        return print('Driving on road')
class Bike(Vehicle):
    def move(self):
        super().move()
        return print('Riding on trail')
class Boat(Vehicle):
    def move(self):
        super().move()
        return print('Sailing on water')
vehicles = [Car(), Bike(), Boat()]
for v in vehicles:
    v.move()

#

class Logger:
    def log(self, message):
        return NotImplementedError
class ConsoleLogger(Logger):
    def log(self, message):
        super().log(message)
        return print('Console: User login successful')
class FileLogger(Logger):
    def log(self, message):
        super().log(message)
        return print('File: User login successful')
class DatabaseLogger(Logger):
    def log(self, message):
        super().log(message)
        return print('Database: User login successful')
loggers = [ConsoleLogger(), FileLogger(), DatabaseLogger()]
for logger in loggers:
    logger.log("User login successful")

#

class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    def turn_on(self):
        raise NotImplementedError
    def turn_off(self):
        raise NotImplementedError
    def status(self):
        raise NotImplementedError
class SmartLight(SmartDevice):
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def status(self):
        if self.turn_on == True:
            return 'Living Room light is ON.'
        elif self.turn_on == False:
            return 'Living Room light is OFF.'
        return 'Living Room light is not turned on/off.'
class SmartThermostat(SmartDevice):
    def __init__(self, name, target_temp):
        super().__init__(name)
        self.target = target_temp
    def set_temperature(self, temp):
        self.target = temp
        return self.target
    def status(self):
        return f'Bedroom thermostat is set to {self.target}°C.'

light = SmartLight("Living Room")
thermostat = SmartThermostat("Bedroom", target_temp=22)
light.turn_on()
thermostat.set_temperature(20)
print(light.status())
print(thermostat.status())

#

class Employee:
    def __init__(self, name):
        self.name = name
class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked
class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def calculate_pay(self):
        return self.salary
class Freelancer(Employee):
    def __init__(self, name, rate_per_project, projects_done):
        super().__init__(name)
        self.rate_per_project = rate_per_project
        self.projects_done = projects_done
    def calculate_pay(self):
        return self.rate_per_project * self.projects_done

employees = [
    HourlyEmployee("John", hourly_rate=20, hours_worked=35),
    SalariedEmployee("Alice", salary=4000),
    Freelancer("Mark", rate_per_project=500, projects_done=4)
]

for emp in employees:
    print(f"{emp.name}: ${emp.calculate_pay()}")












