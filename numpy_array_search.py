import numpy

arr1 = numpy.array([1,2,3,4,5,4,4])
result1 = numpy.where(arr1==4)
print(result1)

arr2 = numpy.array([10,14,93,41,8,7])
result2 = numpy.where(arr2%2==1)
print(result2)

arr3 = numpy.where(arr2%2==0)
print(arr3)

arrSorted = numpy.array([7,8,10,14,41,93])

arr4 = numpy.searchsorted(arrSorted,41)
print(arr4)

arr5 = numpy.searchsorted(arrSorted,8,side="right")
print(arr5)

arr6 = numpy.searchsorted(arrSorted,[14,10,8])
print(arr6)
