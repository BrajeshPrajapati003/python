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


