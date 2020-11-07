import pandas as pd
file= "../data/A121151.csv"
df = pd.read_csv(file)
print(df)
keys = df.keys()
print(keys)
series1 = df.get(keys[0])
print(series1)