import numpy

intArr=numpy.array([1,2,3,4,5])
stringArr = numpy.array(["apple","banana","cherry"])

print(intArr.dtype)
print(stringArr.dtype)

#Arrays with defined datatype

stypeArr=numpy.array([1,2,3,4,5],dtype="S")
print(stypeArr)
print(stypeArr.dtype)

stypeArr=numpy.array([1,2,3,4,5],dtype="U")

print(stypeArr)
print(stypeArr.dtype)

intArr = numpy.array([1,2,3,4],dtype="i4")
print(intArr)
print(intArr.dtype)

#Type conversion 

floatArr = numpy.array([1.1,2.1,3.1])
floatToIntArr = floatArr.astype("i")
print(floatToIntArr)
print(floatToIntArr.dtype)

floatToIntArr2 = floatArr.astype(int)
print(floatToIntArr2)
print(floatToIntArr2.dtype)

intArr2 = numpy.array([1,0,3])
boolArr = intArr2.astype(bool)
print(boolArr)
print(boolArr.dtype)


#Wrong type assignment
wrongTypeConversionArr = numpy.array(['a', '2', '3'],dtype="i")
print(wrongTypeConversionArr)