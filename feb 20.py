"""
Q.1 WAP to create a dictionary at runtime.
Q.2 WAP to create a dictionary where keys will be input by the user
as strings and values will be list of vowels present in that string.

"""
#P1
d={}
n=int(input("Enter number of elements in the dictionary: "))
for i in range(n):
    key=input("Enter a key: ")
    value=int(input("Enter a numerical value: "))
    d.update({key:value})
print(d)

#P2

d={}
s=input("Enter a paragraph: ")
l=s.split()
for i in l:
    key=i
    value=[j for j in i if j in 'aeiou']
    d.update({key:value})
print(d)