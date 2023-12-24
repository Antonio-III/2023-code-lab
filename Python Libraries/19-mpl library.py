import matplotlib.pyplot as plt # graph
import numpy as np # array (not required. list is fine)

xpoints=np.array([0,100])
ypoints=np.array([200,450])

# place the points on the graph and consequently creates the gui
plt.plot(xpoints,ypoints)

xpoints=np.array([100,50])
ypoints=np.array([50,50])

# 3rd arg replaces the end points with the character. Will connect the lines by default
plt.plot(xpoints,ypoints,'o')

# start the app
plt.show()
