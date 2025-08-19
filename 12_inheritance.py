inheritance = '''Inheritance is an object-oriented programming concept where class(subclass) 
derives datas(attributes) and behaviors (methods) from another class(base class).

Base class - The class being inherited from (aka base class or parent).
Subclass - The class that inherits (aka child class).
Override - Redefine a method from the parent in the child.
Extend - Add new methods/attributes in the child.
super() - Calls the parent class method according to MRO.

1. Single Inheritance - One subclass inherits from one base class.
2. Multi-level Inheritance -A subclass of a subclass.
2. Multiple Inheritance - A subclass inherits from multiple base class.
4. Hierarchical Inheritance - Multiple subclasses from the same base class.
'''

meta_tree = '''Meta-Level (How classes are built)
──────────────────────────────────────────────
                          ┌──────────────────┐
                          │      type        │◄─────────────┐
                          └────────┬─────────┘              │
                                   │                        │
     ┌─────────────────────────────▼──────────────────── ┐  │
     │ Defines how classes are built                     │  │
     │ - Builds __mro__                                  │  │
     │ - Handles __new__, __init_subclass__, etc.        │  │
     └───────────────────────────────────────────────────┘  │
                                   │                        │
                                   ▼                        │
                          ┌──────────────────┐              │
                          │     object       │◄─────────────┘
                          └────────┬─────────┘
                                   │
         ┌────────────────────────▼────────────────────────┐
         │ Defines core magic methods:                     │
         │  • __init__(self)                               │
         │  • __str__(self)                                │
         │  • __repr__(self)                               │
         │  • __eq__(self, other)                          │
         │  • __hash__(self)                               │
         │  • __new__(cls)                                 │
         │  • __class__ property                           │
         └─────────────────────────────────────────────────┘

User-Level (You define classes)
──────────────────────────────────────────────

             ▲ (inherits from object)
             │
    ┌────────┴─────────┐
    │  class Flyer:    │  ◄──────────── May override __str__, __init__, etc.
    └──────────────────┘

    ┌────────┐          ┌──────────────┐
    │Swimmer │          │     Duck     │  ◄────── May override or extend magic methods
    └────────┘          └──────┬───────┘
                               │
                ┌──────────────▼───────────────┐
                │ Duck.__mro__ contains:       │
                │   Duck, Flyer, Swimmer,      │
                │   object                     │
                └──────────────────────────────┘

Instance-Level (When you create an object)
──────────────────────────────────────────────

         ┌────────────────────┐
         │  duck = Duck()     │
         └────────┬───────────┘
                  ▼
      ┌──────────────────────────────────────────┐
      │ Instance of Duck                         │
      │ Inherits methods from MRO:               │
      │  - __init__ from Duck or Flyer or object │
      │  - __str__ from Duck or object, etc.     │
      └──────────────────────────────────────────┘
'''

# Examples #

class User:
    def __init__(self, username):
        self.username = username
class Admin(User):
    def __init__(self, username, access_level):
        super().__init__(username)
        self.access_level = access_level
a = Admin("john", "superuser")
print(a.username)
print(a.access_level)

#

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print(D.__mro__)

