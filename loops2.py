'''
take an input n print natural no upto n
# '''
# n = int(input("enter number :"))
# for i in range(1,n+1,1):
#     print(i)

'''print from n to 1'''

# n = int(input("enter number :"))
# for i in range(n,0,-1):
#     print(i)

'''print sum'''

# sum = 0
# n = int(input("enter number : "))
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n = int(input("enter number :"))
# sum = 0
# for i in range(1,n+1,):
#     sum = sum+i
# print("sum =" , sum)

'''print factorial'''

# fact = 1
# n = int(input("enter number: "))
# for i in range(1,n+1):
#     fact*=i
# print(fact)


# n = int(input("enter number :"))
# fac = 1
# for i in range(1,n+1,):
#     fac = fac*i
# print(fac) 

'''print the factors of n'''

# n = int(input("enter number :"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# For loop practice sheet :30-09-2026

'''Q1.Weekly Attendance Analysis

An institution records the attendance status of a student for 
7 consecutive days**. The status is entered as P for Present and
A for Absent.

Write a program to determine the **total number of days the student
was present and absent.'''

# count1 = 0
# count2 = 0

# for i in range(7):
#     atten = input("enter attendence P/A or p/a :")
#     if atten == "p" or atten == "P":
#         count1 += 1
#     elif atten == "a" or atten == "A":
#         count2 += 1
# print(f"present = {count1}")
# print(f"absent = {count2}")

'''Q2. Product Quality Inspection

A factory inspects **10 products. For each product,
enter 1 if it passes inspection and 0 if it fails.

Determine the **number of products that passed and failed
the inspection.'''
# count1 = 0
# count2 = 0
# for i in range(10):
#     a = int(input("enter product 1/0 :"))
#     if a == 1:
#         count1 = count1 + 1
#     else:
#         count2 = count2 + 1
# print(f"pass product is {count1}")
# print(f"fail product is {count2}")




'''Q3. Monthly Savings Analysis

A person records the amount saved on **7 different days.

Write a program to calculate the **total savings and
determine how many days the savings were greater than ₹500'''

# sum = 0
# days = 0
# for i in range(7):
#     record = int(input("enter amount :"))
#     sum = sum + record
#     if record > 500:
#         days = days + 1
# print(f"total saving amount in 7 days is = {sum} and no of days > 500 is = {days}")




'''Q4. Electricity Consumption

A household records its electricity consumption for 7 days.

Write a program to calculate the **total units consumed and
count how many days the consumption was **more than 10 units.'''

# count = 0
# sum = 0

# for i in range(7):
#     units = int(input("enter units :"))
#     sum = sum + units
#     if units > 10:
#         count += 1
# print(f"7 days consume units is = {sum}")
# print(f"consumption more than 10 units = {count}")


'''Q5. Attendance Eligibility

A student has 10 classes. For every class,
enter P for Present and A for Absent.

Calculate the student’s **attendance percentage and
display whether the student has 75% or more attendance'''

# count1 = 0
# count2 = 0

# for i in range(10):
#     atten = input("enter attendance (P/A)")
#     if atten.upper() == "P":
#         count1+=1
#     else:
#         count2+=1
# formula = (count1/10)*100
# print(f"attenfdance = {formula}")
# if formula >= 75:
#     print("student is eligible")
# else:
#     print("Student is not eligible")


# count1 = 0
# count2 = 0

# for i in range(10):
#     days = input("enter attendance p/a :")
#     if days == "p":
#         count1 += 1
#     else:
#         count2 += 1
# formula = (count1 / 10)*100
# print(f"attendance percantage is = {formula}")
# if formula == 75:
#     print("attendance is 75%")
# elif formula > 75:
#     print("attendance is > 75")
# else:
#     print("attendance is < 75")

'''count factors of a number '''

# n = int(input("enter number :"))
# count = 0

# for i in range(1,n+1):
#     if n%i==0:
#        count += 1  
#     #    count = count+1           #we write also this                   
# print(f"Factors of {n} are : {count}")


# n = int(input("enter number :"))
# count = 0

# for i in range(1,n+1):
#     if n%i==0:
#        count += 1                          
# print(f"Factors of {n} are : {count}")

# if count == 2:
#     print(f"{n} is a prime number") 
# else:
#     print(f"{n} is a composite number")


# n = int(input("enter number :"))

# #1 and number itself are factors.
# for i in range(2,n):
#     if n % i == 0:
#         print(f"{n} is a composite number")
#         break
# else:
#     print(f"{n} is a prime number")


# name = "KRisHPaTeL"

# upper = 0
# lower = 0

# for i in name:
#     if i.isupper():
#         upper += 1
#     elif i.islower():
#         lower += 1

# print(f"Upper case letters : {upper}")
# print(f"lower case letters: {lower}")