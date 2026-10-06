import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

# Prints version
print("Numpy version :",np.__version__)

# Prints type as ndarray
print(type(arr))

zeroDimensionArray = np.array(42);
oneDimensionArray = np.array([1,2,3,4,5])
twoDimensionArray = np.array([[1,2,3],[4,5,6]])
threeDimensionArray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
fiveDimensionArray = np.array([1,2,3],ndmin=5)

# 0 Dimension array
print("Zero dimension array :",zeroDimensionArray)

# 1 Dimension array
print("One dimension array :",oneDimensionArray)

# 2 Dimension array
print("Two dimension array :",twoDimensionArray)

# 3 Dimension array
print("Three dimension array :",threeDimensionArray)

print(zeroDimensionArray.ndim)
print(oneDimensionArray.ndim)
print(twoDimensionArray.ndim)
print(threeDimensionArray.ndim)
print(fiveDimensionArray.ndim)



