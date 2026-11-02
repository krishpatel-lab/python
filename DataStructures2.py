'''Q1).print reverse elements in reverse order
reverse the list using the two - pointer appoarch'''

# arr = [10,20,30,40,50]
# n = len(arr)
# mid = n//2
# for i in range(mid):
#     arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
# print(arr)


'''Q2).print + and - element of a list
print both seprately and ingnore zero'''

# a = [10,-5,20,-3,0,8]

# print("positive :")
# for i in a:
#     if i > 0:
#         print(i)

# print("negative :")
# for i in a:
#     if i < 0:
#         print(i)

'''Q3). mean of the list elements 
calculate the average of all elements in a lsit.'''

# a = [10,20,30,40]
# n = len(a)
# sum = 0
# for i in a:
#     sum += i
# print(f"mean is = {sum/n}")

'''Q4). find the grestest element and its index
find the greatest element and print its index '''

# a = [2,96,69,77,145,20]
# max = a[0]
# index = 0
# for i in range(len(a)):
#     elem = a[i]
#     if elem > max:
#         max = elem
#         index = i
# print(f"max is {max} at index {index}")


'''List practice sheet :12-10-2026'''

'''**Q1. Separate Even and Odd Numbers**
Create a list of integers and separate the even and
odd numbers into two different lists.'''

# n = [1, 2, 3, 4, 5, 6]

# print("even :")
# for i in n:
#     if i%2 == 0:
#         print(i)

# print("odd :")
# for i in n:
#     if i%2 != 0:
#         print(i , end = " ")


'''**Q2. Remove Duplicates**

Create a list and remove duplicate 
elements without using set().'''

# a = [1, 2, 3, 2, 4, 1, 5]

'''**Q3. Find the Index of an Element**

Create a list and find the index of a given element 
without using the index() method.'''

# a = [10, 20, 30, 40, 50]
# elem = int(input("enter the number :"))


# for i in a:
#     if i == elem:
#         print(a[i])





'''Q1). missing number '''
# arr = [1,2,4,5]
# n = len(arr)
# og_n = n+1
# og_sum = ((og_n) * (og_n+1)) // 2
# real_sum = 0
# for elem in arr:
#     real_sum += elem

# missing = og_sum - real_sum
# print(missing)


'''Q2). find list is sorted or not means assending order'''

# arr = [10,30,20,40,50]
# is_sorted = True
# n = len(arr)
# for i in range(0,n-1):
#     if arr[i] > arr[i+1]:
#         is_sorted = False
#         break 

# if is_sorted == True: 
#     print("list is sorted")
# else:
#     print("list is un sorted")


'''Q3).check palindromis list'''

# arr = [2,3,15,15,3,2]
# n = len(arr)
# is_palindrome = True
# for i in range(n//2):
#     if arr[i] != arr[n-i-1]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print("list is palindome")
# else:
#     print("list is not a palindrome")




'''online clss 15-10-2026'''


"""
Question: Sort a List in Ascending Order

Write a Python program to sort the elements of a list in
ascending order without using the built-in sort() method.

Example:
Input:  [64, 34, 25, 12, 22, 11, 9]
Output: [9, 11, 12, 22, 25, 34, 64]
"""


# arr = [64, 34, 25, 12, 22, 11, 9]
# n = len(arr)

# for i in range(n):
#     for j in range(n-i-1):    
#         if arr[j] > arr[j+1]:
#             arr[j] , arr[j+1] = arr[j+1] , arr[j]

# print(arr)


        
        
"""
# Find the Pair with the Given Sum
#
# Find all pairs of elements whose sum equals a given target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8]
# Target: 10
#
# Output:
# (2, 8)
# (3, 7)
"""



# arr = [2, 4, 3, 5, 7, 8]
# target = 10
# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         if (arr[i] + arr [j]) == target:
#             print(arr[i],arr[j])






"""
Question: Check Whether a List Is a Sublist of Another List

Write a Python program to check whether all elements of one list
appear consecutively in another list.

Example:
Input:
arr = [10, 20, 30, 40, 50]
sub = [20, 30, 40]

Output:
Sublist Found
"""
# arr =[10, 20, 30, 40, 50]
# n = len(arr)
# sub =[20, 30, 40]
# m = len(sub)
# for i in range(0,n-m+1):
#     if arr[i:i+m] == sub:
#         print("sublist found")
#         break
# else:
#     print("not sublist found")



'''online clss  -> 16-10-2026'''

"""
Question: Rotate a List to the Right by K Positions

Write a Python program to rotate a list to the right by K positions
using a loop.

Example:
Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[4, 5, 1, 2, 3]
# """
# arr = [1, 2, 3, 4, 5]
# k =2
# k = k%len(arr)
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)


"""
Question: Find All Duplicate Elements

Write a Python program to find all elements that appear more than
once in a list. Print each duplicate element only once.

Example:
Input:  [1, 2, 3, 2, 4, 1, 5]
Output: [1, 2]
"""
# arr =[1,2,3,2,4,1,5]
# n = len(arr)
# dup = []
# for i in range(n):
#     count = 1
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             count+=1
#     if count >=2:
#         dup.append(arr[i])
        
# print(dup)




'''online clss -> 17-10-2026'''

"""
Question: Merge Two Sorted Lists Without Using sort()

Write a Python program to merge two sorted lists into a single
sorted list without using the sort() function or any Sorting Algo.

Example:
Input:
arr1 = [1, 4, 7, 10]
arr2 = [2, 3, 8, 9]

Output:
[1, 2, 3, 4, 7, 8, 9, 10]
"""

# arr1 = [1, 4, 7, 10]
# arr2=  [2, 3, 8, 9]

# n1 = len(arr1)
# n2= len(arr2)

# i=0
# j =0
# ans =[]
# while i<n1 and j<n2:
#     if arr1[i]<arr2[j]:
#         ans.append(arr1[i])
#         i+=1
#     else:
#         ans.append(arr2[j])
#         j+=1
# while i < n1:
#     ans.append(arr1[i])
#     i+=1
# while j < n2:
#     ans.append(arr2[j])
#     j+=1
# print(ans)
        
# l1 = [1,4,7,10]
# l2 = [2,3,8,9]

# n1 = len(l1)
# n2 = len(l2)

# ans = []

# i = 0
# j = 0

# while i<n1 and j<n2:
#     if l1[i]<l2[j]:
#         ans.append(l1[i])
#         i+=1
#     else:
#         ans.append(l2[j])
#         j+=1
# while i<n1:
#     ans.append(l1[i])
#     i+=1
# while j<n2:
#     ans.append(l2[j])
#     j+=1
# print(ans)