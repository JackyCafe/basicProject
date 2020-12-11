import pandas as pd
from pandas.core.generic import NDFrame
import logging
import numpy as np

from toolkit.Judy import My_Math as Math

path = "../data/"
logging.basicConfig(level=logging.INFO,filename='mylog.log',filemode='w')

df = pd.read_csv(path+"A121151.csv")
keys = df.keys()
# datas = [[0 for i in range(3)] for j in range(2)]
temptures = []
datas = np.zeros([2,3])
print(datas)
for key in keys:
    temptures.append(np.array(df.get(key)[2:],dtype=float))


for i,tempture in enumerate(temptures):
     datas[0][i] = Math.max(tempture)
     datas[1][i] = Math.average(tempture)

print(keys)
out = pd.DataFrame(datas)
out.to_csv('../data/report.csv',index=False,header=keys)