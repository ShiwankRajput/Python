import matplotlib.pyplot as plt

x = [10,20,30,40,50]
y = [30,45,36,25,19]

plt.barh(x,y,label="x vs y",color="skyblue",edgecolor="black",height=4)
plt.title("bar-graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()