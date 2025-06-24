from abc import ABC, abstractmethod

class BankingSystem(ABC):
    @abstractmethod
    def __init__(self, name: str, balance: int, number: int):
        pass

    @property
    @abstractmethod
    def balance(self):
        pass

    @balance.setter
    @abstractmethod
    def balance(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class User(BankingSystem):
    index = 0
    store_data = {}

    def __init__(self, name: str, balance: int, number: int):
        self.__name = name
        self.__balance = balance
        self.__number = number
        self.store = {'Name': self.__name,
                      'Balance': self.__balance,
                      'Number': self.__number}

    def __call__(self):
        User.index += 1
        User.store_data[User.index] = self.store.copy()
        return User.store_data

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            self.store['Balance'] = self.__balance  # Keep in sync
        else:
            raise ValueError("Mustn't be a negative amount!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.store['Balance'] = self.__balance
            print("Deposit successful!")
            return self.__balance
        raise ValueError("Mustn't be a negative amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.store['Balance'] = self.__balance
            print("Withdraw successful!")
            return self.__balance
        raise ValueError("Mustn't be a negative amount or insufficient balance!")

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Balance: {self.__balance}")
        print(f"Number: {self.__number}")

    @classmethod
    def display(cls):
        return cls.store_data

# Usage
user = User("Areg", 1500, 1)
user()  # register the user
print(User.display())