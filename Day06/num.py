import numpy as np
# array = np.array([1,2,3,4])
# print(array)
# print(type(array))
# print(array.shape)

"""
     
    [   1   2   
        3   4   ]


"""

# print(array[0], array[1], array[2])
# print(array[-1], array[-3])

# array[-1] = 10
# print(array)

# array2D = np.array([[1,2,3],[4,5,6]])
# print(array2D.shape)
# print(array2D[0][1], array2D[1,2])

# array = np.zeros((3,3))
# print(array)

# array = np.ones((2,3))
# print(array)

# array = np.full((3,2), 7)
# print(array)

# array = np.random.random((2,2))
# print(array)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

# print(x+y)
# print("\n")
# print(np.add(x,y))
"""
    6   8
    10 12

"""
# print(x-y)
# print("")
# print(np.subtract(x,y))

print(x*y)
print("")
# print(np.multiply(x,y))

# print(x/y)
# print("")
# print(np.divide(x,y))

# print(np.sqrt(x))
# print(x.dot(y))
# print(np.dot(x,y))