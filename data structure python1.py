# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:35:04 2021

@author: User
"""

array1=[1,3,5,96,47,87]
array2=[4.5,6.5,9.4]
type(array1)
type(array2)

#tuple
student=(1,'amol','zore','science',15000)
type(student)

#list
l1=[1,'mango',4.35,False,9+4j]
type(l1)
l1[0:]
l1[2]
l1[0]=100
print(l1)
l1[1]='apple'
print(l1)
#appending new element
l1.append('mango')
print(l1)
#popping last element
l1.pop()
print(l1)
#reverse
l1.reverse()
#insert
l1.insert(3,'sparya')
print(l1)

#dictionary in python
emp_detail={'amol':20000,'sagar':21000,'nikhil':22000,'marathe':21000,'rahul':35000,'umesh':41000}
emp_detail.keys()
emp_detail.values()
#adding new element
emp_detail['balaji']=70000
print(emp_detail)

#set in python
set1={1,1.34,"sparrow",True,5-6j}
type(set1)
set2={'a','c','b','c',4,4,True}
print(set2)
type(set2)
#add one element
set1.add('hello world')
print(set1)
#uppdate multiple element
set1.update([8,False,'amol','krati'])
print(set1)
#remove an element
set1.remove(False)
print(set1)
