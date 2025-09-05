import numpy as np
# A = np.array([[2,-1],
#               [3,4]])
# x = np.array([1,2])

# Tx= A @ x
# print(f"T(x) = {Tx}")
#scaled vector

# kx,ky = 1.5 , 0.5
# A = np.array([[kx,0],
#               [0,ky]])
# x=np.array([2,3])
# Tx = A @ x
# print(f"Orginal vector  : {x}")
# print(f"Scaled vector : {Tx}")

#Rotation
# theta = np.pi / 2 #90  degrees

# A = np.array([[np.cos(theta), -np.sin(theta)],
#               [np.sin(theta),  np.cos(theta)]])
# x = np.array([3 , 2]) # ->> Orginal vector
# rotated_vector = A @ x
# print(f"Orginal Vector :  {x}")
# print(f"Rotated Vector:  {rotated_vector}")

# Reflection about X axis
# A= np.array([[1,0],
#              [0,-1]])
# x = np.array([4,5])
# reflected_veector= A @ x
# print(f"Orginal_vector :{x}")
# print(f"Reflected_vector :{reflected_veector}")

A= np.array([[2,3],
             [4,9]])

B = np.array([[4,7],
              [4,10]])
x = np.array([1,2])
result1 = B @ (A@x)
intermediate_matrix = B @ A
result2 = intermediate_matrix @ x
print(result1)
print(result2)

