#SETS
'''1. sets are annoted be {} or set()'''
# s = {}
# s = set()       #EMPTY SET
# print(type(s))

'''2. stores only unique elements and removes duplicate 
ones'''
# s = {1,1,2,2,3,4,5}
# print(s)

'''3. sets are unorderd that means there is no indexing in sets
4. sets are hetrogenous 
5. sets are semi-mutable
'''

#LIST TO SET
# s = {1,1,2,3,4,3}
# print(set(s))

'''SETS METHODS.'''
# s = {1,2,3,4}

'''1.  s.add()    -> adds an element to set'''
# s.add(5)
# print(s)

'''2.  s.remove()   -> removes an element if the element
                       didn't exists we will get an KEYERROR'''
# s.remove(3)
# print(s)

'''3.   s.discard()   ->will not show any error if the 
                        element is not present in set '''
# s = {1,2,3,4}
# s.discard(100)
# print(s)

'''SET OPERATIONS.'''

'''1.  .union()  -> merge both the sets'''
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"UNION -> {s1.union(s2)}")
# print(f"UNION -> {s1 | s2}")

'''2.   .intersection()   ->common elements.'''
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# # print(f"INTESECTION -> {s1.intersection(s2)}")
# print(f"INTERSECTION -> {s1 & s2}")

'''3.   .difference()   -> elements present in one set but not in another'''
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"DIFFERENCE -> {s1.difference(s2)}")
# print(f"DIFFERENCE -> {s2.difference(s1)}")
# print(f"DIFFERENCE -> {s1 - s2}")

'''4.   .symmetric_difference()  -> common element didnt print'''
# s1 = {1,2,3,4}
# s2 = {4,5,6,7,8}
# print(f"SYMMETRIC -> {s1.symmetric_difference(s2)}")
# print(f"SYMMECTRIC -> {s1 ^ s2}")

'''
|     ->    UNION
&     ->    INTERSECTION
-     ->    DIFFERENCE
^     ->    SYMMECTRIC
'''

'''FROZENSET  make any set with of fixed elements we cannot
add element and we cannot remove one.
'''
# s = frozenset([1,2,3,4,5])
# s.add(6)
# print(s)

