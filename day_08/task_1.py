with open("day_8/data.txt", "r") as f:
    data, trees = [i.strip() for i in f.readlines()], []
    col_n = len(data[0].strip())
    for row in data:
        trees.append([int(i) for i in row])

    def check_visible(i, j):
        direction = [1, 1, 1, 1]
        cur = trees[i][j]
        # left
        for k in range(0, j):
            compare = trees[i][k]
            if compare >= cur:
                direction[0] = 0
                break
        # right
        for k in range(j+1, col_n):
            compare = trees[i][k]
            if compare >= cur:
                direction[1] = 0
                break
        
        # top
        for k in range(0, i):
            compare = trees[k][j]
            if compare >= cur:
                direction[2] = 0
                break
        
        # below
        for k in range(i+1, len(trees)):
            compare = trees[k][j]
            if compare >= cur:
                direction[3] = 0
                break
        
        return 1 if sum(direction) > 0 else 0

    count = 0
    for i, row in enumerate(trees):
        if i == 0 or i == len(trees)-1:
            count += col_n
            continue
        for j, col in enumerate(row):
            if j == 0 or j == col_n:
                count +=1
                continue
            count += check_visible(i, j)
    
    print(count)
