                                            # SETS

# set1 = {2, 4, "hello", 2, "abhinav"}
# print(set1)
# print(type(set1))
# print(len(set1))

# count no. of unique elements
# list1 = [3, 4, 6, 2, 3, 2, 3, 5, 6, 7, 9]
# set2 = set(list1)
# print(len(set2))

# set1.add(43)
# print(set1)

# set1.discard("hello")
# print(set1)
# set1.discard("Hiii")
# print(set1)

# set1.remove(2)
# print(set1)
# set1.remove(66) # imp: discard() doesn't give error if not found, remove() gives error
# print(set1)

# if 'hello' in set1:
#     print(True)
# else:
#     print(False)

# set1.clear()
# print(set1)

# set2 = set1
# set2.add(66) # deep copy
# print(set1)

# set3 = set1.copy() # shallow copy
# set3.add(67)
# print(set1)


set2 = {1, 8, 5, 2, 4}
set3 = {8, 2, 9, 6}

#union
# print(set2.union(set3)) # union
# print(set2|set3) # union

# intersection
# print(set2&set3) # intersection
# print(set2.intersection(set3)) # intersection

# difference
# print(set2-set3)
# print(set2.difference(set3))
# print(set3-set2)

# symmetric difference (union - intersection)
# print(set2^set3)
# print(set2.symmetric_difference(set3))


                                                # Dictionaries


# dict1 = {}
# print(dict1)
# print(type(dict1))
# print(len(dict1))

# sets = set({})
# print(sets, type(sets), len(sets))

# dict2 = {1: "brajesh", 2.0: "official", "person": 66, True: "developer", 43+66j: [66, 43, 67]}
# print(dict2) # True overwrote 1

# 1: "brajesh" -> got replaced by True: "developer"
# lists can't be used a key in dictionary since it's an unhashable type

# mutable types aren't hashable : list, set -> unhashable
# immutable types are hashable (they can be used as key in dictionary): tuple, string

# IMP: "1 == True == 1.0"


# dict2[2.0] = "vijay" #IMP: it's using the key
# print(dict2)
# dict2[2] = "engineer" # IMP: key lookup, NOT index access
# print(dict2)

# IMP: Dictionaries don't use indexes, They use keys

# dict2.update({1: "tyrant", "person": "student"})
# print(dict2)

# dict3 = dict(brajesh = 43, person1 = 66, person2 = 67)
# print(dict3)


# dict3.pop(3) # error no such key is present
# dict3.pop("person1")
# print(dict3)

# print(dict3.get("person1")) # dict3.get("person1") = dict3["person1"]

# for key, value in dict3.items(): # items() provides a list of tuples
#     print(key, value)


# for key in dict3.keys():
#     print(key)

# for value in dict3.values():
#     print(value)


# list4 = ["brajesh", "vijay", "yogesh", "shivam", "tapper", "alien", "brajesh", "brajesh"]
# # if {} are used in place of [] -> it will become a set not a list
# freq = {}

# for name in list4:
#     if name not in freq:
#         freq[name] = 1
#     else:
#         freq[name] += 1

# print(freq)

# s = "brajesh prajapati"
# freq = {}

# for name in s:
#     if name not in freq:
#         freq[name] = 1
#     else:
#         freq[name] += 1
# print(freq) # or we can simply use getOrDefault()

# d.get("x")        # IMP: returns None if missing
# d["x"]            # IMP: raises KeyError if missing



# ! list comprehension
ls = [1, 2, 3, 4, 5]
new_ls = [num for num in ls if num % 2 == 0]
print(new_ls) # [2, 4]

