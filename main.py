import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('stockdata.csv')
print(df)

df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']
df = df.iloc[::-1]
plt.plot(df['Close'], label='Close Price history')


def movingAvg(days,data):
    avgData = []
    for i in range(days):
        avgData.append(float("NaN"))
    for i in range(days,len(data)):
        avgData.append(sum(data[i-days:i])/days)
    return avgData

data = df["Close"]

df['avgClose'] = movingAvg(100,data)
plt.plot(df['avgClose'])
plt.legend(['Stock Close Price','100-day Moving Average'])
plt.show()
