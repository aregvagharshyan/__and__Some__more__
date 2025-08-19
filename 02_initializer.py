_constructor = '''A initializer is a special method in a class that is automatically called when an object is created. 
In Python, the initializer is called __init__().
The first parameter of a class method (like the initializer __init__) is always self. 
This parameter represents the instance of the class that is being created or modified.

Purpose of self:
It allows you to access and modify the object's attributes and methods.
 • When a method is called on an object, self refers to the specific object that the method is being invoked on.
 
Purpose of the initializer:
 • It initializes the object’s (self) attributes with default or provided values when the object is created.
 • It's typically used to set up or initialize the state of the object.'''

### Example ###

class Car:
    def __init__(self, brand, model): # initializer's calling
        self.brand = brand  # initializing self (object) attribute
        self.model = model  # initializing self (object) attribute

# Creating an object (initializer is called automatically)
my_car = Car("Toyota", "Corolla")

# Accessing object attributes
print(my_car.brand)  # Output: Toyota
print(my_car.model)  # Output: Corolla