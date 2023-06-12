import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as datetime

data = pd.read_csv('HistoricalPrices (1).csv')
print(data.head())

data = data.rename(columns = {' Open':'open', ' High':'High', ' Low': 'Low', ' Close': 'Close'})
data['Date'] = pd.to_datetime(data['Date'])
#plt.plot(data['Date'], data['Close'])
#plt.show()
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(ypoints, 'o:r')
plt.show()