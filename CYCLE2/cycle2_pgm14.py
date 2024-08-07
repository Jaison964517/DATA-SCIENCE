import numpy as np
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
b=np.array([[9,8,7],
            [6,5,4],
            [3,2,1]])
c=np.array([[10,5,9],
            [20,15,19],
            [30,2,19]])
re=np.dot(np.dot(a,b),c)
print("Jaison Jacob\n23mca033\ncycle2_pgm14")
print("Matrix A:")
print(a)
print("MatrixB:")
print(b)
print("Matrix C:")
print(c)
print("Result of(a*b)*c:")
print(re)