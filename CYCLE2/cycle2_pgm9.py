import numpy as np
arr_1d=np.array([1,2,3,4,5])
dia_mat=np.diag(arr_1d)
print("Jaison Jacob\n23mca33\ncycle2_pgm9")
print("\n1D Array:")
print(arr_1d)
print("\nDiagonal Matrix:")
print(dia_mat)
arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
dia_ele=np.diag(arr_2d)
print("\n2D Array :")
print(arr_2d)
print("\nDiagonal Element:")
print(dia_ele)
arr_2d_s=np.array([[1,2,3],[4,5,6]])
diag_ele_s=np.diag(arr_2d_s)
print("\n2D Non-Square Matrix:")
print(arr_2d_s)
print("\nDiagonal Elements(non-square):")
print(diag_ele_s)