import matplotlib.pyplot as plt

food = ['meat','banana','avocados','sweet potatoes','spioach','coconut water','legumes','tomato','watermelon','beans']
calories = [250,130,140,120,20,20,10,50,40,19]
potassium = [40,55,20,30,40,32,10,26,26,20]
fat = [8,5,3,6,1,1.5,0,2,1.5,2.5]

fig = plt.figure(figsize=(12,8))
plt.title("Line-Graph")
plt.plot(food,calories,linewidth=1,color="red",linestyle="-",marker='^')
plt.plot(food,potassium,linewidth=2,color="purple",linestyle="-.",marker=">")
plt.plot(food,fat,linewidth=3,color="green",linestyle=":",marker="<")
plt.xlabel("<-------- x-axis -------->")
plt.ylabel("<-------- y-axis -------->")
plt.show()