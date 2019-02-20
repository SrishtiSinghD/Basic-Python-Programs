#dictionaries
#by:-Srishti Singh

#wap to find whether a string is a pangram or not(LAB 4:P1)

s=input("Enter a string: ")
s.lower()
sset=set(s)
p={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',}
if (sset.intersection(p)==p):
    print("Your string is a pangram")
else:
    print("It is not a pangram")
    
#or
s=input("Enter a string: ")
s.lower()
sset=set(s)
count=[c for c in sset if ord(c) in range(ord('a'),ord('z')+1)]
if len(count)==26:
    print("Your string is a pangram")
else:
    print("It is not a pangram")
    
#or
"""
l1=[]
for i in sset:
    if i.isalpha():
        l1.append(i)
if len(l1)==26:......
""" 
#65 for capital A and 97 for a
print(ord('a')) #converts characters to ASCII
print(chr(97)) #convert ASCII to charcters

print(ord('x')+3*ord('d'))


i=float(input("Enter any number: "))
if (abs(i)-round(i)==0):
    print("Number entered is an integer")
else:
    print("Number entered is not an integer")
    

#Lab 4
#WAP to check whether a string is a pangram or not
#WAP to map two lists into a dictionary
#WAP to count the number of vowels in a string using sets.
    
#P2
l1=[]
l2=[]
a=int(input("Enter number of elements in both the lists: "))
for i in range(a):
    x=int(input("Enter key for your dictionary: "))
    l1.append(x)
for i in range(a):
    x=input("Enter values for your dictionary: ")
    l2.append(x)
d=dict(zip(l1,l2))
print("Your dictionary is {dict}".format(dict=d))

#P3


s=input("Enter any word or string: ")
s.lower()
sv={'a','e','i','o','u'}
count=0
for i in s:
    if len(set(i).intersection(sv))==0:
        count+=1
print("The number of vowels in your string are {vow}".format(vow=len(s)-count))

s="abcdef"
i="a"
for i in s:
    i=i[:-1]
    print(i)

    







