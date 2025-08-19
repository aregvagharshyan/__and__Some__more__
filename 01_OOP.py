_OOP = '''OOP (Object-Oriented Programming) is a programming paradigm that organizes code 
into objects that represent real-world entities.
These objects have attributes (data) and methods (functions that operate on the data). 
OOP makes code more reusable, scalable, and easier to maintain.

Key Concepts of OOP:
 • Class – A blueprint for creating objects.
 • Object – An instance of a class with data(attributes) and behavior(methods).'''

_Class = '''A class in Python is a blueprint for creating objects. It defines the attributes (variables) and methods (functions) that the objects created from it will have.'''
_Object = '''An object is an instance of a class. It represents a specific entity created from a class blueprint.

Key Points:
 • A class defines the structure and behavior.
 • An object is a concrete implementation of that class.
 • Each object has its own unique data but shares the same methods.'''

_class_attribute = 'Are shared across whole class!'
__self_attribute = 'Are unique to each object(instance)!'

### Example ###

class Greeting: # with class level attribute!

    message = "Hello, World!"  # class attribute

    def say_hello():  # method like a this
        return Greeting.message   # accessing class attribute

# Calling the method directly
print(Greeting.say_hello())  # output: Hello, World!

class Greeting2: # with instance(self) level attribute!

    def __init__(self, message):
        self.message = message # self attribute

    def say_hello(self): # method like this too
        message = self.message
        return message # accessing self attribute

# Creating object, calling on in it directly
greeting = Greeting2("Hello, World!")
print(greeting.say_hello())