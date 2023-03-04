import sys

N = int(sys.stdin.readline().rstrip())
BUG_WEIGHT = list(map(int, sys.stdin.readline().split()))
BUG_WEIGHT_SUM = []

BUG_WEIGHT_SUM.append(BUG_WEIGHT[0])
for i in range(1, N):
    BUG_WEIGHT_SUM.append(BUG_WEIGHT_SUM[i-1] + BUG_WEIGHT[i])
HEAD_MIN = BUG_WEIGHT_SUM[N-1]//3

count = 0

for i in range(1, N-1):
    if BUG_WEIGHT_SUM[i-1] > HEAD_MIN:
        break
    
    num = (BUG_WEIGHT_SUM[N-1] - BUG_WEIGHT_SUM[i-1])//2 + BUG_WEIGHT_SUM[i-1] + 1 # 몸통과 꼬리의 중간지점
    start = i
    end = N-1
    
    # 이진탐색으로 찾는 방법...
    while start <= end:
        mid = (start + end)//2
        if num < BUG_WEIGHT_SUM[mid]:
            end = mid -1
        elif num > BUG_WEIGHT_SUM[mid]:
            start = mid + 1
    count += N-1-start  # 최댓값

    # 기본적으로 어캐든 찾는 방법
    '''for j in range(N-1, i, -1):
        if BUG_WEIGHT_SUM[j-1]-BUG_WEIGHT_SUM[i-1] > BUG_WEIGHT_SUM[N-1]-BUG_WEIGHT_SUM[j-1] > BUG_WEIGHT_SUM[i-1]:
            count += 1
        elif BUG_WEIGHT_SUM[j-1]-BUG_WEIGHT_SUM[i-1] <= BUG_WEIGHT_SUM[N-1]-BUG_WEIGHT_SUM[j-1]:
            break
        else:
            pass
            '''
    


print(count)