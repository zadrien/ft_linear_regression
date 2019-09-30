import sys
import Dataset

def grad(prev, new):
    pre = prev - new
    print("precision: ", pre)
    if pre > 0.01:
        return True
    return False

class Gradient:
    def __init__(self, data, learningRate = 5):
        self.learningRate = learningRate
        self.data = Dataset.Dataset(data)
        self.m = len(self.data.s)
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

    def CostFunction(self, t0, t1):
        cf = self.data.Sum(t0, t1) / self.m
        return cf

    def Start(self):
        p = self.CostFunction(self.t0, self.t1)
        while True :
            tmp0 = self.t0 - ((self.learningRate*((self.data.Sum(self.t0, self.t1))))/ self.m)
            tmp1 = self.t1 - ((self.learningRate*((self.data.Sum(self.t0, self.t1, True))))/ self.m)
            print("tmp0: ", tmp0)
            print("tmp1: ", tmp1)
            n = self.CostFunction(tmp0, tmp1)
            print("CostFunction of tmp:", n)
            print("tmp costFunction: ", n)
            if grad(p, n) == False:
                self.t0 = tmp0
                self.t1 = tmp1
                p = n
            else:
                break

    
        
        

if len(sys.argv) == 2:
    gD = Gradient(sys.argv[1])
    print("Learning Rate: ", gD.learningRate)
    print("m: ", gD.m)
    print("theta0: ", gD.t0)
    print("theta1: ", gD.t1)
    print("costfunction theta0: ", gD.data.Sum(gD.t0, gD.t1, False))
    gD.Start()

