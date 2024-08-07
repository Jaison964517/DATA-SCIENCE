import numpy as np
eve_no = np.arange(2,31,2)
slice_res =eve_no[2:9:2]
last_3 =eve_no[-3:]
alternate=eve_no[::2]
last_3_alter =alternate[-3:]
print("Jaison jacob\n23mca033\ncycle2_pgm5")
print("Orginal array:",eve_no)
print("Elemts from result 2 to 8 with step 2:",slice_res)
print("Last 3 elemts from array:",last_3)
print("Alternative elements from Array:",alternate)
print("Last 3 elemets from Alternative array:",last_3_alter)