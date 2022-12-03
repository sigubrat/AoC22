with open("data.txt", "r") as f:
    raw = [line.rstrip() for line in f]
    data = []
    for line in raw:
        first, second = line[:len(line)//2], line[len(line)//2:]
        data.append([first, second])
    
    items = [''.join(set(backpacks[0]).intersection(backpacks[1])) for backpacks in data]
    
    sum = 0
    for item in items:
        sum += ord(item)-96 if item.islower() else ord(item)-38

    print(sum)
    
