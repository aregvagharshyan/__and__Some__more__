polymorphism = '''Same interface, different behavior.'''

one = '''🔹Duck Typing(dynamic) Polymorphism'''

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)

# The function animal_sound(animal) expects an object that has a .speak() method.
# •It doesn’t care what class the object belongs to (Dog, Cat, or even Fox).
# •As long as the object has a .speak() method — it works.


two = '''🔹Inheritance-based Polymorphism'''

class Animal:
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

def make_sound(animal: Animal):
    return animal.speak()

make_sound(Cat())  # "Meow"
make_sound(Dog())  # "Woof"

#➡️ Base class defines the interface; subclasses override the method.

three = '''🔹 Decorator-Based Polymorphism'''

class PlainSender:
    def send(self, message):
        print(f'From base: {message}')
        return message

class Base64EncoderDecorator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def send(self, message):
        print(f'Encodes to base64: {message}')
        return self.wrapped.send(message)

class ROT13EncoderDecorator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def send(self, message):
        print(f'Encodes with ROT13: {message}')
        return self.wrapped.send(message)

class ReverseStringDecorator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def send(self, message):
        reversed_message = message[::-1]
        print(f'Reversed message: {reversed_message}')
        return self.wrapped.send(reversed_message)

plain_sender = Base64EncoderDecorator(ROT13EncoderDecorator(ReverseStringDecorator(PlainSender())))
plain_sender.send('hello')

#➡️ Each decorator wraps another format and adds its own behavior.

four = '''🔹Strategy Pattern(custom)'''

class Strategy:
    def execute(self, data):
        raise NotImplementedError("Subclasses must override execute(data)")
              # This error is powerful, for this case...)
class Upper(Strategy):
    def execute(self, data):
        return data.upper()

class Lower(Strategy):
    def execute(self, data):
        return data.lower()

class Processor:
    def __init__(self, strategy):
        self.strategy = strategy
    def run(self, text):
        return self.strategy.execute(text)

print(Processor(Upper()).run("Hi"))
print(Processor(Lower()).run("Hi"))

#➡️ Swap logic at runtime (interface stays same)