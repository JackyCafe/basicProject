import numpy as np
a = [[1,2],[3,4]]
b = [[1,2,3],[3,4,5]]
print(type(a))
numpy_a = np.array(a)
numpy_b = np.array(b)
print(numpy_a)
print(numpy_b)
print(numpy_a.dot(numpy_b))
print(numpy_a.T)
new_a = np.array([1,2,3,4])
x = np.resize(new_a,(4,1))
print('new_a',x)