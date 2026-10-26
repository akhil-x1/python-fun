import numpy

arr = numpy.array([1,2,3,4,5])

copy = arr.copy()
view = arr.view()

print("Original Array : ",arr)
print("Original Copy : ",copy, " Base : ",copy.base)
print("Original View : ",view, "Base : ", view.base)


print("Assigns 42 to 0th position of original array")
arr[0] = 42

print("Array after update: ",arr)

print("Assigns 21 to 1st position of copy array")
copy[1] = 21

print("Copy after update: ",copy)

print("Assigns 33 to 2nd position of view array")
view[2] = 33

print("View after update: ",view)
