with open("data.txt", "r") as f:
    subroutine = f.read().strip()
    current = [x for x in subroutine[:14]]
    for i in range(14, len(subroutine)):
        current.pop(0)
        current.append(subroutine[i])
        if len(set(current)) == 14:
            print("Answer: ", i+1)
            break


