import matplotlib.pyplot as plt

x_axis=[i for i in range(1,11)]
y_axis=[5,2,4,4,8,7,4,9,10,9]

# marks the x,y pair as 'o', and connect the points in the order of the array
# 'marker' marks the points as 'o', and still connects the dots.
plt.plot(x_axis,y_axis,marker='o')

# give name to the x axis
plt.xlabel('Time (seconds)')

# give name to y axis
plt.ylabel('Temp (degC)')

#start the gui
plt.show()
