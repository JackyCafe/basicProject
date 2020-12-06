import pandas as pd
import numpy as np
from pandas import Series
from pandas.core.generic import NDFrame
import logging
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
path = "../data/"
# logging.basicConfig(level=logging.INFO,filename='mylog.log',filemode='w')
df = pd.read_csv(path+"A121151.csv")
keys = df.keys()
# df.to_csv('../data/A121155.csv',index=False,header=False)
columns = []
for k in keys:
    columns.append(df[k][0])

df1 = pd.read_csv(path+"A121155.csv")
df1.columns= columns

# series = []
# ser : Series
#
plt.figure()
df1.plot.line()

plt.show()