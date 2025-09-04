import numpy as np #numpy.array --> numpy = np
import scipy.linalg as la
# # # #vector
# #v = np.array([1,2,3])
# # # print(v)

# # # #Matrix
# # # A= np.array([[1,2],[3,4]])
# # # print(A)
# # # #Result =[[1 2]
# # #         # [3 4]]

# # # #Scalar Multipliction
# # # v_scaled=8*v  #8 * v
# # # print(v_scaled)        


# # A= np.array([[1,2],[3,4]])
# # '''Result =1 2
# #            3 4
# #     '''
# # B=np.array([[2,4],[6,8]])
# # '''
# # A*B != B*A is not equal
# # mul =A @ B
# # 2  4
# # 6  8     2 x 2
# # '''
# # C = A @ B # -> matrix multiplication
# # mul = A*B # -> element wise multiplication
# # print(C)
# # print(mul)


# # add_v=A + B
# # print(add_v)

# # A_Transpose= A.T
# # print(A_Transpose)

# # 2x+3y = 8 , 5x+4y = 13
# #b = [8,13]
# '''
# A = 2  3
#     5  4
# '''
# A= np.array([[2,3],[5,4]])
# B= np.array([8,13])
# x = np.linalg.solve(A,B)
# print(f"Solution ; {x}")

# A = np.array([[8,3,-2],[-4,7,5],[3,4,-12]])
# B = np.array([9,5,35])
# x = np.linalg.solve(A,B) #[x_value , y_value, , z_value]
# print(x)

# A = np.array([[2,4,5],
#               [1,3,2],
#               [4,2,1]])
# P,L,U = la.lu(A) # [P_value , L_value , Z_value]
# print(f"P = {P}")
# print(f"L = {L}")
# print(f"U = {U}")

# f_value = P @ A
# l_value = L @ U
# print(f"f : {f_value}")
# print(f"l: {l_value}")
# #PA = LU

A = np.array([[1,2,3],
              [3,4,5]])
Q, R = np.linalg.qr(A)
result = Q @ R
print(Q)
print(R) 
print(A)
print(result)


