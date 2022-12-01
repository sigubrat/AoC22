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
        foods.append(food)

    maxFoods = []
    foods = [sum(i) for i in foods]
    for i in range(3):
        maxFoods.append(max(foods))
        foods.remove(max(foods))
    
    print(sum(maxFoods))

    return

if __name__ == "__main__":
    main("data.txt")