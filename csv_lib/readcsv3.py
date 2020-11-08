import pandas as pd
from pandas.core.generic import NDFrame
import logging
from toolkit.Judy import Math

path = "../data/"
logging.basicConfig(level=logging.INFO,filename='mylog.log',filemode='w')

df = pd.read_csv(path+"A121151.csv")
ser = []
keys = df.keys()
for key in keys:
    ser.append(df.get(keys))


out = pd.DataFrame(df)
out.to_csv('../data/A121154.csv', index=False, header=None)