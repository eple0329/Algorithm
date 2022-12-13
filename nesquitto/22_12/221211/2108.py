from collections import Counter

N = int(input())
numList = []
for _ in range(N):
    numList.append(int(input()))
print(round(sum(numList)/N)) # 산술평균
print(sorted(numList)[N//2]) # 중앙값
A = Counter(numList).most_common()
fre = A[0][1]
tmp = []
for i in A:
    if fre == i[1]:
        tmp.append(i[0])
    else:
        break
if len(tmp) == 1:
    print(tmp[0])
else:
    print(sorted(tmp)[1])
print(max(numList) - min(numList)) # 범위