# Search for a number x in this tuple using loop:

tup = (1,4,9,16,25,36,49,64,81,100)

num = int(input("enter a number to serach : "))
index = 0
found = False
while index < len(tup):
    if tup[index] == num:
        print("Found", num, " at index : ", index)
        found = True
        break
    index = index + 1

if not found:
    print("Not Found")
    

