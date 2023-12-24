import matplotlib.pyplot as plt
import random

# what is this?
#figure=plt.figure()

classes=['BSc Y1','BA Y1','BSc Y2','BA Y2','BSc Y3','BA Y3']
students=[random.randint(1,100+1) for i in range(6)]
bozo=['1','2','3','4','5','6']

# labels underneath bars
bar_label=classes

# plot the bar chart
# colors is just alternating. no reason for it
# 1st arg is the bar graph (can be any same-length-as-the-numbers data structure so long as it has unique values), 2nd is the height of it. 3rd is the gap between them
# width of 1 means the bars are touching. tick_label are the names underneath the bars.
plt.bar(bozo,students,width=.9,
        color=['skyblue','lightblue'],tick_label=classes)

# label x-axis
plt.xlabel('Classes')

# label y-axis
plt.ylabel('Students')

# Bar graph title (at the top)
plt.title('Students enrolled in classes!')


# start app
plt.show()
