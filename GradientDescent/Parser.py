import csv

def parse(file):
    x = []
    y = []
    
    f = open(file, "r")
    reader = csv.reader(f)
    next(reader)
    for  row in reader:
        if isfloat(row[0]) == True and isfloat(row[1]) == True:
            x.append(float(row[0]))
            y.append(float(row[1]))
        else:
            print("Not digit:\n", row)
            return

    f.close()

    return [x, y]

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
