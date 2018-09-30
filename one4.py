#BAR GRAPH
import matplotlib.pyplot as plt
left=[1,2,3,4,5]
height=[5,4,3,2,1]
tick_label=['one','two','three','four','five']
plt.bar(left,height,tick_label=tick_label,width=1,color=['red','blue','yellow'])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
