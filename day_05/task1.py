

with open("day_5/data.txt", "r") as f:
    cargo_lines = []
    while True:
        line = f.readline()
        if line.startswith(' 1'):
            numbers = [int(i) for i in line.strip().replace(" ", "")]
            f.readline()
            break
        cargo_lines.append(line.strip("\n"))

    print(cargo_lines)
    cargo = []
    for i in range(len(numbers)):
        cargo.append([])

    
    for line in cargo_lines:
        i = 0
        while i < len(line):
            if line[i] is not " ":
                crate = line[i:i+3]
                to = (i/4)
                cargo[int(to)].append(crate)
                i += 2
            i+=1
    
    instructions = f.readlines()

    def do_move(num, from_crate, to_crate):
        for i in range(num):
            crate = cargo[from_crate-1].pop(0)
            cargo[to_crate-1].insert(0, crate)
        

    for instruction in instructions:
        instr = instruction.split()
        do_move(int(instr[1]), int(instr[3]), int(instr[5]))
    
    res = "".join([i[0] for i in cargo])
    print(res)


