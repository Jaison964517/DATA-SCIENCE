import  numpy as np
mat_s=3
mat=np.random.randint(10,20, size=(mat_s,mat_s))
print("Jaison Jacob\n23mca033\ncycle2_pgm10")
print("\nOrginal Matrix:")
print(mat)
if np.linalg.matrix_rank(mat) == mat_s:
    inv_mat=np.linalg.inv(mat)
    print("\nInverse Matrix")
    print(inv_mat)
else:
    print("\nTHe matrix is not invertable")
rank=np.linalg.matrix_rank(mat)
print("\nRank of a Matrix:",rank)
det=np.linalg.det(mat)
print("\nDeterminant of Matrix:",det)
mat_1d=mat.flatten()
print("\n Matrix as 1D Array:")
print(mat_1d)
eigenval,eigenv=np.linalg.eig(mat)
print("\nEigan values:")
print(eigenval)
print("\n Eigen Vectors:")
print(eigenv)

