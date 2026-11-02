#online class - 5/10/2026
"""
# Q1. Count Numbers Divisible by Both 3 and 5
#
# Take an integer N as input and count how many numbers from 1 to N
# are divisible by both 3 and 5 (multiples of 15).
#
# Example:
# Input: 35
# Output: 2
# (Explanation: The numbers are 15 and 30. Total count = 2)
"""


# n = int(input("enter the number")) 
# count = 0
# #  1 -> N+1
# for i in range(1,n+1):
#     if i % 3 ==0 and i%5==0:
#         count+=1
# print(f"count : {count}")
        



"""
# Q2. Factorial of a Number
#
# Take an integer N as input and 
# calculate its factorial.
# Factorial of N (N!) is the
# product of all positive integers from 1 to N.
# (0! = 1, 5! = 5 * 4 * 3 * 2 * 1 = 120)
#
# Example:
# Input: 5
# Output: 120
"""
# n = int(input("enter the num"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(f"{n}! is {fact}")




"""
# Q3. Check Strong Number 
#
# Take an integer N as input and
# check whether it is a Strong Number.
# A Strong Number is a number
# whose sum of factorials of its
# digits equals the original number.
#
# Example:
# Input: 145
# 1! = 1
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Sum: 1 + 24 + 120 = 145
# Output: Strong Number
"""


# n = int(input("enter the number"))
# temp = n
# sum = 0
# while n >0:  
#     digit = n%10
#     # digit!
#     fact = 1
#     for i in range(1,digit+1):
#         fact*=i
#     sum +=fact
#     n = n//10
# if temp == sum:
#     print("strong number")
# else:
#     print("not a strong number")




"""
# Q4. Sum of Odd Numbers from 1 to N
#
# Take an integer N as 
# input and calculate the sum of all odd numbers from 1 to N.
#
# Example:
# Input: 10
# Output: 25
# (Explanation: 1 + 3 + 5 + 7 + 9 = 25)
"""


# n = int(input("enter the number"))

# sum = 0
# for i in range(1, n+1):
#     if i %2!=0:
#         sum+=i
# print(f"sum of odd numbers from 1 to {n} is {sum}")



# 6/10/2026

"""
# Q5. Print Fibonacci Series up to N Terms
#
# Take an integer N as input and print the first N terms of the Fibonacci series.
# In Fibonacci series, each number is
# the sum of the previous two numbers (starts with 0, 1).
#
# Example:
# Input: 6
# Output:
# 0 1 1 2 3 5
"""

# n = int(input("enter number :"))
# a = 0
# b = 1
# for i in range(n):
#     print(a , end = " ")
#     c = a + b
#     a = b
#     b = c



"""
# Q6. Count Vowels in a String
#
# Take a string as input 
# and count how many vowels (a, e, i, o, u) are present in it.
# Check both lowercase and uppercase 
# vowels without using any string functions.
#
# Example:
# Input: "AbhiSHEK"
# Output:
# Total vowels: 3  (A, i, E)
"""


# name = input("enter name :")
# count = 0
# for ch in name:
#     if ch in "AEIOUaeiou":
#         count += 1
# print(f"total vowel = {count}")



"""
# Q7. Count Occurrences of a Character in a String
#
# Take a string and a target 
# character as input from the user.
# Count how many 
# times that character appears in the string using a loop.
# (Do not use any built-in functions)
#
# Example:
# Enter string: banana
# Enter character to search: a
# Output:
# 'a' appears 3 times
"""


# text = input("enter the text :")
# target = input("enter the charater :")
# count = 0
# for ch in text:
#     if ch == target:
#         count += 1
# print(count)


'''7/10/26'''


"""
# Q8. Print All Numbers Ending with 7 from 1 to N
#
# Take an integer N as input and 
# print all numbers from 1 to N that end with the digit 7.
#
# Example:
# Input: 40
# Output:
# 7 17 27 37
"""
# write a function of this code and return me list
# return 
# list [] 
# append 

# def numbers_ending_with_7(n):
#     result = []
#     for i in range(1,n+1):
#         if i%10==7:
#             result.append(i)
#     return result

# n = int(input("enter the number")) #40
# ans1 =numbers_ending_with_7(n)
# m = int(input("enter the number"))  #20
# ans2 = numbers_ending_with_7(m)
# print(f" fist ans : {ans1}  , second ans : {ans2}")

# n = int(input("enter the number :"))
# for i in range(1,n+1):
#     if i%10 == 7:
#         print(i , end = " ")

# def number_ending_with_7(n):
#     result = []
#     for i in range(1,n+1):
#         if i%10 == 7:
#             result.append(i)
#     return result
# n = int(input("enter number :"))
# print(number_ending_with_7(n))
# m = int(input("enter number :"))
# print(number_ending_with_7(m))


"""
# Q9. Check Harshad (Niven) Number

# Take an integer N as input and 
# check whether it is a Harshad Number.
# A Harshad number is a number 
# that is completely divisible by the sum of its digits.
#
# Example 1:
# Input: 18  -> Sum of digits: 1 + 8 = 9 -> 18 % 9 == 0
# Output: Harshad Number
#
# Example 2:
# Input: 14  -> Sum of digits: 1 + 4 = 5 -> 14 % 5 != 0
# Output: Not a Harshad Number
"""

# n = int(input("enter number :"))
# temp = n
# sum = 0
# while n > 0:
#     digit = n%10
#     sum += digit
#     n //= 10
# if sum > 0 and temp%sum == 0:
#     print("harshad number")
# else:
#     print("not a harshad number")


'''8/10/26'''

"""
# Q10. Digit Frequency

# Take an integer N as input and count how many times
# each digit from 0 to 9 occurs in the number.
#
# Example:
# Input: 122333
#
# Output:
# 1 -> 1
# 2 -> 2
# 3 -> 3
"""

# n = int(input("enter number :"))

# for digit in range(0,10):
#     temp = n
#     count_digit = 0

#     while temp > 0:
#         last_digit = temp%10
#         if last_digit == digit:
#             count_digit += 1
#         temp //= 10
#     if count_digit > 0:
#         print(f"{digit} -> {count_digit}")





"""
# Q11. Find the Smallest Digit in a Number
#
# Take an integer N as input
# and find the smallest digit present in it.
#
# Example:
# Input: 64825
# Output: 2
"""

# n = int(input("enter number :"))
# temp = n
# smallest = 9
# while temp > 0:
#     digit = temp%10
#     if digit < smallest:
#         smallest = digit  
#     temp//=10
# print(f"smallest digit in {n} is = {smallest}")  

