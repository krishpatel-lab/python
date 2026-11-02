#parameters and arguments
'''default parameters '''

# def hello(a , b = 20):      # b is default value, if you enter b it will ressing and if not it will be 10
#     print(a + b)

# hello(20)


'''default argumnets'''
# def informations(name,age,number):
#     print("hello your info is")
#     print(name)
#     print(age)
#     print(number)

# informations(number = 9179665438 , age = 19 , name = "krishpatel")

'''print no from 1-30
you cannot use for and while loop
you cannot uses print statement more than 1'''

#you call function inside a function
#recursion - a function calling function itself
# def numbers(n):
#     if n == 999:
#         return
#     print(n)
#     numbers(n+1)

# numbers(1)

'''stack'''
# def hello1():
#     hello2()
#     print("hello1")

# def hello2():
#     hello3()
#     print("hello2")

# def hello3():
#     hello4()
#     print("hello3")

# def hello4():
#     print("hello4")

# hello1()


# def numbers(n):
#     if n == 31:
#         return
#     numbers(n+1)
#     print(n)

# numbers(1)


'''Function practice sheet :06-10-2026'''



'''Q1. Find the Largest of Three Numbers
Create a function largest() that takes three numbers and 
returns the largest number.'''


# def largest(a , b , c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > a and c > b:
#         return c
#     else:
#         return "both 3 numbers are equal"
# result = largest(12 , 45 , 23)
# print(result)

'''Q2. Check Prime Number
Create a function is_prime() that takes a number and returns
"Prime" if the number is prime, otherwise returns "Not Prime".'''


def is_primne(a):
    