import matplotlib.pyplot as plt

x1 = [10,35,15,43,47,89]
y1 = [8,34,28,76,65,14]
x2 = [45,36,76,15,54,24]
y2 = [14,35,47,85,73,52]

plt.scatter(x1,y1,color="blue",edgecolors="yellow",marker="^")
plt.scatter(x2,y2,color="red",marker="s")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()