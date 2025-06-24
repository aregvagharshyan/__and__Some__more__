
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError('Balance can not be negative!')
        self._balance = amount
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        raise ValueError('Not enough balance!')
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return self._balance
        raise ValueError('Amount can\'t be negative!')
obj_1 = BankAccount(2000)

#

class Student:
    def __init__(self, list_of_grades):
        self.list_of_grades = list_of_grades
    @property
    def list_of_grades(self):
        return self._list_of_grades
    @list_of_grades.setter
    def list_of_grades(self, value):
        if all(0 <= grade <= 100 for grade in value):
            self._list_of_grades = value
        raise ValueError('Wrong grade!')
    def average(self):
        if len(self._list_of_grades) > 0:
            return sum(self._list_of_grades) // len(self._list_of_grades)
        raise ValueError('Empty list!')

#

class User:
    def __init__(self, password):
        self.password = password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        if len(value) >= 6:
            self._password = value
        else:
            raise ValueError('Too short password!')
    def change_pass(self, old_pass, new_pass):
        if old_pass == self._password:
            self._password = new_pass
            return f'Password changed successfully!'
        raise ValueError('Wrong old password!')

#

class Encapsulation:
    def __init__(self, semi, strong):
        self._semi_private = semi
        self.__strong_private = strong
    def get(self):
        return f'{self._semi_private}, {self.__strong_private}'
e = Encapsulation('semi', 'strong')
print(e.get())
print(e._Encapsulation__strong_private)

#

class Two:
    def __init__(self, temperature):
        self.temperature = temperature
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        if value > 0:
            self._temperature = value
        else:
            raise ValueError('Value will be above zero!')
t = Two(32)

#

class Three:
    def __init__(self, password):
        self.password = password
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        if len(value) > 6:
            self.__password = value
        else:
            raise ValueError('Needs more than 6 characters!')

#

class Four:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'Deposit was successfully!'
        else:
            raise ValueError('Amount will be greater than 0!')
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f'Withdraw was successfully'
        else:
            raise ValueError('Not enough money or amount will be greater than 0!')

#

class User1:
    def __init__(self, adress):
        self.adress = adress
    @property
    def adress(self):
        return self._adress
    @adress.setter
    def adress(self, value):
        if '@' in value and '.' in value:
            self._adress = value
        else:
            raise ValueError('Invalid format!')

#

class Character:
    def __init__(self, level):
        self.__level = level
    def gain_xp(self, value):
        if value > 0:
            self.__level += value
            return self.__level
        raise ValueError('Value can\'t be below zero')
    def get_level(self, value):
        if value >= self.__level and value >0:
            raise ValueError('Not enough value!')
        self.__level -= value
        return self.__level
    def display_level(self):
        return self.__level
c = Character(1)
c.gain_xp(2)

#

class Thermometer:
    def __init__(self, temp):
        self.temp = temp
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self, value):
        if -50 < value < 150:
            self._temp = value
        else:
            raise ValueError('Invalid value!')
obj = Thermometer(51)
obj.temp = 120
print(obj.temp)
#

















