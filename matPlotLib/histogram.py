import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(1000)
plt.hist(data,bins=40,color="pink",edgecolor="black")
plt.title("histogram")
plt.xlabel("values")
plt.ylabel("frequency")
plt.show()