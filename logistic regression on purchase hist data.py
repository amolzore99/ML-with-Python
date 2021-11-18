# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:28:02 2021

@author: User
"""
#import library
import pandas as pd
import seaborn as sns

#import data
dataset = pd.read_csv('H:/data analyst/excel/ML/skilledge/Purchase_History.csv')
dataset
dataset.info()

#visuallization
sns.countplot(x='Purchased',data=dataset)
sns.countplot(x='Purchased',hue='Gender',data=dataset)

#creating dummy variable
pd.get_dummies(dataset.Gender)
pd.get_dummies(dataset.Gender,drop_first=True)
gender_dummy=pd.get_dummies(dataset.Gender,drop_first=True)

new_data=pd.concat([dataset,gender_dummy],axis=1)
new_data.drop(['Gender','User ID'],axis=1,inplace=True)

#inputs is independent variable & target is dependent variable
x=new_data.iloc[:,[0,1,3]].values
y=new_data.iloc[:,2].values

#splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.05, random_state = 0)

#import logisticregression &fit the data
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)

pred_val=model.predict(X_test)

#import confusion matrix and find accuracy
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,pred_val)
cm
#TN=45/TP=0/FN=15/FP=0  (45)/(45+15)=75%    if my test size is 15%
#TN=18/TP=0/FN=2/FP=0    (18)/(18+2)=90%    if my test is 5%

print(model.coef_)
print(model.intercept_)

#Step: 1- Preation of Backward Elimination:
#Importing the library:
import statsmodels.api as sm

x1=new_data.drop('Purchased',axis=1)
y1=new_data['Purchased']

import numpy as np
x1=np.append(arr=np.ones((400,1)).astype(int),values=x1,axis=1)
#Applying backward elimination process now
#Firstly we will create a new feature vector x_opt, which will only contain a set of 
#independent features that are significantly affecting the dependent variable.
x_opt= x1[:, [0,1,2,3]]

#for fitting the model, we will create a regressor_OLS object of new class OLS of statsmodels library. 
#Then we will fit it by using the fit() method.
regressor_OLS=sm.OLS(endog = y1, exog=x_opt).fit()

#We will use summary() method to get the summary table of all the variables.
regressor_OLS.summary()

x_opt=x1[:,[0,1,2]]
regressor_OLS=sm.OLS(endog = y1, exog=x_opt).fit()
regressor_OLS.summary()



from sklearn.model_selection import train_test_split
x_BE_train, x_BE_test, y_BE_train, y_BE_test= train_test_split(x_opt, y1, test_size= 0.05,random_state=0)

#import logisticregression &fit the data
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_BE_train, y_BE_train)


predictions = model.predict(x_BE_test)

from sklearn.metrics import confusion_matrix
confusion_matrix(y_BE_test,predictions)



