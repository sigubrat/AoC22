
def main(file):
    foods = []
    with open(file) as f:
        lines = f.readlines()

        food = []
        for line in lines:
            if line.strip():
                food.append(int(line))
            else:
                foods.append(food)
                food = []
    
    max = 0
    for food in foods:
        tmp = sum(food)
        if tmp > max:
            max = tmp
    
    print(max)

    return

if __name__ == "__main__":
    main("data.txt")