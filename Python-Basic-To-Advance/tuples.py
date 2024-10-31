# Tuples in Python
# A built-in data type that lets us create immutable squences of values. 

first_tuple =(2,4,8,4,5,2,1)

print(type(first_tuple))

print(first_tuple[2])
print(first_tuple[0])

# first_tuple[0] = 5 --> TypeError: 'tuple' object does not support item assignment because of immutable

# empty tuple
empty_tuple = () # --> vaild tuple
print(empty_tuple)
print(type(empty_tuple))

# single value tuple --> (5,) - if we don't use comma python will consider it like integer. 
single_value_tuple = (5,) # gice comma after value .
print(single_value_tuple)

# slicing in tuple --> It's work same as list
tuple_slicing = (1,2,4,3,5,7)
print(tuple_slicing[1:4])

# Method in tuple

#tup.index(element) --> returns index of first occurrence
tup = (1,2,4,3,5,7,5)
print(tup.index(3))

# count --> counts total occurrence : tup.count(element)
print(tup.count(5))
