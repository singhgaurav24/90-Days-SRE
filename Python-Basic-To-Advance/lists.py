# list --> A built-in data type that stores set of values, It can store elements of 
# different types(integer,float,string,etc.)
# list are mutable in python

marks = [94.4, 78.9, 78.5, 99.9, 98.7]
print(marks)  # print list
print(type(marks)) # print type of list
print(len(marks))  # length of list
print(marks[0])    # index of list strting with zero
print(marks[1])

student = ["Gaurav", 97.8, 25, "Patna"] # list can store different type of data type unlike array in c++ and java
print(student)
print(student[0])
student[0] = "Golu" # list are mutable, we can chnage it's value. 
print(student)

# print(student[6]) # --> will give error --> IndexError: list index out of range

# List Slicing --> Similar to string slicing
# list_name[ staring_index : ending_index ] --> ending index is not included. 

print(marks[1:4])
print(marks[:5]) # start with 0 index
print(marks[3:]) # ends with last element

# negative slicing in list --> [-5, -4, -3, -2, -1]
print(marks[-5:-2])
print(marks[-2:-5]) # empty list

# List Methods

a_list = [4, 6, 9]
a_list.append(7) # add/append at the end of the list
print(a_list)

a_list.sort()  # sorting in ascending order
print(a_list.sort()) # it will print the NONE as it's changing the original list
print(a_list) # print the sorted list

a_list.sort(reverse=True) # sort in desscending order
print(a_list)

# insert(index, element) --> Insert element at index number
list_2 = [2,3,4,5]
list_2.insert(1,9)
print(list_2)

# remove(4) --> remove the first occurrenece of element --> It will remove the elememt 4
# pop(index) --> removes element at a particular index
list_2.remove(4) # remove the element 4 (first occurrenece)
print(list_2)
list_2.pop(2) # remove the element at index 2
print(list_2)