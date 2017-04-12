import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# download csv data from yahoo finanace
# NYSE
df=pd.read_csv('/home/sukumar/Documents/PythonSnippet/TimeSeriesAnalysis/MovingAverage/table.csv',index_col='Date', parse_dates=True)
#printing head
print(df.head())
#get the closing price
close_price=df['Adj Close']
#lets sort in acsending order
close_price=close_price.sort_index(ascending=True)
#plot the data
close_price.plot(label= 'Close')
#plt.legend()
#plt.show()
#moving average
movavg=close_price.rolling(window=40,center=False).mean()
#print(movavg)
movavg.plot(label='Moving Average')
plt.legend()
plt.show()


