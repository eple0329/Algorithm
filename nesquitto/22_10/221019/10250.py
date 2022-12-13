testCase = int(input().rstrip())
for _ in range(testCase):
    H, W, N = map(int, input().split())
    guestW = N // H + 1
    guestH = N % H
    if guestH == 0:
        guestH = H
        guestW -= 1
    if guestW < 10:
        print(str(guestH) + "0" + str(guestW))
    else:
        print(str(guestH) + str(guestW))