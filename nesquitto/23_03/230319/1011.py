for _ in range(int(input())):
    x, y = map(int, input().split())
    distance = y-x
    if distance == 1:
        print(1)
    elif distance == 2:
        print(2)
    else:
        count = 0
        move = 1
        move_plus = 0
        while move_plus < distance:
            count += 1
            move_plus += move
            if count % 2 == 0:
                move += 1
        print(count)
