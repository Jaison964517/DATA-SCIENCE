import numpy as np
def is_symmetric(mat):
    return(mat ==mat.T).all()

def is_skew(mat):
    return(mat ==mat.T).all()

mat =np.array([[0,1,-2],
               [-1,0,3],
               [2,-3,0]])
print("Jaison Jacob\n23mca033\ncycle2_pgm15")
if is_symmetric(mat):
    print("The matrix is symmetric:")
elif is_skew(mat):
    print("The Matrix is skew-symmetric:")
else:
    print("THe Matrix is neither sym nor skew...")