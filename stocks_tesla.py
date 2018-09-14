import pandas as pd
import pandas_datareader.data as web_ui
import datetime
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = datetime.datetime(2010,1,1)
end = datetime.datetime(2015,1,1)

#define dataframe
df = web_ui.DataReader('TSLA', 'robinhood', start, end)
print(df.head())

#df['Adj Close'].plot()

#plt.show()
