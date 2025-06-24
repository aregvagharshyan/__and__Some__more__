_staticmethod = '''Static methods are methods that do not access or modify class or instance data.
They use the @staticmethod decorator and take neither self nor cls as the first parameter.
In a block we write:
 • No self → it does not operate on instances
 • No cls → it does not operate on the class
 • Use it for utility/helper functions that logically belong to the class'''

### Example ###

class MathUtils:
    # Static method: performs an action unrelated to instance or class
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Using static methods without creating an instance
print(MathUtils.add(3, 5))       # Output: 8
print(MathUtils.is_even(10))     # Output: True

# You can also call them from an instance, though it's not recommended
utils = MathUtils()
print(utils.add(1, 2))           # Output: 3



