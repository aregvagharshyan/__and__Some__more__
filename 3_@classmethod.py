_classmethod = '''Class methods are methods that operate on the class itself, not on instances.
They use the @classmethod decorator and take cls as the first parameter to access or modify class-level data.
In a block we write:
 • cls.attribute → Accessing or modifying a class-level attribute
 • cls() → Creating a new instance of the class'''

### Example ###

class Car:
    # Class variable shared by all instances of the class
    wheels = 4

    def __init__(self, brand, model):
        # Instance variables (specific to each object)
        self.brand = brand
        self.model = model

    # Instance method: can access instance and class data
    def display_details(self):
        print(f"This car is a {self.brand} {self.model} and has {self.wheels} wheels.")

    # Class method: modifies a shared class attribute
    @classmethod
    def set_wheels(cls, new_wheel_count):
        # cls.wheels means we are MODIFYING an existing class-level attribute
        cls.wheels = new_wheel_count
        print(f"Class-wide wheel count changed to {cls.wheels}.")

    # Class method that sets a new class-level attribute
    @classmethod
    def set_class_attribute(cls, door=None):
        # cls.new_attribute means we are CREATING or UPDATING a class-level attribute
        cls.new_attribute = 4  # setting a new class attribute
        return f"new_attribute set to {cls.new_attribute}"

    # Class method that creates a new instance of the class
    @classmethod
    def create_default_car(cls):
        # cls(...) means we are CREATING A NEW INSTANCE using the constructor
        return cls("DefaultBrand", "DefaultModel")


# Create an instance
my_car = Car("Toyota", "Corolla")
# Call instance method
my_car.display_details()
# Output: This car is a Toyota Corolla and has 4 wheels.
# Modify class-level wheels using class method
Car.set_wheels(6)
# Output: Class-wide wheel count changed to 6.
# Display details again — reflects new wheels
my_car.display_details()
# Output: This car is a Toyota Corolla and has 6 wheels.
# Add a new class-level attribute using a class method
print(Car.set_class_attribute())
# Output: new_attribute set to 4
# Show that the new attribute is accessible from the class
print(Car.new_attribute)  # Output: 4
# Create a new instance using a class method (factory pattern)
default_car = Car.create_default_car()
default_car.display_details()
# Output: This car is a DefaultBrand DefaultModel and has 6 wheels.







