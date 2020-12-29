import os

import torch
import numpy as np
from torch.autograd import Variable
from matplotlib import pyplot as plt
os.environ["KMP_DUPLICATE_LIB_OK"]  =  "TRUE"

import torch
import numpy as np
from torch.autograd import Variable
from matplotlib import pyplot as plt

size=150
x: np = np.random.randint(0,70,size)
y: np = np.array(3*x-5+5*np.random.randn(size))

x = Variable(torch.tensor(x))
y = Variable(torch.tensor(y))
x_train = x[0:89]  # 0-89
x_test = x[90:99]  # 90-99
y_train = y[0:89]  # 0-89
y_test = y[90:99]  # 90-99

plt.figure(figsize=(10, 7))
xplot, = plt.plot(x_train.data.numpy(), y_train.data.numpy(), 'o')
plt.show()

learn_rate = 0.0001
a = Variable(torch.rand(1), requires_grad=True)
b = Variable(torch.rand(1), requires_grad=True)

for i in range(1000):
    predictions = a.expand_as(x_train) * x_train + b.expand_as(x_train)  # y_hat = a*x+b
    loss = torch.mean((predictions - y_train) ** 2)
    loss.backward()
    if i % 50 == 0:
        print('loss:', loss)
    a.data.add_(-learn_rate * a.grad.data)
    b.data.add_(-learn_rate * b.grad.data)
    a.grad.data.zero_()
    b.grad.data.zero_()

x_data = x_train.data.numpy()

plt.figure(figsize=(10, 7))
# plt.plot(x_train.data.numpy(),y_train.data.numpy(),'*')
xplot, = plt.plot(x_data, y_train.data.numpy(), 'o')
yplot, = plt.plot(x_data, a.data.numpy() * x_data + b.data.numpy(), '-')
str1 = str(a.data.numpy()[0]) + 'x' + str(b.data.numpy()[0])
plt.xlabel('X')
plt.ylabel('Y')
plt.legend([xplot, yplot], ['Data', str1])
plt.show()
