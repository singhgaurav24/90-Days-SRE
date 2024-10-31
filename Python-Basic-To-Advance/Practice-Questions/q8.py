# WAP to check if a list contains a palindrome of elements.

a_list = [1,2,3,2,1]

a_copy = a_list.copy()
a_copy.reverse()

if a_list == a_copy:
    print("This list contains the palindrome of elements")
else:
    print("This list does not contains the palindrome of elemnts")
