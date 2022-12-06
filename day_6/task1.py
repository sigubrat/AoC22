with open("data.txt", "r") as f:
    subroutine = f.read().strip()
    current = [x for x in subroutine[:4]]
    for i in range(4, len(subroutine)):
        current.pop(0)
        current.append(subroutine[i])
        if len(set(current)) == 4:
            print("Answer: ", i+1)
            break


