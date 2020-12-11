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
series = []
ser : Series
keys = df.keys()
for key in keys:
    ser_list = df[key][2:].to_numpy(float)
    ser =Series(ser_list)
    ser.plot.line(legend=True)
    series.append(ser_list)

plt.legend()
plt.show()
out = pd.DataFrame(np.transpose(series[2:]))
out.to_csv('../data/A121155.csv',index=False,header=False)