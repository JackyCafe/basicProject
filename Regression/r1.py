import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

size = 150
x: np = np.random.randint(0,70,size)
y: np =np.array(2*x-5+5*np.random.randn(size))
x =x.reshape(150,1)
print(np.array(x).shape)
# print(np.array(y).shape)
#
# x,y=make_regression(n_samples=100, n_features=1, noise=50)
# print(X)
# print(np.array(y).shape)


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

regr=linear_model.LinearRegression()
regr.fit(X_train, y_train)
print(regr.coef_)
print(regr.intercept_)
plt.scatter(X_train, y_train)
plt.plot(X_train, regr.predict(X_train),color='blue',linewidth=1)
plt.show()