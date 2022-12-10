def main(file):
    max_food = 0
    with open(file) as f:
        food = 0
        for line in f:
            line = line.strip()
            if line:
                food += int(line)
            else:
                max_food = max(max_food, food)
                food = 0

        max_food = max(max_food, food)

    print(max_food)


if __name__ == "__main__":
    # Change to test.txt if you want to run the test first
    main("day_1/data.txt")