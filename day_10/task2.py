import numpy as np
from pprint import pprint

x = 1
cycle = 0
special_n = 20
special_cycle = 40
crt = np.full((6, 40), ".")

def update_crt():
    sprite = [i + x for i in [-1, 0, 1]]
    row = cycle // 40
    col = cycle % 40

    if col in sprite:
        crt[row][col] = "#"

def print_crt():
    for row in crt:
        for col in row:
            print(col, end="")
        print()

with open("day_10/data.txt", "r") as f:
    program = [i.strip().split() for i in f.readlines()]
    for line in program:
        update_crt()
        cycle+=1
        if line[0] != "noop":
            update_crt()
            x += int(line[1])
            cycle+=1
    
    print_crt()

