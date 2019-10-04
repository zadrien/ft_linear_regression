import sys

iteration = 20000

def Gradient(dataset, learningRate, t0 = 0.0, t1 = 0.0):
    for i in range(0, iteration):
        tmp = derivateCostFunction(dataset, t0, t1)
        
        t0 = t0 - (learningRate * tmp[0])
        t1 = t1 - (learningRate * tmp[1])
    return [ t0, t1 ]

        
    
    

def derivateCostFunction(dataset, t0 = 0, t1 = 0):
    m = len(dataset[0]);
    d0 = 0.0
    d1 = 0.0
    for i in range(0, m):
        d0 += t0 + (t1 * (float(dataset[0][i]) / 10000) ) - float(dataset[1][i])
        d1 += (t0 + (t1 * (float(dataset[0][i]) / 10000)) - float(dataset[1][i])) * (float(dataset[0][i]) / 10000)


    return [ (1/m) * d0, (1/m) * d1]
