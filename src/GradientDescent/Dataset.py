import sys

class Ex:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def cost_function(self, t0, t1):
        return (t0 + t1*self.x) - self.y


class Dataset:
    def __init__(self, data):
        self.s = Parse(data)
        self.m = len(self.s)

    def SumtT0(self, i = 0):
        
def Parse(file):
    f = open(file, "r")
    dataset = []
    f.readline()
    for line in f:
        x = line.rsplit()
        x = x[0].split(",")
        if len(x) == 2:
            if x[0].isdigit() and x[1].isdigit():
                print(x)
                dataset.append(Ex(int(x[0]), int(x[1])))
            else:
                print("Not all digit:\n", line)
                return
        else:
            print("Error too much argument in:\n", line)

    for i in dataset:
        print(i.cost_function(0, 1))
    print("m = ", len(dataset))
    f.close()
    return dataset
