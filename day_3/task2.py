with open("data.txt", "r") as f:
    raw = [line.rstrip() for line in f]
    data = []
    tmp = []
    for i, line in enumerate(raw):
        tmp.append(line)
        if (i+1)%3 == 0 and i != 0:
            data.append(tmp)
            tmp = []

    items = [''.join(set(backpacks[0]).intersection(backpacks[1]).intersection(backpacks[2])) for backpacks in data]

    sum = 0
    for item in items:
        sum += ord(item)-96 if item.islower() else ord(item)-38

    print(sum)