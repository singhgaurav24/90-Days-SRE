# WAP to check if a number is a multiple of 7 or not.

a = int(input("enter a numbers : "))

if(a%7 == 0):
    output = "Yes"
else:
    output = "No"

print("This number is multiple of 7 : ", output)