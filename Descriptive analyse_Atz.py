# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:59:58 2021

@author: User
"""

import pandas as pd
import numpy as np

score=pd.Series([45,84,78,98])
score
score.describe()

subject=pd.Series(['EM','DOM','TD','SPA'])
subject
subject.describe()

info=pd.DataFrame({'score':[45,84,78,98],'subject':['EM','DOM','TD','SPA']})
info
info.describe()
info.describe(include=[np.number])
info.describe(include=[np.object])

high_score={'Name':['Rohit','Rahul','Pujara','Virat'],
             'Opponent':['SA','ENG','AUS','BAN'],
             'Venue':['Kolkatta','Chennai','Delhi','Mumbai'],
             'Score':[212,199,212,254]}
df=pd.DataFrame(high_score)
df
print(df.describe())
print(df.describe(include='object'))
print(df.describe(include='number'))
print(df.describe(include='all'))
