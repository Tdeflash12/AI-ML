import numpy as np 

# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# re_arr= arr.reshape(2,5)
# print(arr)
# print(re_arr)

# arr_1d= ([10,20,30,40])
# for num in arr_1d:
#     print(num, end=" ")

# arr_2d = np.array([[10,20,30],
#                    [40,50,60]])
# for num in np.nditer(arr_2d):
#     print(num)

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

add = a + b
sub =a-b
produt=a*b
div=a/b
exp = b**a
reminder = b % a
print(f"Addtion of two arrays element wise: {add}")
print()
print(f"Subtaction of two arrays element wise: {sub} ")
print()
print(f"Product of two arrays element wise: {produt} ")
print()
print(f"Division of two arrays element wise: {div} ")
print(f"Each element of an array {b} raised to the power 5 gives {exp} ")
print()
print(f"Remainder of {b} divides by {a} element wise: {reminder}")