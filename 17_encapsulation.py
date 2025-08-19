encapsulation = '''Encapsulation is used to hide internal data and control access to it.'''

one = '''1. Using Underscores in Constructor
 • self._var: Semi-private (by convention, “do not touch”).
 • self.__var: Strongly private — name mangling to self._ClassName__var.'''

class Example:
    def __init__(self):
        self._semi = "semi-private"
        self.__strong = "strongly-private"

# Note: __strong is still accessible via obj._Example__strong, but it’s considered bad practice.

two = '''2. Using Getters and Setters (with Decorators).
Encapsulate access to internal attributes through controlled methods.(Getter - read access, Setter - controlled write access, it sets not returns!)'''

class SecureData:
    def __init__(self, value):
        self._value = value  # semi-private

    @property
    def value(self):
        return self._value  # read-only access

    @value.setter
    def value(self, new_value):
        if new_value >= 0:
            self._value = new_value  # controlled write access
        else:
            raise ValueError("Invalid value!")

# Usage:
obj = SecureData(10)
print(obj.value)     # uses getter
obj.value = 100      # uses setter

three = '''3. Encapsulating Methods
 • _semi_method(): Semi-private method (not enforced).
 • __strong_method(): Strongly private method (mangled to _ClassName__strong_method).'''

class Processor:
    def _semi_logic(self):
        return "This is semi-private"
    def __strong_logic(self):
        return "This is strongly private"
    def get_info(self):
        return self.__strong_logic()  # access private method internally

final = '''Encapsulation is not about full security or hiding data like in low-level languages.
It’s about code discipline, maintaining OOP principles, and ensuring clean architecture — making code readable, predictable, and safe to extend.'''