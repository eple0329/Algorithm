while True:
    N = input()
    if N == '0':
        break
    mid = len(N)//2
    isPalindrome = True
    for i in range(mid):
        if N[i] != N[((i+1)*(-1))]:
            isPalindrome = False
            break
    if isPalindrome:
        print('yes')
    else:
        print('no')