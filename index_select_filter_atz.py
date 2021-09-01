# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 11:44:58 2021

@author: User
"""

import pandas as pd
record={'Name':['Rohit','Rahul','Pujara','Virat'],
             'Opponent':['SA','ENG','AUS','BAN'],
             'Venue':['Kolkatta','Chennai','Delhi','Mumbai'],
             'Score':[212,199,212,254]}
df=pd.DataFrame(record)
df
df['Score']
df[['Name','Score']]
df[0:2]
df[0:4]

#view only that rows who score greater than 250
df[df['Score']>250]

#view only that rows who score greater than 200
df[df['Score']>200]

#show only that rows who score in between 200-250
df[(df['Score']>=200) & (df['Score']<250)]

#-----------------Select in Pandas dataframe-------------------------------------------
#select row by using row number in pandas  with .iloc
#.iloc [1:m, 1:n] – is used to select or index rows based on their position 
#from 1 to m rows and 1 to n columns

#select first 2 rows
df.iloc[:2]
df.iloc[:2,]

#select 1 & 2 rows
df.iloc[1:3]

#Select column by using column number in pandas with .iloc
# select first 3 columns
df.iloc[:,0:3]

#select 1st and last column
df.iloc[[0,1,2,3],[0,3]]
#also using lable
df.loc[[0,1,2,3],['Name','Score']]

df.loc[0:3,('Opponent','Score','Venue')]
df.loc[1:2,('Opponent','Venue')]


