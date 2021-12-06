import numpy as np
x =np.array([[2,4,8],[3,4,7]])
print(type(x))
print(x)
print(x.shape)
print(x.dtype)
b = x.reshape(3, 2)
print(b)