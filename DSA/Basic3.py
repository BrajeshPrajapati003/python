# names = ["brajesh", "ravi", "shivam", "yogesh", "divyansh", 43, 43, 66, 66, True, 1.00, 2, 43+66j]

# print(names)
# print(type(names))
# print(len(names))

# print(names[0])
# print(names[-1])
# names[1] = "aditya"
# print(names)
# names.append(67)
# names.append([66, 67]) # ctx: the list will be considered as a single element
# names.extend([43, 66]) # ctx: elements will be inserted one by one (considered as different elements)
# print(names)

# names.insert(3, "anime")
# print(names)

# print(names.count(66))
# list1 = [43, 67, 66]
# print("min: ", min(list1), "max: ", max(list1), "count: ", names.count(43))
# list1.sort()
# print("sorted: ", list1)
# list1.reverse()
# print(list1)


# list2 = [1, 2, 3, 8, 3, 5, 9]
# list3 = list2
# list3.append(43)
# print(list2)

# list4 = list2.copy()
# list4.append(66)
# print(list4)

# print(id(list2))
# print(id(list4))


# tuple1 = (43, 66, 67, "brajesh", True)
# tuple2 = tuple1 # ctx: tuples can't be modified

# print(tuple1, id(tuple1))
# print(tuple2, id(tuple2))

# tuple1 = (43, 67, 66, "yogesh")
# print(tuple1)

# print(tuple1[2:4]) # ctx: slicing can be done on tuples

# list5 = list(tuple1)
# print(type(list5))


str1 = "this is string"
grade = 'A' # this is also a string not a character
print(type(str1), type(grade))

print(len(str1), str1[5])
print(str1.lower())
print(str1.capitalize())
print(str1.upper())
print(str1.replace("i", "b"))
list6 = str1.split(" ")
print(list6)
s = "-".join(list6) # his-is-string
print(s)
print(ord('a'))

#! STRING, TUPLE  ->  IMMUTABLE


# IMP: Remove Duplicates from Sorted Array II (same elements can occur at most twice)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(2, len(nums)):
            if nums[k-1] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k+1

