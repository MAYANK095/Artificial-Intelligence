import matplotlib.pyplot as plt
x=[0,1,2,3,4,5,6,7,8,9]
y=[4,7,6,2,1,3,8,9,5,0]
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.scatter(x,y,label="stars",color="red",marker="*", s=30)
plt.show()