import numpy

#########################
# One Dimensional Array
#########################

arr = numpy.array([1,2,3,4,5])

#First element
print(arr[0])

#Second last element
print(arr[-2])

#Add 3rd and 4th elements
print(arr[2]+arr[3])

#########################
# Two Dimensional Arrays
#########################

twoDimensionalArray = numpy.array([[1,2,3],[4,5,6]])

#Second element on first row
print(twoDimensionalArray[0,1])

#Third element on second row
print(twoDimensionalArray[1,2])


#########################
# Three Dimensional Arrays
#########################

threeDimensionalArrays1= numpy.array([[[1,2,3],[4,5,6]]])

threeDimensionalArrays2 = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(threeDimensionalArrays2[0,1,2])

