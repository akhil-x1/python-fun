import numpy

print("\n###########")

#1-D array
print("1-D array")

print("###########\n")

arr1 = numpy.array([1,2,3])

print("Array : ",arr1)

for x in arr1:
    print(x)

print("\n###########")
#2 D array
print("2-D array")
print("###########\n")

arr2 = numpy.array([[1,2,3],[4,5,6]])

print("Array : ",arr2)
print("\n")

for x in arr2:
    print(x)


print("\nIterating through each item")

for x in arr2:
    for y in x:
        print(y)

print("\n###########")
#3 D array
print("3-D array")
print("###########\n")

arr3 =  numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print("Array : ",arr3)
print("\n")

for x in arr3:
    for y in x:
        for z in y:
            print(z)

print("\n###########")
#nd-Iter array
print("nd-Iter")
print("###########\n")

for x in numpy.nditer(arr3):
    print(x)

print("\n###########")
#op data types
print("op data types")
print("###########\n")

for x in numpy.nditer(arr3,flags=['buffered'],op_dtypes=['S']):
    print(x)


print("\n###########")
#step size
print("step size")
print("###########\n")

for x in numpy.nditer(arr3[:,::2]):
    print(x)

print("\n###########")
#nd-enumerate
print("nd-enumerate")
print("###########\n")

for index, value in numpy.ndenumerate(arr1):
    print(index,value)

print("\n")

for index,value in numpy.ndenumerate(arr2):
    print(index,value)
