import CostFunction

def Gradient(dataset, learningRate, t0 = 0, t1 = 0):

    cf = CostFuntion.CostFunction(dataset, t0, t1)
    while True :
        tmp0 = t0 - learningRate * (derivativeCostFunction(dataset, False, t0, t1))
        tmp1 = t1 - learningRate * (derivativeCostFunction(dataset, True, t0, t1))
        tmpcf = CostFuntion.CostFunction(dataset, tmp0, tmp1)
        print("TO TEST:", tmp0, tmp1, tmpcf)
        if tmpcf < cf:
            t0 = tmp0
            t1 = tmp1
            cf = tmpcf
            print("SAVE:", t0, t1, cf)
        else:
            print("WINNER: ", t0, t1, cf)
            break
        
        
    
    

def derivativeCostFunction(dataset, multiply=False, t0 = 0, t1 = 0):
    i = 0
    m = len(dataset);
    cf = 0
    while i < m:
        cf += ((t0 + (t1 * dataset[i][0])) - dataset[i][1])
        if multiply:
            cf *= dataset[i][0]
        i += 1

    res = cf / m

    return res
