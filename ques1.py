# online clss - 21/10/2026
"""
Question: Find Duplicate Words in a Sentence

Find all words that appear more than once.
Ignore uppercase and lowercase differences.

Input:
"Python is easy and python is powerful and easy"

Output:
['python', 'is', 'easy', 'and']
"""
# sen = "Python.is.easY.and.python.is.powerfuL.and.Easy"
# sen = sen.lower()
# # print(sen)
# words = [] 
# # words = sen.split(" ")
# # word =""

# # for ch in sen:
# #     if ch!=".":
# #         word+=ch
# #     else:
# #         words.append(word)
# #         word =""
# # words.append(word)
# # print(word)
# # print(words)

# # ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful', 'and' ,'easy]
# dup = []

# for i in range(len(words)):
#     count =0
#     for j in range(len(words)):
#         if words[i] == words[j]:
#             count +=1
#     if count>=2 and words[i] not in dup:
#         dup.append(words[i])
# print(dup)
    
'''online clss -> 22/10/2026'''

"""
Question: Group Words of a Sentence by Their Length

Given a sentence, group all unique words by their length into a
dictionary. Ignore uppercase and lowercase differences.

Example:
Input:  "Eat sleep code and repeat code and eat clean"
Output: {3: ['eat', 'and'], 5: ['sleep', 'clean'], 4: ['code'], 6: ['repeat']}
"""

# sen = "Eat sleep code and repeat code and eat clean"
# res = ""
# for ch in sen:
#     if  ord('a') <= ord(ch) <=ord('z'):
#         res += chr(ord(ch)-32)
#     else:
#         res +=ch
# print(res)
        





# ans = {}
# words = sen.split(" ")
# for word1  in words:
#     l = len(word1)
#     temp = []
#     for word2 in words:
#         if  len(word2) == l and word2 not in temp:
#             temp.append(word2)
#     ans[l] = temp
# print(ans)

