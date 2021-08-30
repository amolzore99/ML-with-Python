# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 17:20:17 2021

@author: User
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df=pandas.read_csv('C:/Excel csv file/new.csv')
df
x=pandas.read_csv('C:/Excel csv file/User_Data.csv')
x

# Writing CSV Files with Pandas:
df.to_csv('C:/Excel csv file/update.csv')

# Reading Excel Files with Pandas
df1=pandas.read_excel('C:/Excel csv file/cricket1.xlsx')
df1

# Writing Excel Files with Pandas 
df1.to_excel('C:/Excel csv file/IIT-Ba.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)
