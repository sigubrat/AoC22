with open("day_8/data.txt", "r") as f:
    data, trees = [i.strip() for i in f.readlines()], []
    col_n = len(data[0].strip())
    for row in data:
        trees.append([int(i) for i in row])

    def check_visible(i, j):
        direction = [0, 0, 0, 0]
        cur = trees[i][j]
        # left
        for k in range(j-1, -1, -1):
            compare = trees[i][k]
            direction[0] += 1
            if compare >= cur:
                break
        # right
        for k in range(j+1, col_n):
            compare = trees[i][k]
            direction[1] += 1
            if compare >= cur:
                break
        # top
        for k in range(i-1, -1, -1):
            compare = trees[k][j]
            direction[2] += 1
            if compare >= cur:
                break
            
        # below
        for k in range(i+1, len(trees)):
            compare = trees[k][j]
            direction[3] += 1
            if compare >= cur:
                break
           
        res = 1
        for d in direction:
            res *= d
        return res

    high_score = 0
    for i, row in enumerate(trees):
        if i == 0 or i == len(trees)-1:
            continue
        for j, col in enumerate(row):
            if j == 0 or j == col_n:
                continue
            new = check_visible(i, j)
            if new > high_score:
                high_score = new
    
    print(high_score)
