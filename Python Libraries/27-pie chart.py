import matplotlib.pyplot as plt
import random
classes=['BSc Y1','BA Y1','BSc Y2','BA Y2','BSc Y3','BA Y3']
students_one=[random.randint(1,100+1) for i in range(6)]

#pie_label=classes

plt.pie(students_one,labels=classes,startangle=90,
        explode=(0,0,0,.05,0,0),
        radius=1,autopct='%0.2f%%')
# autopct has to do with how the % is presented. But also its position???


#plt.legend()
plt.show()
