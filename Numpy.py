import numpy as np

# np.array creates a numpy array from a lisr
x = np.array([1,2,3,4])
print(x) 
print(type(x))
print(x.ndim) # it will print the dimension of the array

l =[] #we can create a list in python and then convert it into array using np.array
for i in range(1,5):
    # to take input from the user and store it in list we use for loop 
    # and use variable of integer type  to take input using input() function 
    # and then append it to the list using append() method 
    int_1 = int(input("Enter a number:"))
    l.append(int_1)

print(np.array(l))

arr2 = np.array([[1,2,3],[4,5,6]])
 # created a 2D array using [[]] and then converted it into numpy array 
#  the number of elements in list should be same in each list to create a 2D array 
print(arr2) 
print(arr2.ndim)

arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
 # created a 3D array using [[]] and then converted it into numpy array 
#  the number of elements in list should be same in each list to create a 3D array 
print(arr3) 
print(arr3.ndim)

# we can create multidimensional array using np.array() ndmin = number of dimensions
arrn = np.array([1,2,3,4], ndmin = 20)
print(arrn)
print(arrn.ndim)

# array which contains all element as 0
arr_zero = np.zeros(4)
print(arr_zero)

# we can make it two dimensional or three 
arr_zero1 = np.zeros(((3,4,6)))
print(arr_zero1)

arr_ones = np.ones((6,4))
print(arr_ones)

# we can create a empty array
arr_Empty = np.empty(5)
print(arr_Empty)

# we can print an array or range 
arr_range = np.arange(1,5)
print(arr_range)

# we can create array with spacing
arr_spacing = np.linspace(0,20,num= 5)
print(arr_spacing)