import matplotlib.pyplot as plt
import random
# ignore
#figure=plt.figure()

classes=['BSc Y1','BA Y1','BSc Y2','BA Y2','BSc Y3','BA Y3']
students_one=[random.randint(50,100+1) for i in range(6)]

# second bar must have lower values so as to not overlap the first bar
students_two=[random.randint(0,49+1) for i in range(6)]
print(students_one,students_two)
label_belw_bars=classes

# first bar is plotted first, so if the second bar has higher numbers, it will cover the first bar, rendering it invisible
plt.bar(classes,students_one,color='skyblue')
plt.bar(classes,students_two,color='lightgreen')

plt.xlabel('Classes')
plt.ylabel('Students')

plt.title('Students enrolled')
plt.show()
