# print("Python setup successful....!")

                    # NOTE: Data Types

# x = 20
# y = 20
# print(x + y)

# print(type(x))

# a = "brajesh"
# print(type(a))

# b = True
# c = False
# print(b-c)

# d = 6 + 7j
# print(type(d))

# print(d.real, d.imag)

                    #NOTE: String

# s1 = "this IS a string"

# print(type(s1))
# print(len(s1))

# s2 = " -- this is second string"

# print(s1 + s2)
# print(s1.find('s')) # 3
# print(s1.find('x')) # -1
# print(s1.count('i'))
# s3 = s1.upper()
# s4 = s1.lower()
# print(s3, s4, s1, "---", s1.swapcase())
# print(s1.title()) # capitalize the first letter of every word
# print(s1.capitalize()) # first character have upper case and the rest lower case

# print(s1[0])
# print(s1[0:8:1])
# print(s1[::-1])
# print(s1[::-2])
# print(s1[2::2])

                    # NOTE: Lists

# list = []
# print(type(list))
# l1 = [67, 43, 66, "brajesh", 43.00]
# print(l1)

# print(l1*2) 

# l2 = [3, 4, 5, 66]

# print(l1 + l2) # append



                    # Tuples

t1 = (1, 2, "brajesh", True, 5+6j)
l = [1, 2, "tyrant", False]

# print(type(t1), type(l))

# print(t1[2])
# t1[2] = "tyrant" # Tuples are immutable 
# l[2] = "brajesh"
# print(l) # lists are mutable

# print(t1.index("brajesh"))


                                    # NOTE: Dictionaries

# d = {1: "brajesh", 2: "prajapati"}

# print(d[2])

# d1 = {[1,2,3]:"brajesh"}
# print(d1) # NOTE: TypeError -> (UNHASHABLE TYPE: 'LIST') can't use 'list' as a dict key : list is mutable


# d2 = {(1,2,3): "brajesh"}
# print(d2) # NOTE: tuple is immutable hence no error

# d3 = {{1,2,3}: "brajesh"}
# print(d3) # NOTE: dict & set ares also unhashable types


                                        # NOTE: Exception Handling


# try:
#     a=4
#     b=0
#     print(a/b)
# except Exception as e:
#     print("Exception occured!", "Exception: ", e)
# finally:
#     print("Finally getting executed!!!")



# ls = [43, 66, 67]
# for i in ls: # for else loop
#     print(i)
#     if i == 67:
#         break
# else:
#     print("For executed Successfully")


                                        # NOTE: OOPS PROGRAMMING


# ! FUNCTIONS


# def test():
#     pass

# test()

# def fun1(a, b):
#     print("a = ", a,"b = ",b)

# fun1(43, 66)

# fun1(b=43, a=67) # parameter order can be changed(value will be passed accn to their names)

# def fun2(*args, email): # var args using asterisk
#     print("var args: ", args)
#     print("email: ", email)

# fun2(43, True, 67, "BRAJESH", ["this", "is", "a", "list"], email="prajapatibrajesh003@gmail.com")


# def fun3(**kargs): # var args with double asterisk takes only key value pairs as parameters as treats them as a dict
#     print(kargs)
#     print(type(kargs))

# fun3(name="brajesh", surname="prajapati", role="student")


# lambdaFunc = lambda a, b: a*b
# print(lambdaFunc(4, 3))

# square = lambda a: a**2
# print(square(5))

# lambda2 = lambda **kargs: print(kargs, type(kargs))

# lambda2(brajesh=43, unknown=67, undefined=66)

# def fun4(l):
#     '''
#     This is Docstring for fun4 -> it takes list as parameter and returns the list+2
#     '''
#     l1=[]
#     for i in l:
#         l1.append(i+2)
#     return l1

# print(fun4([43, 66, 67]))

#! Class & Object


# class Solution:
#     def func1(self): # NOTE; self isn't a keyword here
#         print("Solution class func1")

# ob = Solution()
# ob.func1()

# class Solution2:
#     def func1(meow):
#         print("Solution2 Meow func")
    
# ob2 = Solution2()
# ob2.func1()


# class Solution3:
#     classVariable = 'variable'

#     def __init__(self, name, email):
#         self.name = name
#         self.email2 = email

#     def show_mentor(self):
#         print("Mentor name: ", self.show_mentor)
    
# ob3 = Solution3("brajesh", "prajapatibrajesh003@gmail.com")
# print(ob3)
# print(type(ob3))
# ob3.show_mentor("brajesh")

# print(ob3.classVariable)
# print(ob3.name)
# print(ob3.email) # AttributeError: ob3 has no attribute 'email'. email2 is known but not email


#! INHERITANCE


# class parent:
#     def printParent(self):
#         print("This is parent function")

# class Child(parent):
#     pass

# child_ob = Child()
# child_ob.printParent()


# class mentor:

#     def __init__(self, name, email, contact):
#         self.name = name
#         self.email = email
#         self.contact = contact
#         print("Calling mentor constructor")
    
#     def printDetails(self):
#         print(self.name, self.email, self.contact)

# class stud(mentor):
#     def print(self):
#         print("This is stud")

#     def __init__(self):
#         print("This is stud constructor")

# ob = stud("brajesh", "prajapatibrajesh003@gmail.com", "93xxxxxxx")
# print(ob.name)
# print(ob.print())
# print(ob.printDetails())


# class super:
#     def fun1(self):
#         print("Super class function")
    
# class sub:
#     def fun1(self):
#         print("sub class function")

# sub_ob = sub()
# sub_ob.fun1



# class A:
#     def test(self):
#         print("A")

# class B(A):
#     def test(self): # NOTE: Method Overriding
#         print("B")
#         super().test() # CTX: Calling the parent method using super
    

# ob = B()
# ob.test()



# CTX: Method Resolution Order (MRO) 

# class A:
#     def fun1(self):
#         print("Class A method")

# class B:
#     def fun1(self):
#         print("Class B method")
    
# class C(A, B):
#     pass

# class D(B, A):
#     pass

# ob = C()
# obj = D()
# ob.fun1() # No Ambiguity here -> it will print the method inherited from A
# obj.fun1() # it will print the method inherited from B


# CTX: private -> double underscore (__) -> accessed using _className__functionName

# class A:
#     def __privateFun(self):
#         print("Class A's private function")

# ob = A()
# ob._A__privateFun()

# CTX: protected -> single underscore (_) -> accessed using

# class A:
#     def _protectedFun(self):
#         print("Class A's protected function")

# ob = A()
# ob._protectedFun()



class A:
    def __init__(self, salary, balance):
        self.name = name # public variable -> accessible from anywhere
        self._salary = salary # protected variable -> accessible outside the class, but discouraged
        self.__balance = balance # private variable -> double underscore -> "name mangling"

# NOTE: public -> APIs, services, reusable methods
# NOTE: protected (_) -> internal helpers, extensible classes
# NOTE: private (__) -> sensitive logic, internal state



# IMP: Python doesn't have strict private variables. Python uses naming conventions & name mangling

