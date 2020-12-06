from pandas import Series
from pandas_datareader import data as web
from matplotlib import pyplot as plt
import csv
import yahoo_finance as yt
import datetime as dt
import logging
logging.basicConfig(level=logging.INFO)

csvfile = '../csv_data/2330.csv'
start = dt.datetime(2020,11,1)
end = dt.datetime(2020,11,21)

df = web.get_data_yahoo('2330.TW',start,end)
df.to_csv(csvfile)
close :Series = df.get('Close')
close.plot.line()
Open :Series = df.get('Open')
Open.plot.line()
Volume :Series = df.get('Volume')
Volume.plot.bar()
plt.show()

