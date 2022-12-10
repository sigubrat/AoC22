def main(file):
    foods = []
    with open(file) as f:
        lines = f.readlines()

        food = 0
        for line in lines:
            if line.strip():
                food += int(line)
            else:
                foods.append(food)
                food = 0

        foods.append(food)
    
    maxFoods = sorted(foods)[-3:]
    print(maxFoods)
    return

if __name__ == "__main__":
    # Change to test.txt if you want to run the test first
    main("day_01/data.txt")