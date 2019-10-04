import Parser
import Gradient
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv



def plot(data, x):
    m = len(data)
    arr = []
    for i in range(0, m):
        arr.append(x * float(data[i]))
    
    
file = open('../Dataset', 'r+')
print(file)

reader = csv.reader(file)
next(reader)
for row in reader:
    print(row)

quit()
dataset = Parser.Parse('../Dataset')
print(dataset)
if dataset:
    print("Begin traning...")
    t = Gradient.Gradient(dataset,0.01)
    if t:
        print("Trained!", t)
    else:
        print("Error: Gradient Descent")



fig, ax = plt.subplots()

x = np.array(dataset[0])
y = t[0] + (t[1] * (x / 10000))

ax.plot(dataset[0], dataset[1], 'o', alpha=0.5)
ax.plot(x, y, 'r')

ax.set_xlabel('km')
ax.set_ylabel('Price (in euro)')

plt.grid()
plt.show()
