import matplotlib.pyplot as plt
x1=[1,3,5] #x axis values
x2=[2,4,6]
y1=[2,4,6] #y axis values
y2=[1,3,5]
plt.plot(x1,y1,label="one") #to plot
plt.plot(x2,y2,label="two")
plt.xlabel('X axis') #to name x axis
plt.ylabel('y axis') #to name y axis
plt.title('Graph One') #to name the graph
plt.legend() #to display legend
plt.show() #to display the graph
