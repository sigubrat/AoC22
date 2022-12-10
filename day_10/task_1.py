x = 1
cycle = 0
special_n = 20
special_cycle = 40
signal = []

def check_cycle():
    if cycle == special_n-1 or (cycle-special_n+1)%(special_cycle) == 0:
            signal.append(x*(cycle+1))

with open("day_10/data.txt", "r") as f:
    program = [i.strip().split() for i in f.readlines()]

    for line in program:
        check_cycle()
        cycle+=1
        if line[0] != "noop":
            check_cycle()
            x += int(line[1])
            cycle+=1

print(sum(signal))
    