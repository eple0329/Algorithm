A = input()

just_print = False
tmp = []
for i in A:
    if just_print:
        if i == ">":
            just_print = False
            print(i, end="")
        else:
            print(i, end="")
    elif i == "<":
            if tmp != []:
                tmp.reverse()
                for j in tmp:
                    print(j, end="")
                tmp = []
            just_print = True
            print(i, end="")
    elif i == " ":
        if tmp != []:
            tmp.reverse()
            for j in tmp:
                print(j, end="")
            tmp = []
            print(" " , end="")
        else:
            print(" ")
    else:
        tmp.append(i)
if tmp != []:
    tmp.reverse()
    for j in tmp:
        print(j, end="")
    tmp = []