T = int(input())

for _ in range(T):
    n = int(input())
    numberByType = dict()
    for i in range(n):
        typeName = input().split()[1]
        if typeName in numberByType.keys():
            numberByType[typeName] += 1
        else:
            numberByType[typeName] = 1
    solve = 1
    for i in numberByType.items():
        solve = solve * (i[1]+1)
    print(solve-1)