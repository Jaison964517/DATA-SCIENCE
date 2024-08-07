import numpy as np
mat1=np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2 =np.array([[9,8,7],[6,5,4],[3,2,1]])
mat_sum=mat1+mat2
mat_diff=mat1-mat2
mat_pro=mat1*mat2
mat_div=mat1/mat2
mat_mul=np.dot(mat1,mat2)
mat_tran=np.transpose(mat1)
dia_sim=np.trace(mat1)
print("Jaison Jacob\n23mca033\ncycle2_pgm7")
print("matrix1",mat1)
print("Matrix2",mat2)
print("Matrix sum:\n",mat_sum)
print("Matix difference:\n",mat_diff)
print("Matrix Element-wise product:\n",mat_pro)
print("Matrix Elemnt-wise Division:\n",mat_div)
print("Matrix Multiplication\n",mat_mul)
print("Trancepose of matrix1:\n",mat_tran)
print("diagonal sum of matrix1:\n",dia_sim)
