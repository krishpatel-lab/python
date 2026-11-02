'''DICTIONARY
 1. dictionary annoted by {curly bracket}
 2. dictionary are combination of multiple 
 keys:values
 3. dictionary are mutable
 4. dictionary are hetrogenous 
 5. in dictionary keys will be unique but values can be duplicate
 6. dictionary are order 

 '''

# d = {1:10 , 2:20 , 3:30}
# # d[4] = 100    #creating a new key:value pair which never exist 
# # print(d)
# for i in d:
#     print(i , d[i])



'''Dictionary practice sheet : 15-10-202'''

'''
**Q1. Create a Dictionary**

Create a dictionary containing your name, age, and
city. Print the dictionary.
**Example Output:**

{'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}'''

# d = {"name" : "krish patel" , "age" : 19 , "city" : "bhopal"}
# print(d)


'''**Q2. Access a Value**

Given a dictionary, print the value associated with 
the key "name".

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output: Rahul'''

# d = {"name" : "krish patel" , "age" : 19 , "city" : "bhopal"}
# print(d["name"])

'''
**Q3. Add a New Key-Value Pair**

Add a new key "course" 
with value "Python" to the given dictionary.'''

# d = {"name" : "krish patel" , "age" : 19}
# d["course"] = "python"
# print(d)

'''
**Q4. Update a Value**
Update the age of a person to 21.

**Example:**
- Input: {'name': 'Rahul', 'age': 20}
- Output: {'name': 'Rahul', 'age': 21}'''

# d = {"name" : "krish patel" , "age" : 19}
# d["age"] = 21
# print(d)

'''
**Q5. Delete a Key**
Remove the key "city" from the dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output: {'name': 'Rahul', 'age': 20}'''

# d = {"name" : "krish patel" , "age" : 19 , "city" : "bhopal"}
# del d["city"]
# print(d)

'''
**Q6. Check if a Key Exists**
Check whether the key "age" exists in the given dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20}
- Output: Key exists'''

# d = {"name" : "krish patel" , "age" : 19}
# for i in d:
#     if i == "age":
#         print("Key exists")
 
# d = {"name" : "krish patel" , "age" : 19}
# if "age" in d:
#     print("Key exists")
# else:
#     print("Key doesnt exists")

'''
**Q7. Print All Keys**
Print all the keys present in a dictionary using a loop.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output:
name
age
city'''


# d = {"name" : "krish patel" , "age" : 19 , "city" : "bhopal"}
# for i in d:
#     print(i)

'''**Q8. Print All Values**
Print all the values present in a dictionary using a loop.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output:
Rahul
20
Bhopal'''

# d = {"name" : "krish patel" , "age" : 19 , "city" : "bhopal"}
# for i in d:
#     print(d[i])

'''
**Q9. Count Key-Value Pairs**
Count the total number of key-value pairs in a 
dictionary without using len().

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 3'''

# d = {"a" : 10 , "b" : 20 , "c" : 30}
# count = 0
# for i in d:
#     count+=1
# print(count)

'''**Q10. Calculate the Sum of Values**
Calculate the sum of all numerical values in 
a dictionary using a loop.

**Example:**

- Input: {'a': 10, 'b': 20, 'c': 30}
- Output: 60'''

# d = {"a" : 10 , "b" : 20 , "c" : 30}
# sum = 0
# for i in d:
#     sum = sum + d[i]
# print(sum)