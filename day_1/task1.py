
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

    print(max(foods))
    return

if __name__ == "__main__":
    main("test.txt")