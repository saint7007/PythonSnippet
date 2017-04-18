#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import quandl,math,datetime,time
import datetime
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from  matplotlib import style

style.use('ggplot')

quandl.ApiConfig.api_key = 'TFw_tFb_BiQEbxDdpFVu'
df = quandl.get_table('WIKI/PRICES', ticker = 'GOOGL')
df.set_index('date', inplace=True)
print(df.head())
df=df[['adj_open', 'adj_high','adj_low','adj_close','adj_volume',]]
print(df.head())
#rule says high-low/low
df['HighLowPercent']= (df['adj_high']-df['adj_close'])/df['adj_close']*100
df['PercentChange']= (df['adj_close']-df['adj_open'])/df['adj_open']*100
df=df[['adj_close','HighLowPercent','PercentChange','adj_volume']]

forecast='adj_close'
df.fillna(-99999, inplace=True)
forecast_out=int(math.ceil(0.01*len(df)))
df['label']= df[forecast].shift(-forecast_out)


X=np.array(df.drop(['label'],1)) #features


X=preprocessing.scale(X)
X=X[:-forecast_out]
X_lately=X[-forecast_out:]


df.dropna(inplace=True)
y=np.array(df['label'])#label
y=np.array(df['label'])
print(y)
print(len(X),len(y)) #just for a check

X_train, X_test,y_train,y_test=model_selection.train_test_split(X,y,test_size=0.2)
print("before linear classifier")
classifier=LinearRegression()
#let say use SVM
#classifier=svm.SVR()
print("after linear classifier")
classifier.fit(X_train,y_train)
print("after classifier fit")
accuracy=classifier.score(X_test,y_test)  #using different fit and test cause lets say whatever teacher teaches and she ask same ques in test?

print(accuracy) #accuracy is squared error

forecastSet=classifier.predict(X_lately)
print(forecastSet,accuracy,forecast_out)
df['Forecast']=np.nan
lastdate=df.iloc[-1].name
print(type(lastdate))
lastunix=pd.Timestamp(lastdate)
print(lastunix)

for i in forecastSet:
    nextunix = lastunix+datetime.timedelta(days=1)
    df.loc[nextunix]=[np.nan for _ in  range(len(df.columns)-1)]+[i]
    lastunix=nextunix

df['adj_close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()



