n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
num_count = dict()
for i in range(len(arr)-1, -1, -1):
    if arr[i] not in num_count.keys():
        num_count[arr[i]] = 1
    else:
        num_count[arr[i]] += 1
        del arr[i]

sorted_arr = sorted(arr)

start = 0
end = len(sorted_arr)-1

total_count = 0
while start < end:
    if sorted_arr[end] + sorted_arr[start] == k:
        total_count += num_count[sorted_arr[end]] * num_count[sorted_arr[start]]
        end -= 1
        start += 1
    elif sorted_arr[end] + sorted_arr[start] > k:
        end -= 1
    else:
        start += 1

print(total_count)