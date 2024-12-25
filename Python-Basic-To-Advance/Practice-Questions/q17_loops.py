# Print the multiplication table of a number n.

x = int(input("Enter a number : "))

i = 1
print("Multiplicatio table of", x , "is  ")
while i <= 10:
    print(x, " x ", i, " = ", x*i)
    i += 1