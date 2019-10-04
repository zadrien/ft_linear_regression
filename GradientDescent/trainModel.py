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
    

dataset = Parser.parse('../Dataset')
print(dataset)
if dataset:
    print("Begin traning...")
    t = Gradient.Gradient(dataset, 0.01)
    if t:
        print("Trained!", t)
    else:
        print("Error: Gradient Descent")



f = open('variables.csv', 'w')
writer = csv.writer(f, delimiter=',')
writer.writerow(['theta0', 'theta1'])
writer.writerow(t)

f.close();

        
