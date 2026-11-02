import numpy

arr1 = numpy.array([1,2,3])
arr2 = numpy.array([4,5,6])

arr = numpy.concatenate((arr1,arr2))

print("Array 1 : ",arr1)
print("Array 2 : ",arr2)
print("\nAfter concatenation : ",arr)

print("\n\n##########################")
print("Join 2-Dimensional Arrays")
print("##########################\n\n")


###########################
# Join 2-Dimensional Arrays
###########################

arr3 = numpy.array([[1,2],[3,4]])
arr4 = numpy.array([[5,6],[7,8]])
resultantArr2 = numpy.concatenate((arr3,arr4))
resultantArr3 = numpy.concatenate((arr3,arr4),axis=1)

print("Array 1 : ",arr3)
print("Array 2 : ",arr4)
print("\nAfter concatenation : ",resultantArr2)
print("\nAfter concatenation along the axis : ",resultantArr3)

print("\n\n##########################")
print("Stack Arrays")
print("##########################\n\n")

###########################
# Stack Arrays
###########################

arr5 = numpy.array([1,2,3])
arr6 = numpy.array([4,5,6])
resultantArr4 = numpy.stack((arr5,arr6))
resultantArr5 = numpy.stack((arr5,arr6),axis=1)

print("Array 1 : ",arr5)
print("Array 2 : ",arr6)
print("\nAfter stacking : ",resultantArr4)
print("\nAfter stacking along the axis : ",resultantArr5)

print("\n\n##########################")
print("Horizontal Stack Arrays")
print("##########################\n\n")

###########################
# Horizontal Stack Arrays
###########################


arr7 =  numpy.array([1,2,3])
arr8 = numpy.array([4,5,6])
resultantArr6=numpy.hstack((arr7,arr8))

print("Array 1 : ",arr7)
print("Array 2 : ",arr8)
print("\nAfter horizontal stacking : ",resultantArr6)


print("\n\n##########################")
print("Vertical Stack Arrays")
print("##########################\n\n")

###########################
# Horizontal Stack Arrays
###########################

arr9 = numpy.array([1,2,3])
arr10 = numpy.array([4,5,6])

resultantArr7=numpy.vstack((arr9,arr10))

print("Array 1 : ",arr9)
print("Array 2 : ",arr10)
print("\nAfter vertical stacking : ",resultantArr7)


print("\n\n##########################")
print("Depth Stack Arrays")
print("##########################\n\n")

###########################
# Depth Stack Arrays
###########################


arr11 = numpy.array([1,2,3])
arr12 = numpy.array([4,5,6])
resultantArr8 = numpy.dstack((arr11,arr12))

print("Array 1 : ",arr11)
print("Array 2 : ",arr12)
print("\nAfter depth stacking : ",resultantArr8)
