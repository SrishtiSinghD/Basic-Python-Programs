#Program to make a calculator

x=float(input("Enter Number 1: "))
y=float(input("Enter Number 2: "))

print("Choose 1 for Addition: ")
print("Choose 2 for Subtraction: ")
print("Choose 3 for Multiplication: ")
print("Choose 4 for Division: ")
print("Choose 5 for Remainder")

o=int(input("Enter your choice: "))

if(o==1):
    print("Sum is= ",x+y)
elif(o==2):
    print("Subtraction is= ",x-y)
elif(o==3):
    print("Multiplication is= ",x*y)
elif(o==4):
    print("Division is= ",x/y)
elif(o==5):
    print("Remainder is= ",x%y)
else:
    print("Invalid operation")

   


x=float(input("Enter Number 1: "))
y=float(input("Enter Number 2: "))

print("Sum is= ",x+y)
print("Subtraction is= ",x-y)
print("Multiplication is= ",x*y)
print("Division is= ",x/y)
print("Remainder is= ",x%y)