import matplotlib.pyplot as plt
ages=[12,32,3,43,55,33,56,89,98,53,34,34,34,5,6,7,2,11,34]
binsize=10
range=(0,100)
plt.hist(ages,binsize,range,color='green',histtype='bar',rwidth=0.8)
plt.xlabel('Distribution')
plt.ylabel('Age')
plt.show()