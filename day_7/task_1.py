with open("day_7/data.txt", "r") as f:
    lines = f.readlines()
    cd = []
    values = {}

    def handle_command(d):
        if d == "..":
            cd.pop()
        else:
            cd.append(d)

    def update_values(size):
        for i in range(len(cd)):
            key = "".join(cd[:i+1])
            if key not in values:
                values[key] = size
            else:
                values[key] += size

    for line in lines:
        output = line.strip().split()
        if output[0] == "dir" or output[1] == "ls":
            continue
        if output[0] == "$":
            handle_command(output[2])
        else:
            update_values(int(output[0]))
    
    res = 0
    for val in values.values():
        if val <= 100000:
            res += val

    print(res) 