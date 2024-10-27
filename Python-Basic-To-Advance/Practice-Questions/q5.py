# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("enter first numbers : "))
b = int(input("enter second numbers : "))
c = int(input("enter third numbers : "))

print("Numbers are : ", a,b,c)

if(a>b and a>c):
    gratest_number = "First Number", a
elif(b>a and b>c):
    gratest_number = "Second numbaer", b
else:
    gratest_number = "third number", c

print("Greatest number is :", gratest_number)