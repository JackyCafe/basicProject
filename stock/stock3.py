import mplfinance as mpf
from pandas_datareader import data as web
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib as mpl

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
mc = mpf.make_marketcolors(
	up='red',
	down='green',
	edge='i',
	wick='i',
	volume='i',
	inherit=True)

s = mpf.make_mpf_style(
	gridaxis='both',
	gridstyle='-.',
	y_on_right=False,
	marketcolors=mc)

kwargs = dict(type='candle', mav=(3,6,9), volume=True,figscale=0.75, title='2330',style = s,savefig='2330.png')

mpf.plot(df,**kwargs)
print('OK')