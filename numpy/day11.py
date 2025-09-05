import numpy as np

# v1= np.array([1,0,0])
# v2= np.array([0,1,0])
# v3= np.array([1,0,0])

# A = np.column_stack((v1,v2,v3))

# Rank =np.linalg.matrix_rank(A)
# print(f"Rank of the matrix = {Rank}")
# print(A)

# v1 = np.array([1,2])
# v2 = np.array([2,4])  #v2= 2 x v1 --> linearly Dependent
# A = np.column_stack((v1,v2))
# Rank = np.linalg.matrix_rank(A)
# print(f"Rank of the matrix: {Rank}") #1
 
v1 = np.array([1,2,3])
v2= np.array([2,4,6])
v3 = np.array([9,8,10])

A = np.column_stack((v1,v2,v3))
Rank = np.linalg.matrix_rank(A)
print(A)
print(f"Rank : {Rank}")