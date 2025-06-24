from abc import ABC, abstractmethod

class DatabaseConnector(ABC):
    def __init__(self, host, post):
        self.host = host
        self.post = post
    @abstractmethod
    def connect(self):
        pass

class MySQLConnector(DatabaseConnector):
    def connect(self):
        return print(self.host, self.post)

print(DatabaseConnector.__abstractmethods__)
# output will be frozenset({'connect'})

print(MySQLConnector.__abstractmethods__)
# It's concrete, output will be frozenset({})

#


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self):
        pass
class Rectangle(Shape):
    def area(self):
        pass

#c = Shape()
# gives an error!

#

class BaseLogger(ABC):
    def log_prefix(self):
        return "This is log's field!"
    @abstractmethod
    def log(self, message):
        pass
class ConsoleLogger(BaseLogger):
    def log(self, message):
        prefix = self.log_prefix()
        print(f"{prefix} {message}")

console = ConsoleLogger()
console.log('hi')

#

class Plugin(ABC):
    @abstractmethod
    def run(self, context):
        pass
class One(Plugin):
    def run(self, context):
        return print(f'This is first plugin: {context}')
class Two(Plugin):
    def run(self, context):
        return print(f'This is second plugin: {context}')

for i in [One(), Two()]:
    i.run('Hello')

#

class Authenticatable(ABC):
    @abstractmethod
    def first(self):
        pass
class Loggable(ABC):
    @abstractmethod
    def second(self):
        pass
class SubClass(Authenticatable, Loggable):
    def first(self):
        return print(f'This is Authenticatable!')
    def second(self):
        return print(f'This is Loggable!')

subclass = SubClass()
subclass.first()



