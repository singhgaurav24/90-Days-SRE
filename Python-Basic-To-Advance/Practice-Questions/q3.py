# WAP to Grade students depend upon marks.

marks = (float)(input("Enter the makrs of students : "))

if(marks >= 90):
    print("Garde - A")
elif(marks >= 80 and marks < 90):
    print("Grade - B")
elif(marks >= 70 and marks < 80):
    print("Grade - C")
else:
    print("Grade - D")