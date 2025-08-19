from abc import ABC, abstractmethod

# Example of concreate class

class PaymentProcessor(ABC): # Abstraction
    @abstractmethod
    def __init__(self, amount):
        self._amount = amount # Encapsulation
    @property
    @abstractmethod
    def amount(self):
        pass
    @amount.setter
    @abstractmethod
    def amount(self):
        pass

class StripePayment(PaymentProcessor): # Inheritance
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        print(f'Amount is {self._amount}')
        return self._amount

    @amount.setter
    def amount(self, value):
        if value > 0:
            self._amount = value
        else:
            raise ValueError('Can\'t be a negative value!')

class PayPalPayment(PaymentProcessor): # Inheritance
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        print(f'Amount is {self._amount}')
        return self._amount

    @amount.setter
    def amount(self, value):
        if value > 0:
            self._amount = value
        else:
            raise ValueError('Can\'t be a negative value!')

stripe = StripePayment(500)
paypal = PayPalPayment(400)

def show_amount(processor: PaymentProcessor): # Polymorphism
    print(processor.amount)

show_amount(stripe)
show_amount(paypal)

print(StripePayment.__abstractmethods__) # empty, frozenset()

about_1 = '''
So what’s happening in our case?
 • Our subclass StripePayment:
 • Implements __init__ 
 • Implements amount getter 
 • Implements amount setter 
 • Therefore: StripePayment.__abstractmethods__ → frozenset()
   (means: “No abstract methods left — it’s fully concrete”)
'''
























