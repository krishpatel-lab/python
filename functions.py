''' how functions are created
1) inbuild 
Ex - print()
input()
in() , float() , len() etc'''


'''2) user defined functions'''
#defining a function
'''
def hello():
    print("how are you")'''
#calling a function
'''
hello()'''


'''
return
'''
# def hey():
#     return "how are you"      #return the value to the calling block

# a = hey()   #calling book captures the value
# print(a)
# or
# print(hey())


'''parameters and Arguments'''

# def addition(a,b):    #you accept the parameters
#     print(a + b)

# addition(10,20)    #and you provide the argumnets to the parameters

# def palindrome(a):
#     rev = 0
#     copy = a
#     while a != 0:
#         rev = rev * 10 + a%10
#         a = a // 10

#     if copy == rev:
#         print(copy)

# for i in range(1,1000):
#     palindrome(i)


'''Functions practice sheet :05-10-2026

Q1. Add Two Numbers
Create a function add() that takes two numbers as arguments 
and returns their sum'''

# def add(a,b):
#     return a + b
# result = add(10,20)
# print(result)



'''Q2. Check Even or Odd
Create a function check_even_odd() 
that takes a number and returns whether it is Even or Odd.'''

# def check_even_odd(a):
#     if a%2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# result = check_even_odd(7)
# print(result)


'''Q3. Find Square
Create a function square() that takes a number and 
returns its square.'''

# def square(a):
#     return a*a
# result = square(6)
# print(result)


'''Q4. Find Maximum
Create a function maximum() 
that takes two numbers and returns the greater number.'''

# def greater_no(a,b):
#     if a > b:
#         return f"{a}"
#     elif b > a:
#         return f"{b}"
#     else:
#         return f"both {a} and {b} are same"
# result = greater_no(15,25)
# print(result)

'''
Q5. Check Number
Create a function check_number() that 
takes a number and checks whether it is Positive, Negative, 
or Zero.'''

# def positive_negative(a):
#     if a > 0:
#         return "number is positive"
#     elif a < 0:
#         return "number is negitive"
#     else:
#         return "number is zero"
# result = positive_negative(-7)
# print(result)


'''Q6. Calculate Simple Interest
Create a function simple_interest() that takes P, R, and T 
and returns the Simple Interest.

Formula:
SI = (P × R × T) / 100'''

# def simple_interest(P,R,T):
#     return (P*R*T)/100
# result = simple_interest(1000,5,2)
# print(result)

'''Q7. Find Cube
Create a function cube() that takes a number and 
returns its cube.'''

# def cube(a):
#     return a**3
# result = cube(4)
# print(result)

'''Q8. Check Voting Eligibility
Create a function eligible() that takes age as an argument.
If age is 18 or above, return "Eligible", 
otherwise return "Not Eligible".'''

# def eligible(a):
#     if a >= 18:
#         return "Eligible"
#     else:
#         return "Not Eligible"
# result = eligible(20)
# print(result)

'''Q9. Find Factorial
Create a function factorial() that takes a number and 
returns its factorial.'''


# def factorial(a):
#     fact = 1
#     for i in range(1,a+1):
#         fact *= i
#     return fact
# result = factorial(5)
# print(result)


'''Q10. Count Digits
Create a function count_digits() that
takes a number and returns the total number of digits.'''

# def count_digit(a):
#     count = 0
#     while a > 0:
#         a = a // 10
#         count += 1
#     return count

# result = count_digit(12345)
# print(result)


# def count_number(a):
#     count = 0
#     while a > 0:
#         a = a // 10
#         count += 1
#     return count
# result = count_number(123456789)
# print(result)