one = '@staticmethod-based exercises!'

#

class MathUtils:

    @staticmethod
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

print(MathUtils.is_prime(15))

#

class StringUtils:

    @staticmethod
    def count_vowels(s):
        count = 0
        vovels = 'aeiouAEIOU'
        for i in s:
            if i in vovels:
                count += 1
        return count

print(StringUtils.count_vowels("hello world"))

#

class MatrixUtils:

    @staticmethod
    def multiply_matrices(matrix_a, matrix_b):
        rows_a = len(matrix_a)
        cols_a = len(matrix_a[0])
        rows_b = len(matrix_b)
        cols_b = len(matrix_b[0])
        if cols_a != cols_b:
            raise ValueError("Number of columns in A must be equal to the number of rows in B")
        matrix_c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
        return matrix_c

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
result = MatrixUtils.multiply_matrices(matrix_a, matrix_b)
print(result)

#

class SortUtils:

    @staticmethod
    def bubble_sort(arr):
        for j in range(len(arr)):
            for i in range(0, len(arr) - j - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr

arr = [64, 34, 25, 12, 22, 11, 90]
SortUtils.bubble_sort(arr)
print(arr)

#

class Converter:

    @staticmethod
    def decimal_to_binary(n):
        return bin(n)[2:]

print(Converter.decimal_to_binary(10))
print(Converter.decimal_to_binary(255))

#

class Employee:

    @staticmethod
    def average_salary(salaries):
        return sum(salaries) // len(salaries)

salaries = [5000, 6000, 5500, 4000, 7000]
print(Employee.average_salary(salaries))

two = '@classmethod-based exercises!'

#

class Employee:
    base_currency = "USD"

    @classmethod
    def set_currency(cls, currency):
        cls.base_currency = currency

    @classmethod
    def average_salary(cls, salaries):
        print(f"Average salary in {cls.base_currency}")
        return sum(salaries) // len(salaries)

Employee.set_currency("EUR")
print(Employee.average_salary([5000, 6000, 5500]))

#

class Converter:
    prefix = "0b"

    @classmethod
    def set_prefix(cls, new_prefix):
        cls.prefix = new_prefix

    @classmethod
    def decimal_to_binary(cls, n):
        return cls.prefix + bin(n)[2:]

Converter.set_prefix("BIN:")
print(Converter.decimal_to_binary(10))  # BIN:1010

#

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @classmethod
    def from_string(cls, data):
        name, grade = data.split("-")
        return cls(name, int(grade))

s1 = Student.from_string("Anna-90")
print(s1.name, s1.grade)

#

class Matrix:
    @classmethod
    def identity(cls, size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

identity_3x3 = Matrix.identity(3)
print(identity_3x3)

#

class Logger:
    log_level = "INFO"

    @classmethod
    def set_log_level(cls, level):
        cls.log_level = level

    @classmethod
    def log(cls, message):
        print(f"[{cls.log_level}] {message}")

Logger.log("Starting process")
Logger.set_log_level("DEBUG")
Logger.log("Loaded config")

