'''Methods in Dictionary'''

'''1.   .keys()'''

# d = {"ravi" : 80 , "rohan" : 23 , "devraj" : 88}
# print(d.keys())

'''2.   .values()'''
# print(d.values())

'''3.  .items()  -> both keys and values'''
# print(d.items())


'''4.   .pop()    -> key and remove both key and value'''
# d.pop("rohan")
# print(d)


# d = {1:10 , 2:20 , 3:30 , 4:40}

'''5.   .get()  -> agar key present h dictionary so we
                   will get value for that key either wise
                   NONE or ANY MESSAGE'''

# print(d.get(5 , "Not Found"))


'''6.   .update()   -> merge two dictionary '''

# a = {1:10 , 2:20 , 3:30}
# b = {4:40 , 5:50 , 6:60}

# a.update(b)
# print(a)



'''Que.'''
# d = {"ravi" : 70 , "rohan" : 40 , "abhishek" : 33}

'''method - 1'''
# print(d.keys())

'''method - 2'''
# for i in d:
    # print(i)

'''method - 3'''
# for keys , value in d.items():
#     print(keys)

'''Que.  Find the total of marks without using SUM()'''
# d = {"ravi" : 70 , "abhishek" : 33 , "rohan" :12}
# total = 0
# for i in d.values():
#     total = total + i
# print(total)






# d = {"ravi" : 70 , "abhishek" : 33 , "rohan" :12}
# for i in d:
#     if d[i] > 50:
#         print(i)

# for name, marks in d.items():
#     if marks >= 50:
#         print(name)





'''Que.  find the student with the highest marks'''

# d = {"ravi" : 70 , "abhishek" : 33 , "rohan" :12}
# lagest = d["ravi"]
# for i in d:
#     if d[i] > lagest:
#         lagest = d[i]
#         print(i , d[i])

# highest = 0
# top = 0
# for name , marks in d.items():
#     if marks > highest:
#         highest = marks
#         top = name
# print(top , highest)


'''Que.  add bonus 5 marks to every students '''
# d = {"ravi" : 70 , "abhishek" : 33 , "rohan" :12}
# for i in d:
#     print(d[i] + 5)

# for i in d:
#     d[i] = d[i] + 5
# print(d)

'''Dictionary practice sheet :16-10-2026'''

'''Q1. Find the Largest Value
Given a dictionary containing numbers, 
find the largest value without using max().

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Output: 40'''

# d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# largest = d["a"]
# for i in d:
#     if d[i] > largest:
#         largest = d[i]
# print(largest)

# d ={'a': 10, 'b': 25, 'c': 15, 'd': 40}
# largest = d["a"]
# for i in d.values():
#     if i > largest:
#         largest = i
# print(largest)

'''Q2. Find the Smallest Value
Given a dictionary containing numbers, 
find the smallest value without using min().

Example:
Input: {'a': 10, 'b': 25, 'c': 5, 'd': 40}
Output: 5'''


# d = {'a': 10 , 'b': 25 , 'c': 5 , 'd': 40}
# smallest = d['a']
# for i in d.values():
#     if i < smallest:
#         smallest = i
# print(smallest)

'''Q3 . Count Even and Odd Values
Count how many values in a dictionary are even and 
how many are odd.

Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}

Output:
Even: 2
Odd: 2'''

# d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
# odd_count = 0
# even_count = 0
# for i in d.values():
#     if i%2 == 0:
#         even_count+=1
#     # elif i%2 != 0:
#     #     odd_count+=1
#     else:
#         odd_count+=1
# print(f"Even = {even_count}")
# print(f"Odd = {odd_count}")

'''Q4.Sum of Even Values
Find the sum of all even values present in a dictionary.

Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}
Output: 30'''

# d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
# even_values_sum = 0
# for i in d.values():
#     if i%2 == 0:
#         even_values_sum+=i
# print(even_values_sum)


'''Q5. Find a Key with a Given Value
Given a dictionary and a value, 
find the key associated with that value.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Value: 20
Output: b'''

# d = {'a':10,'b':20,'c':30}
# value = 20
# for i in d:
#     if d[i] == value:
#         print(i)

'''Q6.Update All Values
Increase every value in a dictionary by 5.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Output: {'a': 15, 'b': 25, 'c': 35}'''

# d = {'a': 10, 'b': 20, 'c': 30}
# for i in d:
#     print(d[i]+5)

# d = {'a': 10, 'b': 20, 'c': 30}
# for i in d:
#     d[i] = d[i] + 5
# print(d)

'''Q7.Count Values Greater Than a Number
Count how many dictionary values are greater 
than a given number.

Example:
Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
Number: 20
Output: 2'''

# d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# count = 0
# for i in d:
#     if d[i] > 20:
#         count+=1
# print(count)

'''Q8. Create a Dictionary from Two Lists
Given two lists, create a dictionary where the 
first list contains keys
and the second list contains values.

Example:
Keys: ['a', 'b', 'c']
Values: [10, 20, 30]

Output:
{'a': 10, 'b': 20, 'c': 30}'''

# keys = ['a','b','c']
# values = [10 ,20, 30]

# d = {}

# for i in range(len(keys)):
#     d[keys[i]] = values[i]
# print(d)

'''Q9.Count Values Equal to a Given Number
Given a dictionary and a number, 
count how many times that number
appears as a value in the dictionary.

Example:
Input: {'a': 10, 'b': 20, 'c': 10, 'd': 30}
Number: 10
Output: 2'''

# d ={'a': 10, 'b': 20, 'c': 10, 'd': 30}
# count = 0
# number = 10
# for i in d:
#     if d[i] == number:
#         count+=1
# print(count)

'''Q10.Count Positive and Negative Values
Given a dictionary containing numbers, 
count how many values are
positive and how many are negative.

Example:
Input: {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}

Output:
Positive: 3
Negative: 2'''


# d = {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}
# positive = 0
# negative = 0
# for i in d:
#     if d[i] > 0:
#         positive += 1
#     elif d[i] < 0:
#         negative += 1
# print(f"positive = {positive}")
# print(f"negative = {negative}")






# d = {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}
# count_positive = 0
# count_negative = 0
# for i in d:
#     if d[i] > 0:
#         count_positive+=1
#     elif d[i] < 0:
#         count_negative+=1
# print(f"positive = {count_positive}")
# print(f"negative = {count_negative}")