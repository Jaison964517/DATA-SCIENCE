import numpy as np
a =np.array([[15,27,23],[14,53,62],[67,88,19]])
u,s,vt=np.linalg.svd(a)
a_ht =u @ np.diag(s) @ vt
print("Jaison Jacob\n 23mca033\ncycle2_pgm17")
print("Orginal matrix:")
print(a)
print("Singular value:")
print(s)
print("Reconstructed matrix A_ht:")
print(a_ht)