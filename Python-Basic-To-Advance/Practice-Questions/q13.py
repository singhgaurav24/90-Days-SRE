"""
WAP to enter marks of 3 subjects 
"""

marks = {

}

x = int(input("enter marks of chem : "))
marks.update({"chem" : x})

x = int(input("enter marks of math : "))
marks.update({"math" : x})

x = int(input("enter marks of phy : "))
marks.update({"phy" : x})

x = int(input("enter marks of polity : "))
marks.update({"polity" : x})

print(marks)