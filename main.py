import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
days = 10

df = pd.read_csv('stockdata.csv')
print(df)

df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']
df = df.iloc[::-1]
numRows = df.shape[0]
splitInd = int(numRows*0.2)
testData = df.iloc[:splitInd,0:]
trainingData = df.iloc[splitInd:,0:]



def movingAvg(days,data):
    avgData = []
    for i in range(days):
        avgData.append(float("NaN"))
    for i in range(days,len(data)):
        avgData.append(sum(data[i-days:i])/days)
    return avgData

data = trainingData["Close"]

trainingData['avgClose'] = movingAvg(days,data)

plt.plot(trainingData['Close'], label='Close Price history')
plt.plot(trainingData['avgClose'])
daysTxt = str(days)
plt.legend(['Stock Close Price',daysTxt+'-day Moving Average'])
plt.show()
