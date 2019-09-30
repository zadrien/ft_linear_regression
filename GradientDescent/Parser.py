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
