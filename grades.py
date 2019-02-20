"""
Created on Wed Jan  9 10:05:51 2019
@author: Srishti
"""
#Program for grading students on basis of marks obtained

marks=int(input("Enter the marks obtained by student= "))
if(marks>=90 and marks<=100):
    print("The students grade is A")
elif(marks>=80 and marks<90):
    print("The students grade is B")
elif(marks>=70 and marks<80):
    print("The students grade is C")
elif(marks>=60 and marks<70):
    print("The students grade is D")
elif(marks<60 and marks>=0):
    print("Failed")
else:
    print("ERROR!!! MARKS MUST BE BETWEEN 0-100")


