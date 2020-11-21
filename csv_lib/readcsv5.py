import pandas as pd
import numpy as np
from pandas.core.generic import NDFrame

path = "../data/"
df = pd.read_csv(path+"A121151.csv")
keys = df.keys()
temptures = []
datas = np.zeros([2,3])
series: NDFrame
print(df.min())

# temptures.append(np.array(df.get(key)[2:],dtype=float))
