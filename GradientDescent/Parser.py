def Parse(file):
    x = []
    y = []
    
    f = open(file, "r")
    f.readline()
    for str in f:
        line = str.rsplit()
        line = line[0].split(",")
        if len(line) == 2:
            if line[0].isdigit() and line[1].isdigit():
                x.append(int(line[0]))
                y.append(int(line[1]))
            else:
                print("Not digit:\n", line)
                return
        else:
            print("Error too much argument in:\n", line)
    f.close()

    return [x, y]
