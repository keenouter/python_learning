'''
@Author: your name
@Date: 2020-07-13 16:40:56
@LastEditTime: 2020-07-13 16:44:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python_learning\basics\matplot\figure_1_1.py
'''

import matplotlib.pyplot as plt
import numpy as np

x = [0, 0, 5, 10, 15, 15, 10, 5]
y = [5, 10, 15, 15, 10, 5, 0, 0]

plt.fill(x, y, color='cornflowerblue')

plt.xlim(-1, 16)
plt.ylim(-1, 16)

plt.xticks(np.arange(0, 16, 5))
plt.yticks(np.arange(0, 16, 5))

plt.show()
