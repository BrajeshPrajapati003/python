# name = input("Enter your name: ")
# age = int(input("Enter your age: ")) #! take input with input() & cast them, default = str
# height = float(input("Enter your height: "))

# name = "Brajesh Prajapati"
# age = 21
# height = 5.8
# print(name, age)
# print(height)
# print()
# print(name, age, height, sep=",") #! join variables with ,
# print(name, age, end="/") #! end the line with /



# full_name = 'brajesh'
# print(full_name)

# age = 100
# print(full_name, "age = ", age)

# address = "Narmadapuram"
# print(full_name, end = "&&")

#ctx: take age and print it
# age = int(input("Enter your age: "))
# if(age >= 18): 
#     # print("You can drive and drink")

#     test = input("Pass/Fail in exams? ")
#     if(test == "pass" or test == "Pass"): print("you're eligible for Driving license...")
#     else: print("You're can't drive")
# else: print("You are underage!!!")


#ctx: take input & give remarks
# marks = int(input("Enter your marks: "))
# if(marks >= 90):
#     print("Excellent")
# elif(marks >= 70 and marks <90):
#     print("Good")
# elif(marks >= 40 and marks <70):
#     print(Fair)
# else:
#     print("Bad")


# ctx: take temperature and predict weather conditions
# temp = int(input("Enter the temperature: "))
# if temp >= 25 and temp <= 50: #! can also be written as 25 <= temp <= 50
#     print("Hot")
# elif temp >= 10 and temp < 25:
#     print("Cold")
# else:
#     print("Extremely Cold")


#ctx: Ternary operator
# age = int(input("Enter your age: "))
# result = "Eligible" if age >= 18 else "Not Eligible" #! Ternary operator
# print(result)

# ctx: while loop
# i = 0
# while i<5:
#     print(i, end=" ") #! in a single line
#     i += 1
# print()

# ctx: for loop
# list1 = [43, 67, 66]
# for i in list1:
#     print(i) #! in different lines

# ctx: range function
# for i in range(1, 11):
#     print(i, end=" ")
# print()

# for i in range(1, 11, 2): #! range(inclusive, exclusive, jump)
#     print(i, end=" ")
# print()

# for i in range(20, 0, -2): #! range(inclusive, exclusive, jump) in reverse
#     print(i, end=" ")
# print()


# name =  input("Enter your name: ")
# def greet(name): #! function created with def keyword
#     print('Hello ', name)

# greet(name) # function calling


def add2Numbers(a, b):
    return a+b

print(add2Numbers(2, 4))

