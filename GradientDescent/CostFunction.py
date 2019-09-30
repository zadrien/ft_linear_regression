def CostFunction(dataset, t0 = 0, t1 = 0):
    m = len(dataset)
    i = 0;
    tmp = 0

    while i < m:
        tmp += ((t0 + (t1 * dataset[i][0])) - dataset[i][1]) ** 2
        i += 1

    res = tmp / (2 * m)
    return res
        
    
