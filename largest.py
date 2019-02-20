# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:07:36 2019

@author: Dell
"""

#to find th largest and second largest number on the list(sort and second last)
L=[]
s=int(input("How many numbers you want to add in the list? "))
for i in range(s):
    x=int(input("Enter element of list: "))
    L.append(x)
print(L)
maxim=L[0]
for i in range(len(L)):
    if L[i]>maxim:
        maxim=L[i]
print("Your Largest Number is= ",maxim)
for i in range(len(L)):
    if L[i-1]==maxim:
        del(L[i-1])
print(L)
second=L[0]
for i in range(len(L)):
    if L[i]>second:
        second=L[i]
print("Your Second Largest Number is=",second)

