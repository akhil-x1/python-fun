import numpy

arr = numpy.array([1,2,3,4,5])


print(arr[1:4])

print(arr[1:])

print(arr[:4])

print(arr[1:4:2])

print(arr[::2])


#########################
# Negative Slicing
#########################

print(arr[-1:])

print(arr[-3:-1])

print(arr[-3:5])

print(arr[-5:-1:2])

#########################
# 2D array Slicing
#########################

print("2D array Slicing")
print("######################")

twoDimensionalArray = numpy.array([[1,2,3,4,5],[6,7,8,9,10]])

print(twoDimensionalArray[0,3:5])

print(twoDimensionalArray[1,1:3])


print(twoDimensionalArray[0:2,1:3])