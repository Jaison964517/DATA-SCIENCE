import numpy as np
two_dim =np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])
exclu_firstr=two_dim[1:]
exclu_lasec=two_dim[:,:-1]
col_1_2_in_r_2_3=two_dim[1:3,0:2]
col_2_3=two_dim[:,1:3]
ele_first =two_dim[0,1:3]
des=two_dim.ravel()[::-1][4:11]
print("Jaison jacob\n23mca033\ncycle2_pgm6")
print("Orginal array:\n",two_dim)
print("Excluding first row:\n",exclu_firstr)
print("Excluding last column:\n",exclu_lasec)
print("elemnt of the first and 2nd column in the 2 and 3 row:\n",col_1_2_in_r_2_3)
print("element of 2 and 3 rs column:\n",col_2_3)
print("2 and 3 rd elemnt of the first row:\n",ele_first)
print("Descending order:\n",des)