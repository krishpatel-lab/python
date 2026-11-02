''' Q1If the number is positive, 
check whether it is greater than 10 or not.
If the number is not positive, 
print "Not Positive".'''

# num = int(input("enter number :"))
# if num > 0:
#     print("num is +")
#     if num >= 10:
#         print("and num > 10")
#     else:
#         print("and num < 10")
# else:
#     print("num is -")

'''Q2. Number Check
Take a number from the user.
If the number is even,
check whether it is divisible by 4.
If the number is odd, print "Odd Number".
'''

# num = int(input("enter number :"))
# if num%2 == 0:
#     if num%4 == 0:
#         print("num is even and div by 4")
#     else:
#         print("num is even and not div by 4")
# else:
#     print("num is odd")


'''
Q3. ATM Withdrawal
Write a Python program to simulate 
simple ATM withdrawal.

Assume that the correct PIN is 1234 
and the account balance is ₹5000.
Ask the user to enter their PIN.
If the PIN is correct, ask them 
to enter the withdrawal amount.


If the withdrawal amount is less than or 
equal to the balance,
print "Withdrawal Successful".
Otherwise, print "Insufficient Balance".

If the PIN is incorrect, print "Incorrect PIN".
'''

# pin = int(input("enter the pin :"))
# if pin == 1234:
#     amount = int(input("amount to withdraw"))
#     if amount < 5000:
#         print("Withdrawn done")
#     else:
#         print("Insuficient balance")
# else:
#     print("Incorect pin")


'''
Q4. Number Game

Take a number from the user.
If the number is positive, 
check whether it is even or odd.

If the number is even, 
check whether it is divisible by 4 or not.

Print the appropriate result.

Example:
Enter number: 12

Output:
Positive
Even
Divisible by 4
'''

# num = int(input("enter number :"))
# if num > 0:
#     if num%2 == 0:
#         if num%4 == 0:
#             print("+ and even and div by 4")
#         else:
#             print("+ and even and not div by 4")
#     else:
#         print("num is + and odd")
# else:
#     print("num is -")


'''
5. Number Comparison
Take two numbers from the user.

If the first number 
is greater than the second number,
check whether the first number is even or odd.

Otherwise, check whether 
the second number is even or odd.

Example:
Enter first number: 15
Enter second number: 10

Output:
First number is greater
First number is odd
'''

# a = int(input("enter first number :"))
# b = int(input("enter second number :"))

# if a > b:
#     print("a is greater")
#     if a%2 == 0:
#         print("Even")
#     else:
#         print("odd")
# if b > a:
#     print("b is greater")
#     if b%2 == 0:
#         print("Even")
#     else:
#         print("odd")


# else:
#     if b%2 == 0:
#         print("a<b and b is even")
#     else:
#         print("a<b and b is odd")




# Nested If Else practice sheet : 28-09-2026   --- 5
# done = 29-09-2026

'''Q1. Number Classification
Take input of two numbers. First check whether the first number is positive. If positive, check whether it is greater than the second number. Otherwise, print First Number is Not Positive.
Input: 10, 5
Output: First Number is Greater'''

# num1 = int(input("enter first number :"))
# num2 = int(input("enter second number :"))
# if num1>0:
#     if num1 > num2:
#         print("first number is greater")
#     else:
#         print("first number is not possitive")


'''
**Q2. Student Result**

Take marks of two subjects as input. 
First check whether the student has passed the first subject (33 or above) 
If yes, check whether the student has passed the second subject. 
Print Pass or Fail.

Input: 45, 60

Output: Pass'''

# marks1 = int(input("enter the first subject marks :"))
# marks2 = int(input("enter the second subject marks :"))
# if marks1 >= 33:
#     if marks2 >= 33:
#         print("pass")
# else:
#     print("fail")


'''
Q3. Age and Permission

Take age and permission (1 for Yes, 0 for No) as input.
First check whether age is 18 or above. If yes,
check whether permission is 1. Print Allowed or Permission Required.

Input: 20, 1
Output: Allowed'''

# age = int(input("enter age :"))
# permission = int(input("enter permission :"))
# if age >= 18:
#     if permission == 1:
#         print("Allowed")
#     else:
#         print("Permission Required")
# else:
#     print("Not Allowed")


'''
Q4. Number Comparison

Take two numbers as input.
First check whether both numbers are equal.
If not equal, check which number is greater.

Input: 10, 20
Output: Second Number is Greater'''

# a = int(input("enter first number :"))
# b = int(input("enter second number :"))
# if a == b:
#     print("a and b are equal")
# else:
#     if a > b:
#             print("a is greater")
#     else:
#         print("b is greater ")

'''
**Q5. Shopping Discount**

Take shopping amount and membership status
(1 for Member, 0 for Non-member) as input.
First check whether the person is a member. If yes,
check whether shopping amount is 1000 or more.
Print Discount Available or No Discount.

Input: 1500, 1
Output: Discount Available'''

# shopping_amount = int(input("enter shopping amount :"))
# membership_status = int (input("enter menbership status :"))
# if membership_status == 1:
#     if shopping_amount >= 1000:
#         print("Discount Available")
#     else:
#         print("No Discount")
# else:
#     print("No Discount")