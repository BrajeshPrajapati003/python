#                     #! Encapsulation and Abstraction

class PublicClass:
    def __init__(self):
        self.public_attribute = 10

    def public_function(self): # if self not given here -> TypeError
        print("Public function")

# ob1 = PublicClass()
# ob1.public_function() # Public function
# print(ob1.public_attribute) # 10


class PrivateClass:
    def __init__(self):
        self.__private_attribute = 10
    
    def __private_function(self):
        print("Private function")

# ob2 = PrivateClass()
# # print(ob2.__private_attribute) # ! attributeError -> Python performs name mangling, internally stored as _PrivateClass__private_attribute
# print(ob2._PrivateClass__private_attribute) # ! but this is strongly discouraged
# ob2._PrivateClass__private_function() # Private function; but strongly discouraged


class ProtectedClass:
    def __init__(self):
        self._protected_attribute = 10
    
    def _protected_function(self):
        print("Protected function")

# ob3 = ProtectedClass()
# print(ob3._protected_attribute) # 10
# ob3._protected_function # 10
# # ! protected in Python is just a convention -> single underscore means "please don't access this directly"; Python doesn't enforce it


# One child inherits from one parent
class A:
    def show(self):
        print("A")

class B(A): #N Single inheritance
    pass

# one child inherits from multiple parents
class A:
    def methodA(self):
        print("A")

class B:
    def methodB(self):
        print("B")

class C(A, B): #N Multiple Inheritance (MRO - METHOD RESOLUTION ORDER)
    pass

# print(C.__mro__) # C -> A -> B -> object


# Chain-like inheritance
class A:
    pass

class B(A):
    pass

class C(B): # Multiple inheritance
    pass


# Multiple Children inherit from one parent
class A:
    pass

class B(A):
    pass

class C(A): # Hierarchical inheritance
    pass


# Combination of multiple types -> Hybrid Inheritance

# ! Python resolves method conflicts using C3 Linearization (MRO algorithm)


# Method overriding - child class redefining parent method
class A:
    def greet(self):
        print("A")

class B(A):
    def greet(self):
        print("B")


# super() - to call parent method
class B(A):
    def greet(self):
        super().greet()
        print("B after super()")

# ob4 = B()
# ob4.greet()


# MRO (in multiple inheritance) - Python follows C3 Linearization to resolve method order
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

# print(D.__mro__)


# Diamond problem
class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass


# ! Exception Handling
# a = int(input())
# b = int(input())

# try:
#     result = print(a // b)
# except ZeroDivisionError:
#     result = None
#     print("Cannot divide by zero")
# finally:
#     print("Finally block executed!")

