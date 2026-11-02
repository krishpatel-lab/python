'''WHILE LOOPS
kaha se jana hai -> kab tak jana hai -> kaise jana hai

while jab tak yeh condition true hai:
    tab tak yeh code chalega.

jab tak whlie condition false nhi hojati tab tak
loop chale ga 
'''


'''1 - 10 print using while loop'''

# i = 1
# while i <= 50:
#     print(i)       #infinite loop

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1

'''10 - 1'''

# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

'''take input '''

# password = ""
# while password != "Krishpatel":
#     password = input("enter your password :")
# print("Access Granted")

# password = input("enter your password")

# while password != "Krishpatel":
#     password

'''print table of any number take input from user using while loop
'''

# a = int(input("enter number :"))
# i = 1
# while i <= 10:
#     print(a*i)
#     i = i + 1

'''print even number from 2 to 20'''
# i = 2
# while i <= 20:
#     print(i)
#     i = i + 2


'''print sum of even number from 2-20'''
# i = 2
# sum = 0
# while i <= 20:
#     sum = sum + i
#     print(i)
#     i = i +2
# print(f"sum of even number from 2 to 20 is = {sum}")

'''print a number in reverse order 1234'''
#% last digit ko print krwana 
#// last digit permanent remove

# n = 1234
# while n != 0:
#     print(n % 10)
#     n = n // 10


'''line m '''
# n = 1234
# a = 0
# while n > 0:
#     last = n % 10
#     a = a*10 + last
#     n = n // 10
# print(a)

'''how many digit in the number  '''
# n = 1234
# a = 0
# count = 0
# while n > 0:
#     last = n % 10
#     count = count + 1
#     a = a*10 + last
#     n = n // 10
# print(a)
# print(count)

# while loop problems:02-10-2026

'''Q1. Difference between Sum of Odd numbers and Sum of Even Numbers

Take an integer N as input. 
Calculate the sum of even numbers and 
the sum of odd numbers from 1 to N, 
then find the difference between the two sums.'''


# n = int(input("enter number :"))
# even_sum = 0
# odd_sum = 0
# i = 1
# while i <= n:
#     if i%2 == 0:
#         even_sum += i
#     elif i%2 != 0:
#         odd_sum += i
#     i = i + 1
# if even_sum > odd_sum:
#     diff = even_sum - odd_sum
# else:
#     diff = odd_sum - even_sum
# print(f"the difference is = {diff}")

'''Q2. Difference Between Largest and Smallest

Take N numbers as input and calculate the difference between 
the largest and smallest number.'''

# n = int(input("Enter how many numbers: "))

# largest = None
# smallest = None

# for i in range(n):
#     num = int(input("Enter number: "))

#     if largest is None or num > largest:
#         largest = num

#     if smallest is None or num < smallest:
#         smallest = num

# difference = largest - smallest

# print("Largest number =", largest)
# print("Smallest number =", smallest)
# print("Difference =", difference)