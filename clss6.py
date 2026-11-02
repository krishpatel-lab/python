# Q1
# check if an alphabet is vowel or consonant
# ch = input("enter the alphabet :")
# if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#     print ("vowel")
# else:
#     print("consonent")

#in means “is present inside” or “belongs to.”
# ch = input("enter character :")
# if ch in "aeiouAEIOU":
#     print("vowel")
# else:
#     print ("consolant")

# take a input of 3 subjects and print pass after all three sub 
# marks is greater then40 otherwise print fail 

# maths = int(input("enter marks :"))
# science = int(input("enter marks :"))
# english = int(input("enter marks :"))
# if maths > 40 and science > 40 and english > 40:
#     print ("pass")
# else:
#     print ("fail")


# a = int(input("enter first no :"))
# b = int(input("enter second no :"))
# c = int(input("enter third no :"))
# if 


#if Else Practice sheet p26 :26-09-2026 --- 4
#Done - 27-09-2026

#Q1 Take input of a number and check whether it is greater than 5 or not
# a = int(input("enter the number :"))
# if a > 5:
#     print("greater then 5")
# else:
#     print("less then 5")

#Q2. Check Number is Less Than 100
#Take input of a number and check whether it is less than 100 or not.
# a = int(input("enter number :"))
# if a < 100:
#     print("less then 100")
# else:
#     print("greater then 100")

#Q3. Check Age
# Take age as input. If the age is 18 or more, print Can Drive, otherwise print Cannot Drive.
# age = int(input("enter age :-"))
# if age >= 18:
#     print("Drive")
# else:
#     print("Cannot Drive")

#Q4. Check Number is Zero or Not
#Take input of a number and check whether it is zero or not.
# a = int(input("enetr number :-"))
# if a == 0:
#     print("Zero")
# else:
#     print("Not a zero")

#Q5. Check Marks
#Take marks as input. If marks are 50 or more, print Good, otherwise print Try Again.
# marks = int(input("enter marks :-"))
# if marks >= 50:
#     print("Good")
# else:
#     print("Try Again")

#Q6. Check Price
#Take price as input. If the price is greater than 500, print Expensive, otherwise print Affordable.
# price = int(input("enter price:-"))
# if price > 500:
#     print("Expensive")
# else:
#     print("Affordable")

#Q7. Check Number Divisible by 5
#Take input of a number and check whether it is divisible by 5 or not.
# a = int(input("enter number :"))
# if a%5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not a divisible by 5")

#Q8. Check Password
#Take a password as input. If the password is 12345, print Correct, otherwise print Incorrect.
# password = int(input("enter password :"))
# if password == 12345:
#     print("Correct")
# else:
#     print("Incorrect")

#Q9. Check Attendance
#Take attendance percentage as input. If it is 75 or more, print Allowed, otherwise print Not Allowed.
# attendance = int(input("enter attendance :-"))
# if attendance >= 75:
#     print("Allowed")
# else:
#     print("Not Allowed")

#Q10. Check Shopping Amount
#Take shopping amount as input. If the amount is 1000 or more, print Free Delivery, otherwise print Delivery Charges.
# shopping_amount = int(input("enter amount :"))
# if shopping_amount >= 1000:
#     print("Free Delivery")
# else:
#     print("Delivery charges")

#26/09/2026 class6
#Python Conditional Statements - Practice Questions

## Q1. Grade Calculator

# Take the marks of a student as input.

# Print the grade according to the following rules:

# - 90 or above → `"A"`
# - 75 to 89 → `"B"`
# - 60 to 74 → `"C"`
# - 40 to 59 → `"D"`
# - Below 40 → `"Fail"`

# a = int(input("enter marks :"))
# if a >= 90:
#     print("Grade A")
# elif a > 75:
#     print("Grade B")
# elif a > 60:
#     print("Grade C")
# elif a > 40:
#     print("Grade D")
# else:
#     print("Fail")

#Q2. Simple Calculator

# Take two numbers and an operator as input.
# The operator can be:

# - `+`
# - 
# - 
# - `/`

# Perform the corresponding operation and print the result.
# If the user enters an invalid operator, print `"Invalid Operator"`

# a = int(input("enter number :"))
# b = int(input("enter number :"))
# op = input("enter operator :")
# if op == "+":
#     print(a+b)
# elif op == "-":
#     print(a-b)
# elif op == "*":
#     print(a*b)
# elif op == "/":
#     print(a/b)
# elif op == "**":
#     print(a**b)
# else:
#     print("Invalid Operator")

#Q3. Day Number
# Take a number from 1 to 7 as input.
# Print the corresponding day:

