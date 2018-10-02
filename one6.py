import matplotlib.pyplot as plt
import numpy as num
plt.xlabel('x axis')
plt.ylabel('y axis')
x=num.arange(0,4*(num.pi), 0.1)
y=num.sin(x)
plt.plot(x,y)
plt.show()