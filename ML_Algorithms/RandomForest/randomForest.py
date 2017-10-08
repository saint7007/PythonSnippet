import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
train = pd.read_csv("/home/sukumar/Documents/RSnippets/Miscellaneous/train.csv")
test=pd.read_csv("/home/sukumar/Documents/RSnippets/Miscellaneous/test.csv")

Id=test['Id']
y=train['Cover_Type']

train=train.drop(['Id','Cover_Type'],1)
test=test.drop(['Id'],1)

x_train, x_test, y_train, y_test = train_test_split(train, y, test_size=0.3, random_state=44)

rfClassifier=RandomForestClassifier(n_estimators=16,class_weight='balanced',n_jobs=4,random_state=44)
rfClassifier.fit(x_train,y_train)

accuracy=rfClassifier.score(x_test,y_test)
print(accuracy)

rfClassifier.fit(train,y)

prediction=rfClassifier.predict(test)
print(prediction)

output=pd.DataFrame(Id)
output['Cover_Type']=prediction
print(output.head())
output.to_csv("output.csv",index=False)


#/usr/bin/python3.6 /home/sukumar/PycharmProjects/PythonLecture/ForestExploration/randomForest.py
#0.846340388007
#[1 1 2 ..., 3 3 3]
#      Id  Cover_Type
#0  15121           1
#1  15122           1
#2  15123           2
#3  15124           2
#4  15125           2

#Process finished with exit code 0