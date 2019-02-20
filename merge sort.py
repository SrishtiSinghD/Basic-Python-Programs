#Program to merge two lists
L=[]
s=int(input("How many numbers you want to add in the list? "))
for i in range(s):
    x=(input("Enter element of list: "))
    L.append(x)

L1=[]
s=int(input("How many numbers you want to add in the list? "))
for i in range(s):
    x=(input("Enter element of list: "))
    L1.append(x)

M=L+L1
M.sort()
print(M)

