# Dictionary in Python

# dictionaries are used to store data in key:value pairs
# They are unordered, mutable & do not allow duplicate keys.

info = {
    "key"   : "value",
    "fname" : "Gaurav",
    "lName" : "Singh"
}

# print(info)
# print(type(info))

moreInfo = {
    "Name" : "Gaurav Kumar Singh",
    "Language" : ["Python", "Java", "GO", "C", "C++"],
    "DevopsTolls" : ("Git", "AWS", "ci/cd", "K8s", "Terraform", "Azure Devops")
}

# print(moreInfo)
# print(moreInfo["Language"])

# Nested Dictionary:

student = {
    "Name" : "Gaurav Kumar Singh",
    "marks" : {
        "Phy"  : 98,
        "Math" : 100,
        "Chemestry" : 97,
        "Biology" : 93
    }
}
# print(student) # Print the dictonary
# print(student["marks"]["Math"]) # print the value of nested dictionay