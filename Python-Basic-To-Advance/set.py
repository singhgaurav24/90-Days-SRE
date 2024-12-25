# Set in Python
# Set --> Set is the collection of the unordered items.
# Each element in the set must be unique and immutable, 
# that means set itself is mutable it's elements must be immutable. 

# We can not store list and dictionary in sets as they are mutable .

collection = {1, 2, 3, 4}
print(collection)
print(type(collection))

collection_1 = {1, 2, 2, 3, 3, 4} # having depulicate value
print(collection_1) # ignore the duplicate value, it do not give any error.
print(len(collection_1))

empty_dict = {}
empty_set = set()

print(type(empty_dict))
print(type(empty_set))


# Methods in Set

# set.add(element)
empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
empty_set.add(9)
print(empty_set)

# set.remove(element) --> it will give error if the value is not present. 
empty_set.remove(2)
print(empty_set)

# empty_set.remove(5) --> throw error
# print(empty_set)

# set.clear() --> clear the set - empties the set
empty_set.clear()
print(len(empty_set))

# set.pop() --> removes the random values.

# set.union(set2) --> combines both set values and returns new
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) # print the new set doesn't change the original sets

# set.intersection(set2) --> combines the common values and returns new.
print(set1.intersection(set2))
