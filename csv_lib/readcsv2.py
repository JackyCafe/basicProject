import pandas as pd
from pandas.core.generic import NDFrame
import logging
from toolkit.Judy import Math

path = "../data/"
logging.basicConfig(level=logging.INFO,filename='mylog.log',filemode='w')

df = pd.read_csv(path+"A121151.csv")
print(df)
keys = df.keys()
print(keys)
series1: NDFrame
series1 = df.get(keys[0])
series1 = series1[2:]
y = series1.__array__(float) #to arr
series1.to_csv(path+"A121153.csv",header=False,index=False)


