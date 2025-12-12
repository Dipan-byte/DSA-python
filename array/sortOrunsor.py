n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        count += 1

if arr[-1] > arr[0]:
    count += 1

print("YES" if count == 1 else "NO")
