import matplotlib.pyplot as plot
import numpy as np
lan = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
pop = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
exp = [0.2, 0, 0, 0, 0, 0]
plot.pie(pop, labels = lan, explode = exp, shadow = True, autopct='%1.1f%%', startangle = 135)
plot.show()