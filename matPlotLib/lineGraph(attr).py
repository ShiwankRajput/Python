import matplotlib.pyplot as plt

x = [10,20,30,40,50]
y = [70,55,39,48,50]
z = [15,10,35,27,19]

plt.plot(x,y,label="x vs y",color="red",linestyle=":",linewidth=3,marker=">")
plt.plot(x,z,label="x vs z",color="purple",linewidth=1,linestyle="-.",marker="*")
plt.title("line graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()