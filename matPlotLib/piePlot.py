from matplotlib import pyplot as plt

cars = ['Audi','BMW','Tesla','Mercedes','Jaguar']
data = [20,35,78,56,8]

# fig = plt.figure(figsize =(10,7))
plt.pie(data,labels=cars)
plt.show()