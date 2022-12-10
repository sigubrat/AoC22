with open("day_7/data.txt", "r") as f:
    lines = f.readlines()
    directories = {"/": {"size": 0}}
    cd = []
    values = {}

    def update_directory():
        level = directories
        for d in cd:
            if d not in level:
                level[d] = {"size": 0}
                return
            level = level[d]

    def handle_command(cmd):
        if cmd[1] == "ls":
            return

        d = cmd[2]
        if d == "..":
            cd.pop()
        else:
            cd.append(d)
            update_directory()
        return

    def update_values(size):
        for i in range(len(cd)):
            key = "".join(cd[:i+1])
            if key not in values:
                values[key] = size
            else:
                values[key] += size

    def update_size(size):
        if len(cd) == 1:
            directories["/"]["size"] += size
            return

        level = directories
        for d in cd:
            if d not in level:
                return
            level[d]["size"] += size
            level = level[d]
            
    def handle_read(data):
        if data[0] == "dir":
            return
        else:
            update_size(int(data[0]))
            update_values(int(data[0]))
        return

    for line in lines:
        output = line.strip().split()
        if output[0] == "$":
            handle_command(output)
        else:
            handle_read(output)
    
    res = 0
    print(directories)
    print(values)
    for val in values.values():
        if val <= 100000:
            res += val

    print(res) 