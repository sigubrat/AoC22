# A = X = rock
# B = Y = paper
# C = Z = scissor

# Played: result[lose, draw, win]
need = {'X': 0, 'Y': 3, 'Z': 6}
combos = {'A': ['Z', 'X', 'Y'], 'B': ['X', 'Y', 'Z'], 'C': ['Y', 'Z', 'X']}
shape_score = {'X': 1, 'Y': 2, 'Z': 3}

with open("data.txt", "r") as f:
    raw = f.readlines()
    data = [i.split() for i in raw]

    total_score = 0
    for r in data:
        score = 0
        elf = r[0]
        you = r[1]

        score += need[you]
        shapes = combos[elf]

        if (you == 'X'):
            shape = shapes[0]
        elif (you == 'Y'):
            shape = shapes[1]
        else:
            shape = shapes[2]
        
        score += shape_score[shape]
        total_score += score
    
    print(total_score)
        



