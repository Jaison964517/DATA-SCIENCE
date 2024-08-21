import matplotlib.pyplot as plt
y=[2001,2002,2003,2004,2005,2006,2007]
car_v =[24000,22500,19700,17500,14500,10000,5800]
plt.figure(figsize=(10,6))
plt.subplot(111)
plt.plot(y,car_v,linestyle ='-',color='red',marker='*',markersize=20,markerfacecolor='green')
plt.title("Jaison Jacob \n 23mca033\ncycle3_pgm1",loc="right")
plt.title("Value Depreciation",loc="left")
plt.xlabel("year")
plt.ylabel("Car value")
plt.show()