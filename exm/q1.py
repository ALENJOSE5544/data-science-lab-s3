import numpy as np
x =np.array([1.9,2.3,3.5,4.7,5.3,6.1,7.3,8.5,9.1,10.3,11.7,12.9,13.3,14.9,15.7,16.1,17.3,18.3,19.3,20.5])
print(type(x))
print (x)
print(x.shape)


print(x.dtype)

print("Reshape array into 5X4 matrix")
b = x.reshape(5, 4)
print(b)
print("Display the elements of rows 2 to 5 and columns 1 to 3")

print(b[1:4,0:3])

print("Display the elements of 2 nd and 3 rd column")
print(b[:,1:3])

print("Display last 2 elements of last row")

print(b[4,2:4])