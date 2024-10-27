fName = "Gaurav"
mName = "Kumar"
lName = "Singh"
full_name = fName + " " + mName + " " +lName # concatenation 

#Multi Line String
about = """This is Gaurav Kumar Singh
I'm working in _VOIS as a SRE production support ennginer. 
Having about 4-years of experience.
"""
print(full_name)
print(about)

# len() function
print(len(fName)) # length of fName using len() function
print(len(full_name)) # len function also add the spaces

# indexing in python
# indexing always start with 0 
ch  = fName[0]
ch1 = fName[1]

print(ch)
print(ch1)

print(full_name[5])

# Slicing in Python --> Accessing part of a string
# str[starting_index : ending_index] # ending index is not included 

my_name = "Gaurav Singh"
print(my_name[1:4])
print(my_name[0:8])
print(my_name[2:len(my_name)]) # urav Singh
print(my_name[2:]) # urav Singh --> from 2 to len of string
print(my_name[:4]) # Gaur --> start with 0 index to index - 4

# Negative Index
# Gaurav --> [-6,-5,-4,-3,-2,-1]
print(fName[-3:-1]) # ra

# String Functions:

str = "this is Gaurav Singh"

print(str.endswith("gh")) # returns True if str ends with sub-string

# capitalize() --> str.capitalize()
print(str.capitalize()) # capitalizes the first character --> Does not change the orginal str here
print(str)
str = str.capitalize() # change the orginal string
print(str)

# replace() --> str.replace(old,new)
str1 = "this is Gaurav Singh"
print(str1.replace("Gaurav", "Gaurav Kumar"))

# find() --> str.find(word) --> if True : return the first index of first occurrerence
str2 = "This is singhgaurav30"
print(str2.find("gaurav"))
print(str2.find("Golu")) # returns -1 if the value is not found.
print(str2.find("g"))

# count() --> str.count("substr") --> count the occurrence of sub-string
print(str2.count("i"))


