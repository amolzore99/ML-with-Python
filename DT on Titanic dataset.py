# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:55:39 2021

@author: User
"""

#import library
import pandas as pd
import seaborn as sns

#import data
dataset=pd.read_csv('titanic.csv')
dataset
dataset.info()

#change the datatype from object to numeric form
dataset['age']=pd.to_numeric(dataset.age,errors='coerce')
dataset.info()
dataset['fare']=pd.to_numeric(dataset.fare,errors='coerce')
dataset.info()

#identifying missing values
dataset.isnull()
dataset.isnull().sum()

sns.heatmap(dataset.isnull(),yticklabels=False, cmap="viridis")

#handling missing value
#drop null value from fare column
#calculate mean of age dataset & fill this value in null places
dataset.dropna(subset=['fare'],inplace=True)
dataset.isnull().sum()
dataset["age"].fillna(dataset["age"].mean(), inplace=True)
dataset.isnull().sum()
sns.heatmap(dataset.isnull(),yticklabels=False, cmap="viridis")

dataset.info()

#crete dummy varaiable of categorical variable 
pd.get_dummies(dataset.pclass)
pd.get_dummies(dataset.pclass,drop_first=True)
class_dummy=pd.get_dummies(dataset.pclass,drop_first=True)

pd.get_dummies(dataset.sex)
sex_dummy=pd.get_dummies(dataset.sex,drop_first=True)

pd.get_dummies(dataset.embarked)
embark_dummy=pd.get_dummies(dataset.embarked,drop_first=True)

titanic_data=pd.concat([dataset,class_dummy,sex_dummy,embark_dummy],axis=1)
titanic_data.info()

titanic_data.drop(['Passenger_id','pclass','name','sex','ticket','embarked'],axis=1,inplace=True)
titanic_data.info()

x=titanic_data.iloc[:,1:]
y=titanic_data.iloc[:,0]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy',max_depth = 4, min_samples_leaf=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

#TN=171   TP=87   FN=41   FP=24.....(171+87)/(171+87+24+41)...  ACC=79.87

from sklearn import tree

#Simple Decision Tree
tree.plot_tree(classifier)
#image is quite blurred

#Lets try to make decision tree more interpretable by adding filling colors.
tree.plot_tree(classifier,filled = True)
#Although the Decision tree shows class name & leafs are colred but still its view is blurred.

#Lets create a blank chart of desired size using matplotlib library and place our Decision tree there.
import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (10,10), dpi=300)
#The above line is used to set the pixels of the Decision Trees nodes so that
#the content mentioned in each node of Decision tree is visible.
cn=['0','1']
tree.plot_tree(classifier,class_names=cn,filled = True)


#OBSERVATION/CONCLUSION

# [1] Male passenger trvaell in 3(p_class ) with fare less than 12.82 fare ... are in class 1
#(It means this kind of passenger are survived)

# [2] male passenger who travelled in class 3 with greater than 26 fare ... are in class 1 
# (It means this kind of passenger are survived)

# [3] male passenger who not travell in class3 with less than 7 fare... are in class 1
#(It means this kind of passenger are survived)

# [4] female passenger which have age less than 13.5 less than 2.5 sibling & greater than 19.65 fare... are in class 1
#(It means this kind of passenger are survived)

# [5] Male passenger which are not travelled in 3(p_class) with less than 31.33 fare... are  in class 0
#(It means this kind of passenger are NOT survived)

#[6] female passenger who age less than 13.5 & greater than 3.5 with >than 2.5 sibl ....are in class 0
##(It means this kind of passenger are not survived)

#[7] feamale passsenger who age greater than 13.5 with less than 7.53 fare ...are in class 0
#(It means this kind of passenger are not survived)





















