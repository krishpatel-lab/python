'''FOR LOOPS
kaha se jana hai -> kaha tak jana hai -> kaise jana hai
'''
#when u complete a round(loops) is called itration
#automating a task

# a = range(10,50,1)

# for i in a:
#     print("hello world")

'''also write this '''

# for i in range(1,21,1):
#     print(i)


# for i in range(10,81,1):
#     print(i)


# for i in range(-52,40,1):
#     print(i)


# for i in range(100,-101,-1):
#     print(i)

# for i in range(7,71,7):
#     print(i)

# n = int(input("tell your number :"))
# for i in range(n,(n*10)+1,n):
#     print(i)

#For loop practice sheet :29-09-2026
#done - 1/10/2026  

#Q1. Print Numbers from 1 to N
#Take an integer N as input and print all numbers from 1 to N.


# n = int(input("enter number :"))
# for i in range(1,n+1,1):
#     print(i)

#Q2. Print Numbers from N to 1
#Take an integer N as input and print numbers from N to 1.


# n = int(input("enter number :"))
# for i in range(n,0,-1):
#     print(i)

#Q3. Print Even Numbers
#Take an integer N as input and print all even numbers from 1 to N.
# n = int(input("enter number :"))
# for i in range(2,n+1,2):
#     print(i)

#Q4 Print Odd Numbers
#Take an integer N as input and print all odd numbers from 1 to N.

# n = int(input("enter number :"))
# for i in range(1,n+1,2):
#     print(i)

#Q5. Print Multiplication Table
#Take an integer N as input and print its multiplication table from 1 to 10.


# n = int(input("enter number :"))
# for i in range(n,n*11,n):
#     print(i)

#Q6. Sum of First N Natural Numbers
#Take an integer N as input and calculate the sum of numbers from 1 to N.

# sum = 0
# n = int(input("enter number :"))
# for i in range(1,n+1):
#     sum +=i
# print(sum)

#Q7. Count Numbers from 1 to N
#Take an integer N as input and count how many numbers are present from 1 to N.

# count = 0
# n = int(input("enter number : "))
# for i in range(1,n+1):
#     count+=1
# print(count)


#Q8. Print Squares of Numbers
#Take an integer N as input and print the square of each number from 1 to N.


# n = int(input("enter number :"))
# for i in range(1,n+1):
#     # print(i*i)
#     print(i**2)

#Q9. Sum of Even Numbers
#Take an integer N as input and calculate the sum of all even numbers from 1 to N.

# n = int(input("enter number :"))
# sum = 0
# for i in range(0,n+1,2):
#     sum = sum + i
# print("sum =" , sum)

#Q10. Print Multiples of 5
#Take an integer N as input and print the first N multiples of 5.

# n = int(input("enter number :"))
# for i in range(n,n*5+1,n):
#     print(i)


# n = int(input("enter number :"))

# for i in range(1, n + 1):
#     print(i * 5)


# n=5

# for i in range(1,11):
#     ans = n*i
#     print(f"{n} X {i} = {ans}")