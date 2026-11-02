'''Armstrong no '''
#check 153 is armstrong or not
#steps 

#1**3     =   1
#5**3     =   125
#3**3     =   27

#then sum(+) all number the ans is {153} that means the number is 
#armstrong
'''in code'''
# n = 153
# length = len(str(n))
# sum = 0
# temp = n

# while n > 0:
#     last = n % 10
#     sum = sum + last**length 
#     n = n // 10
# print(sum)

# if sum == temp:
#     print("Armstrong Number")
# else:
#     print("Not Aemstrong Number")