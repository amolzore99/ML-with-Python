# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:35:51 2021

@author: User
"""

#.................................Handling missing value.....................................


#counting the missing value

import pandas as pd 
import numpy as np

#create dataframe
emp_details={'name':['sachin','ramesh',np.nan,'vijay','rahul'],
             'age':[23,47,36,np.nan,24],
             'salary':[25000,51000,np.nan,np.nan,np.nan]}
df1=pd.DataFrame(emp_details)
df1

#is there any missing value in dataframe
df1.isnull()
df1.notnull()

#is there any missing value across column
df1.isnull().any()

#How many missing value across column
df1.isnull().sum()


#----------------------Dropping rows with missing Value-------------------------

#Create dataframe
Report_card={'Plyr_name':['rohit','kl','pujara','rahane','virat','pant','sky',np.nan],
             '1st inning':[258,247,113,51,140,48,np.nan,np.nan],
             '2nd inning':[261,214,130,52,156,78,np.nan,np.nan],
             '100+':[1,1,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
             }
df2=pd.DataFrame(Report_card)
df2

df2.isnull()
df2.isnull().any()
df2.isnull().sum()

#Drop all rows which have nan/missing value
df2.dropna()

#drop only whoese entire row nan value
df2.dropna(how='all')

#drop those which has more than 3 nan value
df2.dropna(thresh=3)

#drop nan in spesific column
df2.dropna(subset=['100+'])
df2.dropna(subset=['Plyr_name','100+'])

#dropping rows using axis value
df2.dropna(axis=0)

##dropping column using axis value
df2.dropna(axis=1)

#replace missing value with zero
df2.fillna(0)
df1.fillna(0)

#Replacing Missing Values with Mean of the column
df2['1st inning'].fillna(df2['1st inning'].mean(),inplace=True)
df2

#relacing missin value with median of the column
df2['2nd inning'].fillna(df2['2nd inning'].median(),inplace=True)
df2
df2.fillna(0)

#Replace Missing (or) Generic Values using replace() method
#Many times, we have to replace a generic value with some specific value. 
#We can achieve this by applying the replace method.
df = pd.DataFrame({'one':[10,20,30,40,50,2000], 'two':[1000,0,30,40,50,60]})
print(df)

print (df.replace({1000:10,2000:60}))

#------------------Handling Duplicate Values--------------------------------

#The drop_duplicates() function performs common data cleaning task that deals with duplicate values
#in the DataFrame. This method helps in removing duplicate values from the DataFrame.

emp = {"Name": ["Parker", "Smith", "William", "Parker"],  
"Age": [21, 32, 29, 21]}  
info = pd.DataFrame(emp)  
print(info) 
info = info.drop_duplicates() 
print(info)

emp = {"Name": ["Parker", "Smith", "William", "Parker"],  
"Age": [21, 32, 29, 22]}  
info = pd.DataFrame(emp) 
print(info)
info = info.drop_duplicates()  
print(info)

