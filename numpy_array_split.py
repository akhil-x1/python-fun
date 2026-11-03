import numpy


arr1 = numpy.array([1,2,3,4,5,6,7,8,9])
resultantArray1 = numpy.array_split(arr1,3)
resultantArray2 = numpy.array_split(arr1,4)
print(resultantArray1)
print(resultantArray1[0])
print(resultantArray1[1])
print(resultantArray1[2])
print(resultantArray2)

twoDArray = numpy.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
resultantArray3 = numpy.array_split(twoDArray,3)
print(resultantArray3)

print("\n")
twoDArray2 = numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
resultantArray4 = numpy.array_split(twoDArray2,3)
print(resultantArray4)

twoDArray3 = numpy.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
resultantArray5 = numpy.array_split(twoDArray3,3)
print(resultantArray5)

resultantArray6 = numpy.array_split(twoDArray3,3,axis=1)
print(resultantArray6)

resultantArray7 = numpy.hsplit(twoDArray3,3)
print(resultantArray7)