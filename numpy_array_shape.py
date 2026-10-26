import numpy

arr = numpy.array([[1,2,3,4,5],[1,2,3,4,5]])

print(arr.shape)


#5 dimension array using ndmin

fiveDimensionArr = numpy.array([1,2,3,4,5],ndmin=5)

print("Five dimension array : ",fiveDimensionArr)