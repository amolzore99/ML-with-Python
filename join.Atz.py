# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:11:01 2021

@author: User
"""

import pandas as pd

#Example 1
#create dataframe 1
#top performer for MI in ipl 2019
mi2019={'name':['De cock','surya','ishan','pollard','rohit'],
        'strike rate':[141.15,154.23,149.25,163.25,131.26],
        'best':[89,76,99,86,103]}
df1=pd.DataFrame(mi2019)
df1

#create dataframe 2
#top performer for MI in ipl 2020
mi2020={'name':['Hardik','Bumrah','pollard','bolt'],
        'wicket':[12,27,11,23],
        'economy':[7.26,6.25,8.25,7.10]}
df2=pd.DataFrame(mi2020)
df2

#inner join
print(pd.merge(df1,df2, on='name', how='inner'))

#outer join
print(pd.merge(df1,df2, on='name', how='outer'))

#left join
print(pd.merge(df1,df2, on='name', how='left'))

#right join
print(pd.merge(df1,df2, on='name', how='right'))

#example 2
#create dataframde 1
# best performer for CSK at each batting possition from 2020
CSK={'position':[1,2,3,4,5,6,7],
     'name':['WATSON','FAF','RAINA','AMBATI','DHONI','JADDU','SAM'],
     'strike rate':[131.2,129.25,135.65,148.58,146.63,139.56,161.62],
     'best':[106,96,74,71,51,48,47]}
df3=pd.DataFrame(CSK)
df3

#create dataframe2
# best performer for MI at each batting possition from 2020
MI={'position':[1,2,3,4,5,6],
    'name':['ROHIT','DE COCK','SURYA','POLLARD','KRUNAL','HARDIK'],
    'Boundries':[35,34,46,29,27,24]}
df4=pd.DataFrame(MI)
MI
#using inner join
print(pd.merge(df3,df4, on='position', how='inner'))

#using outer join
print(pd.merge(df3,df4, how='outer'))
print(pd.merge(df3,df4, on='position', how='outer'))

#using left
print(pd.merge(df3,df4, on='position', how='left'))
print(pd.merge(df3,df4, how='left'))

#using right
print(pd.merge(df3,df4, on='position', how='right'))
print(pd.merge(df3,df4, how='right'))



