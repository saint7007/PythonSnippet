import pandas as pd
import  numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

df = pd.read_csv("/home/sukumar/Documents/PythonSnippet/svm/data.csv",header = 0)


print(df.head())

df = df.drop("id",1)

df.diagnosis.unique()
d = {'M' : 0, 'B' : 1}
df['diagnosis'] = df['diagnosis'].map(d)

print(df.head())

features = list(df.columns[1:31])
features


x = df[features]
y = df["diagnosis"]


X_train,X_test,y_train,y_test = train_test_split(x,y,test_size= .4,random_state=0)

#----------------------------------------------------------------------------------------------
#Decision Tree Classifier with criterion gini index
clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)

#DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3,
#            max_features=None, max_leaf_nodes=None, min_samples_leaf=5,
#            min_samples_split=2, min_weight_fraction_leaf=0.0,
#            presort=False, random_state=100, splitter='best')



#----------------------------------------------------------------------------------------------
#Decision Tree Classifier with criterion information gain

clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)




#Pred

y_pred = clf_gini.predict(X_test)
print(y_pred)

y_pred_entropy = clf_entropy.predict(X_test)
print(y_pred_entropy)


print("Ginni Accuracy ", accuracy_score(y_test,y_pred))

print("Entropy Accuracy  ", accuracy_score(y_test,y_pred_entropy))



# run from terminal
# 1 1 1 1 1 0]
#Ginni Accuracy  0.912280701754
#Entropy Accuracy   0.938596491228
