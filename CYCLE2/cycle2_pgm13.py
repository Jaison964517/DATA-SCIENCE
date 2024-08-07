import numpy as np
a=np.array([[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18],
            [19,20,21,22,23,24],
            [25,26,27,28,29,30]])
print("Jaison Jacob\n23mca033\ncycle2_pgm13")
print("Matrix Ais:")
print(a)
b=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix B is:")
print(b)
sub_m=a[:3,3]
print("The sub Matrixis:")
print(sub_m)
res=np.dot(sub_m,b)
print("Matrix after multiplication with sub matrix A and Matrix B:")
print(res)
a[:3,3]=res
print("Matrix A after operation:")
print(a)