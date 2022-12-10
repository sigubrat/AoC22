with open("data.txt", "r") as f:
    lines = [i.split(",") for i in f.readlines()]
    counter = 0
    for line in lines:
        A, B = line[0], line[1].strip()
        A, B = A.split("-"), B.split("-")
        
        if (int(A[0]) <= int(B[0]) and int(A[1]) >= int(B[1])) or (int(B[0]) <= int(A[0]) and int(B[1]) >= int(A[1])):
            counter+=1

    print(counter)

