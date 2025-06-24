decorator_based_polymorphism_tree = '''Goal: 
Add multiple, swappable behaviors to a base object 
→ without modifying the base class
→ while using the same method interface (polymorphism)

────────────────────────────────────
1️⃣ Create a Base Class
│
├── Define the main method(overridden), (e.g. process, predict, send, etc.)
│   ├── This method contains the original logic
│   └── This base class will be treated as an object
│       → It will be passed to decorators via constructor
│       → It becomes the first "wrapped" object in the chain
│
────────────────────────────────────
2️⃣ Create Decorator Classes
│
├── Each decorator must:
│   ├── Accept a wrapped object via __init__(self, wrapped)
│   ├── Store that object in self.wrapped
│   └── Override the same method as the base class
│
├── Inside the overridden method:
│   ├── (Optional) Add logic before forwarding the call
│   ├── Call self.wrapped.method(...)
│   └── (Optional) Add logic after the call
────────────────────────────────────
3️⃣ Chain the Decorators
│
├── Instantiate the base class first
│
├── Wrap it step by step with decorators
│   └── Each decorator wraps the previous one
│
└── Final object becomes a layered stack of behaviors
────────────────────────────────────
4️⃣ Call the Method Once on the Outermost Wrapper
│
├── Single method call triggers all layers:
│   ├── Top-level decorator logic runs
│   ├── Then next decorator logic runs
│   ├── ...
│   └── Finally reaches the base method
│
└── Each layer adds/modifies behavior but shares the same interface
────────────────────────────────────
✅ Final Result:
- You built flexible behavior layering without inheritance
- You reused one method interface (`process()`)
- You can reorder or remove wrappers anytime
- This is **pure polymorphism through composition**'''

# Wrapper - An object/function that adds behavior to another, while preserving its interface
# Wrapped - The original object being extended or decorated

class PaymentProcessor:
    def payment_amount(self, amount):
        print(f'Final payment: {amount}')
        return amount

class DiscountDecorator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def payment_amount(self, amount):
        discount = amount * 10 // 100
        discounted_amount = amount - discount
        print(f'10% discount applied: -{discount}')
        return self.wrapped.payment_amount(discounted_amount)

class TaxDecorator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def payment_amount(self, amount):
        tax = amount * 0.20
        taxed_amount = amount + tax
        print(f'20% tax applied: +{tax}')
        return self.wrapped.payment_amount(taxed_amount)

class CurrencyConverterDecorator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def payment_amount(self, amount):
        eur = round(amount * 0.93, 2)
        print(f'Converted to EUR: {eur}')
        return self.wrapped.payment_amount(eur)


processor = CurrencyConverterDecorator(
    TaxDecorator(
        DiscountDecorator(
            PaymentProcessor() # original object
        )
    )
)
# DiscountDecorator wraps PaymentProcessor() and holds it in self.wrapped.
# TaxDecorator wraps the DiscountDecorator instance, holding it in self.wrapped.
# CurrencyConverterDecorator wraps the TaxDecorator instance.

processor.payment_amount(100)

# When you call:
# processor.payment_amount(100)
# 1.CurrencyConverterDecorator.payment_amount(100) is called
# 2.It converts amount, then calls
# self.wrapped.payment_amount(converted_amount) → calls TaxDecorator.payment_amount
# 3.TaxDecorator adds tax, then calls
# self.wrapped.payment_amount(taxed_amount) → calls DiscountDecorator.payment_amount
# 4.DiscountDecorator subtracts discount, then calls
# self.wrapped.payment_amount(discounted_amount) → calls PaymentProcessor.payment_amount
# 5.PaymentProcessor.payment_amount finally processes (prints) the final amount.


# Another one #

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