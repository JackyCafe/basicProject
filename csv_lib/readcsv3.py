import pandas as pd
import numpy as np
from pandas import Series
from pandas.core.generic import NDFrame
import logging
import matplotlib.pyplot as plt

path = "../data/"
# logging.basicConfig(level=logging.INFO,filename='mylog.log',filemode='w')

df = pd.read_csv(path+"A121151.csv")
series = []
ser : Series
keys = df.keys()
for key in keys:
    ser = df[key][2:].to_numpy(float)
    # ser2 =  Series(ser)
    ser.plot.line()

plt.show()