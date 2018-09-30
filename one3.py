import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[4,5,2,4,6,7,2,4,6,7]
plt.xlim(0,10)
plt.ylim(0,10)
plt.plot(x,y,color="blue",linewidth=3,
         linestyle="dashed",marker="o",markersize=12,markerfacecolor="yellow")
plt.show()