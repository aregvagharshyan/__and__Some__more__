abstraction ='''Abstraction is the process of hiding unnecessary implementation 
details and exposing only the essential features of an object or system.
It simplifies interaction by allowing users to work with a clear interface 
without needing to understand the internal complexity.
_________
Abstract class is a blueprint for other classes:
 • It cannot be instantiated(you can't create objects from it's directly),
   and it's meant to be inherited.
 • It usually defines abstract methods, that must be implemented in subclasses.
---------

Why use Abstract Classes?
 • To provide a common API for related classes.
 • To force subclasses to implement specific methods.
 • To support polymorphism (treat different subclasses uniformly).
 • To share common code while leaving implementation details to subclasses.

 • Option 1: Using ABC (Simplest & Recommended),
              need to import abc module
'''

from abc import ABC, abstractmethod

class MyBase(ABC):
    @abstractmethod
    def do_something(self):
        pass
# • ABC internally sets metaclass=ABCMeta.
# • Cleaner and easier to read.

part_two = '''
 • Option 2: Manually Setting ABCMeta as the Metaclass
'''

from abc import ABCMeta, abstractmethod

class MyBase2(metaclass=ABCMeta):
    @abstractmethod
    def do_something(self):
        pass
# This is more explicit and gives control over custom metaclass behavior

error = '''
What Happens If a Subclass Doesn’t Implement Abstract Methods?
 • Error Example:
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

a = Animal()  # can't instantiate, raises error here
# TypeError: Can't instantiate abstract class MyBase without an implementation

class Dog(Animal):
    pass  # missing implementation!

d = Dog()  # raises error here
# TypeError: Can't instantiate abstract class Dog with abstract method speak

why = '''
Why This Happens
 • Python uses the ABCMeta metaclass to check:
 • “Does the subclass implement all required abstract methods?”
 • If not, Python prevents the object from being created — this is enforced at instantiation time, not class definition
 
In Python, abstract classes created using ABCMeta automatically get a special attribute -
.__abstractmethods__., so we have access internally: 

'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self): pass

    @abstractmethod
    def move(self): pass

class Dog(Animal):
    def speak(self): return "Woof!"

print(Animal.__abstractmethods__)

# {'speak', 'move'}

print(Dog.__abstractmethods__)

# {'move'} — speak is implemented, move is not

in_the_end = '''
Under the Hood:
 • Python’s ABCMeta sets __abstractmethods__ when an abstract (or subclass) is created.
 • It’s a frozenset — immutable and introspectable.
 • It directly drives the following error at runtime:
    - TypeError: Can't instantiate abstract class Dog with abstract method move
 • This error occurs only if __abstractmethods__ of the subclass is non-empty.

When is it checked?
 → At instantiation time (i.e., when calling the constructor).
'''
