# #input and output 
# name = "krish"
# age =  19

# two ways of using variables inside print statement
 
# print ("hello your name is" , name , "and your age is" , age)
# print (f"hello your name is {name} and your age is {age}")     #f is formated string

#inputs
#make sure to use the type conversion while taking the inputs

# age = int(input("what is your age : "))
# print (f"your age after 10 years will be {age + 10}")

#operators [+,-,/,*,//,**,%] - arithmetic operators

# a = int(input("enter first number :"))
# b = int(input("enter second number :"))

# print (f"your sum is {a + b}")
# print (a - b)
# print (a * b)
# print (a / b)
# # print (int(a / b))
# print (a // b)     #float division removes all 
#                    #the values after decimal point 
# print (a ** b)
# print (a % b)

#take input of 3 numbers P , R , T and calculate the simple intrest

# P = int(input("tell your principal :"))
# R = float(input("tell your rate :"))
# T = int(input("tell your time :"))
# si = (P*R*T)/100
# print (f"your simple interest will be {si}")
# now calculate compound intrestS
# ci = (P*(1 + (R/100))**T) - P
# print (f"your CI will be {ci}")




#practice sheet p26 Operators practice sheet: ---- 1   22/09/2026
#done date 23/09/2026

#Q1.Take input of two numbers and add them.
# a = int(input("first number :"))
# b = int(input("second number :"))
# print (f"sum is {a + b}")

#Q2.Take input of two numbers and subtract the second number from the first number.
# print (f"answer is {a - b}")

#Q3.Take input of two numbers and multiply them.
# print (f"answer is {a * b}")

#Q4.Take input of two numbers and divide the first number by the second number.
# print (f"answer is {a / b}")
# print (f"answer is {a // b}")
# print (int(a / b))

# Q5.Take input of a price and quantity and calculate the total cost. 
# P = int(input("price :"))
# Q = int(input("quantity :"))
# print (f"Total cost is {P * Q}")

#Q6.Take input of marks of 3 subjects and calculate the average marks.
# s1 = int(input("maths :"))
# s2 = float(input("chemistry :"))
# s3 = int(input("physics :"))
# print(f"average marks is {(s1 + s2 + s3) / 3}")


# Q7.Take input of a number and find its square.
# a = int(input("enter the number :"))
# print (f"the square is {a ** 2}")

#Q9.Take input of a number and find its remainder when divided by 5.
# a = int(input("enter the no :"))
# print (f"the reminder is {a % 5}")

#Q10.Take input of two numbers and calculate the first number raised to the power of the second number.
# a = int(input("enter first :"))
# b = int(input("enter second :"))
# print (f"answer is {a ** b}")

# Q8.Take input of total minutes and convert them into hours and remaining minutes.
# M = int(input("enter minutes :"))
# H = M // 60
# RM = M % 60
# print (f"{H} hr {RM} min")