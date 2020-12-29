import np as np
import numpy as np
from torch.autograd import Variable
from matplotlib import pyplot as plt
size=150
x: np = np.random.randint(0,70,size)
yd: np = np.array(3*x-5+5*np.random.randn(size))
x = np.concatenate((x[:, np.newaxis],np.ones((x.shape[0], 1))), axis=1)
yd = yd[:, np.newaxis]

learning_rate = 0.001


def sigmoid(x):
    # 應用sigmoid啟用函式
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    # 計算Sigmoid函式的偏導數
    return x * (1 - x)


def train(training_inputs, yd, training_iterations):
    w = np.random.randn(2, 1)
    # w = np.array([[3.0],[1.0]])
    for iteration in range(training_iterations):
        # 得到輸出
        y = sigmoid(np.dot(training_inputs, w))
        # 計算誤差
        error = yd - y
        # 微調權重( x 與 e*sigmoid_derivative )
        adjustments = np.dot(training_inputs.T, error*sigmoid_derivative(y))
        w += learning_rate*adjustments
        fig = plt.figure()
        ax = plt.subplot()
        # ax=fig.add_axes([0, 0, 5, 5])
        plt.figure(figsize=(10, 7))
        # plt.plot(x_train.data.numpy(),y_train.data.numpy(),'*')
        plt.scatter(x[:, 0], yd, s=100, alpha=0.3)
        xs = np.linspace(0, 70, 200)
        ys2 = w[1] + w[0] * xs
        plt.plot(xs, ys2, 'g', linewidth=1)

        plt.show()
    return w


# training_inputs = np.array([(0, 0, 1),
#                             (0, 1, 1),
#                             (1, 0, 1),
#                             (1, 1, 1)])

# yd = np.array([[0, 0, 0, 1]]).T

synaptic_weights = train(x, yd, 15000)
print(synaptic_weights)
print("Ending Weights After Training: ")

# k = -synaptic_weights[0] / synaptic_weights[1]
# b = -synaptic_weights[2] / synaptic_weights[1]

fig = plt.figure()
ax = plt.subplot()
# ax=fig.add_axes([0, 0, 5, 5])
plt.figure(figsize=(10, 7))
# plt.plot(x_train.data.numpy(),y_train.data.numpy(),'*')
plt.scatter(x[:,0],yd,s=100,alpha=0.3)
xs=np.linspace(0,70,200)
ys2=synaptic_weights[1]+synaptic_weights[0]*xs
plt.plot(xs,ys2,'g',linewidth=1)

plt.show()
