import sys
import Dataset

class Gradient:
    def __init__(self, data, learningRate = 10):
        self.learningRate = learningRate
        self.dataset = Dataset.Parse(data)
        self.m = len(self.dataset)
        self.determineVar("./var")

    def determineVar(self, var):
        f = open("var", "r")
        s = f.readline()
        s = s.rstrip()
        print(s)
        s = s.split(",")
        print(s)
        self.t0 = int(s[0])
        self.t1 = int(s[1])
        f.close()

    def CostFunctionY(self, i = 0):
        if i == self.m:
            return 0
        x =  self.dataset[i].cost_function(self.t0, self.t1)
        res = x + self.CostFunctionY(i + 1)
        return res
    
    def CostFunctionX(self, i = 0):
        if i == self.m:
            return 0
        x =  self.dataset[i].cost_function(self.t0, self.t1) * self.dataset[i].x
        return x + self.CostFunctionX(i + 1)

    def CostFunction(self, t0, t1):
        cf = pow(self.CostFunctionY(), 2) / (2 * self.m)
        return cf
        
        
        
        
        

if len(sys.argv) == 2:
    gD = Gradient(sys.argv[1])
    print("Learning Rate: ", gD.learningRate)
    print("m: ", gD.m)
    print("theta0: ", gD.t0)
    print("theta1: ", gD.t1)
    print("costfunction theta0: ", gD.CostFunction(gD.t0, gD.t1))
    
