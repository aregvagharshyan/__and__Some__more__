inheritance_MRO_super = '''Inheritance - Reuse code from base classes, subclass overrides or extends.
MRO - Determines method lookup order, Used especially in multiple inheritance.
super() - Calls the next method in MRO, Safe and dynamic.
'''
MRO = '''✅Python determines which method or attribute to use using the MRO(Method Resolution Order) 
— especially important in multiple inheritance.
✅Use ClassName.__mro__ to inspect it.
✅MRO goes left to right based on how classes are inherited, and uses the C3 linearization algorithm.
'''
tree = '''  object
              ↑
              A
            ↗   ↖
          B       C
            ↖   ↗
              D    '''

# Example_1 #

class A:
    def action(self):
        print("A.action() -> calling super()")
        super().action()
class B(A):
    def action(self):
        print("B.action() -> calling super()")
        super().action()
class C(A):
    def action(self):
        print("C.action() -> calling super()")
        super().action()
class D(B, C):
    def action(self):
        print("D.action() -> calling super()")
        super().action()
# Testing
d = D()
d.action()
# Show MRO
print("D MRO:", D.__mro__)
# D.action() -> calling super()
# B.action() -> calling super()
# C.action() -> calling super()
# A.action() -> calling super()
# Traceback (most recent call last):
#   ...
# AttributeError: 'super' object has no attribute 'action'

# This error appears because A calls super().action() but object(in MRO) has no action() method.

# Example_2 #

class A:
    def action(self):
        print("A.action()")  # No super()
class B(A):
    def action(self):
        print("B.action() -> calling super()")
        super().action()
class C(A):
    def action(self):
        print("C.action() -> calling super()")
        super().action()
class D(B, C):
    def action(self):
        print("D.action() -> calling super()")
        super().action()
# Testing
d = D()
d.action()
# Show MRO
print("D MRO:", D.__mro__)
# D.action() -> calling super()
# B.action() -> calling super()
# C.action() -> calling super()
# A.action()
# D MRO: (<class '__main__.D'>, <class '__main__.B'>,
# <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Example_3 #

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print(D.__mro__)
# (
#   <class '__main__.D'>,     # the class itself
#   <class '__main__.B'>,     # parent 1
#   <class '__main__.C'>,     # parent 2
#   <class '__main__.A'>,     # grandparent
#   <class 'object'>          # root of all classes
# )

print(type(D))         # <class 'type'>
print(isinstance(D, type))  # True

meta_level_tree = ''' Instance:  d
                         ↓
                Class:   D (→ B → C → A → object)
                         ↓
                Metaclass: type
                         ↓
                type is instance of itself (type)'''
