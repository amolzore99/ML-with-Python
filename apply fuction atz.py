# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:26:48 2021

@author: User
"""

import pandas as pd

#using def
def say():
    print('hello world')
say()

def div_2(x):
    return x/2
div_2(11)

def odd_even(x):
    if x%2==0:
       print(x,"is even")
    else:
       print(x,"is odd")
odd_even(22)
odd_even(67)

#create dictionary of series
d={'A':[10,20,54,47,95,65],'B':[55,66,87,48,95,15]}
type(d)
df=pd.DataFrame(d)
df
def adder(a,b):
    return a+b
print(df.pipe(adder,10))

def substrction(a,b):
    return a-b
    return a-b
    return a-b
print (df.pipe(substrction,2))

def multiply(a,b):
    return a*b
print(df.pipe(multiply,3))

def divide(a,b):
    return a/b
print(df.pipe(divide,2))

# apply():Row or Column Wise Function Application.
# It performs the custom operation for either row wise or column wise.
import numpy as np
d={'A':[10,20,54,47,95,65],'B':[55,66,87,48,95,15]}
df=pd.DataFrame(d)
df
#row wise mean
print (df.apply(np.mean,axis=1))
#column wise
print (df.apply(np.mean,axis=0))

#Example 1:
print (df.applymap(lambda x:x*2))
#Example2:
import math as m
print (df.applymap(lambda x:m.sqrt(x)))
