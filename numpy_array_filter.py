import numpy

arr1 = numpy.array([41,42,43,44])
selection = [False,True,False,True]
resultant_arr = arr1[selection]

print(resultant_arr)

arr2 = numpy.array([41,42,43,44])
filter_array=[]

for x in arr2:
    if x < 42:
        filter_array.append(True)
    else:
        filter_array.append(False)

resultant_arr2 = arr2[filter_array]

print("Filter array : ",filter_array)
print("Filtered array",resultant_arr2)

even_array = []

for x in arr2:
    if x%2==0:
        even_array.append(True)
    else:
        even_array.append(False)

print("Even filter : ",even_array)
print("Even array : ",arr2[even_array])

simple_filter = arr2>42
resultant_arr3 = arr2[simple_filter]

print("Simple filter : ",simple_filter)
print("Filtered array : ",resultant_arr2)

arr_new = numpy.array([1,2,3,4,5,6,7,8])

simple_filter2 = arr_new%2==0

print("Simple filter : ",simple_filter2)
print("Filtered array : ",arr_new[simple_filter2])

