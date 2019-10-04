import sys

sys.path.append('./GradientDescent')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Parser

dataset = Parser.parse('Dataset')

t = Parser.parse('./GradientDescent/variables.csv')

print(dataset)
print(t);

fig, ax = plt.subplots()

x = np.array(dataset[0])
y = t[0][0] + (t[1][0] * (x / 10000))

ax.plot(dataset[0], dataset[1], 'o', alpha=0.5)
ax.plot(x, y, 'r')

ax.set_xlabel('km')
ax.set_ylabel('Price (in euro)')

plt.grid()
plt.show()
