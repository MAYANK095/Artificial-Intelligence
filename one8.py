import matplotlib.pyplot as plt
activities=['eat','sleep','rave','repeat']
slices=[5,6,7,8]
colors=['r','g','b','y']
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.pie(slices,labels=activities,colors=colors,startangle=90,shadow= False,
        explode=(1,1,1,1),autopct='%1.1f%%')
plt.show()