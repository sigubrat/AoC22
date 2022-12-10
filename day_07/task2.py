with open("day_7/data.txt", "r") as f:
    lines = f.readlines()
    cd = []
    values = {}
    total_available = 70000000
    required = 30000000

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

    def handle_read(data):
        update_values(int(data[0]))

    for line in lines:
        output = line.strip().split()
        if output[0] == "dir" or output[1] == "ls":
            continue
        if output[0] == "$":
            handle_command(output[2])
        else:
            update_values(int(output[0]))
    
    unused_space = total_available - values['/']
    to_del = required - unused_space
    if to_del <= 0:
        print("No need for deletion, bossman")
    
    possibilities = []
    for d in values.values():
        if d >= to_del:
            possibilities.append(d)
    
    print(min(possibilities))
