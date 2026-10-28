import numpy

arr = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12])

oneDtoTwoDArray = arr.reshape(4,3)
oneDtoThreeDArray = arr.reshape(2,3,2)
unknownDimensionArray = arr.reshape(2,3,-1)

twoColumnArr = numpy.array([[1,2,3,4,5],[6,7,8,9,10]])

print("1D to 2D array : ",oneDtoTwoDArray)
print("1D to 3D array : ",oneDtoThreeDArray)
print("Unknown dimension array : ",unknownDimensionArray)
print("Base (copy or view) : ",oneDtoThreeDArray.base)
print("Array flattening : ",twoColumnArr.reshape(-1))

#Can't reshape to any shape
print("Succesful reshaping : ",twoColumnArr.reshape(2,5))
print("Unsuccesful reshaping : ",twoColumnArr.reshape(3,3))

