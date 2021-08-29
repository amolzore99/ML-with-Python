# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 19:56:37 2021

@author: User
"""

#abs(): Returns the absolute value of a number

#integer number
integer=-21
abs(integer)
print("Absolute of -21 is:",abs(integer))

#floating number
float=-41.9
abs(float)
print("Absolute of -41.9 is:",abs(float))

#all(): It returns true if all items passed in itterable is true
#otherwise it returns false
k=[1,5,9,8,4]
print(all(k))
k.append('False')
print(all(k))
k
k.append(0)
k
print(all(k))

k1=[1,6.5,'abd',False]
print(all(k1))

k2=[0,False]
print(all(k2))

k3=[]
print(all(k3))

#.............................................................................................

#bool():converts value to boolean (True or False)

a=[]
print(a,"is",bool(a))

b=[1]
print(b,"is",bool(b))

c=[0]
print(c,"is",bool(c))

a1= None
print(a1,"is",bool(a1))
a2='sanju'
print(a2,"is",bool(a2))

#sum(): used to of number
scorecard_3=[0,19,1,7,16,2,4,0,11,0,8]
sum(scorecard_3)
total=sum(scorecard_3,10)
total

#len():
str="spyder"
len(str)

#list()   create list in python
xyz=list()
print(xyz)

#convert string into list
name='amol zore'
print(list(name))

#divmod()= used to get qoutient and reminder
divmod(45,9)

#dict():  
atz=dict()
print(dict(atz))
type(atz)

new_dict=dict(a=1,b="amit")
print(dict(new_dict))

result=dict(won=1,loss=2,draw=3)
print(dict(result))

#set()
result=set()
print(set())
type(result)
result_1=set('125')
result_2=set("toyoto")
result_3={4,9,7,8}
print(result)
print(result_1)
print(result_2)
print(result_3)

#pow()
pow(8,2)
print(pow(3,3))
print(pow(-4,3))

#tuple()
tup=1,'ak',1000
x=tuple(tup)
print('x is equal to:',x)

#......................................................................................
#lambda()
#EX.1
x=lambda a,b:a*b
print("Result of a*b=",x(15,6))

#EX.2
M=lambda x:x*x*x+x
M(6)

#lambda function using filter function
#1
marks=[50,33,66,48,98,15,62,48,75,95,51]
find_list=list(filter(lambda x:x%2==0,marks))
find_list
#2
xyz=[11,54,84,64,98,65,4,48,62,14]
ans=list(filter(lambda y:y%4!=0,xyz))
ans

#lambda fuction using map function
#1
l=[1,2,3,4,5,6,8,7,9]
find_l=(list(map(lambda x:x*10+100,l)))
find_l

#lambda fuction using reduce fuction
#1
from functools import reduce     #for import reduce use functools module
new=reduce(lambda x,y:x*y,l)       
new
