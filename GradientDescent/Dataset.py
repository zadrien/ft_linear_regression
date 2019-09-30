import sys

class Ex:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def cost_function(self, t0, t1):
        return ((t0 + t1*float(self.x)) - float(self.y)) ** 2


class Dataset:
    def __init__(self, data):
        self.s = Parse(data)
        self.m = len(self.s)

    def Sum(self, t0, t1, mult = False, i = 0):
        if i == self.m:
            return 0
        x = self.s[i].cost_function(t0, t1)
        if mult == True:
            x *= float(self.s[i].x)
        res = x + self.Sum(t0, t1, i + 1, mult)
        return res
        
def Parse(file):
    f = open(file, "r")
    dataset = []
    f.readline()
    for line in f:
        x = line.rsplit()
        x = x[0].split(",")
        if len(x) == 2:
            if x[0].isdigit() and x[1].isdigit():
                dataset.append([x[0], x[1]])
            else:
                print("Not all digit:\n", line)
                return
        else:
            print("Error too much argument in:\n", line)
    f.close()
    i = 0;
    while i < len(dataset):
        print("->", dataset[i])
        i += 1
    return dataset
