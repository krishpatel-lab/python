'''data structures.'''
#list
'''
1. square brackets -> list[]
2. heterogenous data structure  (a list can store different
data type together)
3. list allows storing duplicate values
4. list are ordered - because they have indexing
and indexing starts from 0
5. list are mutable -> we can change any value anytime
and anywhere'''

# marks = []    #empty list

# marks = [65,56,75,64,6,5,66,45, "krish" , 3.14 , True , 2+1j]
# print(marks)
# print(marks[3])      #index
# print(marks[1:6])      #slicing


# marks = [80,78,80,90,"shreyians",3.14]
# print(marks)
# marks[3] = "modiji"
# print(marks)




'''Traversing'''

# a = [10,20,30,40,50]
# for i in a:
#     print(i)

'''agar kisi keyword ke aage "." nahi laga that 
is a function
AND
"." laga toh methods'''


#Methods in list
'''1.  .append() add the value at the last of list.'''
# marks = [10,20,30,40]
# marks.append(50)
# print(marks)

'''2.   .extend()'''
# marks2 = [70,80,90]
# marks.extend(marks2)
# print(marks)

'''3.  .insert(index , value)'''
# marks.insert(3 , 90)
# print(marks)

'''4.   .remove()'''  #->remove any value from the list but the value is repeated remove the first value 
# a = [10,20,30,40,50]
# a.remove(10)
# print(a)

'''5.   .pop()''' # -> remove any value basis on the index
# a = [10,20,30,40,50]
# a.pop(3)
# print(a)

'''6.   .clear()'''  #-> removes every element and gives empty list
# a = [10,20,30,40,50]
# a.clear()
# print(a)

'''7.  del'''  #-> remove list to the memory
# a = [10,20,30,40,50]
# del a
# print(a)


'''shallow copy'''      #this will change both a and b value
# a = [1,2,3,4,5]
# b = a
# b[3] = 100
# print(a)
# print(b)



'''deep copy'''        # the only change b value index
# a = [1,2,3,4,5]
# b = a.copy()     #deep copy
# b[3] = 100
# print(a)
# print(b)



# a = [1,2,3,4,4,5]
# for i in a:
#     print(i)
# print(len(a))

# a = [10,20,30,40,50,60,70,80]
# for i in range(len(a)):
#     print(i , a[i])

# a = [10,20,30,40,50,60,70,80]
# for i in range(len(a)-1 , -1 , -1):
#     print(i , a[i])

# a = [10,20,30,40,50,60,70,80]
# a2 = []
# for i in range(len(a)-1 , -1 , -1):
#     a2.append(a[i])
# #     a2.insert(len(a2) , a[i])
# print(a2)



'''List practice sheet :09-10-2026'''



'''Q1. Find the Smallest Element

Create a list of numbers and find the smallest element
without using the min() function.'''


# a = [10,20,30,40,50,60,4,2,6,90,1000]
# smallest = a[0]

# for i in a:
#     if i < smallest:
#         smallest = i

# print(f"smallest digit = {smallest}")


'''Q2. Count Positive and Negative Numbers

Create a list and count the number of positive and 
negative elements. Ignore zeros.'''

# a = [10, -5, 20, -8, 0, 7]
# count1 = 0
# count2 = 0
# count3 = 0

# for i in a:
#     if i > 0:
#         count1 += 1
#     elif i < 0:
#         count2 += 1
#     else:
#         count3 +=1

# print(f"positive = {count1}")
# print(f"negative = {count2}")
# print(f"zeroes = {count3}")

'''Q3. Calculate the Average

Create a list of numbers and calculate the average 
of all its elements.'''

# a = [10, 20, 30, 40]
# sum = 0
# for i in a:
#     sum = sum + i
#     average = sum/4

# print(average)

'''Q4. Count Occurrences of an Element

Create a list and count how many times a given number appears in it.'''

# a = [2, 4, 2, 6, 2, 8]
# count = 0
# for i in a:
#     if i == 2:
#         count += 1
# print(count)


'''Q5. Print Elements at Even Indices

Create a list and print the elements present at 
even indices (0, 2, 4, …).'''

# a = [10, 20, 30, 40, 50, 60]
# print(a[0:len(a):2])

'''Q6. Find the Second Largest Element

Create a list and find the second largest distinct 
element without using sort() or max().'''

# a = [10, 25, 15, 40, 30]

# largest = a[0]
# second_largest = None

# for i in a:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i < largest:
#         if second_largest == None or i > second_largest:
#             second_largest = i
# print(second_largest)



'''Q7). Replace Negative Numbers with Zero
Create a list and replace every negative element with 0.'''

# a = [10, -5, 20, -8, 7]
# b = []
# for i in a:
#     if i < 0:
#         i = 0
#     b.append(i)
# print(b)


'''Q8. Find the Sum of List Elements

Create a list of numbers and calculate 
the sum of all its elements.'''

# a = [10, 20, 30, 40]
# sum = 0
# for i in a:
#     sum +=i
# print(sum)


'''Q9. Find the Largest Element

Create a list of numbers and find 
the largest element without using the max() function.'''

# a = [12, 45, 23, 67, 34]
# largest = a[0]
# for i in a:
#     if i > largest:
#         largest = i
#     else:
#         largest = largest 
# print(largest)


'''Q10. Reverse a List

Create a list and reverse its elements 
without using the reverse() method.'''

# a = [10, 20, 30, 40, 50]
# b = []
# for i in range(a+1,0,-1):
#     b.append(a)
# print(a)


# a = [10,20,30,40,50,60,70,80]
# a2 = []
# for i in range(len(a)-1 , -1 , -1):
#     a2.append(a[i])
# #     a2.insert(len(a2) , a[i])
# print(a2)

