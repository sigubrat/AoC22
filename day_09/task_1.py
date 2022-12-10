
visited = set()

pos = {"H": {"x": 0, "y": 0}, "T": {"x": 0, "y": 0}}
last_H_pos = {"x": 0, "y": 0}

def update_visited():
    x, y = pos["T"]["x"], pos["T"]["y"]
    visit = "".join([str(x), ",", str(y)])
    visited.add(visit)

def move_head(d):
    last_H_pos["x"], last_H_pos["y"] = pos["H"]["x"], pos["H"]["y"]
    if d == "L":
        pos["H"]["x"] -= 1   
    elif d == "R":
        pos["H"]["x"] += 1
    elif d == "U":
        pos["H"]["y"] += 1
    elif d == "D":
        pos["H"]["y"] -= 1

def move_tail():
    diff_x, diff_y = pos["H"]["x"] - pos["T"]["x"], pos["H"]["y"] - pos["T"]["y"]
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        pos["T"]["x"], pos["T"]["y"] = last_H_pos["x"], last_H_pos["y"]

def move_knots(direction, steps):
    for _ in range(steps):
        update_visited()
        move_head(direction)
        move_tail()
    update_visited()

with open("day_9/data.txt", "r") as f:
    for line in f.readlines():
        cmd = line.strip().split()
        direction, steps = cmd[0], int(cmd[1])
        move_knots(direction, steps)
    
print(len(visited))