# - 1 → Monday
# - 2 → Tuesday
# - 3 → Wednesday
# - 4 → Thursday
# - 5 → Friday
# - 6 → Saturday
# - 7 → Sunday
# If the number is outside 1 to 7, print `"Invalid Day"`.

# num = int(input("enter number :"))
# if num < 1 or num > 7:
#     print("Invalid Day")
# elif num == 1:
#     print("Monday")
# elif num == 2:
#     print("Tuesday")
# elif num == 3:
#     print("Wednesday")
# elif num == 4:
#     print("Thursday")
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday")
# elif num == 7:
#     print("Sunday")

# #Q4. Divisibility Checker
# Take an integer as input.
# Check whether the number is:
# - Divisible by both 3 and 5
# - Divisible only by 3
# - Divisible only by 5
# - Not divisible by either 3 or 5
# Print the appropriate message.

# a = int(input("enter number :"))
# if a%3 == 0 and a %5 == 0:
#     print("Divisible by both 3 and 5")
# elif a%3 == 0:
#     print("Divisible only by 3")
# elif a%5 == 0:
#     print("Divisible only by 5")
# else:
#     print("Not divisible by either 3 or 5")

# Q5. Triangle Type
# Take three sides of a triangle as input.
# Check the type of triangle:
# - If all three sides are equal → `"Equilateral"`
# - If any two sides are equal → `"Isosceles"`
# - If all three sides are different → `"Scalene"`

# a = int(input("enter side 1 :"))
# b = int(input("enter side 2 :"))
# c= int(input("enter side 3 :"))

# if a == b and b == c and c == a:
#     print("Equilateral")
# elif a == b or b == c or c == a:
#     print("Isosceles")
# else:
#     print("Scalene")

#Q6. Shopping Delivery Charge
# Take the shopping amount as input.
# Calculate the delivery charge:
# - Amount below ₹500 → ₹50 delivery charge
# - Amount from ₹500 to ₹999 → ₹30 delivery charge
# - Amount ₹1000 or above → Free delivery
# Print the final amount including the delivery charge.

# a = int(input("enter amount :"))
# if a < 500:
#     print(f"final amount = {a+50}")
# elif a < 999:
#     print(f"final amount = {a+30}")
# else:
#     print(f"final amount = {a}")


'''Q7. Time of Day

Take the hour as input in 24-hour format.
Print:
- 5 to 11 → `"Morning"`
- 12 to 16 → `"Afternoon"`
- 17 to 20 → `"Evening"`
- 21 to 23 or 0 to 4 → `"Night"`
If the hour is outside `0-23`, print `"Invalid Hour"`.'''

# hr = int(input("enter the hour :"))
# if hr >= 5 and hr <= 11:
#     print("Morning")
# elif hr >= 12 and hr <= 16:
#     print("Afternoon")
# elif hr >= 17 and hr <= 20:
#     print("Evening")
# elif (hr >= 21 and hr <= 23) or (hr >= 0 and hr <= 4):
#     print("night")
# else:
#     print("Invalid hour")


'''
Q8. Electricity Bill

Take the number of units consumed as input.
Calculate the electricity bill according to these rules:
- Up to 100 units → ₹5 per unit
- 101 to 200 units → ₹7 per unit
- Above 200 units → ₹10 per unit

Print the total bill.'''

# unit = int(input("enter units :"))
# if unit <= 100:
#     print(f"Electricity Bill = {unit*5}")
# elif unit <= 200:
#     print(f"Electricity Bill = {unit*7}")
# else:
#     print(f"Electricity bill = {unit*10}")


'''
Q9. Bus Ticket Fare
Take the age of a passenger as input.
The normal ticket price is ₹200.

Apply the following rules:

- Age below 5 → Free
- Age 5 to 17 → 50% discount
- Age 18 to 59 → Full price
- Age 60 or above → 30% discount
Print the final ticket price.'''

# age = int(input("enter age :"))
# if age < 5:
#     print("Free")
# elif age <= 17:
#     print(f"Ticket price = {200 - (200*50)//100}")
# elif age <= 59:
#     print("Ticket price = 200")
# else:
#     print(f"Ticket price = {200 - (200*30)//100}")

'''
Q10. Exam Eligibility

Take a student's attendance percentage and marks as input.
A student is eligible to appear for the final exam only if:
- Attendance is **75% or above**
- Marks are **40 or above**

# If both conditions are satisfied, print "Eligible".
# Otherwise, print Not Eligible'''

# att = int(input("enter attendance percentage :"))
# marks = int(input("enter marks :"))
# if att >= 75 and marks >= 40:
#     print("Eligible")
# else:
#     print("Not Eligible")