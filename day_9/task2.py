
visited = set()

pos = {"0": {"x": 0, "y": 0}, "1": {"x": 0, "y": 0}, "2": {"x": 0, "y": 0}, "3": {"x": 0, "y": 0}, "4": {"x": 0, "y": 0}, "5": {"x": 0, "y": 0}, "6": {"x": 0, "y": 0}, "7": {"x": 0, "y": 0}, "8": {"x": 0, "y": 0}, "9": {"x": 0, "y": 0}}

def update_visited():
    x, y = pos["9"]["x"], pos["9"]["y"]
    visit = "".join([str(x), ",", str(y)])
    visited.add(visit)

def move_head(d):
    if d == "L": pos["0"]["x"] -= 1   
    elif d == "R": pos["0"]["x"] += 1
    elif d == "U": pos["0"]["y"] += 1
    elif d == "D": pos["0"]["y"] -= 1

def move_tail(i):
    prev = str(i-1)
    cur = str(i)
    diff_x, diff_y = pos[prev]["x"] - pos[cur]["x"], pos[prev]["y"] - pos[cur]["y"]
    if abs(diff_x) > 1:
        pos[cur]["x"] += 1 if diff_x > 0 else -1
        if abs(diff_y) > 0:
            pos[cur]["y"] += 1 if diff_y > 0 else -1
    elif abs(diff_y) > 1:
        pos[cur]["y"] += 1 if diff_y > 0 else -1
        if abs(diff_x) > 0:
            pos[cur]["x"] += 1 if diff_x > 0 else -1

def move_knots(direction, steps):
    for _ in range(steps):
        update_visited()
        move_head(direction)
        for i in range(1, 10):
            move_tail(i)
    update_visited()

with open("day_9/data.txt", "r") as f:
    for line in f.readlines():
        cmd = line.strip().split()
        direction, steps = cmd[0], int(cmd[1])
        move_knots(direction, steps)
    
print(len(visited))
