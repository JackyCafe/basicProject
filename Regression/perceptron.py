'''
Created on 2019年9月6日

@author: yhlin
'''
import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    def __init__(self):
        np.random.seed(2)
        self.synaptic_weights = np.random.random((3, 1))

    def __str__(self):
        return "{synaptic_weights}".format(synaptic_weights=self.synaptic_weights)

    def sigmoid(self, x):
        # 應用sigmoid啟用函式
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        # 計算Sigmoid函式的偏導數
        return x * (1 - x)

    def train(self, training_inputs, yd, training_iterations):
        # 訓練模型
        for iteration in range(training_iterations):
            # 得到輸出
            y = self.sigmoid(np.dot(training_inputs, self.synaptic_weights))
            # 計算誤差
            error = yd - y
            # 微調權重( x 與 e*sigmoid_derivative )
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(y))

            self.synaptic_weights += adjustments


neural_network = NeuralNetwork()
print("Beginning Randomly Generated Weights: ")
print(neural_network.synaptic_weights)
# 訓練資料
training_inputs = np.array([(0, 0, 1),
                            (0, 1, 1),
                            (1, 0, 1),
                            (1, 1, 1)])

yd = np.array([[0, 0, 0, 1]]).T

neural_network.train(training_inputs, yd, 15000)

print("Ending Weights After Training: ")
print(neural_network.synaptic_weights)

k = -neural_network.synaptic_weights[0] / neural_network.synaptic_weights[1]
b = -neural_network.synaptic_weights[2] / neural_network.synaptic_weights[1]

fig = plt.figure()
ax = plt.subplot()
# ax=fig.add_axes([0, 0, 5, 5])
ax.scatter([training_inputs[i][0] for i in range(len(training_inputs)) if yd[i] == 0],
           [training_inputs[i][1] for i in range(len(training_inputs)) if yd[i] == 0], color='red')
ax.scatter([training_inputs[i][0] for i in range(len(training_inputs)) if yd[i] == 1],
           [training_inputs[i][1] for i in range(len(training_inputs)) if yd[i] == 1], color='blue')
ax.plot([0, 2], [k * (0) + b, k * 2 + b])

plt.show()

user_input_one = str(input("User Input One: "))
user_input_two = str(input("User Input Two: "))
user_input_three = str(input("User Input Three: "))

print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
print("New Output data: ")
print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
print("Wow, we did it!")