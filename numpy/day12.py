import numpy as np

# arr_3d =np.array([[[2,3,5,],[6,8,9]],[[3,4,7],[4,7,8]]])
# print(arr_3d)

#3 x 3 matrix with all element zero
# zeros_a = np.zeros((3,3))
# print(zeros_a)

#3 x 3 matrix with all element one
# ones_a = np.ones((3,3))
# print(ones_a)

# to create an identity matrix of size 5 x 5
# id_mat=np.eye(6)
# print(id_mat)

# we have to create of first 50 number starting from 1
# arr = np.arange(1,51,2) # 2 is the step
# print(arr)

# arr = np.arange(2,101,2) # 2 is the step
# print(arr) 

# We need an array having 5 values  from 1 to 10 evenly spaced
# sp_arr = np.linspace(1,20,5)
# print(sp_arr)

# random_arr = np.random.rand(4, 4) # -> this create 4 x 4 matrix with all values ranging from 0 to 1
# print(random_arr)

# random_arr=np.random.randint(1,11,size= (4,3))
# print(random_arr)

# arr=np.array([[10,20,30],[20,40,70]], dtype="int16") #float > int
# print(arr)
# print(arr.shape)# -> denotes number of rows and column
# print(arr.size) # --> denotes the total no of number of element in a array
# print(arr.ndim)# -> Total number of dimension of in an array
# print(arr.dtype)# -> print the data types of an array
# print(arr.itemsize)
# print(arr.nbytes)

# arr_1d = np.array([10,20,30,40,50])
# print(arr_1d[1:4])

arr_2d = np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(arr_2d)
# print(arr_2d[-1,:])
# print(arr_2d[::2,2])
anti_diag= np.fliplr(arr_2d).diagonal()
print(anti_diag)

