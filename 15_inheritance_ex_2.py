class Employee:
    def __init__(self, name):
        self.name = name
    def calculate_pay(self):
        raise NotImplementedError
class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly = monthly_salary
    def calculate_pay(self):
        return self.monthly
class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours = hours_worked
        self.rate_hour = hourly_rate
    def calculate_pay(self):
        calculated = self.hours * self.rate_hour
        return calculated
class CommissionEmployee(Employee):
    def __init__(self, name, base_salary, commission, sales):
        super().__init__(name)
        self.base_salary = base_salary
        self.commission_rate = commission
        self.sales = sales
    def calculate_pay(self):
        return self.base_salary + (self.commission_rate * self.sales)

emp = HourlyEmployee(name="Jane", hours_worked=40, hourly_rate=15)
print(emp.calculate_pay())

#

class Account:
    def __init__(self, account_id, balance):
        self.id = account_id
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        raise NotImplementedError
    def display(self):
        return f'{self.id} : {self.balance}'
class SavingsAccount(Account):
    def __init__(self, account_id, balance, interest_rate):
        super().__init__(account_id, balance)
        self.interest = balance * interest_rate
    def apply_interest(self):
        self.balance += self.interest
        return f'Interest applied'
    def withdraw(self, amount):
        if amount > self.balance:
            return f'Not enough amount!'
        self.balance -= amount
        return f'Withdraw successfully!'
class CheckingAccount(Account):
    def __init__(self, account_id, balance, overdraft_limit):
        super().__init__(account_id, balance)
        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):
        if amount > self.balance:
            return f'Not enough amount!'
        self.balance -= amount
        return f'Withdraw successfully!'
acc1 = SavingsAccount("SA001", 1000, 0.03)
acc1.apply_interest()
acc1.withdraw(200)
acc1.display()

#

class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError

class AddTextCommand(Command):
    def __init__(self, buffer, text):
        self.buffer = buffer
        self.text = text
        self.executed = False
    def execute(self):
        self.buffer.append(self.text)
        self.executed = True
    def undo(self):
        if self.executed and self.buffer and self.buffer[-1] == self.text:
            self.buffer.pop()
            self.executed = False
class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
    def execute(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()
    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("Nothing to undo.")
    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
        else:
            print("Nothing to redo.")
buffer = []
cmd_mgr = CommandManager()
cmd_mgr.execute(AddTextCommand(buffer, "Hello "))
cmd_mgr.execute(AddTextCommand(buffer, "world"))
cmd_mgr.undo()
cmd_mgr.redo()
print("".join(buffer))

#

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_price(self):
        return self.price
    def display(self):
        return f'{self.name} - {self.price}'
class Meal(MenuItem):
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = calories
class Drink(MenuItem):
    def __init__(self, name, price, is_alcoholic):
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic
class Order:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        return self.items
    def total(self):
        return sum(item.get_price() for item in self.items)
    def display(self):
        print("Order Summary:")
        for item in self.items:
            item.display()
        print(f"Total: ${self.total()}")
order = Order()
order.add_item(Meal("Burger", 8.5, 600))
order.add_item(Drink("Cola", 2.0, False))
order.display()


