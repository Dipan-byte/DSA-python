n = int(input())
arr = list(map(int, input().split()))

max_from_right = arr[-1]
leaders = [max_from_right]

for i in range(n - 2, -1, -1):
    if arr[i] > max_from_right:
        max_from_right = arr[i]
        leaders.append(arr[i])

print(*leaders)
