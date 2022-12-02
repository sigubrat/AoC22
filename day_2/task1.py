# A = X = rock
# B = Y = paper
# C = Z = scissor

# Played: result[lose, draw, win]
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

        combo = combos[elf]
        outcome = combo.index(you)

        if (outcome == 2):
            score += 6
        elif (outcome == 1):
            score += 3
        
        score += shape_score[you]
        total_score += score
    
    print(total_score)
        



