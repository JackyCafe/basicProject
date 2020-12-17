from mplfinance.original_flavor import candlestick_ohlc
from pandas_datareader import data as web
from matplotlib import pyplot as plt
from matplotlib import style

import matplotlib.dates as mdates
# import fix_yahoo_finance as yf
import datetime as dt
import pandas as pd

style.use('ggplot')


Analysis = '../csv_data/stockdata.csv'

fig = plt.figure()
ax1 = fig.add_subplot(111)

start = dt.datetime(2020, 11, 1)
end = dt.datetime.now()
df = web.get_data_yahoo('2330.TW',start,end)
# df.to_csv(Analysis)
#
# data = pd.read_csv(Analysis, parse_dates=True, index_col='Date')
price = df["Close"]
price.head()

moving_avg = price.rolling(5).mean()

data = df.reset_index()
# data['Date'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
data['Date'] = data['Date'].apply(lambda  d: mdates.date2num(d.to_pydatetime()))
candlestick = [tuple(x) for x in data[['Date', 'Open', 'High', 'Low', 'Close']].values]
candlestick_ohlc(ax1, candlestick, width=0.7, colorup='r', colordown='green', alpha=0.8,)

plt.plot(moving_avg)
plt.show()
plt.savefig('2330.jpg')