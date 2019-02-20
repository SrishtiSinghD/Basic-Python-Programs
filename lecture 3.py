#user input word as a sting and program gives output like uppercase and reverse order of elcomewpk
s=input("Enter any word of your choice : ")
s.upper()
x=s[1:]
y=s[0]
print(x+y+'PK')
L=[1,2,3]
L.insert(2,4)
print(L)

L.remove(3)
del(L[1])
L.sort()#ascending
L.sort(reverse =True)#descending
L[::-1]#reverse string or list
s[::-1]

#user enters a string check whether its pallindrome or not
s=input("Enter any word: ")
if(s==s[::-1]):
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
    
l=[1,2]
m=[3,4]
print(l.extend(m))#add l and m
print(l*2)#repeats l 2 times
print(s*2)#repeats s 2 times

1 in l#True and here 1 is a string
'a' not in l#True here a is taken as a string
'1' in l#False here 1 is taken as a string

l.index(1)#shows index of 1 in list l as well strings

#how to use index see in documentation

help('index')#will show everything and every func
#index from documentation.

dir(l)#gives all the methods we can do on list

#list comprehension
l1=[]
l=[1,2,3,4,5,6,7,8]
for i in l:
    if (i%2==0):
        l1.append(i)
print(l1)

#another way to do this is list comprehension

l=[1,2,3,4,5,6,7,8,9,10]
l1=[i for i in l if i%2==0]
print(l1)


l2=[i**2 for i in l]
print(l2)


"""
"""
L=[]
r=int(input("How many Temperatures you want to convert"))
for i in range(r):
    x=(input("Enter element of list: "))
    L.append(x)
l=[(9/5)*i+35 for i in L]










import math# imports al of the maths directory

x= math.sqrt(9)

from math import sqrt,tan#includes only sqrt and tan 
x= sqrt(24)
x= tan(3)

import math as m# imports math directory as m
x= m.sqrt(9)
print(m.sqrt(9))

































