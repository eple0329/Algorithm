N = int(input())
people = list(map(int, input().split()))
B, C = map(int, input().split())

result = N
for i in people:
    if i-B <= 0:
        continue
    result += (i-B) // C
    if (i-B) % C != 0:
        result += 1
    
print(result)