# Tuples in Python
# A built-in data type that lets us create immutable squences of values. 

first_tuple =(2,4,8,4,5,2,1)

print(type(first_tuple))

print(first_tuple[2])
print(first_tuple[0])

# first_tuple[0] = 5 --> TypeError: 'tuple' object does not support item assignment because of immutable

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))