callBackNum = [[0, 0] for i in range(41)]
callBackNum[0] = [1, 0]
callBackNum[1] = [0, 1]

for i in range(2, 41):
    callBackNum[i] = [callBackNum[i-1][0] + callBackNum[i-2][0],callBackNum[i-1][1] + callBackNum[i-2][1]]

T = int(input())
for _ in range(T):
    num = int(input())
    print(callBackNum[num][0], callBackNum[num][1])