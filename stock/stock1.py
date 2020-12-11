from pandas_datareader import data as web
import datetime as dt
import logging
logging.basicConfig(level=logging.INFO)

csvfile = '../stock_csv/2330.csv'
start = dt.datetime(2020,11,1)
end = dt.datetime(2020,11,24)
df = web.get_data_yahoo('2330.TW',start,end)
df.to_csv(csvfile)
logging.info(df.all)