# https://silverwind1982.pixnet.net/blog/post/329705497
# y = b1x +b0
# b1 = sum((xi-x_bar)*(yi-y_bar)/sum(xi-x_bar)
# ===========================================
# 隨機得到一個數字，可能是負的或正的，可能大於一或小於一，總之就是隨機。
# np.random.randn()

from matplotlib import pyplot as  plt
import numpy as np


# 由0~100 中隨機產生150個值
size=150
x: np = np.random.randint(0,70,size)
#y = 2x-5 + error
y: np =np.array(3*x-5+5*np.random.randn(size))
# plt.scatter(x,y,s=100)
# plt.xlabel('x',fontsize=20)
# plt.ylabel('y',fontsize=20,rotation=0)
# plt.savefig('data_point')
# plt.show()


def lsm_regression(x,y):
    beta=[]
    avg_x = np.mean(x)
    avg_y = np.mean(y)
    b1 = sum((x-avg_x)*(y-avg_y))/sum((x-avg_x)**2)
    b0 = avg_y-b1*avg_x
    beta.append(b0)
    beta.append(b1)
    return beta

def linear_regression(x,y):
    #x = [1,2,3]
    #np.ones((x.shape[0], 1))
    # array([[1.],
    #        [1.],
    #        [1.]])
    # x[:, np.newaxis]=
    # array([[1],
    #        [2],
    #        [3]])
    # np.concatenate((np.ones((x.shape[0], 1)), x[:, np.newaxis]), axis=1)
    # array([[1., 1.],
    #        [1., 2.],
    #        [1., 3.]])

    #x shape(150,2) y_shape=(150,1)
    x = np.concatenate((np.ones((x.shape[0], 1)), x[:, np.newaxis]), axis=1)
    y = y[:, np.newaxis]
    #np.linalg.inv ==>逆矩陣
    print(np.matmul(np.linalg.inv(np.matmul(x.T, x)), x.T))
    beta = np.matmul(np.matmul(np.linalg.inv(np.matmul(x.T, x)), x.T), y)
    return beta

# by_hand = lsm_regression(x,y)
xs=np.linspace(0,70,200)
# ys1=by_hand[0]+by_hand[1]*xs
# plt.scatter(x,y,s=100,alpha=0.3)
# plt.plot(xs,ys1,'r',linewidth=5)

by_hand1 = linear_regression(x,y)
ys2=by_hand1[0]+by_hand1[1]*xs
plt.scatter(x,y,s=100,alpha=0.3)
plt.plot(xs,ys2,'g',linewidth=1)

plt.show()