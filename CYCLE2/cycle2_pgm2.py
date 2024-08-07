import numpy as np
arr_2d =np.array([[1+2j,3+4j,5+6j],[7+8j,9+10j,11+12j]], dtype=complex)
print("Jaison jacob\n23mca033\ncycle2_pgm2")
print("2D Array")
print(arr_2d)
r,c=arr_2d.shape
print("no:of rows:",r)
print("no:of column:",c)
dia=arr_2d.ndim
print("Dimension of the array:",dia)
reshap=arr_2d.reshape(3,2)
print("Reshape array(3*2:")
print(reshap)